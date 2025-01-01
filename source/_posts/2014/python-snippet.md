---
title: 掌握 CentOS 环境下的 Python 技巧
keywords:
  - Python
categories:
  - 新时代码农
tags:
  - Python
  - CentOS
  - Web 开发
  - 数据处理
  - 人工智能
abbrlink: 44bde9f9
date: 2014-07-25 00:00:00
ai:
  - 本文提供了一步指南，在 CentOS 操作系统中安装和配置 Python 环境。包括手动解压并编译 Python 包、查看已安装模块、使用 pip 更新软件包以及运行简单的
    Web 服务器等功能。
description: 本文提供了一步指南，在 CentOS 操作系统中安装和配置 Python 环境。包括手动解压并编译 Python 包、查看已安装模块、使用
  pip 更新软件包以及运行简单的 Web 服务器等功能。
---

在 Linux 系统中，Python 是一个非常流行的编程语言，被广泛应用于 Web 开发、数据分析、人工智能等多个领域。本文将详细介绍如何在 CentOS 操作系统中安装和配置 Python 环境。

## 安装步骤

### 1. 解压 Python 包

首先，你需要下载 Python 的源代码包并将其解压到你的服务器上。由于你要求不使用外部工具安装 Python，我们将手动进行这一步。

```bash
# 假设你已经下载了 Python 的源码压缩包到 /usr/local/src 目录下
tar -xzf Python-3.8.x.tar.gz -C /usr/local/src
```

### 2. 进入解压后的文件夹

接下来，进入 Python 的源代码目录：

```bash
cd /usr/local/src/Python-3.8.x
```

### 3. 配置和安装 Python

现在，我们可以执行 configure 脚本来配置 Python 的编译选项。如果你需要指定安装目录，可以添加 `--prefix` 参数。

```bash
./configure --prefix=/opt/python38
make && make install
```

这个步骤会编译并安装 Python 到指定的目录 `/opt/python38`。

## 查看已安装的模块

进入 Python 交互环境：

```bash
python3
```

然后，使用 `help("modules")` 命令来查看所有已经安装的 Python 模块。

## 查看 pip 版本

要查看当前系统上安装的 pip 版本，可以直接在命令行运行以下命令：

```bash
pip -V
```

或者，如果你使用的是 Python 3.x 版本，你可能需要使用以下命令：

```bash
python3 -m pip -V
```

## 使用 httpstat 模块测试 HTTP 响应

`httpstat` 是一个 Python 模块，可以用来检查 HTTP 请求的响应。下面是如何使用它来测试一个本地服务的例子：

```bash
export HTTPSTAT_SHOW_BODY=true
python /path/to/httpstat.py http://127.0.0.1:8080/json
```

确保将 `/path/to/httpstat.py` 替换为 `httpstat.py` 文件的正确路径。

## 自动生成和安装 requirements.txt 依赖

在处理 Python 项目时，`requirements.txt` 文件是非常重要的。它列出了项目依赖的所有模块及其版本号。以下是自动创建和使用这个文件的方法：

### 生成 requirements.txt 文件

```bash
pip freeze > requirements.txt
```

### 安装 requirements.txt 列出的依赖

```bash
pip install -r requirements.txt
```

这样，你就可以确保在不同的环境中使用相同版本的依赖项。

## 运行简单的 Web 服务器

Python 内置了一个非常方便的 HTTP 服务器模块 `SimpleHTTPServer`，可以用来快速测试你的本地文件。下面是如何启动一个简单的 HTTP 服务器的示例：

```bash
python -m SimpleHTTPServer 7777
```

或者使用 Python 3.x 版本：

```bash
python -m http.server 7777
```

这些命令将在你指定的端口（在这个例子中是 7777）上启动一个简单的 HTTP 服务器。你可以通过浏览器或工具如 Postman 来访问这个服务器。
