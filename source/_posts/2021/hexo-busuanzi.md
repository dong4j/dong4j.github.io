---
title: Docker Compose部署Busuanzi
categories: Hexo
ai:
  - 本文介绍如何在本地服务器自建一个 Hitokoto 服务来替换无法访问的默认服务。通过 Docker Compose 部署包含以下关键步骤：使用官方文档，配置文件详细设置包括监听地址、跨域访问、日志、Redis
    连接和统计数据过期时间等参数。部署后可访问指定 IP 和端口验证服务是否成功运行。同时，文章提供针对 Hexo 的配置指南，包括修改主题中的 CDN 地址和
    Pug 模板文件，以集成自建的 Hitokoto 服务，确保页面加载时调用正确的 JavaScript 脚本。
tags:
  - Hexo
  - Hitokoto
  - 本地服务器
  - 自建插件
  - Docker Compose
abbrlink: c294
date: 2021-06-13 00:00:00
cover:
description: 本文介绍如何在本地服务器自建一个 Hitokoto 服务来替换无法访问的默认服务。通过 Docker Compose 部署包含以下关键步骤：使用官方文档，配置文件详细设置包括监听地址、跨域访问、日志、Redis
  连接和统计数据过期时间等参数。部署后可访问指定 IP 和端口验证服务是否成功运行。同时，文章提供针对 Hexo 的配置指南，包括修改主题中的 CDN 地址和 Pug
  模板文件，以集成自建的 Hitokoto 服务，确保页面加载时调用正确的 JavaScript 脚本。
---

[[hexo-hitokoto|自建 Hitokoto 服务]]
[[hexo-rss|Hexo 添加 RSS 订阅功能]]
[[hexo-load|Hexo 自定义加载动画]]

## 简介

同样是因为默认的 `https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js` 已无法打开, 所以参考 [self-hosted busuanzi](https://github.com/soxft/busuanzi) 在本地服务器自建一个.

## 部署

根据 [官方文档](https://gitee.com/soxft/busuanzi/wikis/install) 使用 docker-compose 直接部署:

```yaml
services:
  busuanzi:
    image: xcsoft/busuanzi:latest
    ports:
      - 8888:8080
    volumes:
      - ./data/config.yaml:/app/config.yaml
      # 如果不需要修改首页, 可以不需要挂载
      - ./data/dist/index.html:/app/dist/index.html
    environment:
      WEB_LOG: true
      WEB_DEBUG: false
      WEB_CORS: "*"
      BSZ_EXPIRE: 0
      BSZ_SECRET: 给一个 uuid 即可
      API_SERVER: 需要修改成最后绑定你的域名
      REDIS_ADDRESS: redis-ip:redis-port
      REDIS_PASSWORD: password
      REDIS_DATABASE: 0
      BSZ_PATHSTYLE: true
      BSZ_ENCRYPT: MD516
```

配置文件:

```yaml
Web:
  Address: 0.0.0.0:8080 # 监听地址
  Cors: "https://xsot.cn,https://google.com" # 跨域访问
  Debug: false # 是否开启debug模式
  Log: false # 是否开启日志
Redis:
  Address: redis:6379 # redis地址
  Password:
  Database: 0
  TLS: false # 是否使用TLS连接redis
  Prefix: bsz # redis前缀
  MaxIdle: 25 # 最大空闲连接数
  MaxActive: 100 # 最大连接数
  MinIdle: 25 # 最小空闲连接数
  MaxRetries: 3 # 最大重试次数
Bsz:
  Expire: 0 # 统计数据过期时间 单位秒, 请输入整数 (无任何访问, 超过这个时间后, 统计数据将被清空, 0为不过期)
  Secret: "bsz" # JWT签名密钥 // 请设置为任意长度的随机值
  Encrypt: "MD516" # 加密算法 (MD516 / MD532) 老版本请使用 MD532
  PathStyle: true # 路径样式 (false: url&path, true: path) 老版本请使用 false,  true 更便于数据迁移

# TIPS, 所有 config 内的设置, 均可使用 环境变量 覆盖
# Ex BSZ_SECRET=123 将覆盖 config.yaml 中的 Bsz.Secret
```

上述的配置文件是官方提供的, 我未做任何修改, 因为在 docker-compose.yml 中都可以直接覆盖.

部署后访问 `http://ip:8888` 检查是否部署成功:

![20241229154732_dxuLdyt7.webp](20241229154732_dxuLdyt7.webp)

我在上面挂载了 `index.html` 是因为需要修改 `<script async src="https://域名/js"></script>` 不然就是官方默认的.

## Hexo 配置

### 修改主题配置

```yaml
CDN:
  ...
  option:
    busuanzi: https://你的域名/js # http://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js 默认的意无法打开
```

### 修改主题代码

修改文件 `themes/anzhiyu/layout/includes/additional-js.pug`

将一下代码:

```javascript
script(async data-pjax src= theme.asset.busuanzi || '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js')'
```

修改为:

```javascript
script(async data-pjax data-prefix="busuanzi_value" src= theme.asset.busuanzi || '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js')
```

记得一定要加上 `data-prefix="busuanzi_value"`, [新老版本兼容问题的处理](https://busuanzi.apifox.cn/doc-5083722).

最后 Hexo 三连击即可显示效果.
