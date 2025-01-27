---
title: nezha-dashboard-config
ai: true
abbrlink: adc3ac9e
date: 2025-01-21 01:27:54
description:
categories:
tags:
cover:
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## 简介





> Dashboard 开启 Debug 模式后可以访问路径 /swagger/index.html 查看详情



## 哪吒监控V1手撸指南

### **1. 下载资源**

- Dashboard下载：[https://github.com/nezhahq/nezha/releases](https://www.nodeseek.com/jump?to=https%3A%2F%2Fgithub.com%2Fnezhahq%2Fnezha%2Freleases)
- Agent下载：[https://github.com/nezhahq/agent/releases](https://www.nodeseek.com/jump?to=https%3A%2F%2Fgithub.com%2Fnezhahq%2Fagent%2Freleases)
- 后台前端资源下载：[https://github.com/nezhahq/admin-frontend/releases](https://www.nodeseek.com/jump?to=https%3A%2F%2Fgithub.com%2Fnezhahq%2Fadmin-frontend%2Freleases)
- 前台前端资源下载：[https://github.com/hamster1963/nezha-dash-v1/releases](https://www.nodeseek.com/jump?to=https%3A%2F%2Fgithub.com%2Fhamster1963%2Fnezha-dash-v1%2Freleases)
  ———————
- 后台前端资源目录：/path/to/dashboard/admin-dist（自己下载资源包释放到该目录）
- 前台前端资源目录：/path/to/dashboard/user-dist（同上）

### **2. 运行Dashboard**

运行命令：/path/to/dashboard -c /path/to/config.config.yaml -db /path/to/sqlite.db

- 自己写个systemd配置文件开机自启
- 首次运行去掉-db /path/to/sqlite.db，并删除旧的sqlite.db（要保留旧数据库的话就重命名文件），让程序自动生成配置文件和数据库
  ***配置文件中：***
- listenport字段为后台地址及Agent连接监听端口，从v1开始合并了两个端口，自己做好反代
- agentsecretkey用于写到Agent的配置文件中，作为Agent连接Dashboard的密钥

### **3. 运行Agent**

运行命令：/path/to/agent -c /path/to/config.yaml

- 自己写个systemd配置文件开机自启
- 首次运行用命令/path/to/agent edit来生成配置文件，按操作指引去选择选项（uuid可以按tab键随机生成）
- 首次生成配置文件后，要修改下配置文件
  ***配置文件中：***
- client_secret填入Dashboard配置文件中的agentsecretkey字段
- server为Dashboard的服务器地址和端口（Dashboard配置文件中listenport的监听端口，自己做好反代）

## nezha 命令行操作

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
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --config value, -c value  配置文件路径
   --help, -h                show help
   --version, -v             print the version
 ```


```bash
$ sudo ./nezha-agent service -h
NAME:
   nezha-agent service - 服务操作

USAGE:
   <install/uninstall/start/stop/restart>

OPTIONS:
   --config value, -c value  配置文件路径
   --help, -h                show help
```





## 相关资料

- [设置 OAuth 2.0 绑定](https://nezha.wiki/guide/q14.html)
- [Nezha Dashboard V1 前端源码](https://github.com/hamster1963/nezha-dash-v1?tab=readme-ov-file)
- [自定义代码](https://nezhadash-docs.buycoffee.top/custom-code)
- [服务器公开备注生成器](https://nezhainfojson.pages.dev/)
- [一些可能好看的项目](https://buycoffee.top/work)
- [欢迎动画]](https://buycoffee.top/blog/tech/2025-redesign)
- [美化 1](https://blog.zmyos.com/nezha-theme.html)
- [美化 2](https://misaka.es/archives/33.html)
- [bing API](https://api-bimg-cc.apifox.cn/)
- [bing api github](https://github.com/flow2000/bing-wallpaper-api?tab=readme-ov-file)
- [分享2009-至今的必应壁纸](https://www.aliyundrive.com/s/VF4HskqwXMk)

### 安全设置

关闭 ssh

https://nezha.wiki/guide/q7.html
https://blog.weedsstars.com/index.php/archives/26/
https://www.nodeseek.com/post-232313-1