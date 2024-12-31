---
title: Ubuntu 图形界面与命令行模式切换及 SSH 服务配置
keywords:
  - Linux
categories:
  - Linux
tags:
  - Ubuntu
  - 图形界面
  - 命令行模式
  - SSH服务
  - 远程访问
abbrlink: ab98e58e
date: 2014-09-22 00:00:00
ai:
  - 在Ubuntu系统中，掌握图形界面与命令行模式的切换和SSH服务配置对于系统管理至关重要。本文提供了如何在两者之间快速切换、安装openssh-server、检查和启动SSH服务、查看IP地址以及修改SSH配置文件以允许root用户通过SSH登录的步骤。
description: 在Ubuntu系统中，掌握图形界面与命令行模式的切换和SSH服务配置对于系统管理至关重要。本文提供了如何在两者之间快速切换、安装openssh-server、检查和启动SSH服务、查看IP地址以及修改SSH配置文件以允许root用户通过SSH登录的步骤。
---

在 Ubuntu 系统的使用过程中，熟练掌握图形界面与命令行模式的切换，以及配置 SSH 服务是非常有用的技能。下面我将分享一些基本的操作步骤，帮助 Ubuntu 初学者们更好地管理自己的系统。

## 图形界面与命令行模式切换

在 Ubuntu 系统中，你可以通过以下快捷键在图形界面和命令行模式之间进行切换：

- **切换到命令行模式**：使用 `Ctrl + Alt + F2` 到 `F6`。每个组合键会打开一个新的命令行界面。
- **切换回图形界面**：使用 `Ctrl + Alt + F7`。

## 安装 openssh-server

为了能够远程登录到你的 Ubuntu 系统，你需要安装 openssh-server。

1. 首先，更新你的系统包列表：
   ```bash
   sudo apt-get update
   ```
2. 接着，安装 openssh-server：
   ```bash
   sudo apt-get install openssh-server
   ```

## 查看和开启 SSH 服务

安装完成后，你可以检查 SSH 服务是否已经开启。

1. 查看当前运行的进程，确认 SSH 服务是否在运行：
   ```bash
   sudo ps -e | grep ssh
   ```
2. 如果 SSH 服务没有运行，你可以通过以下命令启动它：
   ```bash
   sudo service ssh start
   ```

## 查看系统 IP 地址

在配置 SSH 服务之前，你可能需要知道你的系统 IP 地址。可以使用以下命令查看：

```bash
ifconfig
```

## 修改 SSH 配置文件

为了允许 root 用户通过 SSH 登录，你需要修改 SSH 的配置文件。

1. 打开终端窗口，使用以下命令编辑配置文件：
   ```bash
   sudo gedit /etc/ssh/sshd_config
   ```
2. 在打开的编辑器中，找到以下行：
   ```
   PermitRootLogin without-password
   ```
   在这一行的前面加上 `#` 号，将其注释掉。
3. 在文件的合适位置（通常是文件的末尾），添加以下行：
   ```
   PermitRootLogin yes
   ```
4. 保存文件并关闭编辑器。这样，你就允许了 root 用户通过 SSH 登录。

## 结语

通过以上步骤，你现在应该能够熟练地在 Ubuntu 系统的图形界面和命令行模式之间切换，并且成功配置了 SSH 服务。这些技能将帮助你更好地管理和远程访问你的 Ubuntu 系统。如果你是 Ubuntu 新手，这些操作将是一个很好的开始。继续探索和学习，祝你在 Ubuntu 的世界旅程愉快！
