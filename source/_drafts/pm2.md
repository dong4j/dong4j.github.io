---
title: pm2 进程守护 python flask
abbrlink: ba2a34a5
date: 2025-01-18 00:00:00
tags:
categories:
cover:
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover)

### 安装 Node.js

1. 首先，使用以下命令安装 curl（如果尚未安装）：

```
sudo apt update
sudo apt install curl
```

2. 确保你的系统上已安装了 Node.js 的最新版本（可以替换 [LTS](https://so.csdn.net/so/search?q=LTS&spm=1001.2101.3001.7020) 版本为当前最新版本）：

```
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```

3. [安装 Node.js](https://so.csdn.net/so/search?q=%E5%AE%89%E8%A3%85Node.js&spm=1001.2101.3001.7020)：

```
sudo apt install -y nodejs
```

### 安装 pm2

1、安装

```
npm install pm2 -g
```

2、验证

```
pm2 -v
```

or

```
pm2 list
```

### 上传文件至服务器

upload…

### python 配置

#### 生成 requirements.txt

如果你的项目环境中已经安装了所有必要的包，你可以使用

```
pip freeze
```

命令来生成一个包含所有已[安装包](https://so.csdn.net/so/search?q=%E5%AE%89%E8%A3%85%E5%8C%85&spm=1001.2101.3001.7020)及其版本的列表。这个列表可以直接用作 `requirements.txt` 文件。

#### python 虚拟环境

在 Python 中，虚拟环境是一种将一组 Python 包与其他 Python 项目隔离开的方法。这有助于避免依赖冲突和确保项目的可移植性。

创建和管理 Python 虚拟环境的常见方法有：

1.  使用 venv 模块（Python 3.3 及以上版本）
2.  使用 virtualenv 工具
3.  使用 pyenv 工具

##### 使用 Python 自带的 venv 模块创建和管理虚拟环境

```
# 创建虚拟环境
python3 -m venv /path/to/new/virtual/environment
 
# 激活虚拟环境
source /path/to/new/virtual/environment/bin/activate
 
# 退出虚拟环境
deactivate
```

##### 使用 virtualenv 工具创建和管理虚拟环境

首先，你需要安装 virtualenv 工具，如果你还没有安装，可以使用以下命令进行安装：

```
pip install virtualenv
```

然后，你可以使用以下命令创建和管理虚拟环境：

```
# 创建虚拟环境
virtualenv /path/to/new/virtual/environment
 
# 激活虚拟环境
source /path/to/new/virtual/environment/bin/activate
 
# 退出虚拟环境
deactivate
```

##### 使用 pyenv 工具创建和管理虚拟环境

首先，你需要安装 pyenv 工具，如果你还没有安装，可以根据它的官方文档中的安装指南进行安装：https://github.com/pyenv/pyenv-installer

然后，你可以使用以下命令创建和管理虚拟环境：

```
# 创建虚拟环境
pyenv virtualenv 3.7.1 my-virtual-env
 
# 激活虚拟环境
pyenv activate my-virtual-env
 
# 退出虚拟环境
pyenv deactivate
```

注意：在这些命令中，/path/to/new/virtual/environment 是你想要创建虚拟环境的目录。在这个目录中，将会有一个新的 Python 环境，包括 Python 解释器和 pip 的副本。

#### 安装依赖

```
cd ...
pip install requirements.txt
```

#### 编写 flask 启动脚本

##### 直接运行 python flask

```
python3  app.py
```

##### gunicorn 运行 flask

安装模块

```
pip install gunicorn
```

Gunicorn（绿色独角兽，Green Unicorn）是一个 Python 的 WSGI HTTP 服务器，来源于 Ruby 的 Unicorn 项目。它采用 pre-fork 的 worker 模型；在启动时，会在主进程中预先 fork 出指定数量的 worker 进程来处理请求，极大提升了服务器请求负载能力，又可以兼容于多种 Python Web 框架，实现简单，占用系统资源少，速度也相当快。

以多 thread 方式启动（flask 在 wsgi.py 中）：

```
pm2 --name=ai start "gunicorn -c gunicorn_config.py wsgi:app"
```

其中 gunicorn_config.py 参数如下

```
# gunicorn_config.py

# 并发工作进程数
workers = 4  # 可根据服务器 CPU 核心数调整

# 工作模式
worker_class = 'gevent'  # 可以选择 'sync', 'eventlet', 'gevent', 'tornado', 'gthread'

# 每个worker的最大线程数，仅在 gthread 模式下有效
threads = 2  # 默认是1, 仅适用于 gthread 工作模式

# 每个 worker 处理的最大请求数，超过此值后重启worker
max_requests = 1000  # 默认0, 表示禁用自动重启

# 绑定的IP和端口
bind = '127.0.0.1:8000'  # 可以根据需求修改

# 进程名称
proc_name = 'my_gunicorn_app'  # 自定义进程名

# 工作进程的超时时间
timeout = 30  # 默认是30秒

# 连接的最大数量，仅适用于 eventlet 或 gevent 工作模式
worker_connections = 1000  # 适用于异步工作模式

# Keep-Alive时间，连接存活时间
keepalive = 2  # 默认2秒

# 日志配置
accesslog = '-'  # 访问日志输出到控制台
errorlog = '-'   # 错误日志输出到控制台

# 设置日志级别，可选 "debug", "info", "warning", "error", "critical"
loglevel = 'info'

# 是否以守护进程方式运行
daemon = False  # 如果为 True，则表示以守护进程的方式运行

# PID文件路径
pidfile = '/tmp/gunicorn.pid'
```

### 运行 run.sh 文件



## PM2命令列表
| 命令                                            | 描述                       |
| ----------------------------------------------- | -------------------------- |
| `pm2 start <app.js> [--name=<name>]`            | 启动应用                   |
| `pm2 stop <app_name|id>`                        | 停止应用                   |
| `pm2 restart <app_name|id>`                     | 重启应用                   |
| `pm2 delete <app_name|id>`                      | 删除应用                   |
| `pm2 list`                                      | 列出所有应用               |
| `pm2 show <app_name|id>`                        | 显示应用详细信息           |
| `pm2 info <app_name|id>`                        | 显示应用信息（等同于show） |
| `pm2 status`                                    | 显示PM2状态                |
| `pm2 logs`                                      | 显示所有应用日志           |
| `pm2 logs <app_name|id>`                        | 显示指定应用日志           |
| `pm2 flush`                                     | 清空所有日志文件           |
| `pm2 reloadLogs`                                | 重新加载日志               |
| `pm2 deploy`                                    | 部署应用                   |
| `pm2 deploy <configuration_file> <environment>` | 使用配置文件部署到指定环境 |
| `pm2 monit`                                     | 监控所有应用               |
| `pm2 cpu <app_name|id>`                         | 显示应用CPU使用情况        |
| `pm2 memory <app_name|id>`                      | 显示应用内存使用情况       |
| `pm2 startup`                                   | 生成启动脚本               |
| `pm2 save`                                      | 保存当前应用列表           |
| `pm2 resurrect`                                 | 恢复之前保存的应用列表     |
| `pm2 update`                                    | 更新PM2到最新版本          |
| `pm2 scale <app_name|id> <number_of_instances>` | 扩展应用实例数量           |
| `pm2 gracefulReload <app_name|id>`              | 优雅重启应用               |
| `pm2 trigger <app_name|id> <action_name>`       | 触发自定义动作             |
| `pm2 set <key> <value>`                         | 设置PM2配置项              |
| `pm2 unset <key>`                               | 取消设置PM2配置项          |
| `pm2 help`                                      | 显示帮助信息               |
| `pm2 home`                                      | 打开PM2官网                |
| `pm2 plus`                                      | 打开PM2 Plus服务页面       |
| `pm2 module:list`                               | 列出所有PM2模块            |
| `pm2 module:install <module_name>`              | 安装PM2模块                |
| `pm2 module:uninstall <module_name>`            | 卸载PM2模块                |

| 参数                   | 描述                                 |
| ---------------------- | ------------------------------------ |
| `--name`               | 设置应用的名称                       |
| `--cwd`                | 指定启动应用时的工作目录             |
| `--watch`              | 监听文件变化，自动重启应用           |
| `--ignore-watch`       | 忽略监听的文件或目录                 |
| `--max-memory-restart` | 设置应用内存使用上限，超过后自动重启 |
| `--exec-path`          | 指定Node.js的执行路径                |
| `--instances`          | 设置应用实例的数量                   |
| `--instance`           | 指定启动的实例编号                   |
| `--env`                | 设置环境变量                         |
| `--port`               | 指定应用的端口号                     |
| `--cron`               | 设置定时重启任务                     |
| `--interpreter`        | 指定解释器路径                       |
| `--interpreter-args`   | 传递给解释器的参数                   |
| `--output`             | 指定输出日志文件路径                 |
| `--error`              | 指定错误日志文件路径                 |
| `--pid`                | 指定PID文件路径                      |
| `--log-date-format`    | 设置日志日期格式                     |
| `--merge-logs`         | 合并日志文件                         |
| `--no-daemon`          | 不以守护进程方式运行                 |
| `--no-vizion`          | 禁用vizion版本控制                   |
| `--no-autorestart`     | 禁用自动重启                         |
| `--restart-delay`      | 设置重启延迟时间                     |
| `--force`              | 强制重启或停止应用                   |
| `--update-env`         | 更新环境变量                         |
| `--only`               | 只启动指定的应用                     |
| `--kill-timeout`       | 设置强制杀死进程的超时时间           |
| `--wait-ready`         | 等待应用准备好后再继续               |
| `--ready-delay`        | 设置等待准备好的延迟时间             |
| `--attach`             | attaching to application output      |
| `--no-attach`          | do not attach to application output  |
