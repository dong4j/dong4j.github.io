---
title: Git基础命令全解析：掌握版本控制的艺术
keywords:
  - Git
categories:
  - 新时代码农
tags:
  - Git
  - 版本控制
  - 软件开发
  - 代码提交
  - 远程仓库
  - 分支管理
  - 文件名处理
abbrlink: 6952e88b
date: 2014-10-11 00:00:00
ai:
  - 本文涵盖了Git基础命令、代码版本管理、远程仓库操作和项目上传至GitHub等主题。详细介绍了如何初始化项目、添加文件到版本控制、创建分支、合并更改以及使用别名简化操作。此外，文章还指导了删除特定的文件或目录、修改文件名大小写、同步本地与远程仓库以及处理分支和远程地址变更。文章最后提醒，在进行敏感操作时应谨慎，确保不会意外删除重要数据。
description: 本文涵盖了Git基础命令、代码版本管理、远程仓库操作和项目上传至GitHub等主题。详细介绍了如何初始化项目、添加文件到版本控制、创建分支、合并更改以及使用别名简化操作。此外，文章还指导了删除特定的文件或目录、修改文件名大小写、同步本地与远程仓库以及处理分支和远程地址变更。文章最后提醒，在进行敏感操作时应谨慎，确保不会意外删除重要数据。
---

## .gitignore 规则写法

.gitignore 文件用于指定哪些类型的文件应被 Git 忽略。以下是一些常用的忽略规则：

1. **在已忽略文件夹中不忽略特定的子文件夹**：

```
/node_modules/*
!/node_modules/layer/
```

2. **在已忽略文件夹中不忽略特定的文件**：

```
/node_modules/*
!/node_modules/layer/layer.js
```

注意：要使这些规则生效，被忽略的文件或目录需要以 `/*` 结尾。此外，请参考以下规则写法：

- 以斜杠 `/` 开头表示目录；
- 星号 `*` 可匹配多个字符；
- 问号 `?` 匹配单个字符；
- 方括号 `[]` 内包含单个字符的匹配列表；
- 大叹号 `!` 表示不忽略（跟踪）匹配到的文件或目录；

## 取消跟踪已版本控制的文件

你可以使用 `git update-index --assume-unchanged <file>` 命令来取消对一个文件的跟踪。这适用于你希望暂时停止 Git 监控特定文件变动的情况。

```bash
git update-index --assume-unchanged your_file_path
```

## 从版本库中删除文件或目录

如果你想将某个目录（如 `app/test`）从 Git 仓库中移除但不删除本地的文件，你可以按照以下步骤进行操作：

1. **查看要删除的列表**：
   ```bash
   git rm -r -n --cached app/test
   ```
2. **执行实际删除**：

   ```bash
   git rm -r --cached app/test
   ```

3. 修改 `.gitignore` 文件，增加忽略规则以防止 Git 再次跟踪该目录下的文件。例如，在 `.gitignore` 文件中添加如下内容：

   ```markdown
   /app/test/
   ```

4. **提交更改**：

   ```bash
   git commit -m "不再跟踪test文件夹"
   ```

5. 如果有远程分支，将改动推送到远程。

如果你同时想要删除本地的测试目录中的所有文件，则可以使用以下命令：

1. **查看要删除的内容**：
   ```bash
   git rm -r -n test
   ```
2. **执行实际删除**：
   ```bash
   git rm -r test
   ```

## 创建和推送标签

### 创建标签

```bash
git tag <tag_name>
```

或者带有描述信息的标签：

```bash
git tag -a v0.1 -m "版本 0.1 发布" d5a65e9
-a: 指定标签名；-m: 提供附注说明
```

### 查看所有标签

直接运行 `git tag` 命令即可查看当前工作区的所有标签。

### 查看特定标签的描述信息

```bash
git show <tag_name>
```

### 推送标签

#### 单个标签

```bash
git push origin <tag_name>
```

#### 所有标签

使用以下任意一种命令来推送所有的标签：

```bash
git push --tags
或者
git push origin --tags
```

## 删除标签

删除本地标签：

```bash
git tag -d <tag_name>
```

远程标签的删除需要通过 `git push` 命令来完成，具体操作为：

```bash
git push origin :refs/tags/<tag_name>
```

例如：要删除名为 "V3.0.1-Release" 的标签：

```bash
git push origin :refs/tags/V3.0.1-Release
```

## 同步标签

为了同步你的本地和远程仓库的标签，可以先在本地删除所有旧标签后重新拉取所有的最新标签。

```bash
# 删除本地所有标签
git tag -l | xargs git tag -d

# 从远程仓库拉取消除不再存在的引用（分支或标签）
git fetch origin --prune

# 拉取并更新标签
git fetch origin --tags
```

## Git 统计提交次数及代码量变化

统计指定作者的提交次数：

```bash
git log --author=某人名 --since="起始时间，如：2019-01-01" --no-merges | grep -e 'commit [a-zA-Z0-9]*' | wc -l
```

统计指定作者增加和删除的代码量：

```bash
git log --author=某人名 --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "添加行数： %s, 删除行数： %s，总行数变化：%s\n", add, subs, loc }' -
```

## 同时向多处推送代码

### 添加第二个远程地址

如果你希望你的项目可以同时推送到多个远程仓库，首先需要添加额外的远程地址。例如：

```bash
git remote set-url --add origin git@github.com:morethink/programming.git
```

然后你可以通过 `git remote -v` 查看所有的远端分支及其对应地址。

### 同时推送至多个远程

一旦你设置了多个远程仓库，当你执行 `git push origin master` 时，Git 会自动将代码推送到所有已配置的远程仓库。示例如下：

```bash
Everything up-to-date
Everything up-to-date
```

## 强制提交更改

有时候我们可能需要强制推送我们的改动到远程分支（尤其是当我们本地版本较新或希望覆盖远程版本时），这时可以使用 `git push` 命令的 `-f` 或 `--force` 选项：

```bash
git push origin master --force
```

## 克隆指定标签的仓库

如果想要克隆一个特定标签的仓库，可以直接在命令行中执行如下操作：

```bash
git clone --branch [tags标签] [git地址]
```

例如：将某标签下的代码库拉取到本地

```bash
git clone --branch v2.0.3 https://github.com/example/project.git
```

## 配置代理和取消代理设置

有时候为了访问远程仓库，我们可能需要配置 HTTP/HTTPS 的代理服务器。可以通过以下命令进行设置：

设置代理：

```bash
git config --global http.proxy 'socks5://127.0.0.1:$端口号'
```

或者对于 https 的请求：

```bash
git config --global https.proxy 'socks5://127.0.0.1:$端口号'
```

取消代理设置，可以使用以下命令移除全局配置中的 http 和 https 代理：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

或者创建一些别名来简化操作：

```bash
alias fuckgit="git config --global http.proxy 'socks5://127.0.0.1:8889' && git config --global https.proxy 'socks5://127.0.0.1:8889'"
alias unfuckgit="git config --global --unset http.proxy && git config --global --unset https.proxy"
```

## 初始化项目并上传到 GitHub

为了使用 Git，你需要首先全局设置用户信息：

```bash
# 设置用户名和邮箱
git config --global user.name "dong4j"
git config --global user.email "dong4j@gmail.com"
```

然后按照以下步骤进行操作：

1. 进入你的项目目录，并初始化一个新的 Git 仓库。
2. 添加你想要版本控制的文件到暂存区（staging area）。
3. 提交更改并添加描述信息。

```bash
git init
git add fileName
git commit -m '说明'
```

接着，将本地仓库与 GitHub 上的新建仓库关联起来：

```bash
# 关联远程仓库
git remote add origin git@github.com:dong4j/dubbo_demo.git
```

最后上传你的代码到 GitHub：

```bash
git push -u origin master
```

### 强制提交更改并同步本地分支

你可以使用相同的方式推送更新，并且在必要时强制覆盖远程的版本。

```bash
# 同步本地与远程仓库
git pull origin master
```

或者如果需要强制推送更改，则使用：

```bash
git push -u origin master --force
```

## 创建及同步分支

创建新分支的操作相当简单：

```bash
# 创建并切换到新的分支
git checkout -b new_branch_name
```

之后，你可以将这个本地分支推送到远程仓库，并将其与一个远端分支关联起来。完成这些操作后，你就可以在 GitHub 上看到你的分支了。

## 处理大小写不匹配的文件名

如果需要修改文件名中的大小写（这通常是一个敏感的操作），可以使用以下命令：

```bash
git mv --force filename.java FileName.java
```

## 移除版本控制下的某个文件或目录

如果你想要移除某特定文件或者整个目录的 Git 跟踪信息，你可以采用如下的步骤：

首先，在不实际删除任何内容的情况下预览将要执行的操作：

```bash
# 仅显示将会被忽略的内容列表（-n 参数）
git rm -r -n --cached "bin/"
```

然后执行最终命令来移除 Git 跟踪：

```bash
git rm -r --cached "bin/"      // 移除目录的Git跟踪信息，但保留文件在本地。
git commit -m" remove bin folder all file out of control"
```

最后将变更推送到远程仓库：

```bash
git push origin master
```

## 修改文件夹名称或移除版本控制下的空文件夹

添加 .gitkeep 文件至所有未被 Git 跟踪的空文件夹：

```bash
find . −type d −empty -and −not −regex ./\.git.∗ -exec touch {}/.gitkeep \;
```

## 删除远端分支

要删除远程仓库中的一个特定分支，请遵循以下步骤：

1. 查看所有本地及远程分支。
2. 如果需要，先在本地移除指定的分支。
3. 使用 `git push` 命令从原始远程仓库中删除该分支。

```bash
# 查看所有本地和远程分支（-a 表示所有）
git branch -a

# 删除本地分支
git branch -d branchname

# 从远端删除一个分支
git push origin :branchname
```

## 修改远程仓库的地址

修改 Git 远程仓库地址有几种方式：

1. 使用 `set-url` 命令：
   ```bash
   git remote set-url origin [新的URL]
   ```
2. 删除旧的远端并重新添加一个新远端：

   ```bash
   git remote rm origin
   git remote add origin [新的URL]
   ```

3. 直接修改 `.git/config` 文件，定位到正确的部分并更新 URL。

## 修改文件名大小写

若需改变文件名称的大小写（请注意这在某些系统上可能不会生效），可以使用：

```bash
git mv --force filename.java FileName.java
```

这样可以在保留历史记录的同时更改文件名字。
