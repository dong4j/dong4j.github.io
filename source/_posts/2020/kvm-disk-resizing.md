---
title: KVM 虚拟机磁盘容量扩展指南：从文件到文件系统的全面解析
ai:
  - >-
    在这篇博客中，我们深入探讨了如何扩展 KVM
    虚拟机的磁盘容量。我们首先介绍了如何扩展虚拟机的虚拟磁盘文件，然后详细讲解了如何在虚拟机内部扩展分区和文件系统。通过这个指南，您将能够有效地管理虚拟机的存储资源，确保您的虚拟机能够满足不断增长的数据需求。无论您是经验丰富的系统管理员还是虚拟化技术的初学者，这篇文章都将为您提供实用、易于理解的指导。
description: >-
  在这篇博客中，我们深入探讨了如何扩展 KVM
  虚拟机的磁盘容量。我们首先介绍了如何扩展虚拟机的虚拟磁盘文件，然后详细讲解了如何在虚拟机内部扩展分区和文件系统。通过这个指南，您将能够有效地管理虚拟机的存储资源，确保您的虚拟机能够满足不断增长的数据需求。无论您是经验丰富的系统管理员还是虚拟化技术的初学者，这篇文章都将为您提供实用、易于理解的指导。
categories: 'HomeLab:中年男人的快乐源泉'
tags:
  - HomeLab
  - 虚拟机
  - 磁盘容量扩展
  - 虚拟磁盘
  - 分区扩展
  - 文件系统
  - Linux
  - 系统管理
  - 云基础设施
  - 虚拟化技术
abbrlink: 107e2c9
date: 2020-01-10 13:07:29
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## 增加 KVM 虚拟机磁盘容量

在 KVM 中扩展虚拟机磁盘容量分为两步：**扩展虚拟磁盘文件** 和 **扩展虚拟机内的分区和文件系统**。

---

### 第一步：扩展虚拟磁盘文件

#### 1. 确认虚拟磁盘文件路径

使用以下命令查找虚拟机磁盘文件的位置：

```bash
virsh domblklist <虚拟机名称>
```

示例输出：

```
Target     Source
------------------------------------------------
vda        /var/lib/libvirt/images/vm-disk.qcow2
```

记下磁盘文件路径（例如 /var/lib/libvirt/images/vm-disk.qcow2）。

#### 2. 扩展磁盘文件

假设需要将磁盘扩展为 50 GB，根据磁盘格式选择以下命令：

QCOW2 格式磁盘扩展

```bash
qemu-img resize /var/lib/libvirt/images/vm-disk.qcow2 50G
```

RAW 格式磁盘扩展

```bash
qemu-img resize /var/lib/libvirt/images/vm-disk.raw 50G
```

验证磁盘扩展结果

```bash
qemu-img info /var/lib/libvirt/images/vm-disk.qcow2
```

### 第二步：扩展虚拟机内的分区和文件系统

#### 1. 启动虚拟机并登录

启动虚拟机：

```bash
virsh start <虚拟机名称>
```

通过控制台或 SSH 登录虚拟机：

```bash
virsh console <虚拟机名称>
```

#### 2. 检查新增磁盘空间

登录虚拟机后，运行以下命令查看磁盘大小是否更新：

```bash
lsblk
```

示例输出：

```bash
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
vda    254:0    0   50G  0 disk
└─vda1 254:1    0   20G  0 part /
```

- vda 是整个磁盘，vda1 是当前分区。

#### 3. 调整分区

比如我现在的分区:

```bash
➜  ~ fdisk -l
Disk /dev/vda: 100 GiB, 107374182400 bytes, 209715200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2d23b3e0

Device     Boot    Start      End  Sectors  Size Id Type
/dev/vda1           2048 39942143 39940096   19G 83 Linux
/dev/vda2       39944190 41940991  1996802  975M  5 Extended
/dev/vda5       39944192 41940991  1996800  975M 82 Linux swap / Solaris
```


使用 fdisk 扩展分区

1. 启动 fdisk：

    ```bash
    fdisk /dev/vda
    ```

2. 删除原分区（不会丢失数据）：
   - 输入 d 删除分区，依次删除 /dev/vda2 和 /dev/vda1。
3. 重新创建新分区：
   - 输入 n，选择分区类型（默认 primary）。
   - 分区号（如 1）。
   - 起始扇区和终止扇区（默认使用整个磁盘空间）。
4. 保存分区表并退出：
   - 输入 w。
5. 重新加载分区表：

```bash
partprobe /dev/vda
```

#### 4. 扩展文件系统

根据分区的文件系统类型，运行以下命令扩展文件系统：

EXT4 文件系统

```bash
resize2fs /dev/vda1
```

输出:

```bash
resize2fs 1.47.0 (5-Feb-2023)
Filesystem at /dev/vda1 is mounted on /; on-line resizing required
old_desc_blocks = 3, new_desc_blocks = 13
The filesystem on /dev/vda1 is now 26214144 (4k) blocks long.
```

#### 5. 验证扩展结果

运行以下命令检查扩展后的文件系统大小：

```bash
df -h
```

输出：

```bash
文件系统        大小  已用  可用 已用% 挂载点
udev            1.9G     0  1.9G    0% /dev
tmpfs           392M  1.8M  390M    1% /run
/dev/vda1        99G   16G   79G   17% /
tmpfs           2.0G     0  2.0G    0% /dev/shm
tmpfs           5.0M     0  5.0M    0% /run/lock
overlay          99G   16G   79G   17% /var/lib/docker/overlay2...
...
tmpfs           392M     0  392M    0% /run/user/0
```

### 问题

因为原来的 SWAP 分区被删除了, 需要调整 fstab 文件。

```bash
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/vda1 during installation
UUID=1a373f29-fa77-43dd-8d01-e8d848b35b11 /               ext4    errors=remount-ro 0       1
# swap was on /dev/vda5 during installation
#UUID=efbc7849-ed9c-44ef-b34a-c5b8d7e8bab0 none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0
```

将 `swap` 的挂在配置注释掉, 因为我也不打算使用 swap.


## 注意事项

1. 备份数据：扩展磁盘前，请确保虚拟机数据已备份。
2. LVM 情况：
    如果虚拟机使用 LVM，需额外扩展逻辑卷和物理卷： - 扩展物理卷：

    ```bash
    pvresize /dev/vda1
    ```

    - 扩展逻辑卷：

    ```bash
    lvextend -l +100%FREE /dev/mapper/volume-group-logical-volume
    ```

    - 扩展文件系统：

    ```bash
    resize2fs /dev/mapper/volume-group-logical-volume
    ```

3. 确认文件系统类型：不同文件系统（如 EXT4、XFS）使用不同的扩展命令。

## 总结

扩展 KVM 虚拟机磁盘容量涉及两个关键步骤：

1. 使用 qemu-img 扩展磁盘文件。
2. 登录虚拟机，调整分区和文件系统。
