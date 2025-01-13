---
title: Chrome 插件开发实战：从零开始开发一个图片上传工具
ai: true
abbrlink: bdfa
date: 2025-01-11 00:48:57
categories:
tags:
cover: https://cdn.dong4j.site/source/image/20250113235017_acCTt6s4.webp
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![/images/cover/20250113235017_acCTt6s4.webp](https://cdn.dong4j.site/source/image/20250113235017_acCTt6s4.webp)

## 简介

在这篇文章中，我将以一个实际项目为例，带你从零开始学习 Chrome 插件开发。我们将开发一个图片上传工具，它能帮助博主快速处理和上传图片。通过这个项目，你将学习到 Chrome 插件开发的基础知识和实战技巧。

## 为什么要开发这个插件？

作为一名技术博主，我经常需要在文章中插入图片。每次处理图片都需要经过以下步骤：

1. 在网上找到合适的图片
2. 下载到本地
3. 压缩图片
4. 转换格式
5. 上传到图床
6. 复制链接
7. 插入 Markdown 标签

这个过程不仅耗时，而且每添加一张图片都要重复一遍。作为一个程序员，我觉得这种重复性的工作应该被自动化。这就是我开发这个 Chrome 插件的初衷。

## 解决方案：Chrome 扩展

为了解决这个问题，我开发了一个 Chrome 扩展：Image Uploader。它能让你通过简单的右键点击就完成上述所有步骤。

### 主要功能

1. **一键上传**：右键点击网页上的任何图片，选择"上传图片"即可
2. **自动压缩**：可配置的图片压缩功能，平衡图片质量和文件大小
3. **格式转换**：支持将图片转换为 WebP 格式，进一步优化加载性能
4. **多语言支持**：支持中文和英文界面
5. **自定义配置**：可设置自己的图床 API 地址
6. **即时反馈**：上传完成后会显示通知，并自动复制 Markdown 格式的图片链接

### 技术实现

目前我使用的 PicList 的 API 来上传图片, 所以我的方法就是在插件中设置上传 API, 这样能够兼容大多数的图床, 比如 SM.MS、Imgur、阿里云 OSS、腾讯云 COS 等, 这样我也不需要再为每个图床写一个上传方法了,

最重要的是不需要为每个图床添加不同的设置, 只需要设置一个图床的 API 就可以了, 图床的配置有本地的上传工具负责, 我只需要传一个需要上传的文件和配置名即可.

这个扩展的核心功能主要包括：

1. **图片处理**：

   - 使用 Canvas API 进行图片压缩
   - 支持 WebP 格式转换
   - 保持图片质量的同时减小文件体积

2. **用户界面**：

   - 简洁的设置页面
   - 现代化的 UI 设计
   - 支持深色/浅色主题

3. **后台功能**：
   - 异步上传处理
   - 自动重试机制
   - 错误处理和用户提醒

### 使用效果

使用这个扩展后，之前繁琐的图片处理流程简化为：

1. 在网页上找到合适的图片
2. 右键点击 -> 选择"上传图片"
3. 自动完成压缩、转换、上传
4. 图片链接自动复制到剪贴板

整个过程从原来的几分钟缩短到几秒钟，极大提高了写作效率。

## Chrome 插件开发基础

### 什么是 Chrome 插件？

Chrome 插件（Chrome Extension）是一个用 Web 技术（如 HTML、CSS 和 JavaScript）构建的软件程序，可以定制浏览器功能和行为。它就像是浏览器的"小助手"，能够增强我们的浏览体验。

### 插件的核心组件

1. **manifest.json**：插件的配置文件，定义了插件的各种属性和权限

```json
{
  "manifest_version": 3,
  "name": "Image Uploader",
  "version": "1.0",
  "description": "Quick image upload tool for bloggers",
  "permissions": ["contextMenus", "storage", "notifications"],
  "action": {
    "default_popup": "popup.html"
  },
  "background": {
    "service_worker": "background.js"
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

2. **Background Script**：插件的后台脚本，常驻运行

```javascript
// background.js
chrome.runtime.onInstalled.addListener(() => {
  // 创建右键菜单
  chrome.contextMenus.create({
    id: "uploadImage",
    title: "Upload Image",
    contexts: ["image"],
  });
});

// 处理右键菜单点击
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "uploadImage") {
    // 处理图片上传
  }
});
```

3. **Popup**：点击插件图标时显示的弹出窗口

```html
<!-- popup.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="popup.css" />
  </head>
  <body>
    <div class="popup-content">
      <h2>Image Uploader</h2>
      <button id="settings">Settings</button>
    </div>
    <script src="popup.js"></script>
  </body>
</html>
```

4. **Options Page**：插件的设置页面

```html
<!-- options.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="options.css" />
  </head>
  <body>
    <div class="settings-form">
      <label>API Endpoint:</label>
      <input type="text" id="apiUrl" />
      <!-- 其他设置项 -->
    </div>
    <script src="options.js"></script>
  </body>
</html>
```

### 重要的 Chrome API

1. **chrome.contextMenus**：创建右键菜单
2. **chrome.storage**：数据存储
3. **chrome.notifications**：显示通知
4. **chrome.runtime**：处理插件生命周期

## 实战：开发图片上传插件

### 1. 项目结构

```
image-uploader-extension/
├── manifest.json      # 配置文件
├── background.js      # 后台脚本
├── popup.html         # 弹出窗口
├── popup.js
├── options.html      # 设置页面
├── options.js
├── i18n.js           # 国际化
├── icons/            # 图标
└── _locales/         # 语言文件
```

### 2. 核心功能实现

#### 2.1 图片压缩

```javascript
async function compressImage(imageUrl, quality) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => {
      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");

      canvas.width = img.width;
      canvas.height = img.height;

      ctx.drawImage(img, 0, 0);

      canvas.toBlob((blob) => resolve(blob), "image/jpeg", quality / 100);
    };
    img.src = imageUrl;
  });
}
```

#### 2.2 WebP 转换

```javascript
async function convertToWebP(blob) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => {
      const canvas = document.createElement("canvas");
      const ctx = canvas.getContext("2d");

      canvas.width = img.width;
      canvas.height = img.height;

      ctx.drawImage(img, 0, 0);

      canvas.toBlob((webpBlob) => resolve(webpBlob), "image/webp");
    };
    img.src = URL.createObjectURL(blob);
  });
}
```

#### 2.3 上传功能

```javascript
async function uploadImage(blob) {
  const formData = new FormData();
  formData.append("image", blob);

  const response = await fetch(apiUrl, {
    method: "POST",
    body: formData,
  });

  return await response.json();
}
```

### 3. 用户界面设计

#### 3.1 设置页面

我们使用现代的 UI 框架（Tailwind CSS）来构建设置页面：

```html
<div class="container mx-auto p-8">
  <div class="bg-white rounded-lg shadow-lg p-6">
    <h2 class="text-2xl font-bold mb-6">Settings</h2>

    <div class="space-y-6">
      <!-- API 设置 -->
      <div class="form-group">
        <label class="block text-gray-700 mb-2">API Endpoint</label>
        <input
          type="text"
          id="apiUrl"
          class="w-full px-4 py-2 border rounded-lg"
        />
      </div>

      <!-- 压缩设置 -->
      <div class="form-group">
        <label class="block text-gray-700 mb-2"> Compression Quality </label>
        <input type="range" id="quality" min="1" max="100" value="80" />
        <span id="qualityValue">80%</span>
      </div>
    </div>
  </div>
</div>
```

#### 3.2 状态通知

使用 Chrome 的通知 API 提供即时反馈：

```javascript
function showNotification(title, message) {
  chrome.notifications.create({
    type: "basic",
    iconUrl: "icons/icon128.png",
    title: title,
    message: message,
  });
}
```

### 4. 国际化支持

#### 4.1 语言文件

```json
// _locales/en/messages.json
{
  "upload_success": {
    "message": "Image uploaded successfully!"
  },
  "upload_error": {
    "message": "Failed to upload image: $ERROR$",
    "placeholders": {
      "error": {
        "content": "$1"
      }
    }
  }
}
```

#### 4.2 使用翻译

```javascript
function getMessage(key, substitutions) {
  return chrome.i18n.getMessage(key, substitutions);
}
```

## 开发技巧和最佳实践

1. **模块化设计**：将功能分散到不同文件中，便于维护
2. **错误处理**：添加适当的错误处理和用户提示
3. **性能优化**：
   - 使用异步操作处理图片
   - 合理设置压缩参数
   - 缓存常用数据
4. **安全考虑**：
   - 验证 API 响应
   - 限制文件大小
   - 使用 HTTPS

## 调试技巧

1. **使用 Chrome 开发者工具**：

   - 背景页面调试：chrome://extensions
   - 控制台日志
   - 网络请求监控

2. **常见问题解决**：
   - 权限问题：检查 manifest.json
   - 跨域问题：添加适当的权限
   - 资源加载：使用相对路径

## 发布流程

1. **打包插件**：

   - 压缩代码
   - 生成 zip 文件

2. **上传到 Chrome Web Store**：
   - 准备描述材料
   - 设置价格（免费/付费）
   - 等待审核

## 项目实例

完整的项目代码已开源在 GitHub：[image-uploader-extension](https://github.com/dong4j/image-uploader-extension)

如果你也经常写博客，欢迎试用这个扩展。同时，我也欢迎各位开发者：

- 提出建议和意见
- 贡献代码
- 报告问题
- 分享使用体验

## 未来计划

这个扩展还有很多可以改进的地方，比如：

1. ~~支持批量上传~~
2. 添加更多图片处理选项
3. 支持更多图床服务: 兼容更多 API
4. 优化压缩算法
5. 添加上传历史记录

## 扩展阅读

1. [Chrome 文档](https://developer.chrome.com/docs?hl=zh-cn)
2. [Chrome 扩展开发文档](https://developer.chrome.com/docs/extensions/)
3. [Manifest V3 迁移指南](https://developer.chrome.com/docs/extensions/mv3/intro/)

## 结语

开发 Chrome 插件是一个很好的学习 Web 技术的机会。通过这个项目，你不仅能解决实际问题，还能掌握很多实用的开发技能。

希望这篇教程能帮助你开始 Chrome 插件开发之旅。如果你有任何问题或建议，欢迎在 GitHub 上提出 issue 或 PR。
