---
title: NAS 存储共享解决方案
cover: https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_KKA3Ghw8.webp
ai:
  - 提供了一种基于私有云的企业级文件存储和管理解决方案，该方案包括高性能的硬件配置、强大的数据保护功能（如快照备份、容灾恢复）、智能的数据同步与共享机制以及PB级别的在线存储扩容能力。通过利用NAS系统，企业能够实现从内部部署到多用户访问的一站式文件管理和协作环境。此方案旨在满足不同规模和需求的企业对于高可靠、高性能存储的需求，并特别适合于需要处理大量数据、视频编辑、大规模监控应用的场景。
tags:
  - 私有云企业网盘
  - 文件同步共享
  - 备份与容灾
  - 大容量存储
  - 在线扩容
categories: NAS
abbrlink: 7a6d
date: 2020-02-06 00:00:00
description: 提供了一种基于私有云的企业级文件存储和管理解决方案，该方案包括高性能的硬件配置、强大的数据保护功能（如快照备份、容灾恢复）、智能的数据同步与共享机制以及PB级别的在线存储扩容能力。通过利用NAS系统，企业能够实现从内部部署到多用户访问的一站式文件管理和协作环境。此方案旨在满足不同规模和需求的企业对于高可靠、高性能存储的需求，并特别适合于需要处理大量数据、视频编辑、大规模监控应用的场景。
---

<!-- https://unsplash.com/photos/a-close-up-of-a-cable-with-a-black-background-zqnfqFYaIhE -->

![/images/cover/20241229154732_KKA3Ghw8.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_KKA3Ghw8.webp)

目前公司的数据存储模式比较落后, 主要问题在于**数据安全性差**；整体数据量大以及原有大量陈旧的数据难以存储；存在多操作系统平台，设备繁杂导致存放的数据难以共享协作和管理，造成效率低下；员工的离职造成资料丢失。我们需要一个满足需求又安全的方案来解决这样的普遍难题。

NAS 存储共享解决方案包含：**群晖 NAS 服务器**、Backup 插件。

**应用场景：**
企业数据集中存储/共享/备份，企业私有云文件管理器搭建。

## 方案背景

随着企业信息化的发展，企业信息化带来的数据爆炸式增长向企业的数据管理方式提出了挑战，**一方面要应对数据容量的不断扩充，另一方面需要确保所有有效数据的高安全性和可管理性**。目前来看，企业的数据各自存放、分散管理，关联性不强，无法很好的针对不同的业务数据进行统一、有效的管理。

企业的数据存储模式比较落后，成本较高且效率低下，主要问题在于数据安全性差；整体数据量大以及原有大量陈旧的数据难以存储；存在多操作系统平台，设备繁杂导致存放的数据难以共享协作和管理，造成效率低下；员工的离职造成资料丢失。

从对企业单位数据存储的分析中可以看出，要使整个企业内部的数据得到统一管理和安全应用，就必须有一个安全、性价比好、应用方便、管理简单的物理介质来存储和管理企业内部的数据资料。把所有零散的数据和业务系统中的重要数据进行管理，避免在异常情况下数据的丢失。

## 方案设计概述

NAS 网络存储设备是一款特殊设计的文件存储服务器，它能够将网络中的数据资料合理有效、安全地存放和管理起来。 对于企业集中数据中心解决方案而言，主要的建设目标有以下几个：

- 实现网络办公环境下的集中资料共享、交互，改变以往单一的个人共享行为。
- 完成公司、个人、客户资料的安全存放，增强数据的可靠性，实现长期保存。
- 带动公司内部的数据流程，实现数据的知识共享和访问权限控制。

## NAS 是什么

NAS（Network Attached Storage），直译是网络附加存储，简单来说是连接在网络上，具有资料存储功能的设备，也叫做网络存储服务器。实际上，NAS 的功能不单单局限于存储，群晖 NAS 已经成功打造了**丰富的软件生态**。

不仅是个人，工作室、中小企业、500 强企业都在使用 NAS。随着企业的发展，数据量不断增长，传统文件服务器功能有限，软件需要订阅付费，而使用公有云，费用随人员量、数据量的增长而增加。企业可以使用群晖在以下场景中：

1. 使用群晖 NAS 搭建**企业文件服务器**，可以集中存储各部门文件，权限设置简单，员工可在 Windows、macOS 和 Linux 平台之间实现文件无缝共享。
2. 除了可以用作文件服务器，群晖 NAS 还为业务数据提供一体化备份平台，整机保护员工电脑、物理服务器、虚拟机、公有云数据，通过直观的图形化界面，在一个平台上就可以管理所有备份任务，有效保护企业关键业务数据，避免误删、泄露、勒索病毒等意外导致的利益损失。

## 主要功能

### 1. 文件管理

Synology NAS 整合数据存储、存取和共享等一体化文件管理应用，通过 DSM 直观易用的管理界面，无论家庭用户，或是工作繁重的 IT 管理人员，都能轻松完成所有文件同步、安全设置，全权掌控数据。

#### 1.1 存取与共享

文件存取和共享，是 Synology NAS 的核心应用。DSM 支持多种主流通讯协议和多设备存取功能，为您打造顺畅的实时数据应用体验，同时为您的数据提供高安全层级保护。

**支持主流通信协议和操作系统:**

支持主流浏览器、移动平台和操作系统，可灵活融入家庭或企业办公环境，数据存取畅通无阻。

![20241229154732_Wp8tXDs8.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Wp8tXDs8.webp)

**文件和文件夹共享:**

通过分享链接或二维码，可快速分享文件和文件夹，并提供多重安全保护和存取权限选项，为您的数据安全保驾护航。

![20241229154732_JpGaf9hq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_JpGaf9hq.webp)

#### 1.2 同步与管理

![20241229154732_rWYt4kYU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_rWYt4kYU.webp)

![20241229154732_HPuSVats.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_HPuSVats.webp)

### 2. 用户管理

![20241229154732_Koc3L4MW.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Koc3L4MW.webp)

![20241229154732_nATaGC12.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_nATaGC12.webp)

### 3. 办公效率

#### 3.1 Office

团队成员可以随时通过 Web 界面同时编辑同一份文档、电子表格或幻灯片，并支持 Microsoft Office 文件导入编辑与导出分享，通过流畅、实时的线上协作，解决远程协作的沟通难题，从而大幅提升办公效率。

##### 3.1.1 文档

![20241229154732_Y2PzUj4U.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Y2PzUj4U.webp)

##### 3.1.2 电子表格

![20241229154732_fft2Uxbs.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_fft2Uxbs.webp)

##### 3.1.3 幻灯片

![20241229154732_gOu0x64d.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_gOu0x64d.webp)

#### 3.2 协同办公

![20241229154732_3QIzKP9l.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_3QIzKP9l.webp)

### 4. 数据备份

![20241229154732_5s7mHwWs.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_5s7mHwWs.webp)

![20241229154732_p9936ya2.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_p9936ya2.webp)

### 5. 安全性

![20241229154732_7TOwpgwk.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_7TOwpgwk.webp)

![20241229154732_ntLmuG7o.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ntLmuG7o.webp)

### 6. 系统管理

![20241229154732_trkcLymW.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_trkcLymW.webp)

![20241229154732_DMBlNWnx.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_DMBlNWnx.webp)

## 使用场景

### 1. 随时随地存取数据

![20241229154732_DvOAAfzU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_DvOAAfzU.webp)

![20241229154732_ORH181Ul.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ORH181Ul.webp)

![20241229154732_5k4uQ7BU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_5k4uQ7BU.webp)

### 2. 文件服务器

#### 2.1 跨平台即时共享

支持 SMB / NFS / FTP 等多种传输协议，局域网内共享。无需自建 FTP，即可跨平台、多终端随时存取；总部和分支机构间也能便捷下发和上收文件。

![20241229154732_FfAg6Fj8.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_FfAg6Fj8.webp)

#### 2.2 图形化的权限安全管理

图形化界面，操作直观简便，无需输入指令或导入表格。支持委派专人管理权限，并且可设置密码、有效期实现安全分享，通过导出权限报告实现权限审核。

![20241229154732_GtPer2AH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_GtPer2AH.webp)

#### 2.3 不受地域限制的在线办公

通过网页或移动端 App，不受地域限制，即可实现移动办公，还可设置文件离线访问。并且支持在线 Office，多人协作提升团队办公效率。

**群晖跨电脑、跨地域同步及共享方案打通数据孤岛,实现自动同步和即时共享,建立企业文件中心。同时支持多版本备份,避免因误删、勒索病毒等导致文件丢失。**

![20241229154732_7wYwXGdO.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_7wYwXGdO.webp)

![20241229154732_VOIsJvSX.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VOIsJvSX.webp)

![20241229154732_MzQHfGV2.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_MzQHfGV2.webp)

![20241229154732_KFwZCGSl.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_KFwZCGSl.webp)

#### 2.4 文件管理与同步

![20241229154732_0l8VaHxH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_0l8VaHxH.webp)

![20241229154732_OpERLBVc.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_OpERLBVc.webp)

![20241229154732_8QQWajmE.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_8QQWajmE.webp)

![20241229154732_rvZ94CMa.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_rvZ94CMa.webp)

![20241229154732_Hd4dsvyx.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Hd4dsvyx.webp)

![20241229154732_LiFfAnvn.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_LiFfAnvn.webp)

#### 2.5 PB 级存储容量的在线扩容

添加扩展柜进行在线扩容，可支持多达 180 个硬盘，提供 PB 级净存储容量，轻松满足影视后期制作、大规模监控部署等大容量存储需求。

#### 2.6 容灾备份

为文件夹和 iSCSI LUN 建立快照保护，可快速恢复被病毒锁定的文件，防止企业数据丢失。同时可为服务器、虚拟机和 PC 实现免许可证的整机备份方案。

![20241229154732_nUf2ln5g.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_nUf2ln5g.webp)

### 3. 文件同步与共享

![20241229154732_yKeXtvgW.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_yKeXtvgW.webp)

### 4. 私有云企业网盘

![20241229154732_kSNQKTiq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_kSNQKTiq.webp)

![20241229154732_XrVyLXft.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_XrVyLXft.webp)

## 系统展示

![20241229154732_XZqADQCq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_XZqADQCq.webp)

![20241229154732_rPqOZbFH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_rPqOZbFH.webp)

![20241229154732_QwWnhMmq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_QwWnhMmq.webp)

![20241229154732_cooNFI9g.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_cooNFI9g.webp)

![20241229154732_CIu37ozq.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_CIu37ozq.webp)

![20241229154732_ezwtG796.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ezwtG796.webp)

![20241229154732_hGMqv6Er.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_hGMqv6Er.webp)

![20241229154732_JaIdkVM5.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_JaIdkVM5.webp)
