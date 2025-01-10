---
title: Hexo 博客升级指南：集成 RSS 订阅
ai:
  - 本文详细介绍了如何在 Hexo 博客中添加 RSS 订阅功能，包括插件安装、配置以及如何自定义订阅内容。
categories:
  - 经验分享
tags:
  - Hexo
  - RSS
  - 订阅
  - 博客
abbrlink: 564b
date: 2021-06-11 23:04:24
cover: https://cdn.dong4j.site/source/image/20250103184959_gB2NVpXf.webp
description: 本文详细介绍了如何在 Hexo 博客中添加 RSS 订阅功能，包括插件安装、配置以及如何自定义订阅内容。
keywords:
  - Hexo
  - RSS
  - 订阅
  - 博客
---

![/images/cover/20250103184959_gB2NVpXf.webp](https://cdn.dong4j.site/source/image/20250103184959_gB2NVpXf.webp)

Hexo 博客添加 RSS 订阅功能 插件 GitHub [https://github.com/hexojs/hexo-generator-feed](https://github.com/hexojs/hexo-generator-feed) 安装 hexo......

这篇文章介绍了如何在 Hexo 博客中添加 RSS 订阅功能。需要使用时光插件，并提供了 GitHub 地址。在配置 RSS 时，可以选择原子或 RSS2 的类型，设置文件路径，决定展示文章的数量，还可以选择包含文章的全部内容或摘要。同时，也可以自定义订阅图标和订阅内容的顺序。在部署后，直接在根目录中访问配置的文件即可使用 RSS 订阅功能。

插件 GitHub 地址：[https://github.com/hexojs/hexo-generator-feed](https://github.com/hexojs/hexo-generator-feed)

## 安装 `hexo-generator-feed` 插件

```bash
npm install hexo-generator-feed --save
```

## 修改 `_config.yml` 配置

```yaml
feed:
  type: atom
  path: atom.xml
  limit: false
```

`type`: RSS 的类型 (atom/rss2)  
`path`: 文件路径，默认是 atom.xml/rss2.xml  
`limit`: 展示文章的数量, 使用 0 或则 false 代表展示全部  
`hub`: URL of the PubSubHubbub hubs (如果使用不到可以为空)  
`content`: （可选）设置 true 可以在 RSS 文件中包含文章全部内容，默认：false  
`content_limit`: （可选）摘要中使用的帖子内容的默认长度。 仅在内容设置为 false 且未显示自定义帖子描述时才使用。  
`content_limit_delim`: （可选）如果 content_limit 用于缩短 post 内容，则仅在此分隔符的最后一次出现时进行剪切，然后才达到字符限制。默认不使用。  
`icon`: （可选）自定义订阅图标，默认设置为主配置中指定的图标。  
`order_by`: 订阅内容的顺序。 (默认: -date)

## 修改主题配置

```yaml
rss: /atom.xml
```

## 重新生成静态文件

```bash
hexo clean && hexo g
```

在 `public` 文件夹中会生成 `atom.xml` 文件，部署后直接在根目录中访问该文件即可。
