---
title: Redis高效处理：字符串、哈希、列表和有序集合
keywords:
  - Redis
categories:
  - 新时代码农
tags:
  - Redis
  - 数据结构
  - 键管理
  - 字符串
  - 列表
  - 集合
  - 有序集合
  - 消息队列
  - 文章列表
abbrlink: '59843415'
date: 2013-02-20 00:00:00
ai:
  - 本文详述了Redis基础数据结构包括字符串、哈希、列表和有序集合的基本操作及其应用场景。在进行键的管理时，介绍了如何有效地使用这些数据结构解决实际问题。例如，使用哈希实现用户信息存储与查询，列表实现消息队列或文章列表，以及有序集合来处理具有排序需求的数据。
description: 本文详述了Redis基础数据结构包括字符串、哈希、列表和有序集合的基本操作及其应用场景。在进行键的管理时，介绍了如何有效地使用这些数据结构解决实际问题。例如，使用哈希实现用户信息存储与查询，列表实现消息队列或文章列表，以及有序集合来处理具有排序需求的数据。
---

## 基础数据结构

### 字符串

> 字符串类型的值实际可以 是字符串（简单的字符串、复杂的字符串（例如 JSON、XML））、数字 （整数、浮点数），甚至是二进制（图片、音频、视频），但是值最大不能 超过 512MB。

![20241229154732_N5bzodwZ.webp](20241229154732_N5bzodwZ.webp)

```shell
set key value [ex seconds] [px milliseconds] [nx|xx]


setex key seconds value
setnx key value
```

set 命令有几个选项:

- ex seconds：为键设置秒级过期时间。
- px milliseconds：为键设置毫秒级过期时间。
- nx：键必须不存在，才可以设置成功，用于添加。
- xx：与 nx 相反，键必须存在，才可以设置成功，用于更新。

#### set、setnx、set xx 的区别

```shell
redis> get name
dong4j
redis> setnx name dong
# 因为 name 已存在, 设置失败
0
redis> get name
dong4j
redis> set name dong4j xx
# name 存在才能使用 xx
OK
redis> get name
dong4j
```

[使用 setnx 实现分布式锁](https://www.cnblogs.com/linjiqin/p/8003838.html)

#### 批量处理

```shell
redis> mset a 1 b 2 c 3
OK
redis> mget a b c d
0 1
1 2
2 3
3 null
```

#### 计数操作

```shell
# 自增
incr key
# 自减
decr key
# 自增指定数字
incrby key increment
# 自减指定数字
decrby key decrement
# 自增浮点数
incrbyfloat key increment
```

#### 应用场景

由于 Redis 的单线程命令处理机制，如果有多个客户端同时执行 setnx key value， 根据 setnx 的特性只有一个客户端能设置成功，setnx 可以作为分布式锁的一种实现方案

1. 缓存功能  
   ![20241229154732_bEHqjfIe.webp](20241229154732_bEHqjfIe.webp)
2. 计数

```shell
long incrVideoCounter(long id) {
        key = "video:playCount:" + id;
        return redis.incr(key);
}

```

3. 共享 Session
   ![20241229154732_faMHn3jj.webp](20241229154732_faMHn3jj.webp)
4. 限速

   限制获取验证码的频率 一分钟不能超过 5 次

```shell
phoneNum = "138xxxxxxxx";
key = "shortMsg:limit:" + phoneNum;
// SET key value EX 60 NX
isExists = redis.set(key,1,"EX 60","NX");
if(isExists != null || redis.incr(key) <=5) {
        // 通过
} else {
        // 限速
}
```

### 哈希

![20241229154732_kwSAJr0I.webp](20241229154732_kwSAJr0I.webp)

#### 常用操作

```shell
# 设置值
hset key field value
# 获取值
hget key field
# 删除 field
hdel key field [field ...]
# 计算 field 个数
hlen key
# 批量设置或获取 field-value
hmget key field [field ...]
# 批量获取 field-value
hmset key field value [field value ...]
# 判断 field 是否存在
hexists key field
# 获取所有field
hkeys key
# 获取所有value
hvals key
# 获取所有的field-value
hgetall key

# 对 field 自增
hincrby key field
hincrbyfloat key field
# 计算value的字符串长度
hstrlen key field
```

#### 使用场景

![20241229154732_W36e7jqG.webp](20241229154732_W36e7jqG.webp)

```java
UserInfo getUserInfo(long id) {
    // 用户id作为key后缀
    userRedisKey = "user:info:" + id;
    // 使用hgetall获取所有用户信息映射关系
    userInfoMap = redis.hgetAll(userRedisKey);
    UserInfo userInfo;
    if (userInfoMap != null) {
        // 将映射关系转换为UserInfo
        userInfo = transferMapToUserInfo(userInfoMap);
    } else {
        // 从MySQL中获取用户信息
        userInfo = mysql.get(id);
        // 将userInfo变为映射关系使用hmset保存到Redis中
        redis.hmset(userRedisKey, transferUserInfoToMap(userInfo));
        // 添加过期时间
        redis.expire(userRedisKey, 3600);
    } return userInfo;
}
```

### 列表

列表中的每个字符串 称为元素（element），一个列表最多可以存储 2 32 -1 个元素。  
在 Redis 中，可 以对列表两端插入（push）和弹出（pop），还可以获取指定范围的元素列 表、获取指定索引下标的元素等

![20241229154732_ZXix2Mna.webp](20241229154732_ZXix2Mna.webp)

![20241229154732_Q8kTkP5h.webp](20241229154732_Q8kTkP5h.webp)

#### 常用操作

| 操作类型 | 操作                 |
| :------- | :------------------- |
| 添加     | rpush lpush linsert  |
| 查询     | lrange lindex llen   |
| 删除     | lpop rpop lrem ltrim |
| 修改     | lset                 |
| 阻塞操作 | blpop brpop          |

```shell
# 向 poivt 前或后插入元素
linsert key before|after pivot value
```

#### 使用场景

**1. 消息队列**

Redis 的 lpush+brpop 命令组合即可实现阻塞队列，生产 者客户端使用 lrpush 从列表左侧插入元素，多个消费者客户端使用 brpop 命令 阻塞式的“抢”列表尾部的元素，多个客户端保证了消费的负载均衡和高可用性。

![20241229154732_p0w8fDqH.webp](20241229154732_p0w8fDqH.webp)

**2. 文章列表**

场景使用口诀

- lpush+lpop=Stack（栈）
- lpush+rpop=Queue（队列）
- lpsh+ltrim=Capped Collection（有限集合）
- lpush+brpop=Message Queue（消息队列）

### 集合

![20241229154732_EH8AHkt5.webp](20241229154732_EH8AHkt5.webp)

### 有序集合

## 键的管理
