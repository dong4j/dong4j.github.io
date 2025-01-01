---
title: 在CentOS上享受更高效的Shell体验：oh-my-zsh
keywords:
  - Shell
categories:
  - 新时代码农
tags:
  - CentOS
  - oh-my-zsh
  - Shell Installation
  - zsh
  - bash
abbrlink: ac4909f7
date: 2013-02-14 00:00:00
ai:
  - 本教程详细介绍了在CentOS系统上安装和配置oh-my-zsh的过程。首先通过查看当前系统shell确认默认环境，并检查是否已安装zsh包，如果未安装则使用yum命令进行安装。接着指导用户如何将默认的bash
    shell更改为zsh，通过执行chsh命令并重启服务器来完成切换。最后介绍如何在CentOS上安装oh-my-zsh和相关插件，提供详细的操作步骤，并解决可能遇到的locale问题。整个过程包括shell操作、系统软件包管理以及使用终端命令进行配置。
description: 本教程详细介绍了在CentOS系统上安装和配置oh-my-zsh的过程。首先通过查看当前系统shell确认默认环境，并检查是否已安装zsh包，如果未安装则使用yum命令进行安装。接着指导用户如何将默认的bash
  shell更改为zsh，通过执行chsh命令并重启服务器来完成切换。最后介绍如何在CentOS上安装oh-my-zsh和相关插件，提供详细的操作步骤，并解决可能遇到的locale问题。整个过程包括shell操作、系统软件包管理以及使用终端命令进行配置。
---


使用 root 用户登录，下面的操作基本都没有 root 的困扰，如果非 root 用户请切换至 root 用户操作。

**1、查看系统当前的 shell**

```shell
echo $SHELL
```

返回结果如下：

```shell
/bin/bash
```

_PS. 默认的 shell 一般都是 bash_

---

**2、查看 bin 下是否有 zsh 包**

```shell
cat /etc/shells
```

返回结果如下：

```shell
/bin/sh
/bin/bash
/sbin/nologin
/bin/dash
/bin/tcsh
/bin/csh
```

_PS. 默认没有安装 zsh_

---

**3、安装 zsh 包**

```shell
yum -y install zsh
```

安装完成后查看 shell 列表：

```shell
cat /etc/shells
```

返回结果如下：

```shell
/bin/sh
/bin/bash
/sbin/nologin
/bin/dash
/bin/tcsh
/bin/csh
/bin/zsh
```

_现在 zsh 已经安装完成了，需要把系统默认的 shell 由 bash 切换为 zsh_

---

**3、切换 shell 至 zsh，代码如下：**

```shell
chsh -s /bin/zsh
```

chsh 用法请自行查找，返回结果如下：

```shell
Changing shell for root.
Shell changed.
```

按提示所述，shell 已经更改为 zsh 了，现在查看一下系统当前使用的 shell，

```shell
echo $SHELL
```

返回结果如下：

```shell
/bin/bash
```

看样子还没切换过来，需要重启一下服务器，我的习惯做法是在 ECS 的 web 管理平台重启，`reboot`到底好不好使还没试过，大家可以试试

重启过后，使用代码查看当前使用的 shell

```shell
echo $SHELL
```

返回结果：

```shell
/bin/zsh
```

得到如此结果，证明 shell 已经切换成功了。

---

**下面开始安装 oh-my-zsh**
    *oh-my-zsh 源码是放在 github 上的，所以先要安装 git*
**4、安装 git：**

```shell
yum -y install git
```

**5、安装 oh-my-zsh:**

```shell
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
```

如果显示如下界面表示成功：

```shell
         __                                     __
  ____  / /_     ____ ___  __  __   ____  _____/ /_
 / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \
/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /
\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/
                        /____/                       ....is now installed!
Please look over the ~/.zshrc file to select plugins, themes, and options.

p.s. Follow us at https://twitter.com/ohmyzsh.

p.p.s. Get stickers and t-shirts at http://shop.planetargon.com.
```

如果添加插件、更改 themes 请修改~/.zshrc 或自行查询其它资料。

至此，zsh 安装完毕，开始享受 oh-my-zsh 吧，如果执行命令时提示`warning: cannot set LC_CTYPE locale`可用以下方法解决：

修改 profile：

```shell
vi /etc/profile
```

在 profile 末尾添加以下代码：

```shell
export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8
```

引用更改后的 profile：

```shell
source /etc/profile
```

此时 bash 已切换至 zsh。
