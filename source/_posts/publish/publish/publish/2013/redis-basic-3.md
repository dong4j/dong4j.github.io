---
title: Redis 基础三
keywords:
  - Redis
categories:
  - Redis
tags:
  - Redis
abbrlink: 1556580b
date: 2013-02-19 00:00:00
---

## Redis 的 5 种数据结构

![20241229154732_VjP0mAw9.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VjP0mAw9.webp)

## Redis 数据结构和内部编码

![20241229154732_kNOvBCjM.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_kNOvBCjM.webp)

## Redis 的单线程模型

Redis 使用单线程处理命令, 所以一条命令从客户端达到服务端不会立即执行, 所有命令都会进入一个队列, 然后逐个被执行.

**Redis 单线程处理速度快的原因**

1. 纯内存访问, 内存的响应时长约为 100 纳秒
2. 非阻塞 I/O, Redis 使用 epoll 作为 I/O 多路复用技术的实现, 再加上 Redis 自身的事件处理模型将 epoll 中的连接、读写、关闭都转换为事件，不 在网络 I/O 上浪费过多的时间

   ![20241229154732_vK47Dk4P.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_vK47Dk4P.webp)

3. 单线程避免了线程切换和竞态产生的消耗

**存在的问题**

对于每个命令的执行时间有要求.

如果某个命令执行时间过长, 会造成其他命令阻塞
