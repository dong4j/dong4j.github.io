---
title: HomeLab 先导篇：入门指南-开启你的个人云端实验室之旅
cover: /images/cover/20241229154732_dJYxL1SG.webp
sticky: 1
swiper_index: 2
top_group_index: 2
ai:
  - 本文介绍了中年男人三大爱好——充电头、NAS和软路由，并分享了作者作为软件开发者搭建自己的服务器（HomeLab）的经历。文章详细描述了如何选购合适的NAS设备、软路由器以及服务器，以及在搭建过程中遇到的挑战和解决方案。同时，还探讨了为什么选择自建HomeLab的原因，包括搭建实验室的乐趣、数据安全和隐私保护的重要性。文章强调了KISS原则在HomeLab搭建中的应用，即在保证功能的前提下尽量简化系统架构。此外，还介绍了硬件成本和软件成本的考虑因素。最后，总结了整个搭建过程中的关键点和所遇到的问题及解决方案。
tags:
  - HomeLab
  - NAS
  - 软路由
  - 数据安全
  - 隐私保护
  - KISS原则
categories:
  - HomeLab:中年男人的快乐源泉
abbrlink: ff21
date: 2020-04-08 00:00:00
main_color:
description: 本文介绍了中年男人三大爱好——充电头、NAS和软路由，并分享了作者作为软件开发者搭建自己的服务器（HomeLab）的经历。文章详细描述了如何选购合适的NAS设备、软路由器以及服务器，以及在搭建过程中遇到的挑战和解决方案。同时，还探讨了为什么选择自建HomeLab的原因，包括搭建实验室的乐趣、数据安全和隐私保护的重要性。文章强调了KISS原则在HomeLab搭建中的应用，即在保证功能的前提下尽量简化系统架构。此外，还介绍了硬件成本和软件成本的考虑因素。最后，总结了整个搭建过程中的关键点和所遇到的问题及解决方案。
keywords:
  - HomeLab
  - NAS
  - 软路由
  - 数据安全
  - 隐私保护
  - KISS原则
---

![/images/cover/20241229154732_dJYxL1SG.webp](/images/cover/20241229154732_dJYxL1SG.webp)

中年男人的三大爱好：充电头、NAS、软路由。这三大爱好不仅为我们的生活带来了便利，也成为了我们生活的一部分(🤡)。

作为一个软件开发者，我一直梦想着拥有自己的服务器，而 NAS 和软路由则是我通往这个梦想的桥梁。

自从购买了我的第一台 NAS 以来，便打开了一扇新世界的大门。NAS，即网络附加存储（Network Attached Storage），它不仅提供了一个安全的数据存储解决方案，还让我能够实现数据的备份和共享。随着时间的推移，我陆续购买了其他硬件产品，如软路由器、服务器等，逐步搭建起了属于我的 HomeLab。

今天，我想和大家分享一下我搭建 HomeLab 的过程，希望能够帮助到那些同样有志于搭建 HomeLab 的朋友。在接下来的博客文章中，我将详细介绍如何选购合适的 NAS 设备、软路由器以及服务器，并分享我在搭建过程中遇到的挑战和解决方案。

HomeLab 并非遥不可及，只要我们用心去探索和实践，就能开启属于自己的个人云端实验室之旅。让我们一起学习、交流和成长，共同打造一个属于我们的数字王国。

## 前提说明

虽然关于 HomeLab 的文章已经很多了，但我还是想记录下自己搭建 HomeLab 的经历和遇到的问题，以及如何解决这些问题。主要会涉及到以下几个方面：

1. [[homelab-guide|先导篇]]：我的 HomeLab 概要;
2. [[homelab-hardware|硬件篇]]：介绍我所拥有的硬件设备;
3. [[homelab-network|网络篇]]：包括网络环境、异地组网与网络安全;
4. [[homelab-service|服务篇]]：使用 Docker 搭建的各类服务;
5. [[homelab-data|数据篇]]：包括数据存储方案、备份方案和数据恢复方案;
6. [[homelab-data-sync|HomeLab数据同步：构建高效的数据同步网络]]
7. [[homelab-data-backup|HomeLab数据备份：打造坚实的数据安全防线]]
8. [[homelab-upgrade-to-10g|HomeLab 网络续集：升级 10G 网络-再战 10 年]]
9. [[homelab-guide|NAT 内网穿透详解：揭秘网络连接背后的奥秘]]

## 什么是 HomeLab

HomeLab，顾名思义，就是家庭实验室。它可以理解为家庭版的云服务器，用来搭建各种服务，比如个人网盘、媒体服务器等等。HomeLab 的硬件设备通常包括：

1. 服务器：可以是物理服务器或虚拟机，用于搭建各类服务。
2. 存储设备：如 NAS 和硬盘，用于存储数据。
3. 网络设备：如软路由和硬路由，用于管理网络。
4. 其他设备：如摄像头、传感器等，用于收集数据。

## 为什么选择自建 HomeLab

对于我来说，搭建 HomeLab 是一种浪漫的“折腾”。我的目标是：

1. 搭建各种感兴趣的服务的实验室：作为一个喜欢尝试新技术的人来说，搭建各类服务非常有趣。我可以快速尝试和验证新的技术和方案，拥有一套自己的实验室可以让我更加自由地探索。
2. 保证数据安全：我对数据安全非常重视，所以我会把所有的数据都存储在自己的服务器上，而不是使用云存储服务。这样可以保证我的数据不会被第三方控制，我已经受够了七牛云的 OSS，域名变更导致我大量图片无法访问。
3. 更好的隐私保护：家人的照片、儿子的成长记录等私密数据本地私有化存储可以让我更加放心，不会担心数据泄露的问题。

## HomeLab 的原则

**KISS 原则** : Keep It Simple, Stupid

HomeLab 搭建是一件费时费力的过程, 为了避免占用大量个人时间, 我会尽量选择一些简单易用的方案, 避免复杂的配置和操作。

本着够用的原则, 不会选择较为复杂的软件架构.

### 硬件成本

对于重要的数据，我会直接选择成品 NAS，避免数据丢失。而对于其他不是特别重要的服务，我会使用 Docker 搭建，这样可以更加灵活地管理数据，也可以更好地控制成本。因此整个 HomeLab 的搭建围绕着 NAS 展开，而其他一些不重要的服务就直接去咸鱼捡垃圾。

### 软件成本

对于 HomeLab 来说，最大的投入是硬件成本和时间。为了降低时间成本，本着 KISS 原则, 我会直接选择使用 Docker，而且不会搭建 K8S 这类比较折腾的服务，因为目前的服务数量和服务质量还不至于用上 K8S（也许在下次升级的时候会考虑）。

## HomeLab 的硬件

![20241229154732_lXrWkJfN.webp](20241229154732_lXrWkJfN.webp)

![20241229154732_cxOH3POn.webp](20241229154732_cxOH3POn.webp)

硬件介绍将在后续文章中详细介绍。

## 网络架构

![network.drawio.svg](network.drawio.svg)

升级过程：

1. 电信宽带入户, 公网 IP, 全屋千兆;
2. 主要设备添加 2.5G 网口, 添加 2.5G 网口交换机;
3. 添加第二条宽带, 公网 IP, 全屋 2.5G 升级改造;
4. 添加万兆交换机, 主要设备升级万兆网口;

## 自托管服务

Dashboard 对于我来说, 就是一个展示我所有服务的面板, 不需要每个服务器的状态监控, 因此一个书签管理器就足够了, 目前比较满意的就是 Chrome 的插件: [Markoob](https://chromewebstore.google.com/detail/markoob-%E4%B9%A6%E7%AD%BE%E5%90%AF%E5%8A%A8%E5%99%A8/lnhnllkaacmnkffnjgcnokifakeckido?hl=zh-CN), 简约且不复杂.

![20241229154732_fEzFCGJj.webp](20241229154732_fEzFCGJj.webp)

大部分服务使用 Docker 搭建，因此选择设备的刚性条件就是：是否支持虚拟化。

## 数据存储与备份

![20241229154732_9HV3mUqg.webp](20241229154732_9HV3mUqg.webp)

主要围绕 NAS 搭建，包括家庭照片备份和服务器重要文件备份。

## 总结

在搭建过程中遇到过非常多的问题，此系列文章的主要目的也是记录下这些问题和解决方案。因此不会详细介绍较为基础的知识，如果需要可以参考其他文章。

{% link 如何搭建家用 homelab: 先导篇,icyleaf,https://icyleaf.com/2022/02/how-to-homelab-part-0/, https://icyleaf.com/tutorials/how-to-homelab/part-0/cover.png %}
{% link 如何搭建家用 homelab: 硬件和架构,icyleaf,https://icyleaf.com/2023/01/how-to-homelab-part-1-hardware-and-architecture/, https://images.unsplash.com/photo-1549319114-d67887c51aed?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2874&q=80 %}
{% link 如何搭建家用 homelab: Openwrt 软路由,icyleaf,https://icyleaf.com/2023/04/how-to-homelab-part-2-openwrt-soft-router/, https://images.unsplash.com/photo-1521542464131-cb30f7398bc6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2673&q=80 %}
{% link 如何搭建家用 homelab: 数据存储,icyleaf,https://icyleaf.com/2023/07/how-to-homelab-part-3-storages/, https://images.unsplash.com/photo-1686705562930-4f3e46f620d8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3000&q=80 %}

**相关文章:**

1. [[homelab-guide|先导篇]]：我的 HomeLab 概要;
2. [[homelab-hardware|硬件篇]]：介绍我所拥有的硬件设备;
3. [[homelab-network|网络篇]]：包括网络环境、异地组网与网络安全;
4. [[homelab-service|服务篇]]：使用 Docker 搭建的各类服务;
5. [[homelab-data|数据篇]]：包括数据存储方案、备份方案和数据恢复方案;
6. [[homelab-data-sync|HomeLab数据同步：构建高效的数据同步网络]]
7. [[homelab-data-backup|HomeLab数据备份：打造坚实的数据安全防线]]
8. [[homelab-upgrade-to-10g|HomeLab 网络续集：升级 10G 网络-再战 10 年]]
9. [[homelab-guide|NAT 内网穿透详解：揭秘网络连接背后的奥秘]]
