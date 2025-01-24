---
title: Redis命令速查手册：常用指令详解
keywords:
  - Redis
  - 启动方式
  - 配置文件
  - 命令行客户端
  - 持久化路径
  - 日志路径
categories:
  - 新时代码农
tags:
  - Redis
  - 启动方式
  - 配置文件
  - 命令行客户端
  - 持久化路径
  - 日志路径
abbrlink: 570ace06
date: 2013-02-18 00:00:00
ai:
  - 本文详细介绍了Redis的可执行文件及其作用，包括启动Redis的`redis-server`命令、Redis命令行客户端`redis-cli`、基准测试工具`redis-benchmark`等。文章还讲解了如何通过运行参数和配置文件来启动Redis，以及Redis的持久化路径和日志路径的修改方法。此外，文章还介绍了Redis的命令行客户端使用方式，包括交互式方式和命令方式，并列举了停止Redis服务的命令。最后，文章讨论了Redis的全局命令，如`dbsize`、`keys`、`exists`、`del`、`expire`和`type`等，解释了它们的功能和使用方法。
description: 本文详细介绍了Redis的可执行文件及其作用，包括启动Redis的`redis-server`命令、Redis命令行客户端`redis-cli`、基准测试工具`redis-benchmark`等。文章还讲解了如何通过运行参数和配置文件来启动Redis，以及Redis的持久化路径和日志路径的修改方法。此外，文章还介绍了Redis的命令行客户端使用方式，包括交互式方式和命令方式，并列举了停止Redis服务的命令。最后，文章讨论了Redis的全局命令，如`dbsize`、`keys`、`exists`、`del`、`expire`和`type`等，解释了它们的功能和使用方法。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://cover.dong4j.ink:1024)

## Redis 可执行文件说明

| 可执行文件       | 作用                               |
| :--------------- | :--------------------------------- |
| redis-server     | 启动 Redis                         |
| redis-cli        | Redis 命令行客户端                 |
| redis-benchmark  | Redis 基准测试工具                 |
| redis-check-aof  | Redis AOF 持久化文件检测和修复工具 |
| redis-check-dump | Redis RDB 持久化文件检测和修复工具 |
| redis-sentinel   | 启动 Redis Sentinel                |

## 启动方式

**1. 默认配置**

```shell
redis-server
```

**2. 运行参数**

```shell
# 格式
redis-server --configKey1 configValue1 --configKey2 configValue2

# 使用 6380 端口启动 redis
redis-server --port 6380
```

**3. 配置文件**

```shell
redis-server /usr/local/redis/redis.conf
```

**3.1 基础配置**

| 配置名    | 说明                                      |
| :-------- | :---------------------------------------- |
| port      | 端口                                      |
| logfile   | 日志文件                                  |
| dir       | Redis 工作目录 (存放持久化文件和日志文件) |
| daemonize | 是否以守护进程的方式启动 Redis            |

## Redis 命令行客户端

**1. 交互式**

```shell
redis-cli -h 127.0.0.1 -p 6379
```

**2. 命令方式**

```shell
redus-cli -h 127.0.0.1 -p 6379 get hello
```

## 停止 Redis 服务

```shell
redis-cli shutdown
# 关闭之前是否生成持久化文件
redis-cli shutdown nosave|save
```

## 外放访问 Redis

1. 开发 Redis 端口
2. 修改 redis.conf

```shell

bind 127.0.0.1
protected-mode yes

```

修改为

```shell
# bind 127.0.0.1
protected-mode no
```

## 修改持久化路径和日志路径

```shell
# 日志路径
logfile /data/redis_cache/logs/redis.log
# 持久化路径，修改后 记得要把dump.rdb持久化文件
dir /data/redis_cache

dbsize

# 删除所有数据库中的key
flushall
# 删除当前数据库中的所有Key
flushdb
```

## 全局命令

**1. dbsize**

dbsize 命令在计算键总数时不会遍历所有键，而是直接获取 Redis 内置的 键总数变量，所以 dbsize 命令的时间复杂度是 O（1）

**2. keys**

keys 命令会遍历所 有键，所以它的时间复杂度是 O（n），当 Redis 保存了大量键时，线上环境 禁止使用。

**3. exists key**

检查 key 是否存在

**4. del key1 [key2]**

删除 key

del 是一个通用命令，无论值是什么数据结构类型，del 命令都可以将其 删除

**5. expire key seconds**

Redis 支持对键添加过期时间，当超过过期时间后，会自动删除键

```shell
redis> expire name 10
1
redis> ttl name
3
redis> ttl name
0
redis> ttl name
# 返回 -2 时, 说明 key 已被删除
-2
redis> get name
null
```

**6. type (key 的数据结构)**

```shell
redis> set name dong4j
OK
redis> type name
string
redis> type aaa
none
redis> rpush list ab cd ef
3
redis> type list
list
```
