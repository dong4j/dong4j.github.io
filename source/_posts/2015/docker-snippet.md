---
title: Docker基问题记录
keywords:
  - Docker
categories:
  - Docker
tags:
  - Docker升级
  - 容器管理
  - Docker Compose
  - Docker权限
  - 系统清理
abbrlink: 79a8d4c5
date: 2015-10-25 00:00:00
ai:
  - 本文介绍了如何升级到 Docker 的最新版本，并解决了从旧版本直接升级到新版本时可能遇到的问题。此外，文章还提供了安装和管理 Docker Compose
    的方法以及进行了 Docker 磁盘清理与镜像管理的操作指南。其中包括了系统垃圾的清理、容器日志查看、自动启动设置、MySQL 文件目录配置及解决权限问题的方法。
description: 本文介绍了如何升级到 Docker 的最新版本，并解决了从旧版本直接升级到新版本时可能遇到的问题。此外，文章还提供了安装和管理 Docker
  Compose 的方法以及进行了 Docker 磁盘清理与镜像管理的操作指南。其中包括了系统垃圾的清理、容器日志查看、自动启动设置、MySQL 文件目录配置及解决权限问题的方法。
---

## 一、升级到最新版

### 1. 检查当前已安装的 docker 相关软件包

```shell
rpm -qa | grep docker
```

### 2. 卸载旧版本

执行以下命令卸载所有列出的相关软件：

```shell
yum remove docker-<version>
yum remove docker-client-<version>
yum remove docker-common-<version>
# 示例:
# yum remove docker-1.13.1-53.git774336d.el7.centos.x86_64
```

### 3. 升级到最新版

使用 curl 命令安装最新的 Docker 版本:

```shell
curl -fsSL https://get.docker.com/ | sh
```

### 4. 启动和设置开机自启 Docker 服务

- 重启 Docker

```shell
systemctl restart docker
```

- 设置启动项，确保 Docker 在系统启动时自动运行：

```shell
systemctl enable docker
```

## 二、解决升级后容器启动错误

若从旧版本（如 1.13.1）直接升级到新版本（例如 18.06.1），可能会遇到如下报错信息，当尝试启动某些使用`docker-runc`运行时创建的容器时：

```shell
Error response from daemon: Unknown runtime specified docker-runc
```

解决方法是搜索并替换所有提到`docker-runc`为`runc`:

```shell
grep -rl 'docker-runc' /var/lib/docker/containers/ | xargs sed -i 's/docker-runc/runc/g'
systemctl restart docker
docker start f5eb78732bcc # 单独重启容器
```

## 三、安装 Docker Compose

若您的系统未安装 Docker compose，执行以下步骤进行安装：

1. 确认 pip 已正确安装。

```shell
pip -V
# 若没有输出，请按照下述命令进行安装:
yum -y install epel-release
yum -y install python-pip
pip install --upgrade pip
```

2. 安装 Docker Compose 本身：

```shell
pip install docker-compose
docker-compose -version # 检查是否正确安装了Docker Compose
```

## 四、Docker 磁盘清理与镜像管理

### 系统垃圾清理:

使用以下命令清理不需要的容器，网络和镜像等：

```shell
docker system prune
```

查看 Docker 所占用的空间大小, 使用:

```shell
docker system df
```

### 镜像文件存储和加载

- 保存 Docker 镜像至 tar 文件:

```shell
docker save -o xxxx.tar {imageId}
```

- 加载已保存的镜像:

```shell
docker load -i xxxx.tar
```

## 其他问题处理

### MySQL 文件目录设置

当使用外部存储路径时，务必指定`/var/lib/mysql-files` 的完整路径。例如：

```shell
-v /home/mysql/mysql-files:/var/lib/mysql-files/
```

### Docker 权限问题:

对于一些需要 root 权限的操作，可以添加 `--privileged=true` 参数。

## 五、查看容器日志与设置自动启动

- 查看 Docker 容器的日志信息：

```shell
docker logs -t --tail=n [容器id]
```

要确保 Docker 容器在重启后仍能正常运行, 可以在启动时使用`--restart`参数，支持以下值：

- `no`: 不尝试重新启动已退出的容器。
- `on-failure[:N]`: 当容器非零状态退出时才重启。可选地限制为最多 N 次重启
- `always`: 总是重启该容器

例如:

```shell
docker run --restart=on-failure:10 redis # 在失败后尝试重新启动10次。
```

如果已经创建了容器但需要更改其`--restart`策略，使用更新命令：

```shell
docker update --restart=always xxxxx_containername
```
