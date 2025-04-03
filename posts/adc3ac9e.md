<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![20250211170256_jLzrA4QP.webp](https://cdn.dong4j.site/source/image/20250211170256_jLzrA4QP.webp)

## 简介

哪吒面板是一个开源的监控解决方案，旨在帮助用户轻松实现服务器和应用的实时监控。通过 Dashboard、Agent 以及前后台前端资源的配合，用户可以全面掌握系统运行状态。

v1.x 版本相较于老版本简化了部署方式, 我主要用于监控家中的设备, 并开放到了公网, 为了安全起见做了响应的防护, 接下来将简单介绍一下自托管与安全防控.

## 部署

可参考 [官方文档](https://nezha.wiki/guide/dashboard.html) 部署, 因为我需要对前端页面做相应的修改, 所以这里选择使用源码的方式部署.

### 资源下载

- **Dashboard**: [nezha/releases](https://github.com/nezhahq/nezha/releases)
- **Agent**: [agent/releases](https://github.com/nezhahq/agent/releases)
- **后台前端资源**: [admin-frontend/releases](https://github.com/nezhahq/admin-frontend/releases)
- **前台前端资源**: [nezha-dash-v1/releases](https://github.com/hamster1963/nezha-dash-v1/releases)

本人使用 pm2 在家中的服务器上部署, 为了简化部署就写了一键部署脚本, 所以这里需要讲一下部署包的目录结构:

```
.
├── agent														# 代理服务目录, 包含代理配置和二进制文件
│   ├── config.yml
│   └── nezha-agent
├── dashboard												# dashboard 服务目录
│   ├── admin-dist									# 后台前端静态资源目录
│   ├── nezha-dash-v1								# 前台前端项目
│   ├── user-dist										# 前端前端静态资源目录(nezha-dash-v1 项目编译后会自动将静态资源拷贝到此目录)
│   ├── dashboard-linux-amd64				# dashboard 二进制文件
│   ├── config.yaml									# dashboard 配置文件
│   └── sqlite.db										# dashboard 数据库
├── deploy-dashboard.sh							# 自动化部署脚本
├── ecosystem.config.js							# pm2 部署配置
└── download.sh											# 从服务器同步最新的数据库文件等关键数据
```

将上述的资源文件下载后存放到对应的目录, 然后为二进制文件赋予执行权限:

```bash
chmod +x agent/nezha-agent
chmod +x dashboard/dashboard-linux-amd64
```

如果不需要对前台前端页面做任何改动, 直接下载 releases 的 dist 部署即可, 因为我需要修改前台页面, 所以这里下载 nezha-dash-v1 源码, 本地修改完成后自行编译部署.

### nezha-dash-v1 修改

个人对前端页面做了如下修改:

#### 添加 umami 统计

在 index.html 中添加自建的 umami 统计服务:

![20250211180300_vA7FAiiR.webp](https://cdn.dong4j.site/source/image/20250211180300_vA7FAiiR.webp)

#### 隐藏公网的登录入口

为暴露到公网的监控面板做了点安全防控, 避免被人爆破, 修改文件: `src/components/Header.tsx`:

```javascript
	...

  const [showDashboardLink, setShowDashboardLink] = useState(false);

  useEffect(() => {
    // 检查当前页面的主机名和端口号是否为本地部署的 dashboard 地址, 比如: 192.168.1.2:8888
    if (window.location.host === '192.168.1.2:8888') {
      setShowDashboardLink(true);
    }
  }, []);

  ...
```

然后将此文件中的 `<DashboardLink />` 修改为:

```
{showDashboardLink && <DashboardLink />}
```

这样只有在内网访问时才会显示登录按钮.

当然这是前端入口的简单防控, 外部用户仍然可以绕过, 比如在本地通过 Nginx 代理到我的公网域名, 这样 `window.location.host` 获取到的也是 `192.168.1.2:8888`, 所以这里我并没有将真实的局域网暴露出来.

为了进一步加载, 接下来是从接口上进行限制.

因为使用 Nginx 将内网的监控面板暴露到了公网, 所以通过对 Nginx 配置可以限制接口访问:

```
# 禁止访问 /dashboard 以及 /dashboard 后面的路径
location ^~ /dashboard {
    deny all;  # 拒绝所有访问
    return 403;  # 返回 403 Forbidden 错误
}
```

这样外网也无法通过 API 进行爆破.

> 另外可以在服务器端检查请求的来源 IP 地址，确保只有来自内网 IP 地址的请求才能访问登录页面。但字段仍然可以伪造.
>
> 如果不需要暴露到外网, 最好使用 VPN 这种方式访问家中的服务.

---

#### 页面整体放大

目前的前端页面看着太小了, 所以将页面整体放大到原来的 1.25 倍, 在 `index.css` 中添加:

```css
@media (min-width: 1920px) and (min-height: 1080px) {
  html {
    transform: scale(1.25);
    transform-origin: top;
    width: 100vw;
    height: 100vh;
  }
}
```

### 一键部署

#### 安装依赖

首先需要在服务器上安装 Node.js 和 pm2(因为哪吒面板使用 root 运行, 所以我也使用 root 用户安装了 Node.js 和 pm2):

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - \
	&& sudo apt install -y nodejs \
	&& sudo npm install -g pm2 \
	&& pm2 -v
```

#### 一键更新脚本

为了避免数据库被本地覆盖, 所以在部署前使用更新脚本拉取服务器上最新的数据:

```bash
#!/bin/zsh

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

# 配置项
REMOTE_SSH_ALIAS="m920x"  # 服务器的 SSH 别名
REMOTE_DIRECTORY="/opt/nezha"  # 远程目录
LOCAL_DIRECTORY="$SCRIPT_DIR"    # 本地目录

# 时间戳
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# 执行 rsync 同步
echo "[$TIMESTAMP] 开始同步..."
rsync -avz --verbose \
  --exclude '.DS_Store' \
  --exclude '._*' \
  --exclude '__MACOSX' \
  --exclude 'logs/' \
  --exclude 'dashboard-linux-amd64' \
  --exclude 'nezha-agent' \
  --exclude 'admin-dist/' \
  --exclude 'user-dist/' \
  "$REMOTE_SSH_ALIAS:$REMOTE_DIRECTORY/" "$LOCAL_DIRECTORY/"

# 检查同步是否成功
if [ "${PIPESTATUS[0]}" -eq 0 ]; then
    echo "[$TIMESTAMP] 同步完成！"
else
    echo "[$TIMESTAMP] 同步失败！请检查日志。"
fi
```

> 这里的 `m920x` 是我配置到 ssh 别名, 需要进行免密登录配置

#### pm2 部署配置

`ecosystem.config.js` 配置内容:

```javascript
module.exports = {
  apps: [
    {
      name: "nezha-dashboard", // 应用名称
      namespace: "nezha", // 指定命名空间
      version: "1.0.0", // 应用版本
      cwd: "/opt/nezha/dashboard", // 当前工作目录
      script: "./dashboard-linux-amd64", // 主脚本路径，相对于 cwd
      args: " -c ./config.yaml -db ./sqlite.db", // 传递给脚本的参数
      watch: false, // 是否启用文件监控
      ignore_watch: [], // 忽略监控的文件或目录
      exec_mode: "fork",
      instances: 1, // 应用实例数量
      autorestart: true, // 是否自动重启
      env: {},
      log_date_format: "YYYY-MM-DD HH:mm:ss", // 日志时间格式
      error_file: "./logs/error.log", // 错误日志文件
      out_file: "./logs/out.log", // 输出日志文件
      merge_logs: true, // 是否合并日志
    },
  ],
};
```

> `cwd` 需要修改为实际的部署目录, 默认是 `/opt/nezha`.

#### 部署脚本

```bash
#!/bin/bash

# 获取当前脚本的所在目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

# 配置项
REMOTE_SSH_ALIAS="m920x"             # 远程服务器的 SSH 别名
LOCAL_PATH="$SCRIPT_DIR"         # 本地文件路径
REMOTE_PATH="/opt/nezha"       # 远程文件路径（完整路径，包括文件名）

# 提示用户点击回车继续
echo "Press Enter to continue with the deployment..."
read -r

# 部署前端
cd "$SCRIPT_DIR/dashboard/nezha-dash-v1" || exit 1
bun install
rm -rf dist
bun run build

cd "$SCRIPT_DIR" || exit 1
# 拷贝 dist 到 user-dist
rsync -avz --delete \
  --exclude '.DS_Store' \
  --exclude '._*' \
  --exclude '__MACOSX' \
  "$LOCAL_PATH/dashboard/nezha-dash-v1/dist/" "$LOCAL_PATH/dashboard/user-dist/"

# 先同步数据库文件到本地, 避免覆盖
# rsync -avz --verbose \
#   "$REMOTE_SSH_ALIAS:$REMOTE_PATH/dashboard/data/sqlite.db" "$LOCAL_PATH/dashboard/data/sqlite.db"

# 上传文件到远程服务器
rsync -avz --delete \
  --exclude '.DS_Store' \
  --exclude '._*' \
  --exclude '__MACOSX' \
  --exclude "deploy-dashboard.sh" \
  --exclude "download.sh" \
  --exclude "agent/" \
  --exclude "nezha-dash-v1/" \
  "$LOCAL_PATH/" "$REMOTE_SSH_ALIAS:$REMOTE_PATH/"

# 上传完成
echo "Upload complete."

ssh "$REMOTE_SSH_ALIAS" "source /root/.nvm/nvm.sh && pm2 stop nezha-dashboard"
ssh "$REMOTE_SSH_ALIAS" "source /root/.nvm/nvm.sh && pm2 delete nezha-dashboard"
ssh "$REMOTE_SSH_ALIAS" "source /root/.nvm/nvm.sh && pm2 start $REMOTE_PATH/ecosystem.config.js"
if [ $? -ne 0 ]; then
  echo "Error: Failed to reload nezha-dashboard on server '$REMOTE_SSH_ALIAS'."
  exit 1
fi

echo "Server configuration successfully updated and reloaded on '$REMOTE_SSH_ALIAS'."
```

1. 编译 `nezha-dash-v1` 并将 dist 中的静态文件拷贝到 `user-dist`;
2. 上传指定文件到远程服务器;
3. 使用 pm2 启动服务, (这里是先删除然后重新启动, 因为我这里使用 `restart` 会有点问题);

> 记得使用 `source /root/.nvm/nvm.sh`, 直接使用 pm2 会找不到文件.

其实最终调用的启动命令为:

```bash
/path/to/dashboard -c /path/to/config.config.yaml -db /path/to/sqlite.db
```

- **首次运行**: 建议移除 `-db` 参数，让程序自动生成配置文件和数据库。
- **配置文件说明**:
  - `listenport`: 设定 Dashboard 和 Agent 的监听端口，需做好反向代理配置。
  - `agentsecretkey`: 用于 Agent 连接 Dashboard 的密钥。

#### 运行 Agent

上述脚本只是为了部署 dashboard, Agent 因为一般不会频繁修改, 所有这里使用命令行的方式直接启动即可:

```bash
/path/to/agent -c /path/to/config.yaml
```

- **首次运行**: 使用 `./nezha-agent edit` 命令生成配置文件，按照提示完成设置。
- **配置文件说明**:
  - `client_secret`: 输入 Dashboard 配置中的 `agentsecretkey`。
  - `server`: 指定 Dashboard 的服务器地址和端口。

> 如果使用 `agent.sh` 脚本安装的, 可以直接使用 `systemctl restart nezha-agent` 重启代理服务.

---

## 命令行操作

```bash
$ sudo ./nezha-agent -h
NAME:
   nezha-agent - 哪吒监控 Agent

USAGE:
   nezha-agent [global options] command [command options]

VERSION:
   1.6.1

COMMANDS:
   edit     编辑配置文件
   service  服务操作
   help, h  显示命令列表或帮助信息

GLOBAL OPTIONS:
   --config value, -c value  配置文件路径
   --help, -h                显示帮助信息
   --version, -v             显示版本号
```

macOS 重启 agent:

```bash
$ sudo ./nezha-agent service restart
```

Linux 重启 agent:

```bash
$ sudo systemctl restart nezha-agent
```

**服务操作示例:**

```bash
$ sudo ./nezha-agent service -h
NAME:
   nezha-agent service - 服务管理

USAGE:
   <install/uninstall/start/stop/restart>

OPTIONS:
   --config value, -c value  配置文件路径
   --help, -h                显示帮助信息
```

## 参考资料

- [设置 OAuth 2.0 绑定](https://nezha.wiki/guide/q14.html)
- [Nezha Dashboard V1 前端源码](https://github.com/hamster1963/nezha-dash-v1?tab=readme-ov-file)
- [自定义代码](https://nezhadash-docs.buycoffee.top/custom-code)
- [服务器公开备注生成器](https://nezhainfojson.pages.dev/)
- [美化 1](https://blog.zmyos.com/nezha-theme.html)
- [美化 2](https://misaka.es/archives/33.html)

### 安全配置

- [自定义 Agent 监控项目](https://nezha.wiki/guide/q7.html)
- [哪吒探针关闭网页 ssh](https://blog.weedsstars.com/index.php/archives/26/)
- [哪吒 v1 关闭 ssh 脚本](https://www.nodeseek.com/post-232313-1)

> Dashboard 开启 Debug 模式后可以访问路径 /swagger/index.html 查看详情