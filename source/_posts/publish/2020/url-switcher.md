---
title: 打造智能URL切换器：让内外网访问更便捷
ai:
  - >-
    本文介绍了一款名为 URL Switcher Pro 的 Chrome
    扩展，它旨在解决智能家居爱好者在内外网访问家庭服务器时遇到的困扰。这款扩展能够自动检测当前网络环境，并根据配置智能切换内外网 URL，支持批量 URL
    配置管理并提供 URL 可访问性检测。文章详细阐述了其技术实现，包括 URL
    匹配与切换、网络环境检测、配置同步以及国际化支持。此外，还介绍了使用方法、特色功能以及未来的发展方向。通过这款工具，用户可以高效地管理内外网访问，提升访问体验。欢迎访问
    GitHub 仓库获取更多信息或参与项目开发。
description: >-
  本文介绍了一款名为 URL Switcher Pro 的 Chrome
  扩展，它旨在解决智能家居爱好者在内外网访问家庭服务器时遇到的困扰。这款扩展能够自动检测当前网络环境，并根据配置智能切换内外网 URL，支持批量 URL
  配置管理并提供 URL 可访问性检测。文章详细阐述了其技术实现，包括 URL
  匹配与切换、网络环境检测、配置同步以及国际化支持。此外，还介绍了使用方法、特色功能以及未来的发展方向。通过这款工具，用户可以高效地管理内外网访问，提升访问体验。欢迎访问
  GitHub 仓库获取更多信息或参与项目开发。
tags:
  - HomeLab
  - 插件开发
  - 开发技巧
  - 实战案例
  - Chrome
categories:
  - 'HomeLab:中年男人的快乐源泉'
cover: 'https://cdn.dong4j.site/source/image/20250113234024_3rZyCVYe.webp'
abbrlink: 9f1d6e11
date: 2020-06-13 15:08:37
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![/images/cover/20250113234024_3rZyCVYe.webp](https://cdn.dong4j.site/source/image/20250113234024_3rZyCVYe.webp)

## 背景

作为一个智能家居爱好者，我在家里部署了多台服务器以及开发板。因为有公网 IP, 并通过 DDNS 绑定了域名, 我可以随时在外网访问家中的各种服务。

虽然我通过 Surge 的配置可以在外网通过局域网访问家中的内部服务, 当问题是我需要为同一个服务添加多个书签, 当服务数量增多时，书签管理变得异常繁琐。

## 解决方案

为了解决这个问题，我开发了一个 Chrome 扩展 - URL Switcher Pro。这个扩展程序能够：

1. 自动检测当前网络环境
2. 根据配置智能切换内外网 URL
3. 支持批量 URL 配置管理
4. 提供 URL 可访问性检测

## 技术实现

### 1. 核心功能

扩展的核心功能主要包括：

- **URL 匹配与切换**：通过正则表达式进行 URL 模式匹配
- **网络环境检测**：检测 URL 可访问性
- **配置同步**：利用 Chrome 存储 API 实现多设备配置同步
- **国际化支持**：内置中英文语言支持

### 2. 主要技术栈

- Chrome Extension Manifest V3
- Chrome Storage API
- Chrome Tabs & WebNavigation API
- JavaScript ES6+

### 3. 关键代码实现

```javascript
// URL自动检测
async function detectUrlPattern(url) {
  const configs = await chrome.storage.sync.get("siteConfigs");
  for (const config of configs.siteConfigs || []) {
    if (url.includes(config.intranetUrl) || url.includes(config.internetUrl)) {
      // 检测URL可访问性并自动切换
      const intranetAccessible = await checkUrl(config.intranetUrl);
      return intranetAccessible ? config.intranetUrl : config.internetUrl;
    }
  }
  return url;
}

// URL可访问性检测
async function checkUrl(url) {
  try {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
  } catch (error) {
    return false;
  }
}
```

## 使用方法

1. **安装扩展**：

   - 从 Chrome 商店安装或通过开发者模式加载
   - 点击工具栏的扩展图标进行配置

2. **添加 URL 配置**：

   - 配置名称：用于识别不同的服务
   - 内网地址：局域网访问地址
   - 外网地址：公网访问域名

3. **启用自动切换**：
   - 打开全局开关
   - 访问任意配置的 URL 时会自动切换到最佳访问地址

## 特色功能

1. **批量配置管理**：

   - 支持导入/导出配置
   - 方便在多个设备间同步配置

2. **状态检测**：

   - 检测 URL 可访问性
   - 直观的状态指示器显示

3. **智能切换**：

   - 自动检测网络环境
   - 无感知切换到最佳访问地址

## 未来展望

1. **智能缓存**：

   - 实现 URL 访问性能缓存
   - 减少检测请求频率

2. **批量导入**：

   - 支持从书签导入配置
   - 支持批量 URL 格式转换

3. **更多自定义选项**：

   - 自定义检测间隔
   - 更灵活的 URL 匹配规则

## 结语

URL Switcher Pro 通过智能的 URL 切换机制，解决了内外网访问的痛点。它不仅提高了访问效率，也大大简化了 URL 管理的复杂度。对于经常需要在不同网络环境下访问内网服务的用户来说，这是一个不可多的效率工具。

欢迎访问[GitHub 仓库](https://github.com/dong4j/url-switcher-pro)获取更多信息或参与项目开发。
