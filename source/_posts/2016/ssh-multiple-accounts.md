---
title: 自定义SSH密钥，高效管理多个GitHub和GitLab账户
keywords:
  - Spring
categories:
  - Spring
tags:
  - GitHub
  - SSH认证
  - Git配置管理
  - 远程仓库操作
  - 私钥生成
abbrlink: 32516dfc
date: 2016-09-11 00:00:00
ai:
  - 解决在不同 GitHub 账号中遇到的 SSH 访问权限问题。通过生成具有唯一名称的公私钥对，并为每个账号设置相应的 SSH 配置和别名，确保可以成功访问不同的仓库。文章还提供了如何测试连接、使用
    repo 设置替换全局设置以及 GitLab 使用自定义密匙的方法。
description: 解决在不同 GitHub 账号中遇到的 SSH 访问权限问题。通过生成具有唯一名称的公私钥对，并为每个账号设置相应的 SSH 配置和别名，确保可以成功访问不同的仓库。文章还提供了如何测试连接、使用
  repo 设置替换全局设置以及 GitLab 使用自定义密匙的方法。
---

> ERROR: Permission to ArrayDsj/git-test.git denied to dong4j.
> fatal: Could not read from remote repository.

> Please make sure you have the correct access rights
> and the repository exists.

目前有 2 个 github 账号, 一个公司的 gitlab 账号

有一次遇到了

```
ERROR: Permission to XXX.git denied to user
```

错误, 整理了一下,这里做一个记录

## 错误前提

很久以前使用 ssh-keygen 生成一对默认名称的公私匙, 直接导入 github 中就能使用, 这是只在一个用户的情况下, 后台又申请了一个 github 账号, 还是使用 id_rsa.pub 这个默认的公匙, 这就造成了上面的错误.

## 解决方法

为不同的账号生成不同的公私匙

**1. 生成密匙对**

```shell
# 生成密匙对 名称为 user1-github-ssh-key
ssh-keygen -t rsa -f ~/.ssh/user1-github-ssh-key -b 4096 -C "user1@mail.com"

# 生成密匙对 名称为 user2-github-ssh-key
ssh-keygen -t rsa -f ~/.ssh/user2-github-ssh-key -C user2@mail.com

# 因为默认只读取 id_rsa，为了让 SSH 识别新的私钥，需将其添加到 SSH agent 中：
ssh-add ~/.ssh/user1-github-ssh-key
ssh-add ~/.ssh/user2-github-ssh-key

# 登陆2个不同的Github账号, 点击 网页右上侧的 Account Setting 按钮 - 选择 ssh-keys  点击 Add SSH Key
```

**2. 设置 ssh config**

```shell
# Default github user(user1@mail.com)
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/user1-github-ssh-key

 # second user(user2@mail.com)
 # 建一个github别名，新建的帐号使用这个别名做克隆和更新
Host github2
    HostName github.com
    User git
    IdentityFile ~/.ssh/user2-github-ssh-key.pub
```

**3. 连接测试**

```shell
$ ssh -T git@github.com
Hi user1! You've successfully authenticated, but GitHub does not provide shell access.

$ ssh -T github2
Hi user2! You've successfully authenticated, but GitHub does not provide shell access.
```

**4. 使用 repo 设置代替 git 全局设置**

```shell
# 查看 git config 配置
格式：git config [--local| --global | --system] -l
查看仓库级的 config，即 .git/config，命令：git config --local -l
查看全局级的 config，即 ~/.gitconfig，命令：git config --global -l
# 使用 homebrew 安装的 git 的配置文件路径
查看系统级的 config，即 /usr/local/etc/gitconfig，命令：git config --system -l
查看当前生效的配置，命令：git config -l
```

```shell
# 删除全局配置
git config --global --unset user.email

# 在 repo 下使用局部配置
git config --local user.name "user1"
git config --local user.email user1@mail.com
```

**5. git 操作测试**

```shell
# 本地新建项目
git init
git add .
git commit -t 'init'
git remote add origin git@github.com:dong4j/dubbo_demo.git
# push 到远程仓库
git push -u origin master
# 从远程仓库更新
git pull origin master
```

## GitLab 使用自定义密匙

修改 .ssh/config

```
Host  gitlab服务器ip地址
    RSAAuthentication yes
    IdentityFile ~/.ssh/your-ssh-key
```
