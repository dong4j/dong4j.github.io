---
title: 从零开始开发一个 Hexo 插件：以 hexo-plugin-llmstxt 为例
ai: 
  - 从零开始开发一个 Hexo 插件，以 hexo-plugin-llmstxt 为例，涵盖了 llms.txt 的定义、背景、规范，Hexo 插件开发基础，包括插件类型、基本结构和命名规范。详细讲述了开发 hexo-plugin-llmstxt 的步骤，从初始化项目、编写 package.json 到实现核心功能、处理文章内容、文件生成等。还提到了开发过程中的注意事项、测试和发布方法，以及总结和参考资料。旨在帮助开发者理解 Hexo 插件开发流程，为文档处理提供实用工具。
abbrlink: b902d8fd
date: 2025-01-30 11:34:10
description: 从零开始开发一个 Hexo 插件，以 hexo-plugin-llmstxt 为例，涵盖了 llms.txt 的定义、背景、规范，Hexo 插件开发基础，包括插件类型、基本结构和命名规范。详细讲述了开发 hexo-plugin-llmstxt 的步骤，从初始化项目、编写 package.json 到实现核心功能、处理文章内容、文件生成等。还提到了开发过程中的注意事项、测试和发布方法，以及总结和参考资料。旨在帮助开发者理解 Hexo 插件开发流程，为文档处理提供实用工具。
categories:
  - Hexo
tags:
  - 新时代码农
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## 前言

在 AI 时代，越来越多的开发者开始使用 AI 编程助手来提升开发效率。为了让 AI 更好地理解和学习我们的技术文档，社区提出了 `llms.txt` 规范。本文将以开发一个生成 `llms.txt` 的 Hexo 插件为例，介绍 Hexo 插件开发的基本流程。

## 什么是 llms.txt？

### 背景

随着 ChatGPT、Claude 等大语言模型的普及，越来越多的开发者开始使用 AI 编程助手。但是这些 AI 助手在访问网站内容时，往往需要处理复杂的 HTML 结构，这不仅增加了处理成本，还可能影响理解的准确性。

### llms.txt 规范

`llms.txt` 类似于 `robots.txt`，它是一个专门为 AI 准备的纯文本格式的站点内容索引。通过提供结构化的纯文本内容，可以帮助 AI 更好地理解和学习网站的内容。

主要特点：
1. 纯文本格式，易于解析
2. 包含文章的标题、描述和链接
3. 可选包含完整的文章内容
4. 支持 Markdown 格式

## Hexo 插件开发基础

### 插件类型

Hexo 支持多种类型的插件：
- Generator：用于生成静态文件
- Renderer：用于渲染文件
- Helper：用于辅助模板渲染
- Deployer：用于部署
- Processor：用于处理源文件
- Tag：用于在文章中插入特定内容
- Console：用于添加控制台命令

我们的 `llms.txt` 生成插件属于 Generator 类型。

### 基本结构

一个典型的 Hexo 插件目录结构如下：

```
.
├── index.js
├── package.json
├── README.md
└── LICENSE
```

### 插件命名规范

Hexo 插件的命名需要遵循以下规则：
- 以 `hexo-` 开头
- 全小写
- 使用连字符（-）连接单词

## 实战：开发 hexo-plugin-llmstxt

### 1. 初始化项目

首先创建项目目录并初始化：

```bash
mkdir hexo-plugin-llmstxt
cd hexo-plugin-llmstxt
npm init
```

### 2. 编写 package.json

```json
{
  "name": "hexo-plugin-llmstxt",
  "version": "1.0.0",
  "description": "Generate llms.txt for Hexo sites",
  "main": "index.js",
  "keywords": [
    "hexo",
    "llms",
    "ai"
  ],
  "dependencies": {}
}
```

### 3. 实现核心功能

在 `index.js` 中实现插件的核心功能：

```javascript
'use strict';

const fs = require('fs');
const path = require('path');

// 注册生成器
hexo.extend.generator.register('llms', function (locals) {
  // 获取配置
  const config = Object.assign({
    generate_llms_full: false,
    debug: false,
    postsHeader: hexo.config.title,
    description: hexo.config.description,
    sort: 'desc'
  }, hexo.config.llmstxt);

  // 生成文件内容
  // ...
});
```

### 4. 处理文章内容

```javascript
// 处理每篇文章
locals.posts.sort('date', sortOrder)
  .filter(post => post.published !== false)
  .forEach(post => {
    const {
      title,
      raw,
      description,
    } = post;

    // 移除 Front-matter
    const content = raw.replace(/^---[\s\S]+?---\n/, '').trim();
    
    // 生成链接和内容
    // ...
  });
```

### 5. 文件生成

```javascript
// 写入文件
try {
  fs.writeFileSync(llmsFilePath, llmsContent);
  if (config.debug) {
    console.log('生成 llms.txt 成功');
  }
} catch (err) {
  console.error('写入文件时发生错误:', err);
}
```

## 开发过程中的注意事项

1. **错误处理**
   - 确保目录存在
   - 处理文件写入错误
   - 添加调试日志

2. **配置处理**
   - 提供默认值
   - 支持用户自定义
   - 配置项文档化

3. **文件路径**
   - 使用 `path.join` 处理路径
   - 考虑跨平台兼容性

4. **性能优化**
   - 避免重复操作
   - 合理使用内存

5. **代码风格**
   - 遵循 JavaScript 规范
   - 添加适当的注释
   - 保持代码整洁

## 测试和发布

### 本地测试

1. 在本地 Hexo 项目中使用 npm link：
```bash
cd hexo-plugin-llmstxt
npm link
cd /path/to/hexo/project
npm link hexo-plugin-llmstxt
```

2. 运行 Hexo 命令测试：
```bash
hexo clean
hexo generate
```

### 发布到 NPM

1. 登录 NPM：
```bash
npm login
```

2. 发布包：
```bash
npm publish
```

## 源码:

https://github.com/dong4j/hexo-plugin-llms

## 参考资料

- [Hexo 官方文档](https://hexo.io/docs/)
- [LLMs.txt 规范](https://llmstxt.org)
- [具有 LLMs.txt 的站点](https://llmstxt.site/)
- [AI时代的站点地图](https://juejin.cn/post/7447083753187328050) 
- [SiliconCloud 使用文档与 Cursor](https://docs.siliconflow.cn/use-docs-with-cursor)
- [使用 Firecrawl 生成 llmstxt](https://github.com/mendableai/llmstxt-generator)
- [使用 sitemap.xml 生成 llmstxt](https://github.com/dotenvx/llmstxt)

