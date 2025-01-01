---
title: Redis入门：掌握基础，开启高效数据存储之旅
keywords:
  - Redis
categories:
  - Redis
tags:
  - Redis
  - Data Store
  - Key-Value Operations
  - Data Structures
  - Pub/Sub Model
  - Transaction Processing
  - HyperLogLog
  - Caching
  - Session Management
  - Rate Limiting
abbrlink: 6c8ae0af
date: 2013-02-17 00:00:00
ai:
  - Redis 是一个开源、广泛使用的内存数据结构存储系统，它提供了多种数据类型并支持事务和发布/订阅模型。在 Redis 中可以使用诸如键/值对（哈希）、列表、集合等数据结构进行操作。其主要特点是高效率、低延迟和简单的API接口。Redis事务确保了命令执行的原子性和顺序性，并允许用户在多个命令中应用隔离性。此外，发布/订阅模型使得消息可以在多个客户端之间广播，非常适合实时通信和通知服务。
description: Redis 是一个开源、广泛使用的内存数据结构存储系统，它提供了多种数据类型并支持事务和发布/订阅模型。在 Redis 中可以使用诸如键/值对（哈希）、列表、集合等数据结构进行操作。其主要特点是高效率、低延迟和简单的API接口。Redis事务确保了命令执行的原子性和顺序性，并允许用户在多个命令中应用隔离性。此外，发布/订阅模型使得消息可以在多个客户端之间广播，非常适合实时通信和通知服务。
---

## Redis 的 3 种用法

1. 内存缓存
2. 定量数据指标
3. 发布/订阅模型

### 作为内存环境

#### 数据结构

**1. 字符串 string**

```shell
// 设置字符串类型
set mystr "hello world!"
// 读取字符串类型
get mystr

// 通过字符串类型进行数值操作 在遇到数值操作时，redis 会将字符串类型转换成数值。
127.0.0.1:6379> set mynum "2"
OK
127.0.0.1:6379> get mynum
"2"
127.0.0.1:6379> incr mynum
(integer) 3
127.0.0.1:6379> get mynum
"3"
```

> INCR 等指令本身就具有原子操作的特性，所以我们完全可以利用 redis 的 INCR、INCRBY、DECR、DECRBY 等指令来实现原子计数的效果，假如，在某种场景下有 3 个客户端同时读取了 mynum 的值（值为 2），然后对其同时进行了加 1 的操作，那么，最后 mynum 的值一定是 5。不少网站都利用 redis 的这个特性来实现业务上的统计计数需求。

**2. 列表 list**

Redis list 使用链表实现, 所以插入速度快, 查询速度慢

```shell
// 新建一个 list 叫做 mylist，并在列表头部插入元素 "1"
127.0.0.1:6379> lpush mylist "1"
// 返回当前 mylist 中的元素个数
(integer) 1
// 在 mylist 右侧插入元素 "2"
127.0.0.1:6379> rpush mylist "2"
(integer) 2
// 在 mylist 左侧插入元素 "0"
127.0.0.1:6379> lpush mylist "0"
(integer) 3
// 列出 mylist 中从编号 0 到编号 1 的元素
127.0.0.1:6379> lrange mylist 0 1
1) "0"
2) "1"
// 列出 mylist 中从编号 0 到倒数第一个元素
127.0.0.1:6379> lrange mylist 0 -1
1) "0"
2) "1"
3) "2"
```

lists 的应用相当广泛，随便举几个例子：

1. 我们可以利用 lists 来实现一个消息队列，而且可以确保先后顺序，不必像 MySQL 那样还需要通过 ORDER BY 来进行排序。
2. 利用 LRANGE 还可以很方便的实现分页的功能。
3. 在博客系统中，每片博文的评论也可以存入一个单独的 list 中。

**3. 无序集合 set**

```shell
// 向集合 myset 中加入一个新元素 "one"
127.0.0.1:6379> sadd myset "one"
(integer) 1
127.0.0.1:6379> sadd myset "two"
(integer) 1
// 列出集合 myset 中的所有元素
127.0.0.1:6379> smembers myset
1) "one"
2) "two"
// 判断元素 1 是否在集合 myset 中，返回 1 表示存在
127.0.0.1:6379> sismember myset "one"
(integer) 1
// 判断元素 3 是否在集合 myset 中，返回 0 表示不存在
127.0.0.1:6379> sismember myset "three"
(integer) 0
// 新建一个新的集合 yourset
127.0.0.1:6379> sadd yourset "1"
(integer) 1
127.0.0.1:6379> sadd yourset "2"
(integer) 1
127.0.0.1:6379> smembers yourset
1) "1"
2) "2"
// 对两个集合求并集
127.0.0.1:6379> sunion myset yourset
1) "1"
2) "one"
3) "2"
4) "two"
```

> 对于集合的使用，也有一些常见的方式，比如，QQ 有一个社交功能叫做 “好友标签”，大家可以给你的好友贴标签，比如 “大美女”、“土豪”、“欧巴” 等等，这时就可以使用 redis 的集合来实现，把每一个用户的标签都存储在一个集合之中。

**4. 有序集合 zset**

```shell
127.0.0.1:6379> zadd myzset 1 baidu.com
(integer) 1
// 向 myzset 中新增一个元素 360.com，赋予它的序号是 3
127.0.0.1:6379> zadd myzset 3 360.com
(integer) 1
// 向 myzset 中新增一个元素 google.com，赋予它的序号是 2
127.0.0.1:6379> zadd myzset 2 google.com
(integer) 1
// 列出 myzset 的所有元素，同时列出其序号，可以看出 myzset 已经是有序的了。
127.0.0.1:6379> zrange myzset 0 -1 with scores
1) "baidu.com"
2) "1"
3) "google.com"
4) "2"
5) "360.com"
6) "3"
// 只列出 myzset 的元素
127.0.0.1:6379> zrange myzset 0 -1
1) "baidu.com"
2) "google.com"
3) "360.com"
```

**5. 哈希 hashes**

哈希是从 redis-2.0.0 版本之后才有的数据结构。

hashes 存的是字符串和字符串值之间的映射，比如一个用户要存储其全名、姓氏、年龄等等，就很适合使用哈希。

```shell
// 建立哈希，并赋值
127.0.0.1:6379> HMSET user:001 username dong4j password 1234 age 29
OK
// 列出哈希的内容
127.0.0.1:6379> HGETALL user:001
1) "username"
2) "dong4j"
3) "password"
4) "1234"
5) "age"
6) "29"
// 更改哈希中的某一个值
127.0.0.1:6379> HSET user:001 password 12345
(integer) 0
// 再次列出哈希的内容
127.0.0.1:6379> HGETALL user:001
1) "username"
2) "dong4j"
3) "password"
4) "12345"
5) "age"
6) "29"
```

**6. HyperLogLog**

Redis 的 HyperLogLog 使用随机化，以提供唯一的元素数目近似的集合只使用一个常数，并且体积小，少量内存的算法。

HyperLogLog 提供，即使每个使用了非常少量的内存（12 千字节），标准误差为集合的基数非常近似，没有限制的条目数，可以指定，除非接近 264 个条目。

```shell
redis 127.0.0.1:6379> PFADD tutorials "redis"
1) (integer) 1
redis 127.0.0.1:6379> PFADD tutorials "mongodb"
1) (integer) 1
redis 127.0.0.1:6379> PFADD tutorials "mysql"
1) (integer) 1
redis 127.0.0.1:6379> PFCOUNT tutorials
(integer) 3
```

### 作为定量数据指标

### 发布/订阅模型

Redis 的订阅实现了邮件系统，发送者（在 Redis 的术语中被称为发布者）发送的邮件，而接收器（用户）接收它们。由该消息传送的链路被称为通道。

在 Redis 客户端可以订阅任何数目的通道。

```shell
redis 127.0.0.1:6379> SUBSCRIBE redisChat

Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "redisChat"
3) (integer) 1
```

```shell
redis 127.0.0.1:6379> PUBLISH redisChat "Redis is a great caching technique"

(integer) 1

redis 127.0.0.1:6379> PUBLISH redisChat "Learn redis by tutorials point"

(integer) 1

1) "message"
2) "redisChat"
3) "Redis is a great caching technique"
1) "message"
2) "redisChat"
3) "Learn redis by tutorials point"
```

## Redis 事务

Redis 事务让一组命令在单个步骤执行。事务中有两个属性，说明如下：

1. 在一个事务中的所有命令按顺序执行作为单个隔离操作。通过另一个客户端发出的请求在 Redis 的事务的过程中执行，这是不可能的。
2. Redis 的事务具有原子性。原子意味着要么所有的命令都执行或都不执行。

> Redis 的事务由指令多重发起，然后需要传递在事务，而且整个事务是通过执行命令 EXEC 执行命令列表。

```shell
redis 127.0.0.1:6379> MULTI
OK
List of commands here
redis 127.0.0.1:6379> EXEC
```

```shell
redis 127.0.0.1:6379> MULTI
OK
redis 127.0.0.1:6379> SET tutorial redis
QUEUED
redis 127.0.0.1:6379> GET tutorial
QUEUED
redis 127.0.0.1:6379> INCR visitors
QUEUED
redis 127.0.0.1:6379> EXEC

1) OK
2) "redis"
3) (integer) 1
```
