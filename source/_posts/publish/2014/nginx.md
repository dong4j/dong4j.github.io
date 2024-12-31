---
title: Nginx 入门
date: 2014-8-27
keywords:
  - Nginx
categories:
  - Nginx
tags:
  - web服务器
  - 反向代理
  - 高并发
  - 负载均衡
  - SSL/TLS
  - 静态文件处理
  - 动态内容支持
abbrlink: d73767c3
ai:
  - Nginx是一款高性能、可扩展且资源利用效率高的Web服务器和反向代理服务器。它适用于高流量网站、负载均衡和缓存，拥有强大的SSL/TLS支持，并提供简洁易管理的配置文件。与Apache相比，Nginx在处理静态文件时更为高效，在动态内容处理方面通常通过FastCGI或代理实现，且在内存和资源占用上表现更优。
description: Nginx是一款高性能、可扩展且资源利用效率高的Web服务器和反向代理服务器。它适用于高流量网站、负载均衡和缓存，拥有强大的SSL/TLS支持，并提供简洁易管理的配置文件。与Apache相比，Nginx在处理静态文件时更为高效，在动态内容处理方面通常通过FastCGI或代理实现，且在内存和资源占用上表现更优。
---

Nginx（发音为 “Engine-X”）是一个高性能的 HTTP 和反向代理服务器，同时也是一个 IMAP/POP3 代理服务器。由俄罗斯工程师 Igor Sysoev 开发，最早发布于 2004 年。Nginx 的轻量和高并发处理能力让它在高流量网站中迅速流行，目前被广泛用于各类服务器环境中。

## 为什么选择 Nginx？

Nginx 具有以下主要优势：

1. **高并发性能**：Nginx 采用事件驱动（异步）的非阻塞架构，能够高效处理成千上万的并发连接，特别适合高流量应用。
2. **资源效率**：与其他服务器（如 Apache）相比，Nginx 占用的内存和 CPU 资源更少，提供更好的资源利用率。
3. **功能丰富**：Nginx 支持静态文件服务、反向代理、负载均衡、缓存、SSL/TLS 加密等功能，适用多种场景。
4. **高度可扩展**：Nginx 支持模块化配置，可通过模块扩展功能。其配置文件简单明了，便于管理和扩展。

## Nginx 的应用场景

Nginx 具备多种应用场景，常见的包括：

1. **静态文件服务器**：适合静态内容（如 HTML、CSS、JavaScript、图片和视频）的高效分发。
2. **反向代理服务器**：作为代理服务器，Nginx 接收客户端请求并转发到后端服务器（如应用服务器、数据库服务器）。
3. **负载均衡**：在多个后端服务器之间分配流量，以实现均匀负载，提升性能和可靠性。
4. **缓存服务器**：Nginx 可以缓存静态和动态内容，提高页面加载速度，减轻后端服务器负载。
5. **Web 应用加速**：通过 SSL/TLS 加速、压缩、缓存等功能提升网站性能。
6. **邮件代理服务器**：支持 IMAP、POP3 和 SMTP 协议的代理。

## Nginx 的安装

在大多数系统上，Nginx 都可以通过包管理器直接安装。

- **Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install nginx
  ```

- **CentOS/RHEL**:

  ```bash
  sudo yum install nginx
  ```

- **macOS**（使用 Homebrew）:

  ```bash
  brew install nginx
  ```

安装完成后，可以启动 Nginx 服务：

```bash
sudo systemctl start nginx  # Ubuntu/CentOS 等现代发行版
```

验证 Nginx 是否运行：

```
curl -I http://localhost
```

如果 Nginx 运行正常，终端会显示状态代码 200 OK。

## Nginx 的核心配置

Nginx 的主要配置文件通常位于 /etc/nginx/nginx.conf（在不同操作系统可能有所不同），核心配置由若干“块”组成，包括 events、http、server、location 等。

配置文件结构

```
# 全局配置
user www-data;
worker_processes auto;

# 事件配置
events {
    worker_connections 1024;
}

# HTTP 配置
http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    keepalive_timeout  65;

    # 服务器配置
    server {
        listen       80;
        server_name  example.com;

        # 路径匹配
        location / {
            root   /var/www/html;
            index  index.html index.htm;
        }

        # 反向代理
        location /api/ {
            proxy_pass http://backend_server;
        }
    }
}
```

• 全局配置：设置用户权限、工作进程数等。
• 事件块：设置工作进程的最大连接数等。
• HTTP 块：包含静态文件处理、缓存、压缩等。
• Server 块：设置服务器的域名、端口等。
• Location 块：定义不同 URL 路径的处理方式。

## 常用的 Nginx 功能配置

### 1. 静态文件服务

Nginx 可直接作为静态文件服务器，通过 location 指定目录来提供文件服务：

```
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
```

### 2. 反向代理

反向代理是 Nginx 的重要功能，常用于将请求转发到后端服务器：

```
location /api/ {
    proxy_pass http://backend_server;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

在上述配置中，/api/ 路径下的请求会被转发到 http://backend_server。

### 3. 负载均衡

Nginx 支持多种负载均衡算法（如轮询、IP 哈希），用于分发请求到多个后端服务器：

```
http {
    upstream backend_servers {
        server backend1.example.com;
        server backend2.example.com;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend_servers;
        }
    }
}
```

### 4. 缓存设置

缓存可以大幅提升性能，特别是在高流量网站上。Nginx 可以缓存反向代理的内容：

```
proxy_cache_path /data/nginx/cache levels=1:2 keys_zone=my_cache:10m max_size=10g;
server {
    location / {
        proxy_cache my_cache;
        proxy_pass http://backend_server;
        proxy_cache_valid 200 1h;
    }
}
```

### 5. SSL/TLS 配置

Nginx 提供强大的 SSL/TLS 支持，用于加密网站流量：

```
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/nginx/ssl/example.com.crt;
    ssl_certificate_key /etc/nginx/ssl/example.com.key;

    location / {
        root /var/www/html;
    }
}
```

## Nginx 性能优化

1. 调整工作进程数：worker_processes 应设置为 CPU 的核心数，以最大化性能。
2. 优化连接数：worker_connections 控制每个进程的最大连接数，通常设置为 1024 或更高。
3. 启用 Gzip 压缩：可以通过 gzip on; 启用内容压缩，减少带宽占用。
4. 缓存静态文件：利用 expires 指令设置缓存时间，以减少重复请求。

## 常见问题和解决方案

### 1. Nginx 启动失败

检查配置文件是否存在错误：

```
sudo nginx -t
```

### 2. 502 Bad Gateway 错误

通常是由于后端服务器不可达或配置错误导致，检查 proxy_pass 地址是否正确，确保后端服务运行正常。

### 3. 访问过慢

可以通过启用缓存、Gzip 压缩或升级硬件资源来优化性能。

## Nginx 与 Apache 的对比

## Nginx 与 Apache 的对比

| 特性               | Nginx                                       | Apache                                 |
| ------------------ | ------------------------------------------- | -------------------------------------- |
| **架构**           | 事件驱动、异步                              | 线程/进程驱动                          |
| **性能**           | 高并发处理，性能优秀                        | 适合小规模并发，性能较低               |
| **静态文件处理**   | 高效，适合大量并发请求                      | 相对较慢，适合少量静态文件请求         |
| **动态内容处理**   | 通常通过 FastCGI、代理实现                  | 原生支持（如通过 `mod_php`）           |
| **内存和资源占用** | 占用少，资源利用效率高                      | 占用相对较多                           |
| **配置文件**       | 简洁，模块化，易于管理                      | 配置较为复杂，需要手动调整             |
| **负载均衡**       | 原生支持多种负载均衡算法（轮询、IP 哈希等） | 需要额外的模块支持（如 `mod_proxy`）   |
| **SSL/TLS 支持**   | 强大且高效                                  | 需要额外配置或模块支持（如 `mod_ssl`） |
| **反向代理**       | 支持并行处理，性能出色                      | 通过 `mod_proxy` 实现反向代理功能      |
| **模块扩展性**     | 通过编译时选择模块，动态加载有限            | 支持大量第三方模块，灵活配置           |
| **平台兼容性**     | 支持类 Unix 和 Windows 系统                 | 支持类 Unix 和 Windows 系统            |
| **社区与支持**     | 社区活跃，文档完善                          | 社区庞大，支持范围广                   |
| **使用场景**       | 高流量、并发、负载均衡和缓存                | 传统的 Web 服务器和动态内容处理        |
