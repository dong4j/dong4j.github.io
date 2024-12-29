---
title: HomeLab 服务篇：自托管的乐趣-探索和创造个人云端世界的旅程
ai: true
swiper_index: 5
top_group_index: 5
tags:
  - HomeLab
categories:
  - HomeLab
cover: https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_hoB1PW2R.webp
abbrlink: 3b36
date: 2020-04-14 00:00:00
main_color:
---

![/images/cover/20241229154732_hoB1PW2R.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_hoB1PW2R.webp)

在这个充满无限可能的数字时代, 我们有机会通过自托管的云服务平台来构建一个属于个人的云端世界. 这不是简单地访问远程服务器, 而是亲手打造、定制并管理自己的虚拟实验室, 进行各种新奇有趣的服务部署. 这种“折腾”不仅仅是一种乐趣, 更是一种自我挑战和创造力的释放.

从这篇博客开始, 我会不时地介绍一些我在自托管环境中安装和配置的新奇有趣服务. 这些服务或许并非我当下所需, 但正是这种创造需求的精神驱动着我不断地探索新领域、学习新技术. 在这个过程中, 我也希望能够与大家分享我的经验和见解, 一起探讨如何在个人云端世界中找到乐趣和价值.

在这里, 你将会看到我如何一步步搭建属于自己的实验环境, 从选择合适的硬件到配置各种软件服务. 无论是对技术充满热情的爱好者, 还是希望拓展技能的初学者, 这里都会有一些实用的技巧和建议.

让我们一起踏上这段旅程吧！让我们在自托管的乐趣中不断学习、创造和成长. 敬请关注接下来的博客文章, 期待与你的共同探讨和分享.

**相关文章:**

1. [[homelab-guide|先导篇]]：我的 HomeLab 概要;
2. [[homelab-hardware|硬件篇]]：介绍我所拥有的硬件设备;
3. [[homelab-network|网络篇]]：包括网络环境、异地组网与网络安全;
4. [[homelab-service|服务篇]]：使用 Docker 搭建的各类服务;
5. [[homelab-data|数据篇]]：包括数据存储方案、备份方案和数据恢复方案;
6. [[homelab-data-sync|HomeLab数据同步：构建高效的数据同步网络]]
7. [[homelab-data-backup|HomeLab数据备份：打造坚实的数据安全防线]]
8. [[homelab-upgrade-to-10g|HomeLab 网络续集：升级 10G 网络-再战 10 年]]
9. [[homelab-guide|NAT 内网穿透详解：揭秘网络连接背后的奥秘]]

## HomeLab 的核心: Docker

在个人云端实验室（HomeLab）中, Docker 赋予了我们强大的功能和服务部署能力. 它成为了 HomeLab 架构中不可或缺的一部分, 提供了诸多便利:

1. **容器化部署**：Docker 允许我们将应用程序及其依赖项打包在一个称为容器的轻量级执行环境中. 这意味着无论在哪个硬件和操作系统上, 只要安装了 Docker 引擎, 我们就可以轻松地部署和管理这些容器.
2. **可移植性与一致性**：通过使用 Docker, 我们可以保证在不同的开发和生产环境之间的一致性, 因为应用程序运行在相同的隔离环境下. 这大大简化了应用的迁移和部署过程.
3. **资源利用率**：Docker 容器与传统的虚拟机相比, 具有更低的系统开销, 因为它不需要额外的操作系统来支持. 这使得 Docker 能够更高效地利用主机资源.

因此, 是否能够支持 Docker 运行也成为了我在选择硬件时的重要考量因素之一, 至于为什么没有上 K8S, 还是因为对于目前的情况直接使用 Docker 完全能胜任, 暂时还不想因为引入 K8S 增加复杂性.

接下来我将分享在使用 Docker 过程中的实战经验和所遇到的问题, 并在这些底层基础服务稳定运行之后, 继续介绍我的其他服务和应用搭建过程.

### 远程管理

我拥有一个由多个 Docker 主机组成的网络. 为了更有效地管理和监控这些主机及它们上的容器, 我需要一个集中的管理解决方案. 这意味着我需要一种方法来从单一界面访问和控制所有 Docker 实例.

目前正在使用 **[Portainer](https://www.portainer.io/):**

![20241229154732_GOnzu0wY.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_GOnzu0wY.webp)

Portainer Community Edition 是一个轻量级平台, 用于跨 Docker、Swarm、Kubernetes 和 ACI 环境管理容器化应用程序. 它提供用于管理资源的 GUI 和 API, 并且可以部署为 Linux 或 Windows 本机容器.

Portainer 商业版建立在开源基础之上, 包含适合商业用户的高级功能. 社区版定期更新, 大约每几个月更新一次.

好用且免费, 是目前主要的管理工具.

---

另一个是刚部署不久的 **[DPanel](https://github.com/donknap/dpanel)**, 同样支持多 Docker 主机管理, 亮点是支持 [第三方应用商店](https://dpanel.cc/#/zh-cn/manual/setting/store), 不过用起来不是特别流畅, 目前算作备用选择:

![20241229154732_l4aJ1BNh.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_l4aJ1BNh.webp)

**特性**:

- 全中文的界面, 更适合中文环境使用.
- 安装简单, 占用资源极少, 适合各种 Nas 设备、盒子以及小型服务器.
- 以容器的方式运行, 不需要特权模式, 对宿主机没有依赖及侵入, 安全且可靠.
- 提供完善的容器创建及管理功能, 并提供容器域名绑定功能适配简单使用场景.
- 提供的文件管理功能, 可以方便、快速的查看及调试容器内的各种文件.
- 提供完善的网络管理功能, 便于容器之间的互联、互通, 以及各种网络配置需求.
- 支持文本、远程地址、挂载目录等多种 compose.yml 添加方式, 快速部署和管理 Compose 任务.
- 提供多种语言的基础镜像和模板, 可以快速构建属于自己的镜像, 并可以通过 Zip 或是 Git 等方式, 快速实现可持续化构建.

---

**Dockge**

Uptime Kuma 作者的另一个开源项目-[Dockge](https://github.com/louislam/dockge) 是一个用于管理 Docker Compose YAML 文件的堆栈式管理工具. Dockge 提供了创建、编辑、启动、停止、重启和删除堆栈等功能, 并具有交互式编辑器和 Web 终端等特性.

![20241229154732_QEIZq3Kn.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_QEIZq3Kn.webp)

**特性**:

- **功能全面**：支持创建、编辑、启动、停止、重启和删除 Docker Compose 堆栈, 以及更新 Docker 镜像.
- **式体验**：提供交互式编辑器和 Web 终端, 方便用户管理 Docker 环境.
- **跨平台支持**：可在主流 Linux 发行版上运行, 包括 Ubuntu、Debian、Raspbian、CentOS、Fedora 和 ArchLinux.
- **开源免费**：采用 MIT 许可协议, 免费开源.

> Dockge 只能管理单台 Docker 主机, 它的重点是 dockerc-compose 的管理与维护.

---

Docker 集中管控的前提是需要开启 Docker 主机的远程管理端口, 因为涉及到多种类型的系统, 我这里统一整理一下:

#### Linux

```shell
vim /usr/lib/systemd/system/docker.service

# 追加 tcp
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:2375

# 重新加载 Docker 守护进程
systemctl daemon-reload
# 重启 Docker 服务
systemctl restart docker
```

#### macOS

在 macOS 下无法直接修改配置文件来开启 Remote API 服务, 通过运行 `socat` 容器, 将 `unix socket` 上 Docker API 转发到 MacOS 指定的端口：

```shell
docker run -d --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock -p 2375:2375 bobrik/socat TCP-LISTEN:2375,fork UNIX-CONNECT:/var/run/docker.sock
```

或者使用 docker-compose:

```yaml
services:
  docker-socat:
    image: bobrik/socat
    container_name: docker-socat
    restart: unless-stopped
    ports:
      - "2375:2375"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: "TCP-LISTEN:2375,fork UNIX-CONNECT:/var/run/docker.sock"
```

#### OpenWrt

OpenWrt 直接通过 WebUI 修改:

![20241229154732_SxM9gN4W.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_SxM9gN4W.webp)

或者编辑配置文件:

```shell
vim /etc/config/dockerd

config globals 'globals'
	# 添加这一行
	list hosts 'tcp://0.0.0.0:2375'
```

```
# 重启
/etc/init.d/docker restart
```

#### NAS

```shell
# DSM 7.2 之前
sudo vim /var/packages/Docker/etc/dockerd.json
# DSM 7.2
sudo vim /var/packages/ContainerManager/etc/dockerd.json
```

添加如下配置:

```json
"hosts":["tcp://0.0.0.0:2375","unix:///run/docker.sock"]
```

```shell
# 重启 Docker
sudo synosystemctl restart pkgctl-ContainerManager
```

#### 树莓派

```shell
vim /etc/default/docker
# 末尾添加
DOCKER_OPTS="-H tcp://0.0.0.0:2375"
# 重启 docker
sudo systemctl restart docker
```

---

### 一次配置, 到处运行

我的所有 Docker 容器全部使用 docker-compose 启动, 用 docker-compose.yml 文件(可以使用一些转换工具将 docker run 转换成 docker-compose.yml), 方便在不同环境中重现, 然后使用 Synology Drive + Syncthing 同步 docker-compose.yml 文件, 然后在多设备上运行:

![docker-sync.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/docker-sync.drawio.svg)

1. 具备安装 Synology Drive Client 的主机直接使用 Drive 同步数据;
2. 其他的则通过 Syncthing 同步, Mac mini 2018 作为 Synology Drive 和 Syncthing 的枢纽;

这样我在任意设备上新增或修改了 docker-compose.yml 都会通过到其他设备上, 具体配置方式将在下章的 [[homelab-data|数据篇]] 中详细说明.

---

### 数据目录迁移

M920x 的系统盘只有 512G, 因为 M920x 定位为 Docker 容器的主力机, 所以预计 Docker 镜像会占据大量空间, 因此考虑将 Docker 的数据目录迁移到 1T SSD 中. 迁移有两种方案:

1. 使用软链接;
2. 修改默认存储目录;

#### 使用软链接

迁移之前需要停止 Docker, 但是在停止报错了:

```
Stopping 'docker.service', but its triggering units are still active:
docker.socket
```

这是因为 docker.socket 依然在运行, 它是 Docker 的监听套接字, 负责监听 Docker API 请求并触发 docker.service.

在停止 docker.service 之前, 需要先停止 docker.socket：

```shell
sudo systemctl stop docker.socket
sudo systemctl stop docker
```

然后迁移数据:

```shell
rsync -avzP /var/lib/docker /mnt/3.860.ssd/
```

- **-a**: 归档模式, 表示递归传输并保持文件属性;
- **-v**: 显示 rsync 过程中详细信息. 可以使用"-vvvv"获取更详细信息;
- **-P**: 显示文件传输的进度信息. (实际上 `-P=--partial --progress`, 其中的 `--progress` 才是显示进度信息的);
- **-z**: 传输时进行压缩提高效率;

备份数据目录:

```shell
mv /var/lib/docker  /var/lib/docker.bak
```

重启 Docker

```
systemctl restart docker
```

启动 Docker 之后, Docker 写入的路径依然是 `/var/lib/docker` , 但是因为软链接的设置, 实际已经是往新的目录写入了. 至此, 完成了 Docker 安装(存储)目录的迁移.

通过上述方法完成迁移之后, 在确认 Docker 能正常工作之后, 删除原目录备份数据：

```bash
rm -rf /var/lib/docker.bak
```

#### 修改默认存储目录

迁移数据的过程都一样:

```shell
rsync -avzP /var/lib/docker /mnt/3.860.ssd/
```

修改 `/etc/docker/daemon.json`:

```json
{
  "data-root": "/mnt/3.860.ssd/docker",
  ...
}
```

使用 `data-root` 定义数据目录, 最后重启 docker, 验证目录:

```shell
docker info | grep "Docker Root Dir"
```

没问题就可以删除原目录了.

### 容器自动更新

在使用 Docker 的过程中, 虽然我们知道在容器对应的镜像后面添加 latest 标签, 然后通过手动编辑容器, 即可拉取最新镜像, 然后达成更新容器的目的. 但是当建立非常多的容器之后, 使用手动更新容器将会是一件非常繁琐的事情, 这里推荐一款非常优雅的容器更新工具-[Watchtower](https://github.com/containrrr/watchtower).

Watchtower 是一个开源项目, 它可以监控你的 Docker 容器, 并在容器的基础镜像有更新时自动重启容器. 这个工具对于需要持续部署和集成的项目来说非常有用, 可以简化管理工作并确保你的应用始终运行最新的镜像.

我目前的配置如下:

```yaml
services:
  watchtower:
    image: containrrr/watchtower
    restart: unless-stopped
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --http-api-update --http-api-periodic-polls --cleanup
    environment:
      - WATCHTOWER_HTTP_API_TOKEN=xxx
      - WATCHTOWER_NOTIFICATIONS=email
      - WATCHTOWER_NOTIFICATION_EMAIL_FROM=xxx
      - WATCHTOWER_NOTIFICATION_EMAIL_TO=xxx
      - WATCHTOWER_NOTIFICATION_EMAIL_SERVER=xxx
      - WATCHTOWER_NOTIFICATION_EMAIL_SERVER_PORT=xxx
      - WATCHTOWER_NOTIFICATION_EMAIL_SERVER_USER=xxx
      - WATCHTOWER_NOTIFICATION_EMAIL_SERVER_PASSWORD=xxx
      - WATCHTOWER_NOTIFICATION_EMAIL_DELAY=2
    labels:
      - "com.centurylinklabs.watchtower.enable=false"
    ports:
      - 8088:8080
```

1. 使用 `--http-api-update` 开始 API 手动更新功能;
2. 使用 `--http-api-periodic-polls` 开始自动定时更新功能;
3. 使用 `--cleanup` 删除旧的镜像;
4. 使用 `WATCHTOWER_NOTIFICATION_EMAIL` 将更新通过邮件通知, 当然还有其他通知方式;

其中 `WATCHTOWER_HTTP_API_TOKEN` 是 API 的 token, 调用 API 时需要添加到 Header 中, 并使用邮件通知更新的内容.

上述配置会监听当前主机所有的 Docker 容器, 目前适用我现在的场景, 更多的高级功能比如 更新特定容器, 忽略更新某些容器, 监控远程 Docker 容器等可查看官方文档了解.

---

### 常见操作备忘

#### 非 root 用户使用 Docker 命令

Docker 默认使用 Unix 套接字与守护进程通信, 而该套接字的权限只允许 root 用户和 docker 组用户访问, 因此需要将该用户添加到 docker 组.

**群晖**

```shell
sudo synogroup --add docker
sudo synogroup --member docker $USER
sudo chown root:docker /var/run/docker.sock
```

**Linux**:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
# newgrp是一个Linux系统命令, 用于切换当前会话的有效组
newgrp docker
```

#### 批量删除镜像

```shell
docker rmi $(docker images -q)

# 强制删除
docker rmi -f $(docker images -q)
```

#### 容器与寄主机之间拷贝文件

```shell
# 容器 --> 寄主机
docker cp <容器ID>:<容器内路径> <宿主机路径>

# 寄主机 --> 容器
docker cp <宿主机路径> <容器ID>:<容器内路径>
```

#### docker run 互转 docker-compose

- [composerize](https://github.com/composerize/composerize)
- [decomposerize](https://github.com/composerize/decomposerize)

#### docker 代理

##### 运行时代理

1. 配置全局代理（适用于所有容器）

   创建或编辑 Docker 守护进程配置文件:

   ```shell
   sudo mkdir -p /etc/systemd/system/docker.service.d
   sudo nano /etc/systemd/system/docker.service.d/http-proxy.conf
   ```

   添加以下内容：

   ```shell
   [Service]
   Environment="HTTP_PROXY=http://proxy.example.com:8080"
   Environment="HTTPS_PROXY=http://proxy.example.com:8080"
   Environment="NO_PROXY=localhost,127.0.0.1,.example.com"
   ```

   重新加载并重启 Docker 服务：

   ```shell
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```

2. 为特定容器配置代理

   - 使用 docker run 时配置代理

     ```shell
     docker run -e HTTP_PROXY=http://proxy.example.com:8080 \
                -e HTTPS_PROXY=http://proxy.example.com:8080 \
                -e NO_PROXY=localhost,127.0.0.1 \
                ubuntu
     ```

   - 在 docker-compose.yml 中配置代理

     ```shell
     version: '3'
     services:
       web:
         image: nginx
         environment:
           - HTTP_PROXY=http://proxy.example.com:8080
           - HTTPS_PROXY=http://proxy.example.com:8080
           - NO_PROXY=localhost,127.0.0.1,.example.com
     ```

3. 通过 .env 文件管理代理

   ```shell
   # .env
   HTTP_PROXY=http://proxy.example.com:8080
   HTTPS_PROXY=http://proxy.example.com:8080
   NO_PROXY=localhost,127.0.0.1,.example.com
   ```

   在 docker-compose.yml 中引用环境变量：

   ```shell
   services:
     web:
       image: nginx
       environment:
         - HTTP_PROXY=${HTTP_PROXY}
         - HTTPS_PROXY=${HTTPS_PROXY}
         - NO_PROXY=${NO_PROXY}
   ```

4. 在 Dockerfile 中配置代理

   ```shell
   FROM ubuntu
   ARG HTTP_PROXY
   ARG HTTPS_PROXY
   ENV HTTP_PROXY=${HTTP_PROXY}
   ENV HTTPS_PROXY=${HTTPS_PROXY}

   RUN apt-get update && apt-get install -y curl
   ```

   构建时传递代理变量

   ```shell
   docker build --build-arg HTTP_PROXY=http://proxy.example.com:8080 \
                --build-arg HTTPS_PROXY=http://proxy.example.com:8080 \
                -t my_image .
   ```

##### 拉取镜像时使用代理

docker pull /push 的代理被 systemd 接管, 所以需要设置 systemd:

```bash
$ sudo mkdir -p /etc/systemd/system/docker.service.d
sudo vim /etc/systemd/system/docker.service.d/http-proxy.conf
```

```bash
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:8123"
Environment="HTTPS_PROXY=https://127.0.0.1:8123"
```

```
sudo systemctl daemon-reload && sudo systemctl restart docker
```

检查确认环境变量已经正确配置：

```shell
$ sudo systemctl show --property=Environment docker
```

或从 `docker info` 的结果中查看配置项:

![20241229154732_roBMUc0U.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_roBMUc0U.webp)

> docker 镜像由 docker daemon 管理, 所以 **不能用修改 shell 环境变量的方法使用代理服务**, 而是从 systemd 角度设置环境变量.

**修改代理后出现的问题**:

```
Error response from daemon: Get "https://docker.n8n.io/v2/": proxyconnect tcp: net/http: TLS handshake timeout
```

**解决办法:**

- 方式一: 将 https 代理的地址改成 http

  ```bash
  [Service]
  Environment="HTTP_PROXY=http://127.0.0.1:8123"
  Environment="HTTPS_PROXY=http://127.0.0.1:8123"
  ```

- 方式二: 请删除 `https://` 和 `http://`

  ```bash
  [Service]
  Environment="HTTP_PROXY=127.0.0.1:8123"
  Environment="HTTPS_PROXY=127.0.0.1:8123"
  ```

<!--

https://neucrack.com/p/286

https://www.lfhacks.com/tech/pull-docker-images-behind-proxy/

-->

---

#### 容器访问主机网络

这里只是说一下 `host.docker.internal`:

比如, 在主机上运行 MySQL 服务器, Docker 容器可以通过网络访问连接到主机的 MySQL 具体名为 host.docker.internal:3306 . 当在 Windows 或 Mac 计算机上工作时, 这是最简单的技术.

Linux 上的 Docker 引擎用户也可以通过 docker run 的 `--add-host` 标志启用主机的默认名称 `host.docker.internal`.

**docker run**:

```
docker run -d --add-host host.docker.internal:host-gateway my-container:latest
```

**docker-compose**

```shell
services:
  web:
    image: nginx
    ports:
      - "8080:80"
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

extra_hosts 配置会将 host.docker.internal 映射到宿主机.

`–add-host` 标志向容器的 `/etc/hosts` 文件添加一个条目. 上面显示的值将 `host.docker.internal` 映射到容器的主机网关 .

> 上述方式在主机部署 LLM 模型, 而应用层使用 Docker 部署时经常使用到.

## Docker 服务

### Docker 商店

为了简化安装部署 Docker 服务, 我目前使用了多个第三方应用商店:

**[1Panel](https://1panel.cn/)**

![20241229154732_wWV312Dl.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_wWV312Dl.webp)

- **开源, 现代化**：1Panel 是一款开源的 Linux 服务器运维管理面板, 提供 Web 图形界面进行高效管理.
- **功能丰富**：支持主机监控、文件管理、数据库管理、容器管理等功能.
- **快速建站**：深度集成 WordPress 和 Halo 建站工具, 实现一键绑定域名和配置 SSL 证书.
- **安全可靠**：基于容器管理并部署应用, 提供病毒防护、防火墙和日志审计等功能.
- **一键备份**：支持一键备份和恢复, 将数据备份到各类云端存储介质.

**[CasaOS](https://casaos.io/)**

![20241229154732_e38oDLTM.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_e38oDLTM.webp)

- 基于 Docker, 可运行在多种设备上, 包括 x86 和 Raspberry Pi.
- 提供超过 20 个预安装应用和 50+ 个社区验证应用.
- 支持社区贡献, 用户提交新的应用.
- 用户界面简洁优雅, 易于操作.
- 支持备份设置, 方便快速安装和恢复应用.

[**Runtipi**](https://runtipi.io/)

![20241229154732_Z7Jb8Npn.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Z7Jb8Npn.webp)

- **免费开源**: Runtipi 是一款免费且开源的软件, 用户可以自由使用和修改.
- **简化安装**: 通过一键安装, 用户可以轻松地将 200 多个流行的自托管应用程序部署到家中服务器.
- **一键更新**: 用户可以轻松地更新应用程序, 确保它们始终保持最新状态.
- **易于配置**: Runtipi 提供了一个简单的 Web UI, 用户可以轻松地自定义应用程序的配置.
- **SSL 证书管理**: Runtipi 自动管理 SSL 证书, 确保应用程序的安全连接.
- **快速部署**: 用户可以在几分钟内将应用程序从零部署到生产环境.

**OpenWrt 中的第三方商店:**

![20241229154732_ctFyXsKX.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ctFyXsKX.webp)

OpenWrt 本身存在大量第三方应用, 使用 iStore 方便点.

推荐 2 个源地址:

- [https://dl.photonicat.com](https://dl.photonicat.com/)
- [https://dl.openwrt.ai](https://dl.openwrt.ai/)

**NAS 中的第三方商店:**

![20241229154732_uwDcMglt.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_uwDcMglt.webp)

目前在用的几个第三方源:

- **synocommunity**: https://packages.synocommunity.com/
- **spk7**: https://spk7.imnks.com/
- **云梦:** https://spk.520810.xyz:666
- **4saG SPK Server:** https://spk.4sag.ru/
- **Community Package Hub:** https://www.cphub.net

---

> 我的绝大部分服务都已经通过 Docker 容器化技术部署在不同的设备上. 这种灵活的部署方式不仅提高了资源的利用率, 还使得服务的扩展和管理变得更加便捷.
>
> 选择设备时, 我主要考虑两个因素：资源和网络环境. 不同的服务器或设备可能有不同的计算能力、存储容量和网络连接速度, 因此我会根据服务的具体需求来选择最合适的硬件资源.
>
> 接下来, 我将按照设备的分类, 盘点一下我都安装了哪些自托管服务.

## NAS

2 台群晖 NAS 更多的是肩负着数据存储与同步的重任, 使用一主一备的方式保证重要数据的安全性.

DS218+ 的任务是对外提供 Synology Drive 服务, 我的所有工作文件, 家庭照片全部存储在这上面, 而 DS923+ 则侧重于数据备份与影音文件管理, 首先会全量备份 DS218+ 的数据, 还会为其他设备提供备份服务, 其次为家人提供流媒体服务.

> 这里推荐一个 NAS 相关的高质量玩机网站 - [我不是矿神](https://imnks.com/).

### DS218+

#### Vaultwarden

[Vaultwarden](https://github.com/dani-garcia/vaultwarden) 是一个使用 Rust 编写的非官方 Bitwarden 服务器实现, 它与 [官方 Bitwarden 客户端](https://bitwarden.com/download/) 兼容, 非常适合不希望运行官方的占用大量资源的自托管部署, 它是理想的选择. Vaultwarden 主要面向个人、家庭和小型组织.

![20241229154732_ipFMiyMU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ipFMiyMU.webp)

> 如果最近你的 iOS 客户端无法正常登录使用, 可以将服务端更新到最新版本, 我就是这样解决的.

考虑到安全问题, 目前正在使用 Vaultwarden 全面替代 1Password. 因为 Vaultwarden 强制要求通过 HTTPS 访问, 我目前使用 1Panel 来申请证书, 结合 WAF 使用.

如果只是在内网使用的话, 可以参考使用 [mkcert](https://github.com/FiloSottile/mkcert) 来开启 HTTPS.

为了防止数据丢失, 我做了两重保护:

- 将 Vaultwarden 的数据使用 Drive 实时同步到 DS923+, 然后在 DS923+ 上面也启动一个 Vaultwarden, 避免 DS218+ 挂掉之后无法使用;

- 使用脚本离线备份 Vaultwarden 数据文件:

  ```shell
  #!/bin/bash

  NOW=$(date +"%Y.%m.%d")
  # Vaultwarden 的数据目录
  cd /volume1/docker/0.nas
  # 打包整个目录
  zip -q -r vaultwarden_$NOW.zip vaultwarden/
  # 移动到 Synology Drive 相关目录下, 这样就能通过到其他客户端上, 相当于多端备份
  mv vaultwarden_$NOW.zip /volume1/driver/NAS/Bitwarden
  ```

  然后使用定时任务定期备份:

  ![20241229154732_e8P5IGnz.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_e8P5IGnz.webp)

相关教程:

- [受够了密码数据泄漏事件？用 Bitwarden 做自己的安全负责人](https://sspai.com/post/79183)

- https://github.com/dani-garcia/vaultwarden/wiki/Enabling-HTTPS
- [纯内网使用 Bitwarden](https://blog.cfandora.com/archives/449/#cl-2).

---

#### MyIP

[MyIP](https://github.com/jason5ng32/MyIP) 可能是最好用的 IP 工具箱. 轻松检查你的 IP, IP 地理位置, 检查 DNS 泄漏, 检查 WebRTC 连接, 速度测试, ping 测试, MTR 测试, 检查网站可用性, 查询 Whois 信息等等.

我主要拿来做一些连通性测试:

![20241229154732_WHL8FkrH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_WHL8FkrH.webp)

**特性**:

- 🖥️ **看自己的 IP**：从多个 IPv4 和 IPv6 来源检测显示本机的 IP
- 🕵️ **看 IP 信息**：显示所有 IP 的相关信息, 包括国家、地区、ASN、地理位置等
- 🚦 **可用性检测**：检测一些网站的可用性：Google, Github, Youtube, 网易, 百度等
- 🚥 **WebRTC 检测**：查看使用 WebRTC 连接时使用的 IP
- 🛑 **DNS 泄露检测**：查看 DNS 出口信息, 以便查看在 VPN/代理的情况下, 是否存在 DNS 泄露隐私的风险
- 🚀 **网速测试**：利用边缘网络进行网速测试
- 🚏 **代理规则测试**：配合代理软件的规则设置, 测试规则设置是否正常
- ⏱️ **全球延迟测试**：从分布在全球的多个服务器进行延迟测试, 了解你与全球网络的连接速度
- 📡 **MTR 测试**：从分布在全球的多个服务器进行 MTR 测试, 了解你与全球的连接路径
- 🔦 **DNS 解析器**：从多个渠道对域名进行 DNS 解析, 获取实时的解析结果, 可用于污染判断
- 🚧 **封锁测试**：检查特定的网站在部分国家是否被封锁
- 📓 **Whois 查询**：对域名或 IP 进行 whois 信息查询
- 📀 **MAC 地址查询**：查询物理地址的归属信息
- 🌗 **暗黑模式**：根据系统设置自动切换暗黑/白天模式, 也可以手动切换
- 📱 **简约模式**：为移动版提供的专门模式, 缩短页面长度, 快速查看最重要的信息
- 🔍 **查任意 IP 信息**：可以通过小工具查询任意 IP 的信息
- 📲 **支持 PWA**：可以添加为手机应用以及电脑里的桌面应用, 方便使用
- ⌨️ **支持快捷键**：可以随时输入 `?` 查看快捷键菜单
- 🌍 根据可用性检测结果, 返回目前是否可以访问全世界网络的提示
- 🇺🇸 🇨🇳 🇫🇷 支持中文、英文、法文

---

#### DDNS-GO

[DDNS-GO](https://github.com/jeessy2/ddns-go) 能够自动获得公网 IPv4 或 IPv6 地址, 并解析到对应的域名服务.

![20241229154732_KXWXUX58.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_KXWXUX58.webp)

**特性**:

- 支持 Mac、Windows、Linux 系统, 支持 ARM、x86 架构
- 支持的域名服务商 `阿里云` `腾讯云` `Dnspod` `Cloudflare` `华为云` `Callback` `百度云` `Porkbun` `GoDaddy` `Namecheap` `NameSilo` `Dynadot`
- 支持接口/网卡/[命令](https://github.com/jeessy2/ddns-go/wiki/通过命令获取IP参考)获取 IP
- 支持以服务的方式运行
- 默认间隔 5 分钟同步一次
- 支持同时配置多个 DNS 服务商
- 支持多个域名同时解析
- 支持多级域名
- 网页中配置, 简单又方便, 默认勾选`禁止从公网访问`
- 网页中方便快速查看最近 50 条日志
- 支持 Webhook 通知
- 支持 TTL
- 支持部分 DNS 服务商 [传递自定义参数](https://github.com/jeessy2/ddns-go/wiki/传递自定义参数), 实现地域解析/多 IP 等功能

> 在 [[homelab-network|网络篇]] 中详细的介绍.

---

#### LibreSpeed

[LibreSpeed](https://github.com/librespeed/speedtest) 一个基于 HTML5 的自托管网络速度测试工具. 它支持多种后端语言和数据库, 易于部署和使用, 并提供多种测试选项.

![20241229154732_eMc0tcC3.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_eMc0tcC3.webp)

**特点**:

- **功能丰富**：支持下载、上传、抖动测试, 并提供 IP 地址、ISP、距离等信息.
- **兼容性强**：支持所有现代浏览器, 包括移动端.
- **易于部署**：提供详细的指南和视频教程.
- **支持多种后端语言**：包括 PHP、Node、Go、Rust 等.

---

#### Speedtest Tracker

[Speedtest Tracker](https://github.com/alexjustesen/speedtest-tracker) 是一个自托管应用程序, 可监控互联网连接的性能和正常运行时间.

![20241229154732_HntLQamY.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_HntLQamY.webp)

该应用使用 Ookla 的 Speedtest 服务进行网络速度测试, 并记录测试结果, 帮助我们了解自身网络性能和稳定性.

**重要亮点**:

- **功能**：监控网络性能和稳定性, 记录测试结果, 生成历史数据.
- **部署方式**：容器化, 支持 Docker 和 Docker Compose 部署.
- **数据库支持**：支持 SQLite、/MariaDB 和 PostgreSQL 数据库.
- **优势**：开源免费, 可自定义配置, 适用于各种场景.

---

#### Snapdrop

[Snapdrop](https://github.com/SnapDrop/snapdrop) 是一个基于 WebRTC 的本地文件分享渐进式 Web 应用. 项目使用 HTML5、ES6、CSS3、WebRTC、WebSockets 和 NodeJS 等技术构建, 支持用户在浏览器中快速分享文件.

![20241229154732_5YIDLYVG.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_5YIDLYVG.webp)

**重要亮点**:

- **技术栈**: HTML5、ES6、CSS3、WebRTC、WebSockets、NodeJS
- **功能**: 本地文件分享 **特性**: 支持渐进式 Web 应用
- **许可证**: GPL-3.0
- **开源**: 可在 GitHub 上免费下载和使用

> 方便的点是只要有浏览器即可进行文件共享, 这在与 Android 共享文件时比较方便.

---

#### Memos

[Memos](https://github.com/usememos/memos) 是一款轻量级、自托管的笔记工具, 支持 Markdown 语法, 并提供多种自定义选项.

![20241229154732_fxfM2D7h.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_fxfM2D7h.webp)

**重要亮点**:

- **隐私优先**：所有数据本地存储, 保障用户隐私.
- **快速创建**：支持纯文本和 Markdown 语法, 方便格式化和分享.
- **轻量级**：使用 Go 和 React 构建, 性能强大但占用资源少.
- **可定制**：可自定义服务器名称、图标、样式等.
- **开源免费**：代码开源, 可免费使用所有功能.

macOS 上有免费的客户端-[MoeMemos](https://github.com/mudkipme/MoeMemos):

![20241229154732_fgToqa1H.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_fgToqa1H.webp)

---

#### Homebox

[Homebox](https://github.com/XGHeaven/homebox) 用于组建家庭局域网时, 对网络进行调试、检测、压测的工具集合.

![20241229154732_r6wS9X64.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_r6wS9X64.webp)

**特性**:

1. 面向未来浏览器设计
2. 高达 10G 的浏览器速度测试
3. 自带 Ping 检测
4. 丰富的自定义测速参数
5. 服务端无需像传统文件拷贝一样需要固态的支持
6. 友好的 UI 交互
7. 针对低速网络(< 2.5G)优化测速资源占用

---

#### 1Panel

[1Panel](https://github.com/1Panel-dev/1Panel) 是一款开源的 Linux 服务器运维管理工具. 提供 Web 界面, 支持主机监控、文件管理、数据库管理等功能, 并深度集成 WordPress 和 Halo 等建站软件.

因为现在 1Panel 不支持多主机管理, 所以在大多数常用服务器上都安装了 1Panel.

![20241229154732_IoLQHeCb.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_IoLQHeCb.webp)

**重要亮点**:

- 支持主机监控、文件管理、数据库管理等功能 深度集成 WordPress 和 Halo 等建站软件.
- 提供一键安装指南和文档链接.
- 存在专业版, 提供更多功能和技术支持服务

---

#### Syncthing

[Syncthing](https://syncthing.net/) 是一个开源的文件同步客户端与服务器软件, 采用 Go 语言编写. 它可以在本地网络上的设备之间或通过 Internet 在远程设备之间同步文件, 使用了其独有的对等自由块交换协议.

通过发现服务器寻找节点, 如果节点不能直连的情况下, 通过中继服务器穿透内网传输数据. 用户可以自行搭建发现服务器和中继服务器, 在程序里面也可以指定使用相应的服务器. 并提供基于 Web 的控制界面, 这也便于远程服务器的使用.

![20241229154732_TRIl2gkR.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_TRIl2gkR.webp)

**重要亮点**:

- **私有性**: 文件仅在本地设备上存储, 无中央服务器, 保护数据安全.
- **安全性**: 使用 TLS 加密, 确保通信安全, 并采用证书认证设备.
- **开源**: 源代码开放, 确保透明可信任性.
- **易用性**: 界面简洁, 配置简单, 易于上手.
- **多平台**: 支持 macOS、Windows、Linux 等多种操作系统.

> [[homelab-data|数据篇]] 再详细介绍如何结合 Synology Drive 同步文件的思路.

目前都是在局域网内共享文件, 为了方便放在公司的 R2S 也能同步文件, 需要搭建发现服务和中继服务.

##### 发现服务

Syncthing 依靠发现服务器在互联网上寻找对等点. 任何人都可以运行发现服务器并将 Syncthing 安装指向它.

[discosrv](https://github.com/syncthing/discosrv) 下载并上传服务器后直接运行即可:

```shell
➜  discosrv ./stdiscosrv
stdiscosrv v1.23.4 "Fermium Flea" (go1.20.2 linux-amd64) teamcity@build.syncthing.net 2023-04-05 13:25:55 UTC [purego]
Server device ID is 1111111-2222222-3333333-4444444-5555555-6666666-7777777-8888888
```

拿到发现服务器的 ID 后, 将该 ID 填写至 **Syncthing** 客户端中, 填写位置如下:

![20241229154732_OAInVUPJ.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_OAInVUPJ.webp)

格式为: `https://服务器 IP:port/?id={发现服务器 ID}`.

记得防火墙开启 8443 端口, 发现服务器默认端口为 8443, 若想更改, 可以使用 `./stdiscosrv -listen=你的端口` 来启动.

##### 中继服务

Syncthing 依赖于社区贡献的中继服务器网络. 任何人都可以运行中继服务器, 它会自动加入中继池并可供 Syncthing 用户使用.

[relaysrv](https://github.com/syncthing/relaysrv) 下载并上传服务器后直接运行即可:

```shell
➜  relaysrv ./strelaysrv -pools=""
2024/12/02 15:05:38 main.go:141: strelaysrv v1.22.1 "Fermium Flea" (go1.19.2 linux-amd64) teamcity@build.syncthing.net 2022-11-02 06:27:53 UTC
2024/12/02 15:05:38 main.go:147: Connection limit 52428
2024/12/02 15:05:38 main.go:259: URI: relay://0.0.0.0:{port}/?id=aaaaaaa-bbbbbbb-ccccccc-ddddddd-eeeeeee-fffffff-ggggggg-hhhhhhh&networkTimeout=2m0s&pingInterval=1m0s&statusAddr=%3A22070
```

![20241229154732_Ig5uN2Qn.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Ig5uN2Qn.webp)

格式为:`relay://你的服务器IP:22067/?id=中继服务器ID&networkTimeout=2m0s&pingInterval=1m0s&statusAddr=%3A22070`

注意：

- `-pools=""`: 意思是不加入任何中继池, 可以保持你的中继服务器为私有的;
- 记得开放防火墙 22067 端口, 若想更换端口, 可以使用 `-listen=你的端口` 来更改端口;

---

### DS923+

#### Stirling-PDF

[Stirling-PDF](https://www.stirlingpdf.com/) 是一款功能强大的本地托管 Web PDF 处理工具. 它支持各种 PDF 操作, 如拆分、合并、转换、旋转、压缩等, 并提供了丰富的功能和定制选项, 适用于个人和团队.

![20241229154732_wQbrqMTX.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_wQbrqMTX.webp)

**重要亮点**:

- **本地托管**：无需安装, 通过 Docker 运行, 方便快捷.
- **功能丰富**：支持多种 PDF 操作, 如页面操作、转换操作、安全和权限、操作等.
- **易于定制**：可自定义应用程序名称、标语、图标等.
- **支持多种语言**：目前支持 37 种语言.
- **可扩展性**：支持扩展 OCR 和压缩功能.

---

<!--

#### Zerox OCR

[Zerox OCR](https://github.com/getomni-ai/zerox)

-->

#### Draw.io

[Draw.io](https://github.com/jgraph) 是一款免费且开源的在线绘图工具, 现已更名为 **diagrams.net**. 它支持创建各种图表, 如流程图、网络拓扑图、UML 图、组织结构图等. Draw.io 提供直观的拖放式界面, 支持本地和云端存储（如 Google Drive、OneDrive、GitHub 等）, 适合团队协作和个人使用, 广泛应用于软件开发、项目管理和文档设计等领域.

![20241229154732_TVib1acn.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_TVib1acn.webp)

做开发的朋友应该经常用到, Draw.io 在 IDEA, Visual Studio Code 等常见开发平台上都有集成, 目前使用最多的是 [桌面版](https://github.com/jgraph/drawio-desktop), 支持各大平台.

**相关资源**:

- [drawio-libs](https://github.com/jgraph/drawio-libs)
- [other drawio-libs](https://github.com/JF-Dumont/drawio-libs)
- [使用来自网络的自定义形状库](https://www.drawio.com/blog/public-custom-libraries)

---

#### Excalidraw

[Excalidraw](https://github.com/excalidraw/excalidraw) 是一个开源的虚拟手绘风格白板工具, 支持协作和端到端加密. 它可以帮助用户创建各种手绘风格的图表、线框图或其他图形, 适用于绘图、设计、会议记录等多种场景.

![20241229154732_WTC7w3BE.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_WTC7w3BE.webp)

**主要特点**：

- **无限画布**： 可以自由地拖动、缩放和移动画布, 不受限制.
- **手绘风格**： 支持各种绘图工具, 包括线条、矩形、、箭头等, 并提供丰富的样式选项.
- **自定义**： 可以自定义画布背景、工具栏、颜色等, 满足个性化需求.
- **图片和形状库**： 支持导入图片和形状库, 方便快速创建图形.
- **国际化**： 支持多种语言, 方便全球用户使用.
- **导出功能**： 支持将图形导出为 PNG、SVG 和可复制粘贴的格式, 方便分享和编辑.

> 目前依赖于 Draw.io 源文件可在 Markdown 查看且可直接编辑的特性, Excalidraw 还不具备, `.excalidraw` 格式文件虽然能二次编辑, 但是无法在 Markdown 中预览. 因此 Excalidraw 算备选方案偶尔使用.

---

#### Portainer

[Portainer](https://www.portainer.io/) 一款用于管理和部署 Docker、Swarm 和 Kubernetes 集群的容器管理软件. 它提供集中式界面, 简化容器化进程, 并支持多云和边缘环境.

![20241229154732_GOnzu0wY.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_GOnzu0wY.webp)

**重要亮点**:

- **跨平台管理**：支持 Docker、Swarm 和 Kubernetes, 适用于多云和边缘环境.
- **用户友好的界面**：提供直观的 UI, 简化操作流程.
- **安全访问**：支持集中式验证和授权.
- **多云和边缘支持**：适用于不同环境, 包括数据中心、云和边缘设备.

---

#### 小雅 Alist

[docker-xiaoya](https://github.com/monlor/docker-xiaoya) 使用 Docker Compose 一键部署 Xiaoya 服务的全套解决方案, 支持 Alist + Emby + Jellyfin 的一键部署, 并兼容多种平台和架构.

![20241229154732_wCLUNTfT.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_wCLUNTfT.webp)

**重要亮点**:

- **一键部署**：简化了 Xiaoya 服务的部署流程, 无需人工干预.
- **全平台支持**：兼容 Linux、Windows、Mac、Synology 等平台, 以及 X 和 Arm 架构.
- **集成脚本**：所有脚本集成到 Docker 镜像, 避免污染系统环境.
- **自动更新**：支持自动更新镜像、云盘数据、服务配置和媒体数据.
- **多种云盘支持**：支持小雅 Alist、夸克网盘、PikPak 网盘和阿里云盘资源.

---

#### RSSHub

[RSSHub](https://github.com/DIYgod/RSSHub) 是一个可以将**任何**内容都可以抓取然后转换成 RSS 订阅的网站.

项目的 slogan **万物皆可 RSS**, 它不仅可以订阅各种博客、论坛、新媒体, 甚至社交媒体、推特等都不在话下, 很强, 详见[食用指南](https://docs.rsshub.app/zh/guide/).

该项目已经持续发展 6 年了, 一直在持续更新, 甚至今年[进行了一次重构](https://diygod.cc/6-year-of-rsshub), 不得不佩服大佬们的行动力.

![20241229154732_OObcuEZH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_OObcuEZH.webp)

除此之外, 官方还提供了 [Radar 功能](https://docs.rsshub.app/zh/guide/#radar), 结合浏览器插件就可以发现你正在访问的站点 RSSHub 是否已经支持订阅了, 如果支持了可以一键转换成订阅的地址, 很方便. 不仅如此, 还支持移动端.

![20241229154732_HV9qq6Zt.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_HV9qq6Zt.webp)

**重要亮点**:

- **功能**: 将各种内容源转换为 RSS, 支持超过 5,000 个全球实例.
- **特点**: 易于使用、功能强大、支持丰富的插件和扩展.
- **相关项目**: RSSHub Radar、RSSBud、Aid 等.
- **贡献者**: 超过 1,100 位贡献者.
- **部署**: 支持 GitHub Pages、Vercel 等多种部署方式.

<!--

https://razeen.me/posts/improve-information-sources-with-rss/

-->

---

#### Navidrome

[Navidrome](https://github.com/navidrome/navidrome) 允许用户从任何浏览器或移动设备访问其音乐库, 并提供丰富的功能, 例如处理大型音乐库、支持多种音频格式、多用户支持、自动监控库等.

![20241229154732_ple0Nxse.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ple0Nxse.webp)

**重要亮点**:

- Navidrome 是一个开源音乐服务器项目.
- 支持从任何设备访问音乐库.
- 支持多种音频格式.
- 多用户支持, 每个用户拥有自己的播放等.
- 自动监控音乐库变化.
- 界面基于 Material UI.
- 兼容 Subsonic/Madsonic/Airsonic 客户端.

---

#### Music Tag Web

[Music Tag Web](https://github.com/xhongc/music-tag-web) 是一款可以编辑歌曲的标题, 专辑, 艺术家, 歌词, 封面等信息的音乐标签编辑器程序, 支持 FLAC, APE, WAV, AIFF, WV, TTA, MP3, M4A, OGG, MPC, OPUS, WMA, DSF, DFF, MP4 等音频格式. 我主要使用自动刮削功能来批量修改音乐标签.

只有 V2 版本才具备高级功能, 需要付费使用.

![20241229154732_YQl8DLNI.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_YQl8DLNI.webp)

**特性**:

- 支持大部分音频格式元数据的查看、编辑和修改
- **支持批量自动修改（刮削）音乐标签**
- 支持音乐指纹识别, 即使没有元数据也可以识别音乐
- 支持整理音乐文件, 按艺术家, 专辑分组, 或者自定义多级分组
- 支持文件排序, 按照文件名, 文件大小, 更新时间排序
- 支持批量转换音乐元数据繁体转简体, 或者简体转繁体
- 支持文件名称的拆分解包, 补充缺失元数据信息
- 支持文本替换, 批量替换音乐元数据中脏数据
- 支持音乐格式转换, 引入 ffmpeg 支持音乐格式转换
- 支持整轨音乐文件的切割
- 支持多种音乐标签来源
- 支持歌词翻译功能
- 支持显示操作记录
- 支持导出专辑封面文件, 支持自定义上传专辑封面
- 支持适配移动端 UI, 支持手机端访问
- 支持使用小爱同学播放本地音乐, 播放 NAS 本地音乐

---

#### Roon

[Roon](https://roon.app/en/) 是一款专业的音乐播放和音乐库管理软件，旨在为音乐爱好者提供更丰富、更深入的音乐体验。

DS923+ 安装 Roon 的 Core Server, 将无损音乐全部导入到 Roon, 在 macOS 和 iPhone 就可以方便的听音乐了.

![20241229154732_kR2q8gAJ.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_kR2q8gAJ.webp)

**主要功能**：

- **音乐库管理**： 将所有音乐文件整合到一个中央库中，方便管理和浏览。
- **音乐信息丰富**： 提供艺术家、专辑、歌曲的详细信息，包括传记、评论、照片、歌词、巡演日期等。
- **无缝播放**： 支持多种音乐播放设备和平台， AirPlay、Chromecast、Roon Ready、Squeezebox、智能电视、智能音箱、USB/HDMI 播放器、移动设备等。
- **高保真音质**： 采用专业音频引擎，提供高保真音质，让音乐更真实、更生动。
- **Nucleus**： Roon 的专用服务器，提供更强大的音乐处理能力和更灵活的配置选项。

---

## M920x

M920x 是 x86 平台, 作为 Docker 容器的核心宿主机, 已部署多项服务.

### 雷池 Safeline

![20241229154732_QTQjeMVr.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_QTQjeMVr.webp)

在 [[homelab-network|网络篇]] 中有 WAF 的详细介绍以及应用场景.

### Dify

[Dify](https://github.com/langgenius/dify) 是一个开源的 LLM 应用开发平台. Dify 提供直观的用户界面, 结合 AI 工作流、RAG 管道、代理能力、模型管理、可观察性功能等, 帮助用户快速从原型开发到生产部署.

![20241229154732_2pK3lVHY.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_2pK3lVHY.webp)

**重要亮点**:

- **功能丰富**：支持 AI 工作流、RAG 管道、代理、模型管理、可观察性等功能.
- **模型支持**集成 GPT、Mistral、Llama3 等多种 LLM 模型.
- **易于使用**：提供云端服务、社区版和企业版, 方便用户使用.
- **开源免费**：遵循 Dify 开源许可证, 免费使用.

### Netmaker

[**Netmaker**](https://github.com/gravitl/netmaker) 是一个开源的高性能、基于 **WireGuard** 的 **虚拟网络管理平台**. 它允许用户轻松构建和管理跨地域的安全虚拟网络（VPN）, 适用于云环境、数据中心、物联网 (IoT) 设备等场景. Netmaker 通过自动化网络配置和管理, 大幅降低了运维成本, 并提供了与现有基础设施无缝集成的能力.

![20241229154732_iQxUFXbA.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_iQxUFXbA.webp)

**主要功能**

1. **基于 WireGuard 的高性能网络**: 提供加密、高速的点对点通信, 通过 WireGuard 协议实现低延迟和高安全性.
2. **自动化网络配置**: 自动配置节点、子网和隧道, 大幅减少手动设置和管理步骤.

3. **多平台支持**: 支持 Linux、Windows、macOS, 以及容器化环境（Docker/Kubernetes）.

4. **集中管理界面**: 提供 Web UI 和 API 接口, 便于集中管理网络配置、监控和运维.

5. **动态节点管理**: 支持动态 IP 分配、负载均衡, 以及节点的自动发现和连接.

6. **多云和混合环境支持**: 兼容多种云平台（如 AWS、Azure、GCP）和本地数据中心, 适用于混合云环境.

7. **高可扩展性**: 通过水平扩展支持大规模节点和复杂拓扑, 适用于企业级网络需求.

8. **ACL 和安全规则管理**: 支持访问控制列表 (ACL) 和自定义防火墙规则, 确保网络安全.

### Coolify

[Coolify](https://coolify.io/) 是一款开源且可自托管的平台, 旨在为开发者提供类似 Heroku、Netlify 和 Vercel 的服务. Coolify 支持多种编程语言和框架, 允许用户将应用程序部署到任何服务器, 包括个人服务器、VPS、Raspberry Pi、云服务器等. 该平台提供了丰富的功能, 如推送部署、免费 SSL 证书、自动数据库备份 Webhook 集成、强大的 API 和实时终端等, 旨在提供高效、灵活的开发环境.

![20241229154732_sRYeCMVK.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_sRYeCMVK.webp)

**重要亮点**:

- **兼容性**：Coolify 兼容多种编程语言和框架, 支持静态网站、API、后端、数据库、等多种类型的应用程序.
- **部署灵活性**：支持部署到任何服务器, 包括个人服务器、VPS、Raspberry Pi、云服务器等, 并支持 Docker 和 Docker Swarm.
- **服务多样性**：可以部署任何与 Docker 兼容的服务, 并提供许多一键式服务.
- **集成与自动化**：提供与 GitHub、GitLab、Bitbucket、Gitea 等平台的集成, 支持推送部署和自动数据库备份.
- **安全性**：提供 SSL 证书, 确保数据传输安全, 并允许用户完全控制自己的数据.
- **控制性**：提供强大的 API 和实时终端, 允许用户直接在浏览器中管理服务器, 并与 CI/CD 管道集成.
- **社区和赞助**：Coolify 拥有一个活跃的社区, 并提供赞助商支持.

![20241229154732_XXA3r2Un.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_XXA3r2Un.webp)

> 目前只安装部署了, 还没完全用起来

---

### n8n

[n8n](https://github.com/n8n-io/n8n) 是一款开源的流程自动化工具, 允许用户通过连接各种服务和应用程序来构建自动化流程. 它采用基于节点的编程方式, 易于使用且功能强大.

![20241229154732_5h6yU0pd.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_5h6yU0pd.webp)

**主要特点**：

- **易于使用**： n8n 采用拖放式的节点编辑器, 用户可以轻松地将节点连接起来, 创建复杂的自动化流程.
- **可扩展性**： n8n 支持用户添加自定义节点, 以扩展其功能.
- **丰富的**： n8n 提供了 200 多个集成节点, 包括常用的社交媒体、邮件、数据库、云服务等.
- **开源**： n8n 是开源软件, 用户可以自由地使用、修改和分发它.

**适用场景**：

- **自动化日常任务**： 例如, 自动化邮件发送、数据同步、文件处理等.
- **构建复杂的业务流程**： 例如, 自动化客户关系管理、供应链管理、数据分析等.

相关资源:

- [n8n 的自托管 AI 入门套件](#AI-starter-kit)

- [在本地运行 LLM：5 种最佳方法（+ 自托管 AI 入门套件）](https://blog.n8n.io/local-llm/)
- [在群晖部署 n8n 的一些坑和经验](https://1q43.blog/post/5821/)

<!--

### Cockpit

[Cockpit](https://cockpit-project.org/)

---

-->

### Smokeping

[SmokePing](https://github.com/oetiker/SmokePing) 是一个开源的网络延迟监控系统, 它通过定期测量目标主机的响应时间并生成图形化的结果, 帮助用户实时监控网络性能. 它基于 RRDtool 库进行数据存储和图形展示, 支持多种插件和定制化配置, 适用于各种网络环境和需求.

![20241229154732_zsOwYKR6.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_zsOwYKR6.webp)

**重点功能：**

1. **网络延迟监控**：定期测量目标主机的响应时间, 并生成直观的图形化结果.
2. **动态 IP 支持**能够处理动态 IP 地址, 确保监控的连续性和准确性.
3. **插件扩展**：支持多种插件, 扩展功能, 例如数据源集成、通知系统等.
4. **Web 模板定制**：提供丰富的 Web 模板选项, 方便用户自定义图形界面.
5. **配置文件管理**：提供详细的配置文件, 方便用户根据实际需求进行定制.
6. **跨平台支持**：适用于各种 Unix 系统, 包括 Linux、MacOS 和.
7. **易于集成**：与其他网络监控工具和系统无缝集成.

---

### IT Tools

[IT Tools](https://github.com/CorentinTh/it-tools) 是一个集合了多种开发者常用在线工具的平台, 拥有简洁的界面和良好的用户体验. 它旨在帮助开发者提高工作效率, 轻松处理各种开发任务.

![20241229154732_Y1Y3jCOi.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Y1Y3jCOi.webp)

**重点功能**:

- **在线工具**： 提供多种在线工具, 例如代码格式化、代码压缩、在线 API 测试等, 覆盖开发、测试、文档等多个方面.
- **工具分类**： 工具按照功能分类, 方便用户快速找到所需工具 **自定义工具**： 用户可以自定义添加工具, 满足个性化需求.
- **集成**： 部分工具支持与其他平台集成, 例如 GitHub、GitLab 等.
- **代码示例**： 每个工具都提供代码示例, 帮助用户快速上手.

### Uptime Kuma

[Uptime Kuma](https://github.com/louislam/uptime-kuma) 是一款易于使用的自托管监控工具, 可以监控各种服务的可用性, 例如 HTTP(s)、TCP、Ping、DNS 记录、游戏服务器等. 它具有友好的界面、丰富的通知选项和多种部署方式, 非常适合个人和企业使用.

![20241229154732_kNhdmHz5.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_kNhdmHz5.webp)

**重点功能**:

- **多种监控类型**：支持 HTTP(s)、TCP、Ping、DNS 记录、游戏服务器、Docker 容器等多种监控类型.
- **丰富的通知选项**：支持 Telegram、Discord、Gotify、Slack、Pushover、SMTP 邮件等多种通知方式, 并支持自定义通知模板.
- **友好的界面**：提供响应式、快速的用户界面, 方便用户查看和管理监控数据.
- **多语言支持**：支持多种语言, 方便全球用户使用.
- **多种部署方式**：支持 Docker、Node.js 等多种部署方式, 方便用户根据需求选择合适的部署方式.
- **状态页面**可以创建多个状态页面, 并将状态页面映射到特定的域名.
- **Ping 图表**：可以查看历史监控数据, 并生成 Ping 图表.
- **证书信息**：可以查看监控服务的 SSL/TLS 证书信息.
- **代理支持**：支持代理设置, 方便用户通过代理进行监控.
- **双因素认证**：支持双因素认证, 提高账户安全性.

> 目前主要的监控工具, 使用 [Bark](https://bark.day.app) 进行消息通知.

<!--

M920x 是在 `/mnt/4.860.ssd/Drive/docker/docker-compose` 目录下运行的 uptime-kuma, 数据目录在 `/mnt/4.860.ssd/Drive/docker/docker-data` 中.

-->

### Homepage

<!--

http://192.168.31.7:2000/

https://gethomepage.dev/
https://www.himiku.com/archives/homepage.html

-->

[Homepage](https://github.com/gethomepage/homepage) 是一个高度可定制的个人主页项目, 支持 Docker 和服务 API 集成. 项目提供快速搜索、书签、天气支持等功能, 并集成了超过 100 个服务和第三方应用程序.

![20241229154732_2gDay2gg.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_2gDay2gg.webp)

**重要亮点**:

- **高度可定制**：支持自定义主题、CSS、JS、布局和本地化.
- **快速**：静态生成, 加载速度快.
- **安全**： API 请求都通过代理, 保护 API 密钥安全.
- **服务集成**：集成超过 100 个服务和应用程序, 例如 Radarr、Sonarr 等.
- **信息小部件**：提供天气、时间、搜索等信息小部件.
- **Docker 集成**：支持 Docker 集成和自动服务发现.

相关资源:

- [Dashboard Icons](https://github.com/walkxcode/dashboard-icons)

### Nezha Monitoring

<!--

http://192.168.31.7:8008/

-->

[Nezha Monitoring](https://github.com/nezhahq/nezha) 是一款开源的、轻量级的监控工具, 旨在帮助用户轻松监控服务器和网站状态. 它支持多种监控指标, 包括系统状态、HTTP、TCP、Ping 等, 并提供推送警报、定时任务和 Web 终端等实用功能. 该工具采用 Go 语言开发, 并提供中文和英文文档, 方便用户使用.

![20241229154732_02qgJDlI.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_02qgJDlI.webp)

**主要功能：**

- **服务器监控**： 监控服务器资源使用情况, 包括 CPU、内存、磁盘、网络等.
- **服务监控**： 监控服务器上的服务状态, 例如 Web 服务、数据库服务等.
- **任务管理**： 创建和管理自动化任务, 例如定时任务、脚本执行等.
- **通知管理**： 设置接收服务器状态异常通知, 例如邮件、短信等.
- **DDNS**： 自动更新 DNS 记录, 方便服务器.
- **内网穿透**： 将内网服务器映射到公网, 方便远程访问.
- **设置**： 配置监控项、数据展示等.
- **分组**： 将服务器分组管理.

### APITable

[APITable](https://github.com/apitable/apitable) 是一个面向 API 的低代码平台, 用于构建协作应用程序. 它提供了丰富的功能, 可以帮助用户轻松创建和管理各种应用程序, 例如项目管理、客户关系管理、业务智能等.

![20241229154732_7Ezss4Vw.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_7Ezss4Vw.webp)

**重点亮点**:

- **实时协作**： 支持多人实时协作编辑, 提高团队效率.
- **自动表单**： 自动生成表单, 无需手动编写代码.
- **API 首面板**： 提供直观的 API 面板, 用户使用 API.
- **无限跨表链接**： 支持无限跨表链接, 实现数据关联.
- **强大的行/列权限**： 支持行/列权限控制, 保障数据安全.
- **嵌入式**： 支持嵌入式, 方便用户将 APITable 应用程序集成到其他应用程序中.
- **丰富的数据库-电子表格 UI**： 提供多种视图类型, 例如网格视图、画廊视图、甘特图视图等.
- **丰富的**： 提供多种官方模板, 方便用户快速创建应用程序.
- **机器人自动化**： 支持机器人自动化, 提高工作效率.
- **BI 仪表板**： 提供 BI 仪表板, 方便用户进行数据分析和可视化.
- **可扩展性**： 支持自定义组件、图表、仪表板等, 满足用户个性化需求.

---

### CasaOS

[CasaOS](https://casaos.io/) 是一款基于 Docker 的开源个人云操作系统, 旨在提供简单易用的个人云体验. 它支持丰富的应用程序, 并拥有友好的用户界面, 适合用于搭建媒体中心、私有云、智能家居等场景.

![20241229154732_JQAtbuPc.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_JQAtbuPc.webp)

**重点亮点**：

- **简单易用**：用户界面简洁直观, 易于上手.
- **应用程序丰富**：支持超过 20 个预安装应用程序和 50+ 个社区验证应用程序.
- **兼容性强**：支持 86 和 Raspberry Pi 设备.
- **基于 Docker**：易于扩展和定制.

---

### Open WebUI

[Open WebUI ](https://github.com/open-webui/open-webui) 一个功能丰富、易于使用的自托管 WebUI, 旨在完全离线运行. 它支持各种 LLM 运行器, 包括 Ollama 和兼容 OpenAI 的 API.

![20241229154732_8PC1JmDq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_8PC1JmDq.webp)

**重点亮点**:

- **易于设置**：使用 Docker 或 Kubernetes (kubectl, kustomize 或 helm) 轻松安装, 支持带 :ollama 和 :cuda 标签的镜像.
- **Ollama/OpenAI API 集成**：无缝集成 OpenAI 兼容的 API, 并支持 Ollama 模型.
- **细粒度权限和用户组**：管理员可以创建详细的角色和权限, 确保安全的环境并定制用户体验.
- **免提语音/视频通话**：集成免提语音和视频通话功能, 提供更动态的聊天环境.
- **模型构建器**：通过 Web UI 轻松创建 Ollama 模型, 并支持导入来自 Open WebUI 社区的模型.
- **本地 Python 函数调用工具**：支持在工具工作区中添加纯 Python 函数, 并实现 LLM 与自定义函数的无缝集成.
- **RAG 集成**：支持检索增强生成 (RAG), 将文档交互无缝集成到聊天体验中.
- **Web 搜索功能**：支持使用 SearXNG、Google PSE、Brave Search、serpstack、serper、Serply、DuckDuckGo、TavilySearch、SearchApi 和 Bing 等提供商进行 Web 搜索, 并将结果直接注入到聊天体验中.
- **图像生成集成**：支持使用 AUTOMATIC1111 API、ComfyUI (本地) 和 OpenAI 的 DALL-E (外部) 进行图像生成.
- **多模型对话**：可以轻松与各种模型同时进行对话, 利用它们的独特优势.
- **管道和 Open WebUI 插件支持**：支持将自定义逻辑和 Python 库集成到 Open WebUI 中.

---

### LobeChat

[LobeChat](https://github.com/lobehub/lobe-chat) 是一款功能强大的开源 AI 聊天框架, 致力于打造现代、高效的智能对话体验. 它支持多种 AI 服务提供商, 涵盖文本、图像、语音等多模态交互, 并提供知识库、插件系统、多用户管理等丰富功能, 让用户轻松构建个性化、可扩展的聊天机器人. Lobe Chat 旨在为开发者提供便捷、高效的工具, 推动 AI 聊天技术的发展.

![20241229154732_ff8ygTBy.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ff8ygTBy.webp)

**重点亮点**:

- **多模态支持**： 支持文本、图像、语音等多种模态, 提供更丰富的交互体验.
- **知识库**： 支持文件上传、知识管理和检索, 方便用户管理信息.
- **插件系统**： 支持自定义插件, 扩展, 例如搜索、图像生成等.
- **多用户管理**： 支持多用户登录和权限管理, 适合团队协作.
- **PWA 支持**： 支持渐进式网页应用, 提供类似原生应用的流畅体验.
- **自定义主题**： 支持自定义主题, 满足个性化需求.

---

### MaxKB

[MaxKB](https://github.com/1Panel-dev/MaxKB) 是一款基于大语言模型和 RAG 的开源知识库问答系统, 广泛应用于智能客服、企业内部知识库、学术研究与教育等场景.

![20241229154732_hOhYdKMO.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_hOhYdKMO.webp)

**重点亮点**:

- **开箱即用**：支持直接上传文档/自动爬取在线文档, 支持文本自动拆分、向量化和 RAG（检索增强生成）, 有效减少大模型幻觉, 智能问答交互体验好.
- **模型中立**：支持对接大模型, 包括本地私有大模型（Llama 3 / Qwen 2 等）、国内公共大模型（通义千问 / 腾讯混元 / 字节豆包 / 百度千帆 / 智谱 AI / Kimi 等）和国外公共大模型（OpenAI / Claude / Gemini 等）.
- **灵活编排**：内置强大的工作流引擎和函数库, 支持编排 AI 工作过程, 满足复杂业务场景下的需求 **无缝嵌入**：支持零编码快速嵌入到第三方业务系统, 让已有系统快速拥有智能问答能力, 提高用户满意度.

### One API

[One API](https://github.com/songquanpeng/one-api) 是一个 OpenAI 接口管理 & 分发系统, 支持多种大模型, 包括 Azure OpenAI API、Anthropic Claude、Google PaLM2/Gemini、智谱 ChatGLM、百度文心一言、阿里通义千问、讯飞星火认知、360 智脑以及腾讯混元等.

![20241229154732_vtlqwol5.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_vtlqwol5.webp)

**重点亮点**:

- **支持多种大模型**：无需切换 API, 即可通过统一的 API 格式访问所有大模型.
- **支持 stream 模式**：通过流式传输实现打字机效果, 提供更流畅的交互体验.
- **支持多机部署**：方便用户进行和升级.
- **支持令牌管理**：设置令牌的过期时间、额度、允许的 IP 范围以及允许的模型访问.
- **支持兑换码管理**：支持批量生成和导出兑换码, 方便用户进行充值.
- **支持用户分组和渠道分组**：支持为不同分组设置不同的倍率.
- **支持模型映射**：重定向用户的请求模型方便用户进行自定义.
- **支持失败自动重试**：提高系统的健壮性.
- **支持绘图接口**：方便用户进行绘图操作.
- **支持丰富的自定义设置**：包括系统名称、logo、页脚、首页、关于页面等.
- **支持系统访问令牌调用管理 API**：方便用户进行扩展和自定义.

同类产品:

- [One Hub](https://github.com/MartialBE/one-hub?tab=readme-ov-file)

---

### Gitea

[Gitea](https://github.com/go-gitea/gitea) 是一个开源的 Git 服务软件, 旨在提供易于使用且功能强大的自托管 Git 仓库托管平台. 它支持多种平台和架构, 并提供代码审查、团队协作等功能, 非常适合个人或团队进行软件开发. Gitea 的社区活跃, 文档完善, 易于扩展, 是构建自托管 Git 服务器的理想选择.

![20241229154732_epp5JO9j.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_epp5JO9j.webp)

**重点亮点**:

- **跨平台支持**：Gitea 支持 Linux、macOS、Windows 等平台, 并兼容多种架构.
- **功能丰富**：提供 Git 仓库托管、代码审查、团队协作、包管理等功能.
- **易于使用**：界面简洁易用, 新手也能快速上手.
- **开源免费**：Gitea 是开源软件, 免费使用.
- **社区活跃**：拥有庞大的社区和贡献者群体, 问题解决和功能迅速.

#### 部署

```yaml
networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea:1.22.3
    container_name: gitea
    environment:
      - USER_UID=1002
      - USER_GID=1002
      - GITEA__database__DB_TYPE=mysql
      - GITEA__database__HOST=192.168.31.7:3306
      - GITEA__database__NAME=gitea
      - GITEA__database__USER={username}
      - GITEA__database__PASSWD={password}
    restart: always
    networks:
      - gitea
    volumes:
      - /mnt/4.860.ssd/docker/gitea:/data
      - /home/git/.ssh/:/data/git/.ssh
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3400:3000"
      - "2222:22"
```

1. USER_UID 和 USER_GID 使用 git 用户 id;
2. 使用自建 MySQL;
3. 自定义 gitea 存储目录: /mnt/4.860.ssd/docker/gitea ([后期备份](https://docs.gitea.cn/administration/backup-and-restore/));
4. 添加 `/home/git/.ssh/` 用于 SSH 直通;

#### SSH 直通

1. 主机上生成 key

   ```bash
   sudo -u git ssh-keygen -t rsa -b 4096 -C "Gitea Host Key"
   ```

2. 主机上创建脚本: `/usr/local/bin/gitea`, 并赋予执行权限: `chmod +x /usr/local/bin/gitea`

   ```bash
   ssh -p 2222 -o StrictHostKeyChecking=no git@127.0.0.1 "SSH_ORIGINAL_COMMAND=\"$SSH_ORIGINAL_COMMAND\" $0 $@"
   ```

3. 主机上添加 `authorized_key`:

   ```bash
   echo "$(cat /home/git/.ssh/id_rsa.pub)" >> /home/git/.ssh/authorized_keys
   ```

4. 在 gitea 上添加 ssh 配置后进行下面的配置:

   ```bash
   vim /mnt/4.860.ssd/docker/gitea/gitea/conf/app.ini

   [server]
   DOMAIN = gitea.lan
   SSH_DOMAIN = gitea.lan
   ROOT_URL = http://gitea.lan:3400/
   ```

主要是将 ip 修改为域名:

客户机配置 1. 添加 hosts: `192.168.31.7 gitea.lan`

5. 添加 .ssh/config 配置:

   ```bash
   Host gitea.lan
       HostName gitea.lan
       User git
       Port 2222
       IdentityFile ~/.ssh/server
   ```

测试: `ssh -T git@gitea.lan`:

```txt
Hi there, xxx! You've successfully authenticated with the key named xxx.yyy, but Gitea does not provide shell access.
If this is unexpected, please log in with password and setup Gitea under another user.
```

---

### Jellyfin 代理配置

新建 `/etc/default/jellyfin_proxy.env` 并添加:

```shell
http_proxy=192.168.1.88:7890
https_proxy=192.168.1.88:7890
all_proxy=socks5://192.168.1.88:8080
```

修改 `/etc/systemd/system/jellyfin.service.d/override.conf`:

```shell
[Service]
EnvironmentFile = /etc/default/jellyfin_proxy.env
```

重启:

```shell
sudo systemctl daemon-reload && sudo systemctl restart jellyfin.service
```

Jellyfin 有个坑点, 至少对于我测试的两个地址: 一个是环回地址 (127.0.0.1), 一个是局域网地址 (192.168.31.88, 使用局域网的另一台设备做代理服务器) 来说, 设置环境变量时不能加上协议头 (`http://` 或 `https://`), 否则就算设置成功也不会生效, 不清楚是不是 Jellyfin 的玄学 bug, 亦或者说是神奇 feature 😑. 所以上文写的都是没有加协议头的配置, 可以走代理并正常工作, 加了即使设置成功, 在 Jellyfin 里也无效 ~(然而在其他环境这两个环境变量的协议头是可加可不加的, 不影响)~.

### Nginx Proxy Manager

[Nginx Proxy Manager](https://nginxproxymanager.com/) 是一个基于 Docker 的 Nginx 反向代理管理工具, 它提供了简单易用的界面来管理 Nginx 代理主机.

![20241229154732_VO44KEDv.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VO44KEDv.webp)

**重点亮点**:

- **简单易用**：无需深入了解 Nginx 或 Let's Encrypt, 即可轻松创建转发域名、重定向、流和 404 主机.
- **免费 SSL**：支持 Let's Encrypt 自动续订 SSL 证书, 或提供自定义 SSL 证书.
- **功能丰富**：提供访问列表、基本 HTTP 认证、高级 Nginx 配置、用户管理、权限控制和审计日志等功能.
- **适用于家庭网络**：可以轻松将家庭网络中的网站托管在公网上, 并支持端口转发和域名指向设置.

使用 DNSPOD 时报错:

```
ModuleNotFoundError: No module named 'zope' #2440
```

[Fetching Title#rlbf](https://github.com/NginxProxyManager/nginx-proxy-manager/issues/2440)

解决方法:

```shell
# 进入 docker 容器
docker exec -it /bin/bash xxxx
pip install certbot-dns-dnspod
pip install zope -i https://pypi.tuna.tsinghua.edu.cn/simple
```

申请证书时报错:

```
Another instance of Certbot is already running
```

解决方法:

```
find / -type f -name '.certbot.lock' -exec rm {} \;
```

---

### 1Panel

使用 1Panel 安装了 `OpenResty`, 并创建了静态站点, 用于生成 Surge 的规则. 为了方便文件共享编辑, 将`/mnt/lankxin.u/docker/docker-compose/sub/data/subconverter/rules/ACL4SSR` 通过软链接的方式添加到了 `/opt/1panel/apps/openresty/openresty/www/sites/ACLSSR/index` 目录下, 配置后报 **404 问题**.

官方给的解决版本是设置 `disable_symlinks off`, 但是并不能解决上述问题, 因为默认就是 off:

![20241229154732_aZ8ulzeH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_aZ8ulzeH.webp)

问题的原因是 OpenResty 使用 docker 容器启动, 进入容器查看发现识别不了 `/mnt/lankxin.u/docker/docker-compose/sub/data/subconverter/rules/ACL4SSR` 目录, 因此需要将此目录映射到容器中:

![20241229154732_CHLTtY12.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_CHLTtY12.webp)

---

### Hishtory

[Hishtory](https://github.com/ddworken/hishtory) 是一个更好的 shell 历史记录. 它将您的 shell 历史记录存储在上下文中（哪个目录中运行命令、命令是否成功或失败、花费了多长时间等）. 所有这些都存储在本地并进行端到端加密, 以便同步到其他计算机. 所有这些都可以通过`hishtory`CLI 轻松查询. 意思是能够在多台设备之间同步命令行记录.

![20241229154732_bPhPdPuS.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_bPhPdPuS.webp)

安装方式非常简单:

```
curl https://hishtory.dev/install.py | python3 -
```

然后重新打开一个 shell(如果你使用 zsh, 直接 source .zshrc 也行), 使用 `Control+R` 即可查看历史记录. 使用 `hishtory status` 查看状态与密钥, 然后在另一台主机上通过上述命令安装, 并使用 `hishtory init {密钥}` 来同步历史记录.

#### hishtory-server

当然也可以执行部署 `hoshtory-server` 来作为多台主机历史记录的同步服务器:

```yaml
services:
  hishtory-server:
    image: lscr.io/linuxserver/hishtory-server:latest
    container_name: hishtory-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - HISHTORY_SQLITE_DB=/config/hishtory.db #optional
    ports:
      - 4000:8080
    restart: unless-stopped
```

然后修改各个主机中的 `hishtory` 配置(我使用 `oh-my-zsh`, 所以直接修改 .zshrc 即可):

```shell
export PATH="$PATH:/Users/dong4j/.hishtory"
# 添加这一行
export HISHTORY_SERVER="http://{hoshtory-server 的 IP}:4000"
source /Users/dong4j/.hishtory/config.zsh
```

最后重新加载配置:

```shell
source .zshrc
```

这样就能使用自托管的 `hoshtory-server` 在多个主机之间同步命令行历史记录了.

---

### 常用中间件

#### MediaMTX

[MediaMTX](https://github.com/bluenviron/mediamtx) 是一款功能强大的实时媒体服务器和媒体代理, 支持视频和音频流的发布、读取、代理、录制和播放. 它可以将不同协议的媒体流进行路由, 实现多种媒体流的互联互通.

我目前主要用来播放树莓派摄像头上的视频:

![20241229154732_cwXHOY7g.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_cwXHOY7g.webp)

> [[raspberry-pi-stream|树莓派结合 MediaMTX/WVP + ZLMediaKit 实现视频流播放的教程]]

**主要功能**：

- **支持多种协议**： 支持 SRT、WebRTC、RTSP、RTMP、HLS 等多种主流媒体协议, 兼容性良好.
- **实时处理**： 可实时处理媒体流, 包括转换、解码、编码、压缩等操作.
- **多路复用**： 可同时处理多个媒体流, 并提供不同的访问路径.
- **录制和回放**： 可将媒体流录制到磁盘, 并支持回放.
- **安全认证**： 支持用户认证和访问控制, 保障媒体流的安全.
- **灵活配置**： 提供丰富的配置选项, 可满足不同场景的需求.

#### WVP PRO + ZLMediaKit

[WVP PRO](https://github.com/648540858/wvp-GB28181-pro) 是一个基于 GB28181-2016 标准实现的开箱即用的网络视频平台, 负责实现核心信令与设备管理后台部分, 支持 NAT 穿透, 支持海康、大华、宇视等品牌的 IPC、NVR 接入. 支持国标级联, 支持将不带国标功能的摄像机/直播流/直播推流转发到其他国标平台, 流媒体服务基于 [ZLMediaKit](https://github.com/ZLMediaKit/ZLMediaKit).

![20241229154732_u8EjJ7jh.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_u8EjJ7jh.webp)

**特性**:

- 实现标准的 28181 信令, 兼容常见的品牌设备, 比如海康、大华、宇视等品牌的 IPC、NVR 以及平台.
- 支持将国标设备级联到其他国标平台, 也支持将不支持国标的设备的图像或者直播推送到其他国标平台
- 前端完善, 自带完整前端页面, 无需二次开发可直接部署使用.
- 完全开源, 且使用 MIT 许可协议. 保留版权的情况下可以用于商业项目.
- 支持多流媒体节点负载均衡.

#### JSON Crack

[JSON Crack](https://github.com/AykutSarac/jsoncrack.com) 专注于简化 JSON 数据的处理和可视化. 它通过将 JSON 数据转换为交互式图表, 帮助用户更直观地理解数据结构和关系. 此外, 它还提供格式化、验证、代码生成等功能, 支持多种数据格式, 是处理 JSON 数据的理想选择.

![20241229154732_IxKLtILH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_IxKLtILH.webp)

**重点**：

- **可视化 JSON 数据**： 将复杂的 JSON 结构以图表形式展现, 方便用户快速理解和分析数据.
- **格式化与验证**： 自动格式化 JSON 数据, 并提供验证功能, 确保数据格式正确.
- **多种格式支持**： 支持多种数据格式, 包括 JSON、YAML、CSV、XML 和 TOML, 满足不同需求.

**亮点**：

- **交互式体验**： 通过交互式图表, 用户可以展开和折叠数据结构, 探索数据细节.
- **易于使用**： 界面简洁直观, 操作简单, 即使是非技术用户也能轻松上手.
- **安全可靠**： 数据处理完全在本地进行, 无需上传或存储数据, 确保用户隐私安全.
- **多功能性**： 除了可视化, 还提供格式化、验证、代码生成等功能, 满足 JSON 数据处理的全面需求.

相关资源:

- [JSON Crack VS Code 插件](https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode)
- [IDEA 中的插件](https://plugins.jetbrains.com/plugin/22308-jsoncrack)

##### 部署

```bash
git clone git@github.com:AykutSarac/jsoncrack.com.git
cd jsoncrack.com
docker build -t jsoncrack .
docker-compose up -d
```

<!-- 下面全部使用 1Panel 部署 -->

其他一些常用的开发中间件全部使用 1Panel 部署:

- mongodb
- nacos
- kafka
- mysql
- postgresql
- emqx
- redis

## AI.Station

这台主机因为耗电量有点高, 只会在使用时开一下, 目前主要用作 AI 相关的测试环境, 后期打算换成 22G 版本的 2080Ti 玩一玩.

### Stable Diffusion

[Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 是一个基于 Gradio 库实现的 Stable Diffusion 模型的网页界面. 它提供了一系列功能, 方便用户使用 Stable Diffusion 模型进行图像生成和编辑.

就是看了 [这篇文章](https://medium.com/@croath/%E4%BD%8E%E6%88%90%E6%9C%AC%E4%BD%93%E9%AA%8C%E7%94%9F%E6%88%90-ai-%E5%B0%8F%E5%A7%90%E5%A7%90%E7%85%A7%E7%89%87-85ffa7c13cd7)开始入坑的, 可以说是因为 **Stable Diffusion** 组装了 **AI.Station** 这台主机, 也是我尝试的第一款 AI 工具, 目前博客的 cover 图片也是通过它来生成的.

![20241229154732_tkgmSIsV.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_tkgmSIsV.webp)

**主要功能**：

- **图像生成**：支持 txt2img 和 img2img 模式, 可以输入文字描述生成图像, 或将图像作为输入进行风格迁移或内容编辑.
- **图像编辑**：支持 outpainting、inpainting、color 等功能, 可以扩展图像内容、修复图像缺陷或改变图像颜色.
- **模型扩展**：集成了 GFPGAN、CodeFormer、RealESRGAN、ESRGAN、SwinIR、Swin2SR、LDSR 等模型, 可以修复人脸、修复图像、提升图像分辨率等.
- **参数控制**：提供丰富的参数设置选项, 包括采样方法、注意力机制、生成参数等, 可以控制图像生成的风格和质量 **批量处理**：支持批量处理图像, 可以同时生成多张图像.
- **自定义脚本**：支持自定义脚本, 可以扩展功能或实现特定需求.

**其他特点**：

- **易于使用**：网页界面简洁易用, 操作方便.
- **跨平台**：支持 Windows、Linux、macOS 等操作系统.
- **开源**：开源代码, 方便用户学习和改进.

#### 相关资源

##### 模型资源

- [9 个 Stable Diffusion 模型网站](https://www.mdnice.com/writing/a6c04462013e469793b3ff41830a7b08)
- [Stable Diffusion 常用模型下载与说明](https://blog.csdn.net/libaiup/article/details/139167972)

##### 教程

- [Stable Diffusion 教程](https://github.com/ai-vip/stable-diffusion-tutorial)
- [外婆都能看懂的 Stable Diffusion 入门教程](https://www.uisdc.com/stable-diffusion-3)
- [万字长文：Stable Diffusion 保姆级教程](https://blog.csdn.net/jarodyv/article/details/129387945)
- [超详细的胎教级 Stable Diffusion 使用教程](https://mp.weixin.qq.com/s/eFi-xoVDQomzCBr5kO9nHA)
- [视频教程-Stable Diffusion 教程 从入门到精通](https://www.youtube.com/playlist?list=PL4L5yXcAegdxwcD2RRffQntmXygv26auT)

#### 相关问题

```
ImportError: Using SOCKS proxy, but the 'socksio' package is not installed. Make sure to install httpx using `pip install httpx[socks]`.
```

```shell
pip install 'httpx[socks]'
```

> zsh 环境不能直接使用 `pip install httpx[socks]`, 这是 Zsh 的路径扩展机制导致的问题, 它会尝试将方括号 [] 视为通配符

验证:

```
python -c "import httpx; print(httpx.__version__)"
```

然而上述操作并无法解决, 下面才是正确的方法:

```
unset all_proxy && unset ALL_PROXY
```

因为我开启了终端代理, 需要先关闭代理.

### ComfyUI

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) 是一个功能强大的扩散模型图形界面、API 和后端工具, 提供基于图//流程图的界面, 让您无需编写代码即可设计和执行复杂的稳定扩散工作流程.

![20241229154732_rUrd5dZq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_rUrd5dZq.webp)

**主要特点**：

- **图形界面**： 使用节点/图/流程图界面, 无需代码即可设计和执行工作流程.
- **兼容多种模型**： 支持 SD1.x、SD2.x、SDXL、Stable Video Diffusion、Stable、SD3 和 Stable Audio 等多种扩散模型.
- **高效管理**： 异步队列系统、智能内存管理、仅重执行更改部分等优化功能.
- **模型兼容**： 支持加载 ckpt、safetensors 和 diffusers 模型/检查点, 以及独立的 VAE 和 CLIP 模型.
- **文本处理**： 支持嵌入/文本反转、Loras (regular, locon 和 loha)、超网络等文本功能.
- **工作流程管理**： 可以从 PNG、WebP 和 FLAC 文件加载包含种子的工作流程, 并保存/加载工作流程为 JSON 文件.
- **多种工具**： 支持区域合成、修复、ControlNet 和 T2I-Adapter、升采样模型 (ESRGAN、SwinIR、Swin2SR 等)、unCLIP 模型、GLIGEN、模型合并、LCM 模型和 Loras、XL Turbo、AuraFlow、HunyuanDiT、TAESD 隐式预览等功能.
- **离线工作**： 完全离线工作, 无需下载任何内容.
- **配置文件**： 可以通过配置文件设置模型搜索路径.

> ConfyUI 官网的 [桌面版](https://github.com/Comfy-Org/desktop) 最近开始公测了, 下载地址:
> Windows (NVIDIA) NSIS x64: [Download](https://download.comfy.org/windows/nsis/x64)
> macOS ARM: [Download](https://download.comfy.org/mac/dmg/arm64)

#### 相关资源

- [ComfyUI 入门和进阶指南](https://www.uisdc.com/zt/comfyui)
- [系列教程](https://comfyui-wiki.com/zh/tutorial)
- [RunComfy 的教程](https://www.runcomfy.com/zh-CN/tutorials)
- [视频教程-ComfyUI 入门到精通](https://www.youtube.com/playlist?list=PL4L5yXcAegdy6aZGttxu2lVhjSaYVAquX)
- [视频教程-ComfyUI 系统教程](https://www.youtube.com/playlist?list=PLPr2bJ5ZkFrx4MmCLHemoHC3qWEGk6XN1)

### AI starter kit

[Self-hosted AI starter kit](https://github.com/n8n-io/self-hosted-ai-starter-kit) 是一个开源的 Docker Compose 模板, 旨在快速搭建本地 AI 和低代码开发环境. 它由 **[n8n](#n8n)** 精心打造, 集成了自托管 n8n 平台和一系列兼容的 AI 产品和组件, 让您可以轻松开始构建自托管的 AI 工作流程.

![20241229154732_38N0rSw2.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_38N0rSw2.webp)

**主要功能**：

- **自托管 n8n 平台**：低代码平台, 拥有超过 400 个集成和高级 组件.
- **Ollama**：跨平台 LLM 平台, 可安装和运行最新的本地 LLM.
- **Qdrant**：开源、高性能向量存储, 拥有全面的 API.
- **PostgreSQL**：数据工程领域的“工作马”, 安全处理大量数据.

> 我还是用 ChatGLM4 把, 至少上面的问题它能回答出来:
>
> ![20241229154732_AlTfxeF4.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_AlTfxeF4.webp)

#### 安装 Nvidia 容器工具包

1. 配置存储库

   ```bash
   curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
       | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
   curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
       | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
       | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
   sudo apt-get update
   ```

2. 安装工具包

   ```bash
   sudo apt-get install -y nvidia-container-toolkit
   ```

#### 配置 Docker 以使用 Nvidia 驱动程序

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

上述命令在 `/etc/docker/daemon.json` 添加如下内容:

```json
"runtimes": {
      "nvidia": {
          "args": [],
          "path": "nvidia-container-runtime"
      }
  }
```

#### 部署

```bash
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
docker compose --profile gpu-nvidia up -d
```

> 如果需要在非本机上访问 WebUI, environment 需要添加 `N8N_SECURE_COOKIE=false`.

启动后需要耐心等待 `llama3.2:latest` 模型下载完成后才能执行聊天. 下载模型花了大概 10 分钟:

![20241229154732_xut64rTN.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_xut64rTN.webp)

---

## MBP

macOS 下推荐使用 [OrbStack](https://orbstack.dev/) , 它是一款替代 Docker Desktop 的轻量级 Docker 和 Linux 运行环境. 它具有启动快、占用资源少、易于集成等特点, 并提供容器、Kubernetes 和 Linux 发行版等功能.

![20241229154732_jbwSIPKq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_jbwSIPKq.webp)

**重要亮点**:

- **轻量级**：占用资源少, 对电池续航影响小.
- **速度快**：启动速度快, 网络性能优异.
- **易于集成**：与 Docker Desktop 兼容, 支持远程 SSH 和文件共享.
- **功能丰富**：支持容器、Kubernetes 和 Linux 发行版等功能.
- **性能优异**：在性能测试中优于 Docker Desktop.

### LM Studio

[LM Studio](https://lmstudio.ai/) 是一个可以本地运行大型语言模型（LLM）的工具, 用户无需连接互联网即可在电脑上运行各种 LLM, 包括 Llama、Mistral、Phi 等

![20241229154732_ziXFTeHa.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ziXFTeHa.webp)

**重点亮点**:

- **本地运行**：无需连接互联网, 在本地电脑上运行 LLM.
- **模型库丰富**：支持多种 LLM 模型, 包括 Llama、Mistral、Phi、Gemma、DeepSeek、Qwen2.5 等.
- **文档对话**：可以与本地文档进行对话, 获取信息或生成内容.
- **多种接口**：支持通过 Chat UI 或 OpenAI 兼容的本地服务器使用模型.
- **模型下载**：可以下载 Hugging Face 上的任何兼容模型文件.
- **隐私保护**：不收集用户数据, 保护用户隐私.

**优势**:

- **无需互联网**：随时随地使用 LLM, 不受网络限制.
- **隐私保护**：保护用户数据安全, 避免数据泄露风险.
- **功能丰富**：满足多种 LLM 应用需求.
- **易于使用**：简洁的界面, 易于上手.

![20241229154732_ehBTUUoX.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ehBTUUoX.webp)

目前是我主要使用的本地 LLM 工具, 且兼容 OpenAI API, 这样我就可以在其他需要 LLM 的应用中使用.

### Ollama 相关问题

```shell
# 允许跨域
launchctl setenv OLLAMA_ORIGINS "*"
# 更改模型位置
launchctl setenv OLLAMA_MODELS "/Users/dong4j/Library/CloudStorage/SynologyDrive-AI/models/ollama"
# 修改 bind
launchctl setenv OLLAMA_HOST "0.0.0.0"
```

这里补充一下如果是在 Docker 中安装, 有可能会遇到 [Unable to make cors work in docker container](https://github.com/ollama/ollama/issues/3365) 问题, 不过最新版本已经修复了.

## Mac mini 2018

作为最后一代支持 Intel 芯片的 macOS 主机, 二手已经卖不起价了, 所以留着当台服务器用. 最大的问题就是发热严重, 现在散热风扇 24 小时开着, 一点不敢怠慢, 希望还能多用几年.

### Rsync Server

Mac mini 2018 通过雷雳 3 连接着一个 8T 的 LaCie d2 Professional, 用作重要数据的冗余备份.

目前通过 Rsync 将 DS923+ 上的重要数据同步到 LaCie d2 上. 具体的配置方式将在 [[homelab-data|数据篇]] 详细说明, 主要涉及到 Rsync 的 Server 启动模式以及 macOS 上的自启动配置.

![20241229154732_9bWUOu7s.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_9bWUOu7s.webp)

### V2ray

另一种 VPN 方案, 使用 Surge 作为客户端连接家中的设备和服务:

> 使用 V2ray 只作为连接家中网络, 不作其他用途.

```yaml
services:
  v2ray:
    command: "v2ray -config /srv/docker/v2ray/config.json"
    image: "v2ray/official:latest"
    restart: always
    ports:
      - "54321:54321"
    volumes:
      - "/path/to/data:/srv/docker/v2ray"
```

`config.json` 配置如下:

```json
{
  "inbounds": [
    {
      "port": 54321,
      "protocol": "vmess",
      "settings": {
        "clients": [
          {
            "id": "ac2a5d46-a3c4-4c35-9db1-614f403dedff",
            "alterId": 64
          }
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {}
    }
  ]
}
```

Surge 配置如下:

```
💻 V.Intel = vmess, your.domain.name, 54321, username=ac2a5d46-a3c4-4c35-9db1-614f403dedff
```

---

### NextChat

[NextChat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) 是一个基于 ChatGPT 和 Gemini 的跨平台应用, 支持 Web、PWA、Linux、Windows、MacOS 等多种平台. 它可以帮助用户一键部署自己的 ChatGPT 应用, 并提供 GPT3、GPT4 和 Gemini Pro 等多种 AI 模型支持.

![20241229154732_TdYndv4v.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_TdYndv4v.webp)

**重点亮点**:

- **一键部署**：只需在 Vercel 上进行简单操作, 即可在 1 分钟内完成部署.
- **轻量级**：Linux/Windows/MacOS 版本的客户端体积小巧（约 5MB）, 易于安装和使用.
- **兼容自部署模型**：支持与自部署的 LLM 模型（如 RWKV-Runner 和 LocalAI）无缝配合.
- **隐私保护**：所有数据都保存在本地浏览器中, 确保用户隐私安全.
- **丰富的功能**：支持 Markdown、响应式设计、深色模式、PWA 等功能, 并提供预制角色海量内置 prompt 列表.
- **多语言支持**：支持英语、简体中文、繁体中文、日语、西班牙语等多种语言.

### ChatGPT on WeChat

[ChatGPT on WeChat](https://github.com/zhayujie/chatgpt-on-wechat) 是基于大模型搭建的聊天机器人, 同时支持 微信公众号、企业微信应用、飞书、钉钉 等接入, 可选择 GPT3.5/GPT-4o/GPT-o1/ Claude/文心一言/讯飞星火/通义千问/ Gemini/GLM-4/Claude/Kimi/LinkAI, 能处理文本、语音和图片, 访问操作系统和互联网, 支持基于自有知识库进行定制企业智能客服.

![20241229154732_G3FSok7x.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_G3FSok7x.webp)

[效果演示](https://cdn.link-ai.tech/doc/cow_demo.mp4)

### Dify on WeChat

[Dify on WeChat](https://github.com/hanfangyuan4396/dify-on-wechat) 项目为 [chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat) 下游分支, 额外对接了 LLMOps 平台 [Dify](https://github.com/langgenius/dify), 支持 Dify 智能助手模型, 调用工具和知识库, 支持 Dify 工作流.

![20241229154732_s934kJDk.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_s934kJDk.webp)

Dify 接入微信生态的详细教程请查看文章 [**手摸手教你把 Dify 接入微信生态**](https://docs.dify.ai/v/zh-hans/learn-more/use-cases/dify-on-wechat).

## Mac mini M2

Mac mini M2 主要作为 AI 辅佐主机, 部署了一些小模型来辅佐 RAG 的建设, 比如:

- reranker
- m3e-large

## 软路由

### R2S

#### AdGuard Home

[AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) 是一款免费开源的网络广告和跟踪器屏蔽软件, 它通过充当 DNS 服务器来阻止跟踪域, 从而防止您的设备连接到这些服务器.

![20241229154732_wJLNXSok.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_wJLNXSok.webp)

**特性**:

- **网络级保护**： AdGuard Home 可以覆盖您家中所有设备的网络, 无需在设备上安装任何客户端软件.
- **强大的功能**： 它不仅能够屏蔽广告和跟踪器, 还可以阻止恶意软件、钓鱼网站、成人内容, 并强制进行安全搜索.
- **自定义规则**： 您可以添加自定义规则来屏蔽特定网站或广告.
- **易于使用**： AdGuard Home 非常易于设置和使用, 即使是非技术用户也可以轻松上手.
- **开源**： AdGuard Home 是开源软件, 这意味着您可以查看其源代码, 并根据自己的需求进行修改和扩展.

R2S 的 OpenWrt 固件自带 **AdGuard Home** 服务, 目前主要用来拦截广告.

---

#### OpenClash

[OpenClash](https://github.com/vernesong/OpenClash) 是一个基于 OpenWrt 的 **Clash** 客户端插件, 旨在为 OpenWrt 路由器用户提供强大的网络代理管理功能. OpenClash 支持多种代理协议（如 VMess、Shadowsocks、Trojan 等）, 并允许用户灵活配置规则进行流量分流.

![20241229154732_tsSGCxrN.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_tsSGCxrN.webp)

**特性**:

- **图形化管理界面**：通过 OpenWrt 的 Luci 界面, 用户可以轻松配置和管理 Clash.

- **多配置文件支持**：允许用户切换和管理多个代理配置文件.

- **实时日志与调试工具**：便于用户查看代理运行状态并快速排查问题.

- **自动化更新**：支持订阅配置文件和规则的自动更新, 保持最新网络环境.

#### SmartDNS

[SmartDNS](https://github.com/pymumu/smartdns) 一个运行在本地的 DNS 服务器, 旨在通过获取最快的网站 IP 地址来提高网络访问速度. 它支持 DoH 和 DoT 协议, 并兼容多种操作系统, 如树莓派、OpenWrt 和 Windows.

![20241229154732_PmqxAXjC.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_PmqxAXjC.webp)

**特性**:

- **多虚拟 DNS 服务器**： 支持多个虚拟 DNS 服务器, 每个服务器拥有不同的端口、规则和客户端, 实现不同场景下的需求.
- **多 DNS 上游服务器**： 支持配置多个上游 DNS 服务器, 并行查询并返回访问速度最快的解析结果, 提高查询效率和可靠性.
- **客户端独立控制**： 支持基于 MAC 或 IP 地址控制客户端使用不同的查询规则, 实现家长控制等功能.
- **返回最快 IP 地址**：域名所属 IP 地址列表中查找访问速度最快的 IP 地址, 并返回给客户端, 提高网络访问速度.
- **多种查询协议**： 支持 UDP、TCP、DOT 和 DOH 查询及服务, 以及非 53 端口查询；支持通过 socks5, HTTP 代理查询.
- **特定域名 IP 地址指定**： 支持指定域名的 IP 地址, 实现广告过滤、避免恶意网站等功能.
- **域名高性能后缀匹配**：持域名后缀匹配模式, 简化过滤配置, 过滤效率高.
- **域名分流**： 支持域名分流, 不同类型的域名向不同的 DNS 服务器查询, 支持 iptable 和 nftable 更好的分流；支持测速失败的情况下设置域名结果到对应 ipset 和 nftset 集合.
- **多平台支持**： 支持标准 Linux 系统（树莓派）、OpenWrt 系统各种固件和华硕路由器原生固件. 支持 WSL（Windows Subsystem for Linux, 适用于 Linux 的 Windows 子系统）.
- **IPv4、IPv6 双栈**： 支持 IPv4 和 IPV 6 网络, 支持查询 A 和 AAAA 记录, 支持双栈 IP 速度优化, 并支持完全禁用 IPv6 AAAA 解析.

---

#### PushBot

[PushBot](https://github.com/zzsj0928/luci-app-pushbot) 支持多种推送服务, 包括钉钉、企业微信、微信、飞书等, 并提供设备状态监控、流量统计等功能.

![20241229154732_vrU8TQzI.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_vrU8TQzI.webp)

**重要亮点**:

- 支持多种推送服务, 包括钉钉、企业微信、微信、飞书等.
- 提供设备状态监控、流量统计等功能.
- 支持设备别名、白名单、名单等设置.
- 代码基于 serverchan 提供的接口进行发送信息.

### R5S

#### WireGuard Easy

[WireGuard Easy](https://github.com/wg-easy/wg-easy) 是一个基于 Web 界面的 **WireGuard** VPN 管理工具, 旨在简化 WireGuard 服务器的设置和管理. 它提供了一个用户友好的界面, 使用户能够轻松创建、管理和监控 WireGuard 配置, 而无需手动编辑配置文件.

![20241229154732_AyoFVrAx.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_AyoFVrAx.webp)

**特性**:

- **简化的 WireGuard 配置管理**：通过 Web UI, 用户可以轻松地添加和管理 WireGuard 客户端和服务器配置.

- **支持多用户管理**：可以为多个客户端生成和管理 WireGuard 密钥对, 方便分配和控制访问权限.

- **实时状态监控**：提供 WireGuard 连接状态的实时更新和日志记录, 帮助用户监控 VPN 服务的运行状况.

- **Docker 支持**：wg-easy 可以通过 Docker 容器部署, 便于跨平台使用.

---

#### Bark

[Bark](https://github.com/Finb/Bark) 允许用户将自定义通知推送到他们的 iPhone. 它可以将各种信息, 如短信、邮件、社交媒体更新等, 转换为语音或文字通知, 方便用户在无法查看手机时接收重要信息.

Bark 支持多种通知方式, 包括 Pushover、IFTTT、HTTP API 等, 并可以与各种应用程序和服务进行集成. 用户可以通过 bark-server 搭建自己的 [Bark 服务器](https://github.com/Finb/bark-server), 实现完全自托管的解决方案.

![20241229154732_nKrY4HMo.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_nKrY4HMo.webp)

目前使用 Bark 作为推送服务的有:

- Uptime Kuma
- OpenWrt 的 PushBot
- 脚本执行结果推送
- 浏览器插件推送
- Synology NAS 的 Webhook

**相关资源:**

- [Bar Server Markdown](https://github.com/adams549659584/bark-server)

---

### H28K

#### Linux Command

[Linux Command](https://github.com/jaywcjlove/linux-command) 是一个开源项目, 旨在收集整理 Linux 命令手册、详解、学习资源等内容, 并提供方便快捷的搜索工具. 该项目由 GitHub 用户 jaywcjlove 维护, 并生成了一个 Web 网站方便用户使用.

![20241229154732_etdTnBBP.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_etdTnBBP.webp)

**主要特点**：

- **内容全面**： 搜集了 580 多个 Linux 命令, 涵盖文件管理、文件传输、备份压缩、磁盘管理、系统设置、系统管理、文本处理网络通讯、设备管理、电子邮件与新闻组等多个方面.
- **方便搜索**： 提供强大的搜索功能, 用户可以快速找到所需的命令及其相关信息.
- **多种版本**： 提供多种版本, 包括 Web 版本、微信小程序、Chrome 插件、Raycast 版本、Alfred 版本、Android 版本、Mac/Win/Linux 版本等, 方便用户在不同平台上使用.
- **易于部署**： 提供多种部署方式, Docker、Vercel、宝塔面板等, 方便用户自行部署.

## HK1 Box

### Home Assistant

[Home Assistant](https://www.home-assistant.io/) 一款开源的智能家居自动化平台. 它支持多种设备和服务的集成, 提供强大的自动化功能, 并强调本地控制和隐私保护.

目前还没有花太多心思去做配置:

![20241229154732_gdpIiGkb.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_gdpIiGkb.webp)

**重要亮点**

- **开源社区**: 由全球爱好者和开发者共同维护.
- **设备兼容性**: 支持超过 1000 种设备和服务的集成.
- **自动化功能**: 可以根据时间、事件和条件自动控制智能家居设备.
- **本地控制**: 数据存储和处理均在本地, 确保隐私安全.
- **移动应用**: 提供官方移动应用, 方便远程控制和监控.

### Node-RED

[Node-RED](https://nodered.org/) 是一个基于 Node.js 的低代码编程平台, 旨在简化事件驱动应用程序的开发. 它提供直观的浏览器编辑器, 允许用户通过拖放节点的方式连接硬件、API 和在线服务, 构建复杂的流程. Node-RED 适用于各种场景, 包括物联网、数据集成和自动化等.

![20241229154732_fGEzcSLj.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_fGEzcSLj.webp)

**重点亮点**:

- **低代码编程平台**： Node-RED 是一个用于事件驱动的应用程序的低代码编程平台, 它允许用户通过图形界面连接各种硬件设备、API 和数据源.
- **可视化编程**： 用户可以通过拖放节点来构建应用程序, 无需编写代码, 这降低了开发难度, 并提高了开发效率.
- **广泛的应用场景**： Node-RED 可用于各种场景, 例如物联网、自动化、数据分析等.
- **开源项目** Node-RED 是一个开源项目, 由 OpenJS Foundation 维护.
- **活跃社区**： Node-RED 拥有一个活跃的社区, 用户可以在这里获取帮助、分享经验和贡献代码.
- **丰富的节点库**： Node-RED 提供了丰富的节点库, 用户可以从中选择所需的节点来构建应用程序.
- **跨平台**： Node-RED 支持多种操作系统, 包括 Windows、Linux 和 macOS.

---

## 其他服务

### Captive Portal 检测服务

大家肯定都连过公共场所的 wifi 热点, 比如麦当劳等地方的. 他们的 wifi 往往一连上去就会弹出一个要求登录或者微信关注之类的页面, 只有在这个页面完成操作了才能正常访问网络的. 之前看到这个很神奇, 为什么一连 wifi, 手机就会自动打开这个网页的, 就知道 android 系统应该是提供了一些接口的. 最近接触到这个, 查了一下才知道这个东西叫做 `captive portal`, 就是专门用来给后端的网关提供鉴权计费之类的服务的. 很多公共场合的 wifi 热点应该都用了这么一个技术, 比如酒店, 商场, 银行等等.

`Captive Portal` 的作用就是检测网络的连通性, 这个在分流规则中非常常见, 下面是一些常用的 `Captive Portal` 站点:

| 服务提供者 | 链接                                                       | 大陆体验 | 境外体验 | http/https | IP Version |
| ---------- | ---------------------------------------------------------- | -------- | -------- | ---------- | ---------- |
| Google     | http://www.gstatic.com/generate_204                        | 5        | 10       | 204/204    | 4+6        |
| Google     | http://www.google-analytics.com/generate_204               | 6        | 10       | 204/204    | 4+6        |
| Google     | http://www.google.com/generate_204                         | 0        | 10       | 204/204    | 4+6        |
| Google     | http://connectivitycheck.gstatic.com/generate_204          | 4        | 10       | 204/204    | 4+6        |
| Apple      | [http://captive.apple.com](http://captive.apple.com/)      | 3        | 10       | 200/200    | 4+6        |
| Apple      | http://www.apple.com/library/test/success.html             | 7        | 10       | 200/200    | 4+6        |
| MicroSoft  | http://www.msftconnecttest.com/connecttest.txt             | 5        | 10       | 200/error  | 4          |
| Cloudflare | http://cp.cloudflare.com/                                  | 4        | 10       | 204/204    | 4+6        |
| Firefox    | http://detectportal.firefox.com/success.txt                | 5        | 10       | 200/200    | 4+6        |
| V2ex       | http://www.v2ex.com/generate_204                           | 0        | 10       | 204/301    | 4+6        |
| 小米       | http://connect.rom.miui.com/generate_204                   | 10       | 4        | 204/204    | 4          |
| 华为       | http://connectivitycheck.platform.hicloud.com/generate_204 | 10       | 5        | 204/204    | 4          |
| Vivo       | http://wifi.vivo.com.cn/generate_204                       | 10       | 5        | 204/204    | 4          |

我的目的是检测 WireGuard 是否能连接家中的网络, 所以准备在家中的某台服务器上自建一个 `Captive Portal` 服务, 减少外部网络的依赖.

直接在 Nginx 配置中添加如下内容即可:

```ini
server {
    listen   80;
    listen   443 ssl http2;
    server_name  your.domain.name;
    location = /generate_204 {
    return   204;
    }
}
```

比如 `Captive Portal` 服务部署在家中的 `192.168.10.33` 服务器上, 测试为:

```bash
$ curl -i 192.168.10.33/generate_204
HTTP/1.1 204 No Content
Server: openresty
Date: Tue, 03 Dec 2024 14:17:49 GMT
Connection: keep-alive
```

然后就可以在 **Surge** 的 `proxy` 配置中使用, 比如:

```
🌤️ H28K = wireguard, section-name=H28K, test-url=http://192.168.10.33/generate_204, ip-version=v4-only
```

`test-url` 表示 **Surge** 会通过此地址去测试 **WireGuard** 隧道是否正常(因为 **WireGuard** 也部署在内网, **Surge** 会将流量通过 **WireGuard** 发送到 `192.168.10.33/generate_204`, 所以只要能够测试通过就代表隧道是通畅的.

在没有自建 `Captive Portal` 服务之前, 我都是通过访问小米路由器的 WebUI 来检测网络是否正常, 但是较多的响应内容会增加测试的延迟, 所以就使用了上述方式来优化.

<!--

https://www.cnblogs.com/chenxiaomeng/p/11993741.html

-->

---

### 公网 IP 获取服务

因为使用别家的服务来给 DDNS-GO 会出现限流的情况, 所以在 ECS 上自行部署了一个这样的服务.

#### 获取 JSON 格式

```ini
server {
   listen 80;
   listen [::]:80;

   listen 443 ssl http2;
   listen [::]:443 ssl http2;

   # 用以支持 HTTP/3, 若所用 Nginx 版本支持 HTTP/3, 可去掉注释
   # listen 443 http3;
   # listen [::]:443 http3;

   server_name ipv4.ddnsip.cn ipv6.ddnsip.cn ddnsip.cn;

   # 用以支持 HTTP/3, 若所用 Nginx 版本支持 HTTP/3, 可去掉注释
   # add_header Alt-Svc 'h3=":443"; ma=86400';

   # HSTS
   add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";

   # 允许跨域（在其他站点调用接口会用到）
   add_header Access-Control-Allow-Origin *;
   add_header Access-Control-Allow-Headers "Origin, X-Requested-With, Content-Type, Accept";
   add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";

   # 获取 IP 地址
   location / {
       default_type application/json;
       return 200 '{"ip":"$remote_addr"}';
       # 若使用 CDN 请将$remote_addr改为$http_x_forwarded_for
     }

   # 证书配置
   ssl_certificate /root/.acme.sh/*.ddnsip.cn/fullchain.cer;
   ssl_certificate_key /root/.acme.sh/*.ddnsip.cn/*.ddnsip.cn.key;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
}
```

#### 获取纯文本

```ini
server {
   listen 80;
   listen [::]:80;

   listen 443 ssl http2;
   listen [::]:443 ssl http2;

   # 用以支持 HTTP/3, 若所用 Nginx 版本支持 HTTP/3, 可去掉注释
   # listen 443 http3;
   # listen [::]:443 http3;

   server_name ipv4.ddnsip.cn ipv6.ddnsip.cn ddnsip.cn;

   # 用以支持 HTTP/3, 若所用 Nginx 版本支持 HTTP/3, 可去掉注释
   # add_header Alt-Svc 'h3=":443"; ma=86400';

   # HSTS
   add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";

   # 获取 IP 地址
   location / {
       default_type text/plain;
       return 200 $remote_addr;
       # 若使用 CDN 请将$remote_addr改为$http_x_forwarded_for
     }

   # 证书配置
   ssl_certificate /root/.acme.sh/*.ddnsip.cn/fullchain.cer;
   ssl_certificate_key /root/.acme.sh/*.ddnsip.cn/*.ddnsip.cn.key;
   ssl_session_timeout 5m;
   ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3;
   ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
   ssl_prefer_server_ciphers on;
}
```

这有现成的:

- [https://www.ddnsip.cn/](https://www.ddnsip.cn/)
- [https://ip.ddnsip.cn/](https://ip.ddnsip.cn/)

---

### 分流规则服务

我有多种客户端且在多个地方需要用到分流规则:

- Surge

- OpenClash
- 其他终端上的 Clash

为了简化规则的管理, 需要一个集中管理分流规则和规则转换的服务, 目前选择 [Subconverter Web](https://github.com/CareyWang/sub-web) + [Sub-Store](https://github.com/sub-store-org/Sub-Store) 结合的方式来完成规则统一管理与规则转换.

#### 逻辑图

![sub.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/sub.drawio.svg)

1. `Subconverter Server` 作为规则转换服务, 可以根据配置生成配置文件, 可选择客户端类型以及远程配置:

   ![20241229154732_VfhO8Aar.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VfhO8Aar.webp)

   - 可以预先设置几个常用的配置, 而 **自定义远程配置地址** 可以直接使用 Nginx 搭建一个静态网站, 随时修改规则;
   - 转换后可以使用 **MyUrls** 短链服务自动生成短链接, 方便分享与使用;

2. 参数中可设置: Emoji, 是否开启 UDP, 排序节点, **关闭证书检查** 以及是否只返回节点列表.
   因为有些订阅地址如果证书过期, sub-store 会无法解析, 所以需要先使用 `Subconverter Server` 处理一次(关闭证书检查), 然后将短链接给到 `sub-store` 使用.

3. 转换后的短链接会直接配置到 Clash 和 OpenClash 中, 保证多端规划一致;
4. sub-store 主要作用是收集整理订阅地址返回的节点列表, 虽然 `Subconverter Server` 也支持这个功能, 但是`sub-store` 拥有更多的节点配置功能, 比如 正则过滤, 区域过滤, 正则删除, 节点去重等等功能:
   ![20241229154732_wQmAUaFA.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_wQmAUaFA.webp)

5. `sub-store` 处理后的节点会给 Surge 使用(Surge 目前是单独的规则与配置, 主要是主力机在使用, 所以特殊的配置要多一些, 而 Clash 和 OpenClash 则是给内网的设备使用, 规则相对简单一些, 所以需要 `Subconverter Server` 去统一管理规则, 避免重复操作), `policy-path` 中配置 `sub-store` 的节点地址即可:

   ![20241229154732_e22kWb9J.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_e22kWb9J.webp)

6. `sub-store` 会在多台服务器上部署, 然后使用 Nginx 来进行负载, 而 `sub-store` 的数据文件则通过 **Syncthing** 在动态服务器之间同步;
7. `sub-store` 还有一个 Surge 版本, 需要在 Surge 客户端上安装相应的模块, 目前用的比较少, 主要是因为会存在循环依赖问题: 更新配置需要开启代理, 而开代理又必须先得更新配置.....

#### 部署

`Subconverter Web`, `Subconverter Server` 和 `MyUrls` 可通过 [docker-compose 一键部署](https://github.com/stilleshan/dockerfiles/tree/main/sub).

如果只需要在内网使用, 记得修改一下 `config.js` 中的 `apiUrl` 和 `shortUrl`, docker-compose.yml 中的 `myurls.environment.MYURLS_DOMAIN` 也要做相应修改.

可以挂载下面的目录, 方便修改规则与其他配置:

```yaml
services:
  subconverter:
    image: stilleshan/sub
    container_name: sub
    volumes:
      - ./conf:/usr/share/nginx/html/conf
      # 规则所在目录
      - ./data/subconverter:/base
      - ./data/subweb:/usr/share/nginx/html
    ...
```

`Sub-Store` docker-compose 部署:

```yaml
version: "3"
services:
  sub-store:
    image: instartlove/sub-store
    container_name: sub-store
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./data/root.json:/app/root.json
      - ./data/sub-store.json:/app/sub-store.json
```

#### 使用方式

`Subconverter` 和 `Sub-Store` 的功能侧重点不一样, 可以说是相辅相成的, 可以总结为:

1. 非 Surege 客户端使用 `Subconverter` 统一规则;
2. Surege 客户端只使用 `Sub-Store` 节点处理功能;
3. `Subconverter` 处理 `Sub-Store` 无法解析的 HTTPS 证书失效的订阅地址;

所以会结合两者的优点与侧重点按场景使用:

1. `Sub-Store` 使用原始订阅地址处理节点列表, 提供给 Surge 客户端使用;
2. 如果 HTTPS 证书失效, 会将原始订阅地址先使用 `Subconverter` 处理一次, 参数使用 **关闭证书检查** 并只返回节点列表, 然后将短链接给到 `Sub-Store` 使用;
3. `Subconverter` 使用 `Sub-Store` 处理后的节点列表, 配合自定义规则生成 `Clash` 和 `OpenClash` 的通用配置, 保证两端规则一致;

`Sub-Store` 和 `Subconverter` 同时具备将多个订阅地址合并为同一个配置的功能(组合订阅), 我的方式是在 `Sub-Store` 中将节点合并, 然后将合并后的节点列表给到 `Subconverter` , 根据客户端类型选择不同的规则生成配置文件:

![20241229154732_7f0XSl03.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_7f0XSl03.webp)

#### 使用场景

比如我有 3 个订阅地址, 分别是 A, B, C, 其中 C 的 HTTPS 证书过期, 以及一个自定义的 home 节点列表:

![20241229154732_OFztI62Y.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_OFztI62Y.webp)

分别在不同场景下使用 `Sub-Store` 和 `Subconverter`.

##### 在公司的设备上使用

![sub-company.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/sub-company.drawio.svg)

公司的设备(R2S) 需要访问家中的网络与外网, 所以使用了 AIO + 自定义 Home 节点列表, 然后使用 `Subconverter` 的组合订阅功能生成最终配置.

##### 在家中的设备上使用

家中的设备不需要 Home 节点, 所以直接是用 AIO 节点列表, 然后使用 `Subconverter` 生成最终配置.

##### 在 Surge 客户端上使用

Surge 只需要 AIO 节点列表, 不需要 `Subconverter` 生成配置.

#### 配置同步

配置同步只会涉及到 `Sub-Store`, 它自带通过 `Gist` 同步, 但是需要手动点击下载才能同步, 因为我在多个服务器上都部署了 `Sub-Store` , 所以这种同步方式不太优雅.

`Sub-Store` 容器暴露出来文件只有 2 个, `root.json`是节点配置, `sub-store.json` 是服务配置, 所以我只需要将这 2 个文件同步到其他服务器即可, 最方便的就是是用 **Syncthing**.

> **Syncthing** 相关的数据同步方案将在 [[homelab-data|数据篇]] 详细介绍.

---

### 网络

#### 连通性检查

通过 Ping 去检测网络是否正常, 如果不正常就要通知 Uptime Kuma

```bash
#!/bin/bash

# 检测网络是否畅通
function ping_domain() {
    # ping的域名或者DNS(阿里云的)
    local domain=223.5.5.5
    # ping的次数
    local tries=6
    # 请求成功次数
    local packets_responded=0

    for i in $(seq 1 $tries); do
        if ping -c 1 $domain >/dev/null; then
            ((packets_responded++))
            sleep 1
        fi
    done

    # 如果请求成功总次数大于2, 则表示成功
    if [ $packets_responded -ge 2 ]; then
        echo "true"
    else
        echo "false"
    fi
}

# 检测网络连接函数
function check_network() {
    # 如果ping 6次至少有2次包未响应, 则执行一下代码
    if [ $(ping_domain) = "false" ]; then
        # 如果N无法连接网络, 则重启网络
        echo "$(date '+%Y-%m-%d %H:%M:%S') 网络连接失败"
        curl {uptime-kuma webhook}
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') 网络连接正常"
        curl {uptime-kuma webhook}
    fi
}

check_network

echo "$(date '+%Y-%m-%d %H:%M:%S') network 检查完毕"
```

#### WireGuard 检查

可以传入不同的 WireGuard 端口来检测多个 WireGuard 服务, 顺带检测一下 IPSec 服务.

```bash
#!/bin/sh

port=$1
# 检查 WireGuard 端口是否存在
WireGuard=$(netstat -an | egrep ":${port}" | awk '$1 == "udp" && $NF == "0.0.0.0:*" {print $0}' | wc -l)
# 检查 IPSec 的端口是否存在
IPSec=$(netstat -an | egrep ":4500" | awk '$1 == "udp" && $NF == "0.0.0.0:*" {print $0}' | wc -l)

if [ "$WireGuard" == 0 ]; then
    curl {uptime-kuma webhook}
else
    curl {uptime-kuma webhook}
fi

if [ "$IPSec" == 0 ]; then
    curl {uptime-kuma webhook}
else
    curl {uptime-kuma webhook}
fi
```

#### VPN 检查

检查外部网络是否正常

```bash
#!/bin/bash

# 检测网络是否畅通
function curl_domain() {
    http_code=$(curl -sIL --connect-timeout 5 -w "%{http_code}\n" -o /dev/null http://www.v2ex.com/generate_204)
    if [ "$http_code" != "204" ]; then
        echo 'OpenClash 未正常工作'
        curl {uptime-kuma webhook}
    else
        echo 'OpenClash 正常'
        curl {uptime-kuma webhook}
    fi
}
curl_domain
```

## 资源推荐

- [Awesome-Selfhosted](https://awesome-selfhosted.net/):

  包含超过 1500 个自托管的开源软件项目, 涵盖各种领域, 如博客、论坛、社交媒体、邮件服务、数据库、办公软件、媒体服务器、游戏等.

  ![20241229154732_fc7ddJ4c.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_fc7ddJ4c.webp)

- [Awesome Homelab](https://www.awesome-homelab.com/):

  收录超过 150 个开源应用, 涵盖智能家居、实验室建设、效率提升等多个方面.

  ![20241229154732_3zWlmZGe.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_3zWlmZGe.webp)

- [theme.park](https://theme-park.dev/):

  包含多款自托管服务主题:

  ![20241229154732_iG1943kQ.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_iG1943kQ.webp)

<!--

https://razeen.me/tags/homelab/page/3/

https://dao.fm/2024/05/14/%E7%A0%81%E5%86%9C%E6%85%8E%E5%85%A5-%E5%85%A5%E5%9D%91%E8%BD%AF%E8%B7%AF%E7%94%B1%EF%BC%8C%E9%80%80%E7%83%A7idc%EF%BC%8Chomelab%E6%8A%98%E8%85%BE%E8%AE%B0/


https://wiki-power.com/Homelab-%E8%BD%BB%E9%87%8F%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFCasaOS/
https://chi.miantiao.me/posts/homelab-services/

-->

<!--

TODO List

- 整理微信收藏的文章, 输出 AI 相关的文档
- 整理 GitHub 星标
- B 站收藏整理
- Bark 问题处理
- Uptime Kuma 问题处理
- Homepage 配置
- 哪吒面板配置

-->

**相关文章:**

1. [[homelab-guide|先导篇]]：我的 HomeLab 概要;
2. [[homelab-hardware|硬件篇]]：介绍我所拥有的硬件设备;
3. [[homelab-network|网络篇]]：包括网络环境、异地组网与网络安全;
4. [[homelab-service|服务篇]]：使用 Docker 搭建的各类服务;
5. [[homelab-data|数据篇]]：包括数据存储方案、备份方案和数据恢复方案;
6. [[homelab-data-sync|HomeLab数据同步：构建高效的数据同步网络]]
7. [[homelab-data-backup|HomeLab数据备份：打造坚实的数据安全防线]]
8. [[homelab-upgrade-to-10g|HomeLab 网络续集：升级 10G 网络-再战 10 年]]
9. [[homelab-guide|NAT 内网穿透详解：揭秘网络连接背后的奥秘]]
