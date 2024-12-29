---
title: Docker 入门
keywords:
  - Docker
categories:
  - Docker
tags:
  - Docker
abbrlink: fa8faa2e
date: 2015-10-25 00:00:00
---

# Docker 入门指南

Docker 是一个开源的应用容器引擎，让开发者能够将软件及其运行时环境封装起来以方便地进行移植和部署。通过使用 Docker，可以快速打包、发布以及运行应用程序在几乎任何地方（包括物理机或虚拟机上）。它利用 Linux 内核的资源隔离特性来实现轻量级的操作系统级虚拟化，使得开发人员能够创建和管理容器化的应用和服务。

## 安装 Docker

### 在 Ubuntu 上安装 Docker

1. 更新包索引：

```shell
$ sudo apt-get update
```

2. 安装必要的软件包以允许 `apt` 使用 HTTPS 来获取安全存储库：

```shell
$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

3. 添加 Docker 的官方 GPG 密钥:

```shell
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

4. 利用该密钥来验证 Docker 存储库中的所有软件包的完整性和真实性：

```shell
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

5. 再次更新你的存储库索引:

```shell
$ sudo apt-get update
```

6. 安装 Docker CE（Community Edition）：

```shell
$ sudo apt-get install docker-ce
```

7. 验证安装是否成功，运行一个简单的容器来输出 "Hello from Docker" 消息：

```shell
$ sudo docker run hello-world
```

如果一切正常，则你已经正确安装了 Docker。

### Windows 和 macOS 安装

对于 Windows 或 macOS 用户，可以下载并使用 Docker Desktop for Mac 或 Docker Desktop for Windows。这提供了图形界面和命令行工具来管理容器。

## 基本概念与术语

- **Image（镜像）**：Docker 镜像是一个轻量级、独立的、包含所有必要的代码以及依赖关系的打包文件，可以用来创建容器。
- **Container（容器）**：基于镜像生成的一个运行实例。每个容器都拥有自己的一组进程和资源。

- **Repository（仓库）**：存储和共享 Docker 镜像的地方。

## 基本命令

### 搜索镜像

```shell
$ docker search [image_name]
```

### 下载镜像

```shell
$ docker pull [image_name]
```

### 列出本地所有镜像

```shell
$ docker images
```

### 运行容器

```shell
$ docker run -it --name my_container [image_name] /bin/bash
# 或者，启动一个在后台运行的容器：
$ docker run -d --name my_container [image_name]
```

`-it`: 交互模式加上分配终端

### 列出正在运行的所有容器

```shell
$ docker ps
```

### 列出所有容器（包括已经停止）

```shell
$ docker ps -a
```

### 进入一个已启动的容器内

```shell
$ docker exec -it [container_name] /bin/bash
```

`-it`: 交互模式加上分配终端

### 查看日志

```shell
$ docker logs [container_id]
```

### 停止一个运行中的容器

```shell
$ docker stop [container_id]
```

### 删除容器

```shell
$ docker rm [container_name]
```

如果该容器正在运行，需要先停止它。

### 删除镜像

```shell
$ docker rmi [image_name]
```

如果该镜像被某个容器使用，则必须先删除其关联的容器。可以使用`-f`强制删除。

```shell
$ docker rmi -f [image_name]
```

## 构建自己的 Docker 镜像

假设你有一个 Dockerfile 文件来描述你的应用程序，你可以通过以下命令构建一个镜像：

```shell
$ docker build -t my_image .
# 如果需要指定标签（tag），可以使用-t参数
$ docker build --tag=my_image:version .
```

## Docker Compose

Docker Compose 是用于定义和运行多容器 Docker 应用程序的工具。通过一个名为`docker-compose.yml` 的文件，你可以描述一组服务、网络及卷。

```yaml
version: "3"
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

在配置好此文件后：

- 使用`docker-compose up` 来启动服务。
- 若要停止容器，可以运行 `docker-compose down`。
