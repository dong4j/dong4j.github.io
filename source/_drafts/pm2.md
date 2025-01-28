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

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})


### 使用 PM2 守护 Flask 应用：从安装到配置详解

PM2 是一个功能强大的 Node.js 进程管理工具，不仅适用于 JavaScript 项目，也能很好地守护 Python 应用。本文将详细介绍如何在服务器上使用 PM2 来守护一个基于 Flask 的 Python 应用。

---

#### **1. 安装环境**

##### **安装 Node.js**

PM2 是基于 Node.js 的工具，因此需要先安装 Node.js 环境：

```bash
sudo apt update && sudo apt install curl -y

curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install nodejs -y
```

##### **安装 PM2**

使用 npm 全局安装 PM2：

```bash
npm install pm2 -g
```

验证安装是否成功：

```bash
pm2 -v  # 查看版本
pm2 list  # 列出当前管理的所有进程
```

---

#### **2. 准备 Flask 应用**

##### **生成依赖文件**

在 Python 项目中，通常会使用 `requirements.txt` 来管理依赖包。如果尚未生成该文件，可以通过以下命令创建：

```bash
pip freeze > requirements.txt
```

##### **配置虚拟环境（可选但推荐）**

为了保持项目的独立性，建议为 Flask 应用创建一个 Python 虚拟环境。

```bash
python3 -m venv my_flask_env  # 创建虚拟环境
source my_flask_env/bin/activate  # 激活虚拟环境
```

激活后，在虚拟环境中安装项目依赖：

```bash
pip install -r requirements.txt
```

##### **编写启动脚本**

Flask 应用通常需要通过 `gunicorn` 或 `uwsgi` 来运行，以提高性能和并发处理能力。

假设你的 Flask 应用文件为 `app.py`，以下是使用 `gunicorn` 启动的配置示例：

```bash
# 安装 gunicorn
pip install gunicorn

# 使用 gunicorn 启动 Flask 应用
gunicorn -b "0.0.0.0:8000" --workers 4 app:app
```

你也可以为 `gunicorn` 配置一个参数文件（如 `gunicorn_config.py`），以进一步优化性能：

```python
# gunicorn_config.py

bind = '0.0.0.0:8000'           # 绑定地址和端口
workers = 4                     # 工作进程数，根据 CPU 核心调整
worker_class = 'gevent'         # 使用异步工作者模式
timeout = 60                   # 请求超时时间（秒）
accesslog = '-'                # 输出访问日志到标准输出
errorlog = '-'                 # 输出错误日志到标准输出
```

---

#### **3. 使用 PM2 守护 Flask 应用**

##### **直接启动**

你可以将 `gunicorn` 命令通过 PM2 管理：

```bash
pm2 start gunicorn -c gunicorn_config.py wsgi:app --name=flask_app
```

##### **使用自定义脚本**

为了更好地管理，可以编写一个启动脚本（如 `start.sh`）：

```bash
#!/bin/bash

# 激活虚拟环境（如果需要）
source /path/to/my_flask_env/bin/activate

# 使用 gunicorn 启动 Flask 应用
gunicorn -c gunicorn_config.py wsgi:app
```

然后通过 PM2 管理该脚本：

```bash
pm2 start start.sh --name=flask_app
```

##### **配置文件（可选）**

你也可以为 PM2 编写一个 JSON 配置文件（如 `ecosystem.config.js`），以便管理和部署多个应用。

```javascript
module.exports = {
  apps: [{
    name: 'Flask App',
    script: './start.sh',  // 启动脚本路径
    cwd: '/path/to/your/project',  // 工作目录
    env: {
      NODE_ENV: 'production'
    },
    watch: false,          // 是否监听文件变化（默认 false）
    max_memory_restart: '100M'  // 内存限制，超过后自动重启
  }]
}
```

然后运行：

```bash
pm2 start ecosystem.config.js
```

---

#### **4. PM2 常用命令**

以下是 PM2 的一些常用命令，帮助你更好地管理应用：

| **命令**               | **描述**                                 |
|-------------------------|------------------------------------------|
| `pm2 list`              | 列出所有正在运行的应用                 |
| `pm2 start <script>`    | 启动一个新的应用                        |
| `pm2 stop <id/name>`    | 停止指定的应用                         |
| `pm2 restart <id/name>` | 重启指定的应用                         |
| `pm2 delete <id/name>`  | 删除指定的应用（停止并移除配置）       |
| `pm2 logs`              | 查看所有应用的日志                     |
| `pm2 monit`             | 监控应用的性能和资源使用情况           |
| `pm2 save`              | 保存当前应用的状态，以便后续恢复       |
| `pm2 reload`            | 优雅地重启 PM2 服务                    |

---

#### **5. 配置文件参数（高级）**

PM2 提供了丰富的配置选项，可以通过命令行或配置文件指定：

| **参数**                  | **描述**                                 |
|---------------------------|------------------------------------------|
| `--name <app_name>`       | 设置应用的名称                         |
| `--cwd <directory>`       | 指定启动时的工作目录                   |
| `--watch`                 | 启用文件变化监听，自动重启应用         |
| `--ignore-watch <path>`   | 忽略某些文件或目录的变化               |
| `--max-memory-restart <size>` | 设置内存使用上限，超过后自动重启       |
| `--env <key=value>`       | 设置环境变量                           |

---

#### **6. 总结**

通过 PM2，你可以轻松地守护 Flask 应用，实现进程管理和自动恢复功能。无论是简单的脚本启动还是复杂的多应用配置，PM2 都能提供强大的支持。希望本文的详细步骤和命令示例能够帮助你快速上手！



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
| `pm2 stop <app_name/id>`                        | 停止应用                   |
| `pm2 restart <app_name/id>`                     | 重启应用                   |
| `pm2 delete <app_name/id>`                      | 删除应用                   |
| `pm2 list`                                      | 列出所有应用               |
| `pm2 show <app_name/id>`                        | 显示应用详细信息           |
| `pm2 info <app_name/id>`                        | 显示应用信息（等同于show） |
| `pm2 status`                                    | 显示PM2状态                |
| `pm2 logs`                                      | 显示所有应用日志           |
| `pm2 logs <app_name/id>`                        | 显示指定应用日志           |
| `pm2 flush`                                     | 清空所有日志文件           |
| `pm2 reloadLogs`                                | 重新加载日志               |
| `pm2 deploy`                                    | 部署应用                   |
| `pm2 deploy <configuration_file> <environment>` | 使用配置文件部署到指定环境 |
| `pm2 monit`                                     | 监控所有应用               |
| `pm2 cpu <app_name/id>`                         | 显示应用CPU使用情况        |
| `pm2 memory <app_name/id>`                      | 显示应用内存使用情况       |
| `pm2 startup`                                   | 生成启动脚本               |
| `pm2 save`                                      | 保存当前应用列表           |
| `pm2 resurrect`                                 | 恢复之前保存的应用列表     |
| `pm2 update`                                    | 更新PM2到最新版本          |
| `pm2 scale <app_name/id> <number_of_instances>` | 扩展应用实例数量           |
| `pm2 gracefulReload <app_name/id>`              | 优雅重启应用               |
| `pm2 trigger <app_name/id> <action_name>`       | 触发自定义动作             |
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
