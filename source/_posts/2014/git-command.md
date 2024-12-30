---
title: Git 命令大全
keywords:
  - Git
categories:
  - Git
tags:
  - Git教程
  - 版本控制系统
  - 基础命令
  - 高级功能
abbrlink: 858a1037
date: 2014-10-06 00:00:00
ai:
  - 本篇文章全面介绍了使用Git进行版本控制的核心命令和操作。它涵盖了基础概念、核心命令以及一些高级用法，从仓库初始化到文件提交，从分支管理到远程同步，并深入讨论了撤销更改、代码归档等高级功能。文章以Markdown格式呈现，内容包括创建仓库、添加和删除代码、创建和切换分支、进行合并、解决冲突、提交更改、远程仓库的协作以及一些特殊情况下的操作，如强制推送和回滚修改。通过逐步指导和详细解释每一步的操作原理，帮助开发者掌握Git的基本到高级使用技巧。
description: 本篇文章全面介绍了使用Git进行版本控制的核心命令和操作。它涵盖了基础概念、核心命令以及一些高级用法，从仓库初始化到文件提交，从分支管理到远程同步，并深入讨论了撤销更改、代码归档等高级功能。文章以Markdown格式呈现，内容包括创建仓库、添加和删除代码、创建和切换分支、进行合并、解决冲突、提交更改、远程仓库的协作以及一些特殊情况下的操作，如强制推送和回滚修改。通过逐步指导和详细解释每一步的操作原理，帮助开发者掌握Git的基本到高级使用技巧。
---

## 新建代码库

在开始任何项目前，我们通常需要创建一个新的代码库。这可以通过以下方式完成：

```bash
# 在当前目录创建新的git仓库
$ git init
# 初始化一个新目录作为Git代码库（如果这个目录已存在）
$ git init [project-name]
# 克隆远程代码库至本地
$ git clone [url]
```

### 注意事项：

- 请确保选择合适的位置和项目名称，避免与现有文件或目录冲突。
- 如果要克隆一个项目，请确认你有访问权限以及所选 URL 是正确的。

## 配置

配置 Git 有助于确保你在提交时信息准确且一致：

```bash
# 查看当前Git的全局配置
$ git config --list
# 编辑本地或全球的gitconfig文件
$ git config -e [--global]
# 设置提交代码时的基本用户信息（推荐使用--global）
$ git config [--global] user.name "[name]"
$ git config [--global] user.email "[email address]"
```

### 注意事项：

- 使用`--global`标志设置配置项，可以确保在所有项目中都保持一致性。
- 确保你的用户名和邮箱是独一无二的，并且与你在代码托管平台上使用的账户信息一致。

## 增加/删除文件

这些命令用于管理仓库中的文件：

```bash
# 添加指定文件到暂存区
$ git add [file1] [file2] ...
# 将目录及其子目录的所有更改添加到暂存区
$ git add [dir]
# 将工作区中所有的改动都提交至暂存区（包括新添和修改过的文件）
$ git add .
# 使用交互模式，每次变更前提示确认是否要将该文件的部分或全部变更提交（可选）
$ git add -p
# 从工作区删除文件，并将这次删除放入暂存区
$ git rm [file1] [file2] ...
# 停止追踪指定文件，但保留在本地（不从磁盘中删除）
$ git rm --cached [file]
# 更改文件名并将其更改提交到暂存区
$ git mv [file-original] [file-renamed]
```

### 注意事项：

- 使用`git add .`时要特别小心，确保你了解所有变化。
- 在执行`rm`命令前，最好先确认被删除的文件是否是你想要移除的。

## 代码提交

这些命令用于将暂存区的内容提交到本地仓库中：

```bash
# 提交暂存区的所有更改至仓库（需要填写一条commit信息）
$ git commit -m [message]
# 提交特定文件或目录至仓库，附带消息
$ git commit [file1] [file2] ... -m [message]
# 直接提交工作区内所有已追踪过的改动至仓库区
$ git commit -a
# 在commit时显示详细变更信息（diff）
$ git commit -v
# 使用新的commit覆盖上一次的提交，适用于没有实际内容变化但需修改commit信息的情况
$ git commit --amend -m [message]
# 对特定文件进行二次提交（在已有的commit基础上）
$ git commit --amend [file1] [file2] ...
```

### 注意事项：

- 使用`git commit --amend`仅当没有推送过代码时是安全的，否则可能会引起冲突。
- 提交信息应简明扼要且具有描述性。

## 分支

分支管理对于大型项目来说至关重要：

```bash
# 列出所有本地分支名称
$ git branch
# 查看远程仓库的所有分支及其最新提交记录
$ git branch -r
# 显示所有本地和远程分支列表
$ git branch -a
# 在当前目录创建一个新分支，但不切换到该分支上
$ git branch [branch-name]
# 创建并立即检查出新的分支（相当于执行两次命令）
$ git checkout -b [branch]
# 根据特定的commit建立一个新的分支
$ git branch [branch] [commit]
# 远程分支的追踪关系配置
$ git branch --track [branch] [remote-branch]
# 切换到指定的分支，并更新工作目录中的文件
$ git checkout [branch-name]
# 快速切换回之前活跃过的最后一个分支
$ git checkout -
# 为现有本地分支和远程仓库上的一个分支建立追踪关系
$ git branch --set-upstream-to=[remote/branch] [local-branch]
# 合并指定分支的内容到当前工作区中
$ git merge [branch]
# 从其他提交引入变更至当前分支（不会修改历史记录）
$ git cherry-pick [commit]
# 删除本地的分支
$ git branch -d [branch-name]
# 移除远程仓库上的一个分支
$ git push origin --delete [branch-name] 或者
git branch -dr [remote/branch]
```

### 注意事项：

- 切换分支前，请确保你已保存并提交所有更改。
- 删除分支时务必谨慎，这将永久移除所有未推送的变更。

## 标签

标签用于标记重要的版本或里程碑：

```bash
# 显示全部标签列表
$ git tag
# 在当前提交创建一个轻量级标签（默认）
$ git tag [tag]
# 创建一个带有注释信息的附带对象引用的标签（可选）
$ git tag -a [tag] -m "blablabla"
# 删除本地的标签
$ git tag -d [tag]
# 在远程仓库中删除标签，需要先推送后移除
$ git push origin --delete [tagName]
# 查看指定标签的信息及其提交历史记录
$ git show [tag]
# 将所有本地标签推送到远程
$ git push [remote] --tags
# 也可以指定要推送的某个标签
$ git push [remote] [tagname]
```

### 注意事项：

- 删除标签时需要小心，确保你不需要这个版本的历史记录。
- 推送标签之前，请确认该操作不会覆盖任何重要的历史标记。

## 查看信息

这些命令用于检查仓库的状态和变化：

```bash
# 显示工作区中哪些文件有变更或尚未追踪（git status）
$ git status
# 以时间线形式展示当前分支的历史记录（可以使用各种格式化选项，如--pretty=format:等）
$ git log
# 展示每次提交的差异及其涉及的文件列表（git log --stat）
$ git log --stat
# 查找包含某个关键词的commit历史纪录
$ git log -S [keyword]
# 显示自指定标签以来的所有变更，每条记录一行（git log tag...HEAD --pretty=format:%s）
$ git log [tag] HEAD --pretty=format:%s
# 筛选并显示符合特定模式或文本的提交信息摘要（--grep=feature相当于-S feature但匹配所有文件而非仅限于单个文件）
$ git log [tag] HEAD --grep feature
# 查看某文件在不同版本之间的变更历史，包括名称更改记录（git whatchanged等同于log --follow但以更简洁的方式展示）
$ git log --follow [file]
$ git whatchanged [file]
# 以diff的形式输出指定文件的详细提交历史记录
$ git log -p [file]
# 显示最近五次提交信息，格式简练（git log -5相当于log --oneline --no-walk HEAD^5..HEAD）
$ git log -5 --pretty --oneline
# 统计所有提交者的活跃度排名和提交总数（类似shortlog但显示作者名而非commit hash）
$ git shortlog -sn
# 查找并列出某个文件的修改者及其最后一次编辑时间
$ git blame [file]
# 比较工作目录与暂存区之间的差异，显示尚未添加至暂存或已移除的内容（git diff等同于diff-index --cached HEAD --）
$ git diff
# 显示暂存区相较于上一个提交的修改内容（git diff --staged）
$ git diff --cached [file]
# 对比工作区中的文件与最近一次commit的差异（git diff HEAD...）
$ git diff HEAD
# 生成两个分支之间的diff报告，展示它们合并后可能产生的冲突或区别
$ git diff [first-branch]...[second-branch]
# 统计某段时间内的代码变更行数（比如今天的工作量）
$ git diff --shortstat "@{0 day ago}"
# 查看某个commit的详细信息和提交内容
$ git show [commit]
# 列出指定commit所涉及的所有文件列表，不显示差异或元数据
$ git show --name-only [commit]
# 显示某次特定版本中某文件的内容（git cat-file blob等价于show）
$ git show [commit]:[filename]
# 查看最近几次本地提交记录简要信息
$ git reflog
```

### 注意事项：

- 使用`git log`查看历史时，可以结合各种参数和选项来定制输出内容。
- `git blame`是一个强大的工具，但频繁使用可能会对性能产生影响。

## 远程同步

远程操作是与团队成员共享代码的关键：

```bash
# 从远程仓库下载最新变动到本地暂存区（不会合并到工作目录）
$ git fetch [remote]
# 显示所有已配置的远程仓库及其URL等信息
$ git remote -v
# 查看特定远程分支的所有配置详情
$ git remote show [remote]
# 添加新的远程仓库，并指定别名或简称用于后续操作
$ git remote add [shortname] [url]
# 从远程仓库下载最新代码并合并到本地分支（通常与pull命令结合使用）
$ git pull [remote] [branch]
# 同步本地指定分支至对应的远程分支，确保两者一致
$ git push [remote] [branch]
# 强制推送当前分支的更改至远程仓库，忽略任何可能存在的冲突或问题
$ git push [remote] --force
# 将所有本地分支同步推送到远程服务器上（git push --all等同于遍历所有分支并执行push命令）
$ git push [remote] --all
# 指定将本地master分支推送至远程仓库的主干分支，首次推送时设置默认关联关系
$ git push -u origin master
```

### 注意事项：

- 强制推送到远程通常意味着覆盖他人的工作，务必在沟通后进行。
- 使用`git pull`之前，最好先确保自己的代码已完全提交。

## 撤销操作

这些命令用于撤销错误的更改或恢复特定状态：

```bash
# 从暂存区还原指定文件至工作目录（相当于checkout）
$ git checkout [file]
# 将特定commit中某个文件的状态重置到暂存区，同时保留其在工作目录中的当前版本
$ git checkout [commit] [file]
# 还原所有已添加到暂存区的变更至工作区
$ git checkout .
# 仅将指定文件从暂存区恢复至上一次提交状态（保持工作区不变）
$ git reset [file]
# 同时重置暂存区和工作区，使得与上一次commit完全一致
$ git reset --hard
# 将当前分支的指向回溯到某个commit，并同步更新暂存区，但保留工作目录中的最新修改（不推荐此操作）
$ git reset [commit]
# 强制重置当前HEAD至指定commit状态，覆盖所有未提交过的改动且不留记录
$ git reset --hard [commit]
# 仅将分支的指向移动到某个历史位置，同时保持暂存区和工作目录中的全部修改
$ git reset --keep [commit]
# 创建一个新的commit用于撤销之前的一个或多个更改（git revert等同于创建新提交而不仅仅是回滚）
$ git revert [commit]
# 暂时存储尚未提交的更改至栈中，以便稍后恢复使用
$ git stash
# 将最新的stash弹出并应用于工作区
$ git stash pop
```

### 注意事项：

- `git reset --hard`是一个危险的操作，请确保了解其影响后再执行。
- 使用`revert`命令可以创建一个新的 commit 来撤销特定的更改，适合需要记录历史的情况。

## 其他

还有一些额外的功能和操作：

```bash
# 生成一个压缩文件包用于发布或分发代码
$ git archive
```

### 注意事项：

- `git archive`是一个非常有用的工具，特别是当你需要创建归档版而不带任何 Git 元数据时。
