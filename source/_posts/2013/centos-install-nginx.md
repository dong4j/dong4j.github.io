---
title: 从零开始：安装并配置CentOS Nginx服务
keywords:
  - Centos 64位
  - Nginx
  - 安装
  - 依赖库
  - libpcre.so.1
categories:
  - 新时代码农
tags:
  - Centos 64位
  - Nginx
  - 安装
  - 依赖库
  - libpcre.so.1
abbrlink: 779e9fe6
date: 2013-02-17 00:00:00
ai:
  - 本文介绍如何在Centos 64位系统上安装Nginx。首先需要下载Nginx的tar包及依赖的工具，然后进行编译和安装。最后通过浏览器访问服务器IP来验证Nginx是否成功启动。如果出现找不到libpcre.so.1的问题，可以通过创建符号链接来解决。
description: 本文介绍如何在Centos 64位系统上安装Nginx。首先需要下载Nginx的tar包及依赖的工具，然后进行编译和安装。最后通过浏览器访问服务器IP来验证Nginx是否成功启动。如果出现找不到libpcre.so.1的问题，可以通过创建符号链接来解决。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

系统 Centos 64 位

## 第一步，首先下载 Nginx 的 tar 包及安装依赖的工具 tar 包。

Nginx: [http://nginx.org/en/download.html](http://nginx.org/en/download.html)

Nginx 需要依赖下面 3 个包  
gzip 模块需要 zlib 库 ( 下载: [http://www.zlib.net/](http://www.zlib.net/) )  
rewrite 模块需要 pcre 库 ( 下载: [http://www.pcre.org/](http://www.pcre.org/) )  
ssl 功能需要 openssl 库 ( 下载: [http://www.openssl.org/](http://www.openssl.org/) )

分别解压。  
具体命令：

```shell
wget http://nginx.org/download/nginx-1.13.2.tar.gz
wget http://www.zlib.net/zlib-1.2.11.tar.gz
wget https://ftp.pcre.org/pub/pcre/pcre-8.40.tar.gz
wget https://www.openssl.org/source/openssl-fips-2.0.16.tar.gz

tar zxvf openssl-fips-2.0.16.tar.gz
tar zxvf nginx-1.13.2.tar.gz
tar zxvf zlib-1.2.11.tar.gz
tar zxvf pcre-8.40.tar.gz
```

---

## 第二步 编译安装

安装顺序：先安装三个依赖包再安装 nginx

```shell
cd 到各个解压目录下运行
./configuer && make && make install
```

安装 c++ 编译环境

```shell
yum install gcc-c++
```

---

## 第三步 运行 nginx

安装好的 nginx 路径在：

```shell
/usr/local/nginx

```

默认的配置文件的路径在：

```shell
/usr/local/nginx/conf/nginx.conf
```

运行 nginx：

```shell
/usr/local/nginx/sbin/nginx
```

通过浏览器访问服务器 ip，出现以下标志就是启动成功了：

```shell
Welcome to nginx!

If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.com.

Thank you for using nginx.
```

有问题之处烦请在留言中指出，非常感谢。

## 问题

Nginx 启动提示找不到 libpcre.so.1 解决方法  
WebServer 2012-08-26 Nginx,libpcre  
启动 nginx 提示：error while loading shared libraries: libpcre.so.1: cannot open shared object file: No such file or directory，意思是找不到 libpcre.so.1 这个模块，而导致启动失败。

```shell
[root@lee ~]# /usr/local/webserver/nginx/sbin/nginx
nginx: error while loading shared libraries: libpcre.so.1: cannot open shared object file: No such file or directory
```

经过搜索资料，发现部分 linux 系统存有的通病。要解决这个方法非常容易

如果是 32 位系统

```shell
[root@lee ~]#  ln -s /usr/local/lib/libpcre.so.1 /lib
```

如果是 64 位系统

```shell
[root@lee ~]#  ln -s /usr/local/lib/libpcre.so.1 /lib64
```

然后在启动 nginx 就 OK 了

```shell
[root@lee ~]# /usr/local/webserver/nginx/sbin/nginx
```
