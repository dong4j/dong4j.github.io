---
title: Redis scan命令学习
keywords:
  - Redis
categories:
  - Redis
tags:
  - Redis
  - scan命令
  - sscan命令
  - hscan命令
  - zscan命令
description: scan命令详解
abbrlink: 958ae77b
date: 2017-01-30 00:00:00
ai:
  - 本文详细介绍了Redis命令中的scan、sscan、hscan和zscan的功能及其使用方法。特别强调了在生产环境中避免直接使用`keys *`命令的原因，因为它会返回所有键，导致查询时间过长并阻塞服务器。此外，文章还解释了cursor（游标）的作用，用于指示查询的开始位置，并且提供了使用MATCH参数进行模糊匹配以找到特定类型的键的方法。文章通过实例演示了这些命令的功能和用法，包括对集合、哈希表和有序集合的遍历过程。
---

## 1. 介绍

`scan`命令的作用和`keys *`的作用类似，主要用于查找 redis 中的键，但是在正式的生产环境中一般不会直接使用`keys *`
这个命令，因为他会返回所有的键，如果键的数量很多会导致查询时间很长，进而导致服务器阻塞，所以需要 scan 来进行更细致的查找

`scan`总共有这几种命令：`scan`、`sscan`、`hscan`、`zscan`，分别用于迭代数据库中的：数据库中所有键、集合键、哈希键、有序集合键，命令具体结构如下：

```bash
scan cursor [MATCH pattern] [COUNT count] [TYPE type]
sscan key cursor [MATCH pattern] [COUNT count]
hscan key cursor [MATCH pattern] [COUNT count]
zscan key cursor [MATCH pattern] [COUNT count]
```

## 2. scan

`scan cursor [MATCH pattern] [COUNT count] [TYPE type]`，cursor 表示游标，指查询开始的位置，count 默认为 10，查询完后会返回下一个开始的游标，当返回 0 的时候表示所有键查询完了

```bash
127.0.0.1:6379[2]> scan 0
1) "3"
2)  1) "mystring"
    2) "myzadd"
    3) "myhset"
    4) "mylist"
    5) "myset2"
    6) "myset1"
    7) "mystring1"
    8) "mystring3"
    9) "mystring4"
   10) "myset"
127.0.0.1:6379[2]> scan 3
1) "0"
2) 1) "myzadd1"
   2) "mystring2"
   3) "mylist2"
   4) "myhset1"
   5) "mylist1"
```

MATCH 可以采用模糊匹配找出自己想要查找的键，这里的逻辑是先查出 20 个，再匹配，而不是先匹配再查询，这里加上 count
20 是因为默认查出的 10 个数中可能不能包含所有的相关项，所以把范围扩大到查 20 个，我这里测试的键总共有 15 个

```bash
127.0.0.1:6379[2]> scan 0 match mylist* count 20
1) "0"
2) 1) "mylist"
   2) "mylist2"
   3) "mylist1"
```

TYPE 可以根据具体的结构类型来匹配该类型的键

```bash
127.0.0.1:6379[2]> scan 0 count 20 type list
1) "0"
2) 1) "mylist"
   2) "mylist2"
   3) "mylist1"
```

## 3. sscan

`sscan key cursor [MATCH pattern] [COUNT count]`，sscan 的第一个参数总是集合类型的 key

```bash
127.0.0.1:6379[2]> sadd myset1 a b c d
(integer) 4
127.0.0.1:6379[2]> smembers myset1
1) "d"
2) "a"
3) "c"
4) "b"
127.0.0.1:6379[2]> sscan myset1 0
1) "0"
2) 1) "d"
   2) "c"
   3) "b"
   4) "a"
127.0.0.1:6379[2]> sscan myset1 0 match a
1) "0"
2) 1) "a"
```

## 4. hscan

`hscan key cursor [MATCH pattern] [COUNT count]`，sscan 的第一个参数总是哈希类型的 key

```bash
127.0.0.1:6379[2]> hset myhset1 kk1 vv1 kk2 vv2 kk3 vv3
(integer) 3
127.0.0.1:6379[2]> hgetall myhset1
1) "kk1"
2) "vv1"
3) "kk2"
4) "vv2"
5) "kk3"
6) "vv3"
127.0.0.1:6379[2]> hscan myhset1 0
1) "0"
2) 1) "kk1"
   2) "vv1"
   3) "kk2"
   4) "vv2"
   5) "kk3"
   6) "vv3"
```

## 5. zscan

`zscan key cursor [MATCH pattern] [COUNT count]`，sscan 的第一个参数总是有序集合类型的 key

```bash
127.0.0.1:6379[2]> zadd myzadd1 1 zz1 2 zz2 3 zz3
(integer) 3
127.0.0.1:6379[2]> zrange myzadd1 0 -1 withscores
1) "zz1"
2) "1"
3) "zz2"
4) "2"
5) "zz3"
6) "3"
127.0.0.1:6379[2]> zscan myzadd1 0
1) "0"
2) 1) "zz1"
   2) "1"
   3) "zz2"
   4) "2"
   5) "zz3"
   6) "3"
```
