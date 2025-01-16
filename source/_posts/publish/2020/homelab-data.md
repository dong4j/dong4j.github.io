---
title: HomeLab 存储与备份：数据堡垒-保障数据和隐私的存储解决方案
swiper_index: 1
top_group_index: 1
ai:
  - 本文深入探讨了在HomeLab中实现高效数据存储、备份和同步方案的重要性。文章介绍了3-2-1备份原则，即至少保留三份数据副本，存放在两种不同类型的媒介上，并且有一份异地备份，以确保数据的安全性和可用性。文章还详细说明了如何对数据进行分类，包括系统与配置文件、个人与家庭数据、工作与代码存储、媒体与资源以及虚拟机与容器备份等。此外，文章介绍了如何在NAS系统中实现这些备份和同步策略，并提供了一些实用的技巧和建议。
tags:
  - HomeLab
  - 数据存储
  - 备份策略
  - 3-2-1原则
  - 数据分类
categories:
  - HomeLab:中年男人的快乐源泉
cover: https://cdn.dong4j.site/source/image/20241229154732_woi0CTG0.webp
date: 2020-04-16 00:00:00
main_color:
description: 本文深入探讨了在HomeLab中实现高效数据存储、备份和同步方案的重要性。文章介绍了3-2-1备份原则，即至少保留三份数据副本，存放在两种不同类型的媒介上，并且有一份异地备份，以确保数据的安全性和可用性。文章还详细说明了如何对数据进行分类，包括系统与配置文件、个人与家庭数据、工作与代码存储、媒体与资源以及虚拟机与容器备份等。此外，文章介绍了如何在NAS系统中实现这些备份和同步策略，并提供了一些实用的技巧和建议。
keywords:
  - HomeLab
  - 数据存储
  - 备份策略
  - 3-2-1原则
  - 数据分类
---

![/images/cover/20241229154732_woi0CTG0.webp](https://cdn.dong4j.site/source/image/20241229154732_woi0CTG0.webp)
[封面来源: Unsplash-Taylor Vick](https://unsplash.com/photos/cable-network-M5tzZtFCOfs)

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


## 简介

在本篇博客中，我们将深入探讨如何在 HomeLab 中实现高效的数据存储、备份和同步方案。

随着个人数据的不断增长，数据的安全性和可用性变得越来越重要。为此，我们可以采用一种被称为 **3-2-1 原则** 的备份策略，以确保我们的数据在发生意外时能够得到及时恢复。

**[3-2-1 备份原则](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/) 的核心要点如下：** (另外一些细节分析可以看韦易笑在知乎的回答:[《如何长时间保存重要数据？》](https://www.zhihu.com/question/313837243/answer/660457814?edition=yidianzixun&utm_source=yidianzixun))

- **3 份备份数据**：我们不应依赖单一的数据备份，而应该拥有至少两份数据副本作为额外的安全保障。这样可以大大降低因单一备份故障导致数据丢失的风险。
- **2 种不同的存储形式**：为了进一步确保数据的冗余和安全，我们应该使用两种不同类型的媒介来存储数据。例如，除了传统的本地硬盘外，我们还可以考虑将数据上传到云服务提供商，或者制作物理媒体如 DVD 作为备份数据的存储方式。
- **1 份异地备份**：考虑到自然灾害、火灾等不可抗力因素可能导致本地备份失效的情况，我们应该至少有一份数据备份在离本地较远的地方。这样即使发生了极端情况，我们也能从异地备份中恢复数据。

在执行 321 原则之前，我们还需要进行一步重要的工作——对数据进行分类。不是所有的数据都需要进行严格的备份保护。例如，一些可以通过互联网轻松获取的电影和游戏文件，可能就不需要作为重点备份对象。相反，我们应该集中精力对那些具有高价值、难以恢复或不可替代的数据进行全面的备份保护。

通过遵循 321 原则并合理分类数据，我们可以在 HomeLab 中建立一个强大的数据堡垒，确保我们的数据和隐私得到有效保障。接下来，我们将详细介绍如何在 NAS 系统中实现这些备份和同步策略，并提供一些实用的技巧和建议。让我们一起探索如何打造一个既安全又高效的数据存储解决方案吧！

---

## 备份策略

以下是为 HomeLab 实施有效备份策略的关键步骤：

1. **确定备份内容**：确定需要备份的数据，包括系统文件、应用程序配置、个人文件等。
2. **选择备份工具**：根据需求和设备选择合适的备份工具，如 Rsync、Duplicati 或其他商业备份解决方案。
3. **制定备份计划**：根据数据的重要性和变动频率制定备份计划，如每天、每周或每月进行备份。
4. **配置备份目标**：为备份数据选择合适的存储介质和位置，确保遵循 3-2-1 备份原则。
5. **监控和验证备份**：定期检查备份是否成功完成，并验证备份数据的完整性。
6. **测试数据恢复**：定期进行数据恢复测试，确保在实际需要时能够快速恢复数据。

## 确定备份内容

### 数据分类

在 **HomeLab** 环境中, 数据文件通常可以分为已下几类:

#### 系统与配置

这些文件主要用于系统恢复和环境重建，确保 HomeLab 稳定运行，避免因系统故障导致数据丢失或服务不可用。

1. **系统镜像**：
   - 树莓派、开发板、NAS（如 DSM）、虚拟机镜像（KVM）等;
   - 操作系统完整备份（如 OpenWrt 路由系统、Ubuntu Server）;
2. **配置文件**：
   - **服务配置**：例如 docker-compose.yml 文件、Nginx Proxy Manager 配置等;
   - **网络配置**：WireGuard 配置、Surge 配置、DNS 记录等;
   - **开发相关的配置**: IntelliJ IDEA 配置和插件、Maven 配置、Obsidian 配置和插件等;
   - **系统个性化设置**：macOS/Linux 上的 dotfiles（zsh、vim、tmux、ssh 配置）;

#### 数据类

数据类文件包括所有由个人用户生成或存储的数据，这些文件通常是不可替代的，必须重点保护。

1. **个人与家庭数据**：

   - 家庭照片、视频、个人记录（笔记、电子书库）;
   - 重要文档：工作文件、简历、报表、手稿等。

2. **工作与代码存储**：

   - 源代码、项目文档、开发环境数据。
   - Git 仓库备份（可在本地或远程镜像保存）。

3. **数据库与应用数据**：
   - 自托管服务的数据备份，如 Bitwarden 数据库、Home Assistant 配置。
   - MySQL、PostgreSQL、MongoDB 等数据库定期导出和备份;

#### 媒体与资源

主要包括视频、音乐、电子书等非独一无二的资源，备份时可降低优先级，主要确保可访问性。

1. **影视资源**：电影、电视剧、综艺节目等;

2. **音乐资源**：NAS 中的无损音乐;

3. **电子书与学习资料**：课程资源、PDF 文件、技术书籍等;

#### 虚拟机与容器备份

对于运行在 HomeLab 中的虚拟机（VM）和容器化应用，备份镜像和数据是重建服务的关键。

1. **虚拟机备份**：KVM/QEMU、VMware ESXi、Proxmox VE 虚拟机镜像;

2. **容器备份**：Docker 镜像与容器卷（Volume）数据;

   参考:

   - [4 Easy Ways to Backup Docker Volumes](https://dev.to/code42cate/4-easy-ways-to-backup-docker-volumes-cjg)
   - [docker-volume-backup](https://github.com/offen/docker-volume-backup)
   - [Backup and Restore of Docker Volumes: A Step-by-Step Guide](https://osmosys.co/blog/backup-and-restore-of-docker-volumes-a-step-by-step-guide/)
   - [Back Up and Share Docker Volumes with This Extension](https://www.docker.com/blog/back-up-and-share-docker-volumes-with-this-extension/)

#### 自动化脚本与工具

在 HomeLab 环境中，很多任务依赖自动化脚本和工具，备份这些内容可以节省重建时间.

1. **自动化脚本**：Shell 脚本、Ansible Playbook、Python 脚本等自动化任务;
2. **工具配置**：如 CI/CD 流水线配置（GitLab Runner、Jenkins）, 自动备份任务（Cron Job、systemd 定时任务）;

---

### 备份原则

#### 自产内容备份

自产内容是个人资产的精华，它们不仅包含了宝贵的数据，还体现了个人的成长经历。为了确保这些内容的安全，我们需要对其进行细致的分类和备份。

##### 内容类

内容类数据是个人生活中不可或缺的部分，主要包括以下几类：

- **家庭照片**：记录了家庭生活的点点滴滴，是珍贵的回忆。备份时需确保照片的原始质量和分辨率不受损失。
- **个人笔记**：包括学习笔记、日记、灵感记录等，是个人成长和思考的见证。需备份为可检索的格式，以便日后查阅。
- **工作文件与源代码**：工作中产生的文档、报告、项目源代码等，关系到职业发展和工作成果的保存。应采用版本控制工具进行备份，以便追溯历史版本。

##### 配置类

配置类数据虽然不直接产生内容，但它们是保证 HomeLab 硬件和软件正常运行的关键。主要包括：

- **OpenWrt 系统配置**：网络设备的操作系统，备份后可快速恢复网络环境。
- **DSM 配置**：群晖 NAS 的配置文件，包含存储池、共享文件夹、用户权限等重要信息。
- **树莓派系统镜像**：小型服务器或实验设备的操作系统，备份后可快速恢复系统状态。
- **docker-compose.yml**：容器编排文件，确保服务的一致性和可迁移性。
- **macOS 配置文件**：包括系统设置、应用配置等，便于在新设备上快速恢复工作环境。
- **自动化脚本**: 一些自用的小脚本, 包括自启动, 定时任务等启动方式的配置;
- 关键自托管服务的数据, 比如 **Bitwarden 数据**;

以上两类数据均需遵循 **3-2-1 备份原则**，即至少保留三份备份，其中两份存储在不同介质上，一份存放在异地。

#### 珍贵资源

珍贵资源主要是来自互联网或其他渠道的共享资源，比如学习资料、电子书、工具软件、技术文档等。这类资源虽然不具备唯一性，但整理与归档仍然能提升存储效率与可用性。

对于这类数据，可以采取以下备份策略：

- **本地双备份**：在同一存储设备上保存两份副本，以防数据丢失。
- **定期检查**：定期检查备份文件的完整性和可访问性，确保数据安全。

#### 影视文件

影视文件包括电影、电视剧、综艺节目等。这类文件通常体积较大，但并非稀缺资源，重新获取的成本较低。因此，存储时应注重高效率与便利性。

影视文件通常体积较大，备份时需考虑存储空间和访问便捷性。

**存储建议**

1. **网络云盘**：

   - 选择存储空间大、支持在线播放的云盘，如 **115 网盘**、**阿里云盘** 和 **百度网盘**。
   - 使用 **Alist** 等工具，直接挂载云盘资源，提供流媒体播放体验。

2. **本地存储（可选）**：
   - 对于非常喜欢的影视作品，可以使用 NAS 或外接硬盘进行存储，并配合 **Plex**、**Emby** 等媒体服务器管理与播放。
   - 可以设置自动化下载工具（如 **qBittorrent**）定期整理和下载新资源。

---

## 工具选择

在选择备份工具时，主要考虑以下几个标准：

- **支持本地和云备份**：这样可以确保数据在本地和远程都有备份。
- **支持增量备份**：只备份自上次备份以来发生变化的数据，节省时间和存储空间。
- **支持压缩和加密**：保护数据安全的同时，减少存储需求。
- **支持将备份数据分割成一定大小**：这对于远程备份尤其有用，可以提高小文件的上传速度，降低大文件上传失败的风险。
- **支持定时备份**：自动化的定时备份可以确保数据始终是最新的。
- **稳定性和易用性**：工具需要稳定运行，并且用户界面友好，易于操作。

以下是一些常用的备份工具.

### Duplicati

[Duplicati](https://github.com/duplicati/duplicati) 拥有一系列强大的功能，使其成为自助式云备份的首选工具：

![20241229154732_itkz82Ci.webp](https://cdn.dong4j.site/source/image/20241229154732_itkz82Ci.webp)

- **强大的加密**：Duplicati 使用 AES-256 加密（或 GNU 隐私卫士）来在上传之前保护所有数据的安全性。
- **增量备份**：Duplicati 首次上传完整备份，然后存储较小的增量更新，以节省带宽和存储空间。
- **定时备份**：内置的计划程序可以自动保持备份最新。
- **集成应用提醒**：Duplicati 会在备份完成，失败后及时通知你，让你睡个好觉
- **支持多种目标**：加密的备份文件可以传输到 FTP、Cloudfiles、WebDAV、SSH（SFTP）、Amazon S3 等目标。

在备份过程中把小文件打包成块, 块大小可以调到很大, 可以更好地支持小文件不友好的后端, 上传速度更高, 但依赖本地数据库且 CPU 占用高. 恢复文件慢.

---

### Duplicacy

[Duplicacy](https://github.com/gilbertchen/duplicacy): 不依赖本地数据库, 但在服务器上会产生大量小文件, 备份失败率相对更高一些, 速度比较慢. 恢复文件相对较快.

**CLI** 开源且对个人免费, GUI 版本收费.

Duplicacy 目前提供以下存储后端：

- Local disk
- SFTP
- Dropbox
- Amazon S3
- Wasabi
- DigitalOcean Spaces
- Google Cloud Storage
- Microsoft Azure
- Backblaze B2
- Google Drive
- Microsoft OneDrive
- Hubic
- OpenStack Swift
- **WebDAV (under beta testing)**
- pcloud (via WebDAV)
- Box.com (via WebDAV)
- File Fabric by Storage Made Easy

**参考**:

- [Duplicati 助你守护家庭数据](https://nasdaddy.com/how-to-install-duplicati-on-your-nas/)
- [Big Comparison - Borg vs Restic vs Arq 5 vs Duplicacy vs Duplicati](https://forum.duplicati.com/t/big-comparison-borg-vs-restic-vs-arq-5-vs-duplicacy-vs-duplicati/9952)

---

### Kopia

[Kopia](https://github.com/kopia/kopia/) 支持将 [加密](https://kopia.io/docs/features/#end-to-end-zero-knowledge-encryption) 和 [压缩的](https://kopia.io/docs/features/#compression) 快照保存到以下所有 [存储位置](https://kopia.io/docs/features/#save-snapshots-to-cloud-network-or-local-storage)：

- **Amazon S3**以及任何**与 S3 兼容的云存储**
- **Azure Blob 存储**
- **Backblaze B2**
- **Google 云端存储**
- 任何支持**WebDAV 的远程服务器或云存储**
- 任何支持**SFTP 的远程服务器或云存储**
- **Rclone**支持的一些云存储选项
  - 除了 Kopia 之外，还需要下载并设置 Rclone，但之后 Kopia 会管理/运行 Rclone
  - Rclone 支持是实验性的：并非所有 Rclone 支持的云存储产品都经过测试可以与 Kopia 配合使用，有些可能无法与 Kopia 配合使用；Kopia 已经通过 Rclone 测试可以与**Dropbox**、**OneDrive**和**Google Drive 配合使用**
- 本地计算机以及任何网络连接存储或服务器
- 通过设置 [Kopia 存储库服务器来拥有自己的服务器](https://kopia.io/docs/repository-server/)

{% asciinema 299387 %}

---

### 常用工具

<!--

[MicroBin](https://github.com/szabodanika/microbin): 文本和文件共享 Web 应用程序、阅后即焚；

-->

- [Nextcloud](https://nextcloud.com/): 私有云盘，完成 PC 端文件同步、版本控制，提供 web 端、移动端 app；

- [Immich](https://immich.app/): 相册备份、浏览，提供 web 端、移动端 app；

- [Resilio Sync](https://www.resilio.com/sync/): P2P 文件同步，全平台文件同步；

- [Restic](https://github.com/restic/restic)：支持 Linux、Windows、mac 平台，支持备份、恢复和 mount 三种操作，用法简单，后端支持：本地文件夹、SFTP、HTTP rest server、AWS S3、Openstack Swift、BackBlaze B2、微软 Azure Blob 存储、Google Cloud Storage

- [Rsync](https://github.com/RsyncProject/rsync): 一个用的比较多的同步工具，可以简单的实现文件级别的备份。

  有很多人写过相关的文档：

  - [基于 rsync 的数据异地备份方案](http://wiki.lostsummer.love/Docker/基于rsync的数据异地备份方案.html)
  - https://www.cnblogs.com/kevingrace/p/6601088.html
  - https://www.jianshu.com/p/db46c42bf51e
  - https://blog.csdn.net/weixin_41843699/article/details/90246940
  - https://averagelinuxuser.com/backup-and-restore-your-linux-system-with-rsync/

- [Rclone](https://github.com/rclone/rclone): 用于在云存储之间同步文件和目录。该程序支持多种云存储提供商，包括 Google Drive、S3、Dropbox 等，并提供多种功能，如文件同步、加密、压缩等.

  - [利用 Rclone 将 PVE 备份同步到 OneDrive](https://www.dolingou.com/article/rclone-pve-backup-onedrive)
  - [rclone 食用手册，快速上手自动备份，实现 Google Drive 同步网站的备份目录](https://vilark.com/167.html)

- [Mackup](https://github.com/lra/mackup?tab=readme-ov-file): 它可以帮助用户在 macOS 和 Linux 系统中同步应用程序配置文件。Mackup 支持多种存储方案，如 Dropbox、Google Drive 和 iCloud，并支持多种应用程序，如 Git、1Password、Visual Studio Code 等。

  ⚠️Mackup 在 Macos Sonoma 中无法正常工作，因为它不支持首选项的符号链接文件。运行此代码将破坏所有用户首选项，并且无法恢复。有关更多信息，请参阅问题 [#1924](https://github.com/lra/mackup/issues/1924)和 [2035](https://github.com/lra/mackup/issues/2035)。

### 其他工具

- [awesome-sysadmin-Backups](https://github.com/awesome-foss/awesome-sysadmin?tab=readme-ov-file#backups)
- [List of Backup Software](https://github.com/restic/others)

### 参考

- [Synchronization and backup programs - ArchWiki (archlinux.org)](https://wiki.archlinux.org/title/Synchronization_and_backup_programs#Chunk-based_increments)

## 需求整理

基于 HomeLab 数据特性的四象限分类：

![20241229154732_8WFfKaV8.webp](https://cdn.dong4j.site/source/image/20241229154732_8WFfKaV8.webp)

### 重要且敏感

- **象限一：关键的个人数据**
  - **特点**：包含个人敏感信息，对个人生活或工作至关重要;
  - **例子**：家庭照片和视频、个人身份信息、密码以及其他个人隐私相关和认证授权相关的文件(比如 2FA 二维码, 恢复密钥);
- **备份策略**：采用 **3-2-1 备份原则**，加密后备份到云端;

### 重要不敏感

- **象限二：技术配置与项目数据**
  - **特点**：对 HomeLab 的运行至关重要，但不含敏感个人信息;
  - **例子**：系统配置文件、源代码、自动化脚本、虚拟机镜像、docker-compose.yml 等;
- **备份策略**: 采用 **3-2-1 备份原则**，直接备份到云端, 方便直接查看文件内容;

### 不重要但敏感

- **象限三：敏感但非关键数据**
  - **特点**：可能包含敏感信息，但对 HomeLab 的日常运行影响不大;
  - **例子**：旧邮件、非活跃账户信息、不再使用但包含敏感数据的文档;
- **备份策略**：本地冗余备份, 不存储到云端;

### 不重要不敏感

- **象限四：非关键公共数据**
  - **特点**：对 HomeLab 的运行影响较小，且不包含敏感信息;
  - **例子**：下载的影视文件、软件安装包、公共文档、非敏感的网络日志等;
- **备份策略**：本地备份, 备份频率可以较低，仅在需要时备份。

## 逻辑图

Synology 提供了非常多的文件同步与备份方案, 比如:

- [备份解决方案概览](https://global.download.synology.com/download/Document/Software/WhitePaper/Os/DSM/All/cht/backup_solution_guide_cht.pdf)
- [文件同步与共享方案](https://www.synology.cn/zh-cn/dsm/solution/cross-office_file_sharing)
- [多平台文件备份方案](https://www.synology.cn/zh-cn/dsm/solution/personal_backup)
- [系统, 服务服务器, 文件服务器与虚拟机备份方案](https://www.synology.cn/zh-cn/dsm/feature/active-backup-business/overview)

而我恰巧有 2 台 Synology NAS, 且 Synology 提供的方案完全能够满足我的需求, 所以我的整个数据同步与备份方案全部围绕 Synology NAS 展开:

![Synchronization-and-Backup.drawio.svg](https://cdn.dong4j.site/source/image/Synchronization-and-Backup.drawio.svg)

### 数据同步线

整体使用 **Synology Drive** 套件作为同步工具, Client 与 NAS 之间同步 **Drive** 数据, 2 台 NAS 之间使用 **Synology Drive ShareSync** 和 **Cloud Sync** 同步数据.

### 数据备份线

DS923+ 作为最终备份文件的存储地, 其他设备通过脚本或 Synology 备份套件将数据备份到 DS923+, 然后统一使用 **Hyper Backup** 备份到外置硬盘以及云端.

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
