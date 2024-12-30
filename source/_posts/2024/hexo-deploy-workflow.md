---
title: Hexo 博客部署与图片处理指南：自定义脚本的多平台实践与技巧
tags:
  - 图片处理
  - 自动清理脚本
  - ffmpeg转换
  - Hexo配置
  - HomeLab部署
abbrlink: 598d
date: 2024-12-30 10:45:57
categories:
ai:
  - 本文讨论了图片处理过程和优化方法，包括手动删除多余的图片、将图片转换成webp格式、上传到图床并替换图片标签、以及部署到服务器或GitHub。同时介绍了Hexo配置文件使用方式：通过`--config`参数指定自定义配置文件路径，允许在多个文件中合并配置，并说明了主题配置的两种方法——主题特定的配置文件和独立的配置文件。最后提到可以将内容部署到HomeLab或GitHub以及备份策略。
description: 本文讨论了图片处理过程和优化方法，包括手动删除多余的图片、将图片转换成webp格式、上传到图床并替换图片标签、以及部署到服务器或GitHub。同时介绍了Hexo配置文件使用方式：通过`--config`参数指定自定义配置文件路径，允许在多个文件中合并配置，并说明了主题配置的两种方法——主题特定的配置文件和独立的配置文件。最后提到可以将内容部署到HomeLab或GitHub以及备份策略。
cover: /images/cover/hexo-deploy-workflow.png
---

![alt text](/images/cover/hexo-deploy-workflow.png)

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>



## 简介



## xxx



[在 GitHub Pages 上部署 Hexo](https://hexo.io/zh-cn/docs/github-pages)

[使用 Github Action 自动部署](https://blog.anheyu.com/posts/asdx.html)

## 图片处理

以前的处理步骤:

1. 图片修改后需要手动删除多余的图片;
2. 将图片转换成 webp
3. 通过工具上传到图床, 然后替换图片标签
4. 部署到服务器或 github

存在的问题:

### 自动清理图片脚本

### 使用 ffmepg 将图片转换为 webp

### 批量上传图片并创建部署的文档

为什么要这么做

#### hexo 配置

### 使用代替配置文件

<!-- 
https://hexo.io/zh-cn/docs/configuration#%E4%BD%BF%E7%94%A8%E4%BB%A3%E6%9B%BF%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6
-->

可以在 hexo-cli 中使用 `--config` 参数来指定自定义配置文件的路径。 你可以使用一个 YAML 或 JSON 文件的路径，也可以使用逗号分隔（无空格）的多个 YAML 或 JSON 文件的路径。

```
# use 'custom.yml' in place of '_config.yml'
$ hexo server --config custom.yml

# use 'custom.yml' & 'custom2.json', prioritizing 'custom2.json'
$ hexo server --config custom.yml,custom2.json
```

当你指定了多个配置文件以后，Hexo 会按顺序将这部分配置文件合并成一个 `_multiconfig.yml`。 后面的值优先。 这个原则适用于任意数量、任意深度的 YAML 和 JSON 文件。 请注意，**列表中不允许有空格**。

如果 `custom.yml` 中指定了 `foo: bar`，在 custom2.json 中指定了 `"foo": "dinosaur"`，那么在 `_multiconfig.yml` 中你会得到 `foo: dinosaur`。

### 使用代替主题配置文件

通常情况下，Hexo 主题是一个独立的项目，并拥有一个独立的 `_config.yml` 配置文件。

除了自行维护独立的主题配置文件，你也可以在其它地方对主题进行配置。

**配置文件中的 `theme_config`**

> 该特性自 Hexo 2.8.2 起提供

```
# _config.yml
theme: "my-theme"
theme_config:
  bio: "My awesome bio"
  foo:
    bar: "a"
# themes/my-theme/_config.yml
bio: "Some generic bio"
logo: "a-cool-image.png"
  foo:
    baz: 'b'
```

最终主题配置的输出是：

```
{
  "bio": "My awesome bio",
  "logo": "a-cool-image.png",
  "foo": {
    "bar": "a",
    "baz": "b"
  }
}
```

**独立的 `_config.[theme].yml` 文件**

> 该特性自 Hexo 5.0.0 起提供

独立的主题配置文件应放置于站点根目录下，支持 `yml` 或 `json` 格式。 需要配置站点 `_config.yml` 文件中的 `theme` 以供 Hexo 寻找 `_config.[theme].yml` 文件。

```
# _config.yml
theme: "my-theme"
# _config.my-theme.yml
bio: "My awesome bio"
foo:
  bar: "a"
# themes/my-theme/_config.yml
bio: "Some generic bio"
logo: "a-cool-image.png"
  foo:
    baz: 'b'
```

最终主题配置的输出是：

```
{
  "bio": "My awesome bio",
  "logo": "a-cool-image.png",
  "foo": {
    "bar": "a",
    "baz": "b"
  }
}
```

> 我们强烈建议你将所有的主题配置集中在一处。 如果你不得不在多处配置你的主题，那么这些信息对你将会非常有用：Hexo 在合并主题配置时，Hexo 配置文件中的 `theme_config` 的优先级最高，其次是 `_config.[theme].yml` 文件。 最后是位于主题目录下的 `_config.yml` 文件。
>
> `_config.yml.theme_config > _config.[theme].yml > _config.yml`
>
> `hexo server --config _config.yml,_config.[theme].yml`

### 部署到 HomeLab

### 部署到 GitHub

## 备份
