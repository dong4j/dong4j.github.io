---
title: 在 CentOS 上安装 Nginx
keywords:
  - Shell
categories:
  - Shell
tags:
  - CentOS
  - Nginx安装
  - 依赖库
  - C++编译环境
  - 服务器配置
abbrlink: 779e9fe6
date: 2013-02-17 00:00:00
ai:
  - 本教程详细介绍了如何在CentOS系统上安装Nginx服务器。首先，下载了Nginx以及依赖包如zlib、pcre和openssl。接着，解压文件并配置编译环境。通过命令行操作，分别对各个依赖包进行配置、编译和安装。然后，安装Nginx并设置其路径及配置文件位置。最后，运行Nginx服务并通过浏览器验证启动状态。教程中还提到了一个常见问题——当Nginx启动时无法找到libpcre.so.1模块的解决方法：在32位系统中创建符号链接到/lib目录，在64位系统中则创建到/lib64目录，即可顺利解决问题。
description: 本教程详细介绍了如何在CentOS系统上安装Nginx服务器。首先，下载了Nginx以及依赖包如zlib、pcre和openssl。接着，解压文件并配置编译环境。通过命令行操作，分别对各个依赖包进行配置、编译和安装。然后，安装Nginx并设置其路径及配置文件位置。最后，运行Nginx服务并通过浏览器验证启动状态。教程中还提到了一个常见问题——当Nginx启动时无法找到libpcre.so.1模块的解决方法：在32位系统中创建符号链接到/lib目录，在64位系统中则创建到/lib64目录，即可顺利解决问题。
---

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
