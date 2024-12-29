---
title: 解决 git 仓库体积过大导致 push 失败的问题
ai: true
categories: 问题集
tags: Git
abbrlink: b051
date: 2024-12-28 15:39:35
cover: https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229170536_bsenV6FP.webp
---

![/images/cover/20241229170536_bsenV6FP.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229170536_bsenV6FP.webp)

## 背景

最近在进行博客迁移, 以前吃过图床的亏, 所以这次将图片全部保留在本地, 并使用 GitHub 和 Gitee 来作备份, 但是因为大量的图片提交导致出发了 Gitee 的仓库体积限制, 在最近几次提交时, 出现了如下错误:

```bash
remote: Powered by GITEE.COM [1.1.5]
remote: Set trace flag 784c0784
remote: Repo size: 1077.199MB, exceeds quota 1024MB
remote: Push rejected for repository [size exceeds limit]
remote: HelpLink:           https://gitee.com/help/articles/4232
remote: Repository GC:      https://gitee.com/xxx/hexo-site/settings#git-gc
remote: Enterprise Edition: https://gitee.com/enterprises#commerces
To gitee.com:dong4j/hexo-site.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'gitee.com:xxx/hexo-site.git'
```

## 解决

根据 Gitee 的官方文档介绍, Gitee 平台目前对仓库的配额如下：

| 套餐   | 免费版      | 基础版      | 标准版      | 高级版      | 尊享版      |
| ------ | ----------- | ----------- | ----------- | ----------- | ----------- |
| 单仓库 | 最大 500 MB | 最大 1 GB   | 最大 1 GB   | 最大 2 GB   | 最大 3 GB   |
| 单文件 | 最大 50 MB  | 最大 100 MB | 最大 100 MB | 最大 200 MB | 最大 300 MB |

### 1. 清理不必要的对象

首先可以尝试清理一些不必要的 Git 对象:

```bash
git gc --prune=now
```

这个命令会压缩 Git 仓库中的历史，清理松散对象，并删除无法访问的对象。

> 存储库 GC 可以检查仓库中未使用的对象和资源，将其删除或压缩成更小的对象，从而优化 Git 在存储库性能，减少存储库磁盘占用。
>
> 当仓库体积膨胀导致访问速度下降时，通过 Git GC 将可能提高仓库的访问速度。
>
> 阶段时间内使用多次强推从仓库中删除了大量数据，使用 Git GC 可以删除未使用的对象，释放存储空间。

![20241228154907_R1PsKEVu.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241228154907_R1PsKEVu.webp)

执行后并没有减少仓库体积, 所以还要继续.

### 2. 删除大文件的历史记录

前面说了我的仓库提交了很多图片和少量 mp4 等大体积文件, 所以我们可以使用 `git-filter-repo` 工具来删除它们的历史记录。

在 macOS 下安装 `git-filter-repo`:

```bash
brew install git-filter-repo
```

然后可以运行以下命令来删除特定文件类型的历史记录：

```bash
git filter-repo --invert-paths --path-regex '\.(jpg|jpeg|png|gif|mp4|webp|svg)$' --force
```

执行之后的效果:

![20241228155218_2lI2gpOj.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241228155218_2lI2gpOj.webp)

清理效果非常好, **但是** 把我仓库里面的所有图片全部清空了, 我要的是只删除历史记录中提交的图片.....

还有我有备份, 从来吧..

### 3. bfg-repo-cleaner

这次使用一个开源项目 [bfg-repo-cleaner](https://github.com/rtyley/bfg-repo-cleaner?tab=readme-ov-file),

下载 jar 文件然后重命名为 **bfg.jar**, 比如我要删除大于 1M 的所有历史记录:

```bash
$ java -jar bfg.jar --strip-blobs-bigger-than 100M some-big-repo.git

$ cd some-big-repo.git
$ git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

效果还不错:

![20241229144920_hpRQYnln.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144920_hpRQYnln.webp)

[其他示例](https://rtyley.github.io/bfg-repo-cleaner/)

<!-- markdownlint-disable-next-line MD033 -->

<meta name="referrer" content="no-referrer"/>
