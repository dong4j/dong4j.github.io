---
title: HomeLab数据备份：打造坚实的数据安全防线
ai: true
swiper_index: 7
top_group_index: 7
tags:
  - HomeLab
categories:
  - HomeLab
cover: https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_oUxZug2L.webp
abbrlink: 84ce
date: 2020-04-25 00:00:00
main_color:
---

![/images/cover/20241229154732_oUxZug2L.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_oUxZug2L.webp)
[封面来源: Unsplash-Kvistholt Photography](https://unsplash.com/photos/photo-of-computer-cables-oZPwn40zCK4)

## 数据备份

备份是 **Homelab** 必不可少的一部分，按照不同的系统架构，备份大致有下列几类：

- 文件级别的备份：直接在应用所属宿主机上运行定时任务，增量或者全量将文件复制到其他远程位置，可以使用 **Synologo Drive**, **Rsync**, **Rclone**, **Restic** 等这类工具进行备份;
- 应用级别的备份：通过应用完成备份，例如 Gitlab, Portainer, 1Panle, Home Assistant 等自带的备份功能，可以将用户数据和数据库等数据一起备份到远程位置，
- 系统级别的备份：例如 macOS 自带的备份（Time Machine），树莓派和 OpenWrt 的全系统备份, OpenWrt, DSM 等自带的系统级备份功能, 或者其他软件实现的全盘备份(比如 rsync + dd 命名)。
- 虚拟化备份：在有虚拟化的时候，整个操作系统等于多个文件，所以只需要将此文件备份便能实现整个虚拟机的备份，比如 **Parallels Desktop** 的 **\*.pvm** 虚拟机文件, UTM 的 **\*.utm** 虚拟机文件, KVM 的虚拟机文件等;
- 存储卷备份: 一种 **完整备份策略**，会将整个存储卷（文件系统）作为一个单元进行备份, 比如 [**Synology Snapshot Replication**](https://www.synology.cn/zh-cn/dsm/feature/snapshot_replication);
- RAID (磁盘冗余阵列)：虽然 RAID 不能算作一种备份方式, 但是提供了一定程度的数据冗余与可靠性, 比如我的 2 台 NAS 都通过 SSD 组了 RAID1, 确保在一块 SSD 坏了的情况下系统仍然能够运行.

> 数据备份这一章我会先从各个服务器开始总结, 因为最后备份文件都会汇总到 DS923+ 上, 所以会最后说明 Synology NAS 的备份.

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

---

### 树莓派备份

树莓派设备有 4 个:

- Raspberry Pi Zero 2 W
- Raspberry Pi 4B
- Raspberry Pi 5B \* 2

#### TF 复制

在 Linux 系统中一键备份树莓派系统 SD 卡的脚本 脚本文件来源: https://blog.csdn.net/qingtian11112/article/details/99825257

**使用方法：**

step1：下载脚本文件 `rpi-backup.sh` 到 Linux 系统中
step2：把需要备份的 SD 卡插入 Linux 系统中，用 df -h 命令查询下 SD 卡对应的设备名。
step3：进入脚本文件 `rpi-backup.sh` 所在目录，只需要下面两行命令即可完成 SD 卡备份，最终 img 文件会生成在 `~/backupimg/` 文件夹下:

```bash
# 赋可执行权限
sudo chmod +x rpi-backup.sh
# 第一个参数是树莓派 SD 卡 /boot 分区的设备名，第二个参数是 / 分区的设备名, 视情况修改
./rpi-backup.sh /dev/sdb1 /dev/sdb2
```

#### dd 命令

```bash
# 1.使用 dd 复制文件到 NAS(提前使用 NFS 将 NAS 挂载到树莓派上)
sudo dd if=/dev/mmcblk0 of=/mnt/ds923/remote/PI4/20240730.img bs=1MB status=progress
# 2.使用 PiShrink.sh 压缩文件 (在 /mnt/lankxin.u/Developer 目录下执行)
sudo ./pishrink.sh /mnt/ds923/remote/PI4/20240816.img /mnt/ds923/remote/PI4/20240816-lite.img
```

> 上述方式在树莓派上执行, 需要提前挂载 NAS 到本地.

#### 通过网络复制

```bash
# 将 远程的 /dev/mmcblk1 备份到 本机的 backup_image.img
ssh root@<ip_board_to_be_backup> "dd if=/dev/mmcblk1" | dd of=backup_image.img bs=1M status=progress
```

> 此方法同样适用 eMMC 备份, 出处: [**HOW TO CLONE EMMC (NANOPI NEO CORE)**](https://forum.armbian.com/topic/11404-how-to-clone-emmc-nanopi-neo-core/).

上述方式都会生成一个 img 文件, 后续如果要恢复, 可以使用像 **balenaEtcher** 这类工具将最新的 img 文件烧录到 SD 卡上.

---

使用第二种 **dd 命名** 备份树莓派 SD 卡时, 需要在每台树莓派上执行, 且还需要挂载 NAS, 所以我使用另一种方式集中化处理的方式.

有 2 种方式:

1. 直接在 NAS 上通过网络复制 SD 卡, 然后使用 **pishrink.sh** 减小镜像大小;
2. 在其他主机上执行, 使用 **pishrink.sh** 减小镜像大小后再自动上传到 DS923+;

第一种方案的问题是 **pishrink.sh** 无法直接在 DS923+ 上运行, 为了避免安装 **pishrink.sh** 的依赖对 NAS 有影响, 我的计划是在 M920x 上执行整个流程, 最后将压缩后的镜像上传到 DS923+ 上.

所以第一步就是在 M920x 上安装依赖并下载脚本:

```bash
sudo apt update && sudo apt install -y wget parted gzip pigz xz-utils udev e2fsprogs
wget https://raw.githubusercontent.com/Drewsif/PiShrink/master/pishrink.sh
chmod +x pishrink.sh
```

下面是自动化脚本:

```bash
#!/bin/bash

# 在 m920x 上备份树莓派的 SD 卡
# 用法:
# ./backup_sd.sh pi4 /dev/mmcblk1 3
# ./backup_sd.sh zero2w /dev/mmcblk1 3
# ./backup_sd.sh pi51 /dev/mmcblk1 3
# ./backup_sd.sh pi52 /dev/mmcblk1 3

# 检查参数
if [[ $# -lt 3 ]]; then
  echo "Usage: $0 <REMOTE_SD> <REMOTE_DEVICE> <MAX_BACKUPS>"
  echo "Example: $0 raspberrypi /dev/mmcblk1 3"
  exit 1
fi

# 参数赋值
REMOTE_SD="$1"                                  # 树莓派的 SSH 别名
REMOTE_DEVICE="$2"                              # 树莓派的 SD 卡设备
MAX_BACKUPS="$3"                                # NAS 上保留的最大镜像文件数
LOCAL_DIR="/mnt/2.870.ssd/pi.backup"            # 本地备份存放目录
PISHRINK_PATH="${LOCAL_DIR}/pishrink.sh"        # pishrink.sh 脚本路径
NAS_TARGET="/volume4/backups/SD/${REMOTE_SD}"   # NAS 目标目录
TIMESTAMP=$(date "+%Y%m%d%H%M%S")               # 时间戳
LOCAL_IMAGE="$LOCAL_DIR/temp_image_${REMOTE_SD}_$TIMESTAMP.img"
LOCAL_IMAGE_LITE="$LOCAL_DIR/${REMOTE_SD}_lite_$TIMESTAMP.img"
LOG_FILE="$LOCAL_DIR/backup_${REMOTE_SD}_${TIMESTAMP}.log"

# 确保本地备份目录存在
mkdir -p "$LOCAL_DIR"

# 日志记录函数
log_message() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 检查并创建 NAS 目标目录
log_message "Checking and creating NAS target directory if it doesn't exist..."
ssh ds923 "mkdir -p $NAS_TARGET"
if [[ $? -ne 0 ]]; then
  log_message "Error creating NAS target directory. Exiting."
  exit 1
fi
log_message "NAS target directory is ready: $NAS_TARGET"

# 第一步：备份 SD 卡到本地
log_message "Starting SD card backup from $REMOTE_SD..."
ssh $REMOTE_SD "dd if=$REMOTE_DEVICE" | dd of=$LOCAL_IMAGE bs=1M status=progress 2>>"$LOG_FILE"
if [[ $? -ne 0 ]]; then
  log_message "Error during SD card backup. Exiting."
  exit 1
fi
log_message "SD card backup completed: $LOCAL_IMAGE"

# 第二步：压缩镜像文件
log_message "Compressing the backup image using pishrink..."
$PISHRINK_PATH $LOCAL_IMAGE $LOCAL_IMAGE_LITE >>"$LOG_FILE" 2>&1
if [[ $? -ne 0 ]]; then
  log_message "Error during image compression. Exiting."
  exit 1
fi
log_message "Compression completed: $LOCAL_IMAGE_LITE"

# 删除原始未压缩镜像文件
rm -f "$LOCAL_IMAGE"
log_message "Deleted uncompressed backup image: $LOCAL_IMAGE"

# 第三步：上传到 NAS
log_message "Uploading compressed image to NAS..."
rsync -azvP $LOCAL_IMAGE_LITE ds923:$NAS_TARGET >>"$LOG_FILE" 2>&1
if [[ $? -ne 0 ]]; then
  log_message "Error during upload to NAS. Exiting."
  exit 1
fi
log_message "Upload completed: $LOCAL_IMAGE_LITE"

# 删除本地压缩镜像文件
rm -f "$LOCAL_IMAGE_LITE"
log_message "Deleted local compressed backup image: $LOCAL_IMAGE_LITE"

# 第四步：清理 NAS 上多余的备份
ssh ds923 "
  find ${NAS_TARGET} -type f -name '*.img' | sort -r | tail -n +$((MAX_BACKUPS + 1)) | while read -r file; do
    echo \"删除远程的旧备份: \$file\"
    rm -f \"\$file\"
  done
"

echo "备份完成并清理。"

# 清理本地旧日志文件，保留最新 5 份
log_message "Cleaning up old local logs..."
cd "$LOCAL_DIR" && ls -t backup_${REMOTE_SD}_*.log | tail -n +6 | xargs -r rm -f
if [[ $? -ne 0 ]]; then
  log_message "Error during log cleanup."
  exit 1
fi

log_message "Log cleanup completed. Retained latest 5 logs for $REMOTE_SD."

log_message "Backup process finished successfully!"
```

**添加定时任务**:

```bash
# pishrink.sh 需要 root 运行
sudo crontab -e
```

```bash
0 10 * * 7 /mnt/2.870.ssd/pi.backup/backup.sd.sh pi4 /dev/mmcblk0 3
30 10 * * 7 /mnt/2.870.ssd/pi.backup/backup.sd.sh pi51 /dev/mmcblk0 3
0 11 * * 7 /mnt/2.870.ssd/pi.backup/backup.sd.sh pi52 /dev/mmcblk0 3
30 11 * * 7 /mnt/2.870.ssd/pi.backup/backup.sd.sh zero2w /dev/mmcblk0 3
```

---

#### 参考

- [再推荐一个备份树莓派系统的脚本 | 树莓派实验室](https://shumeipai.nxez.com/2020/10/28/backup-the-raspberry-pi-system-as-an-img-file.html)
- [【小白教程】给你的 openwrt 启动盘做个可恢复“快照”。-OPENWRT 专版-恩山无线论坛 - Powered by Discuz!](https://www.right.com.cn/forum/thread-4056313-1-1.html)
- [树莓派系统备份\_51CTO 博客\_树莓派备份](https://blog.51cto.com/wangjichuan/5691223)
- [树莓派安装系统和系统备份还原\_树莓派备份系统镜像\_红色小小螃蟹的博客-CSDN 博客](https://blog.csdn.net/yangcunbiao/article/details/123079103)
- [树莓派备份系统到硬盘 | AllanHao](https://allanhao.com/2022/09/18/2022-09-18-rpi-backup/)
- [GitHub - nanhantianyi/rpi-backup: raspberry pi backup，树莓派系统备份，最小镜像备份](https://github.com/nanhantianyi/rpi-backup)
- [树莓派系统镜像一键备份脚本, 最小化镜像保存-次世代 BUG 池](https://neucrack.com/p/107)
- [GitHub - mghcool/Raspberry-backup: 树莓派备份脚本](https://github.com/mghcool/Raspberry-backup)
- [树莓派备份系统到硬盘 | AllanHao](https://allanhao.com/2022/09/18/2022-09-18-rpi-backup/)
- [克隆树莓 Raspberry Pi Mode4 的 TF 卡\_tf 卡克隆-CSDN 博客](https://blog.csdn.net/zhuoqingjoking97298/article/details/114875177)
- [教你树莓派 4B 的系统备份方法教程大全（全卡+压缩备份） - bongem - 博客园](https://www.cnblogs.com/bongem/p/12312878.html)
- [GitHub - BigBubbleGum/RaspberryBackup: 在 Linux 系统中一键备份树莓派系统 SD 卡的脚本](https://github.com/BigBubbleGum/RaspberryBackup)
- [PiShrink](https://github.com/Drewsif/PiShrink) && [在 macOS 中运行](https://github.com/Drewsif/PiShrink/issues?q=macos)
- [树莓派系统压缩备份——PiShrink 应用实操-CSDN 博客](https://blog.csdn.net/m0_37728676/article/details/108581488)
- [树莓派系统镜像一键备份脚本, 最小化镜像保存-次世代 BUG 池](https://neucrack.com/p/107)
- [树莓派系统镜像备份及压缩至最小的方法\_树莓派压缩备份-CSDN 博客](https://blog.csdn.net/u013735688/article/details/121130583)
- [GitHub - elespec/rpi-backup: RaspberryPi Backup shell](https://github.com/elespec/rpi-backup?tab=readme-ov-file)
- [MAC 上备份（复制）树莓派镜像 | 个人笔记存档](https://www.zhangjc.tech/backup_or_copy_raspberrypi_image_on_mac/)

---

### OpenWrt 备份

OpenWrt 设备有 4 个:

- R2S \* 3
- R5S

#### 自动备份脚本

```bash
#!/bin/bash

# 参数配置
DEST_DIR=$1      # 本地备份目的地目录（例如: /mnt/lankxin.u/backup）
BACKUP_PREFIX=$2 # 备份文件前缀（例如: backup-r2s2）
MAX_BACKUPS=$3   # 最大保留备份数量（例如: 5）
REMOTE_DIR="/volume1/driver/Others/Router/backup/automatic"  # 远程备份目录

# 检查参数是否足够
if [ -z "$DEST_DIR" ] || [ -z "$BACKUP_PREFIX" ] || [ -z "$MAX_BACKUPS" ]; then
  echo "使用方法: $0 <备份目的地目录> <备份文件前缀> <最大备份数量>"
  exit 1
fi

# 备份文件路径
backup_file="/tmp/${BACKUP_PREFIX}-$(date +%F).tar.gz"

# 创建备份
umask go=
sysupgrade -b "$backup_file"
echo "备份文件: ${backup_file}"

# 将备份文件复制到指定目的地目录
cp "$backup_file" "$DEST_DIR"

# 同步到远程服务器
rsync -azvP "$backup_file" "ds218:$REMOTE_DIR"

# 删除临时备份文件
rm -rf /tmp/${BACKUP_PREFIX}-*.tar.gz

# 保留本地备份数量
echo "检查并清理本地备份文件..."
find "${DEST_DIR}" -type f -name "${BACKUP_PREFIX}-*.tar.gz" -printf '%T+ %p\n' | \
sort -r | \
tail -n +$((MAX_BACKUPS + 1)) | \
awk '{print $2}' | \
while read -r file; do
  echo "删除旧的本地备份: $file"
  rm -f "$file"
done

# 保留远程备份数量
echo "检查并清理远程备份文件..."
ssh ds218 "
  find ${REMOTE_DIR} -type f -name '${BACKUP_PREFIX}-*.tar.gz' -printf '%T+ %p\n' | \
  sort -r | \
  tail -n +$((MAX_BACKUPS + 1)) | \
  awk '{print \$2}' | \
  while read -r file; do
    echo \"删除远程的旧备份: \$file\"
    rm -f \"\$file\"
  done
"

echo "备份完成并清理。"

# bark 通知
curl http://192.168.x.x:port/token/系统备份成功\(R2S.U\)\?group\=System.Backup
```

脚本的作用是自动生成备份文件, 然后通过 `rsync` 上传到 NAS 的 `/volume1/driver/Others/Router/backup/automatic` 目录下, 而 `/volume1/driver` 目录后续会被其他套件备份.

> 脚本中的 **ds218** 是一个 ssh 别名, 需要在 .ssh/config 中配置, 且配置免密登录.

然后在 OpenWrt 系统中添加定时任务:

```bash
# 每周 2, 4, 6 早上 5 点执行
0 5 * * 2,4,6 /root/backup.sh /mnt/lankxin.u/backup r2st 5 > /tmp/backup.log 2>&1
```

![20241229154732_GLxIfNZ5.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_GLxIfNZ5.webp)

> crontab 规则:
>
> ```
> * * * * * 需要执行的命令
> - - - - -
> | | | | |
> | | | |  ----- 一星期中的第几天 (0 - 6) (其中0表示星期日)
> | | |  ------- 月份 (1 - 12)
> | |  --------- 一个月中的第几天 (1 - 31)
> |  ----------- 一天中的第几小时 (0 - 23)
>  ------------- 一小时中的第几分钟 (0 - 59)
> ```
>
> 示例:
>
> | 分钟 0-59 | 小时 0-23 | 月内第几天 1-31 | 月份 1-12 | 每周第几天 0-6(0 表示周日) | 效果                                                   |
> | --------- | --------- | --------------- | --------- | -------------------------- | ------------------------------------------------------ |
> | \*        | \*        | \*              | \*        | \*                         | 每分钟执行一次                                         |
> | \*/5      | \*        | \*              | \*        | \*                         | 每五分钟执行一次                                       |
> | 12        | \*/3      | \*              | \*        | \*                         | 每过 3 个小时后的第 12 分钟执行一次                    |
> | 57        | 11        | 15              | 1,6,12    | \*                         | 在 1、6、12 月中的 15 号的 11 点 57 分各执行一次       |
> | 25        | 6         | \*              | \*        | 1-5                        | 工作日期间（周 1 到周 5），每天早上 6 点 25 分执行一次 |
> | 0         | 0         | 4,12,26         | \*        | \*                         | 每月的第 4、12、26 日，晚上 12 点执行一次              |

#### WebUI 手动备份

在修改了配置后及时手动执行备份操作:

![20241229154732_mNVD9sKb.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_mNVD9sKb.webp)

下载后的备份文件我会直接扔到 **~Synology/Others/Router/backup/manual** 以同步到 NAS 的 **driver** 目录, 而此目录最终会被其他套件备份.

### eMMC 备份

eMMC 设备有 4 个:

- H28K (Armbian)
- HB1 Box (Armbian)
- NanoPi NEO4 \* 2 (Ubuntu/Debian)

首先需要确认 eMMC 的分区:

```bash
➜  ~ fdisk -l

Disk /dev/mmcblk1: 29.13 GiB, 31272730624 bytes, 61079552 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: B6CA70E8-D82F-BA42-AFC0-6A872D21A362

Device          Start      End  Sectors  Size Type
/dev/mmcblk1p1  32768   557055   524288  256M Linux extended boot
/dev/mmcblk1p2 557056 60456959 59899904 28.6G Linux filesystem
```

可以确认分区为 **/dev/mmcblk1**, 然后使用下面的命令构建镜像:

```bash
# 将 远程的 /dev/mmcblk1 备份到 本机的 backup_image.img
ssh root@<ip_board_to_be_backup> "dd if=/dev/mmcblk1" | dd of=backup_image.img bs=1M status=progress
```

![20241229154732_ZllEgtpX.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ZllEgtpX.webp)

因为我有多个 eMMC 设备, 所以写了一个自动化脚本执行:

```bash
#!/bin/bash

# 脚本目录
SCRIPT_DIR=$(dirname "$0")
# 日志文件路径
LOG_FILE="$SCRIPT_DIR/backup_emmc.log"

# 将所有输出重定向到日志文件
exec > >(tee -a "$LOG_FILE") 2>&1

# =========================
# 自动化 eMMC 备份脚本
# =========================

# 参数
REMOTE_EMMC="$1"          # 远程主机(.ssh/config 别名, 免密登录)
REMOTE_DEVICE="$2"        # 远程备份的设备路径 (如 /dev/mmcblk1)
BACKUP_DIR="$3"           # 本地备份存储路径 (如 /path/to/backups)
BACKUP_PREFIX="$4"        # 备份文件名前缀 (如 backup_emmc)
MAX_BACKUPS="$5"          # 最大保留备份数量 (如 5)

# 检查参数是否完整
if [ -z "$REMOTE_EMMC" ] || [ -z "$REMOTE_DEVICE" ] || [ -z "$BACKUP_DIR" ] || [ -z "$BACKUP_PREFIX" ] || [ -z "$MAX_BACKUPS" ]; then
  echo "Usage: $0 <REMOTE_EMMC> <REMOTE_DEVICE> <BACKUP_DIR> <BACKUP_PREFIX> <MAX_BACKUPS>"
  exit 1
fi

# 创建备份目录（如果不存在）
mkdir -p "$BACKUP_DIR"

# 获取当前时间戳
TIMESTAMP=$(date +%Y%m%d%H%M%S)

# 本地备份文件路径
BACKUP_FILE="$BACKUP_DIR/${BACKUP_PREFIX}_${TIMESTAMP}.img"

# 开始备份
echo "Starting backup from $REMOTE_EMMC:$REMOTE_DEVICE to $BACKUP_FILE"
ssh ${REMOTE_EMMC} "dd if=${REMOTE_DEVICE} bs=1M" | dd of=$BACKUP_FILE bs=1M status=progress

# 检查备份是否成功
if [ $? -eq 0 ]; then
  echo "Backup completed: $BACKUP_FILE"
else
  echo "Backup failed!"
  exit 1
fi

# 删除多余的备份文件
echo "Cleaning up old backups..."
find "$BACKUP_DIR" -type f -name "${BACKUP_PREFIX}_*.img" -printf '%T+ %p\n' | \
sort -r | \
tail -n +$((MAX_BACKUPS + 1)) | \
awk '{print $2}' | \
while read -r file; do
  echo "Deleting old backup: $file"
  rm -f "$file"
done

echo "Backup process completed."
```

将上述脚本保存为 `backup.emmc.sh`，并赋予执行权限：

```bash
chmod +x backup.emmc.sh
```

运行脚本:

```bash
./backup.emmc.sh <REMOTE_EMMC> <REMOTE_DEVICE> <BACKUP_DIR> <BACKUP_PREFIX> <MAX_BACKUPS>
```

- REMOTE_EMMC：要备份的设备的别名, 需要在 `.ssh/config` 配置, 并在设备端开启免密登录;
- REMOTE_DEVICE：需要备份的设备路径（如 /dev/mmcblk1）;
- BACKUP_DIR：本地存储备份文件的目录;
- BACKUP_PREFIX：备份文件名前缀（如 backup_emmc）;
- MAX_BACKUPS：保留的最大备份数量（如 5）。

示例:

```bash
# 备份到当前目录下
./backup.emmc.sh h28k /dev/mmcblk1 . h28k 5
```

添加定时任务:

```bash
sudo crontab -e
```

每天凌晨 2 点执行:

```bash
0 2 * * * /path/to/backup.emmc.sh <REMOTE_EMMC> <REMOTE_DEVICE> <BACKUP_DIR> <BACKUP_PREFIX> <MAX_BACKUPS>
```

> 如果是在 NAS 上执行, 直接使用 WebUI 设置定时任务即可:
>
> 比如备份脚本路径: `/volume4/backups/eMMC/backup.emmc.sh`, 设置任务计划:
>
> ![20241229154732_km0ameIh.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_km0ameIh.webp)
>
> ```bash
> /volume4/backups/eMMC/backup.emmc.sh h28k /dev/mmcblk1 /volume4/backups/eMMC h28k 5
> ```

---

### Linux 备份

Linux 主机只包括 M920x 和 Station 2 个 Ubuntu Server 这种相对来说较大的主机, 其他的比如 Armbian 等衍生的 Linux 系统不包含在内.

#### M920x 备份

在 [Synology NAS](#物理服务器备份) 一节中会使用 **Active Backup for Business** 的 [物理服务器备份功能](#物理服务器备份) 备份 M920x 的系统盘.

M920x 是作为 Docker 主力机使用, 所以上面启动了大量的 Docker 容器以及少量 KVM 虚拟机, 这部分数据我打算使用 `rsync` 增量备份到另一块 SSD 上(M920x 有 4 块独立的 1T SSD):

```bash
#!/bin/bash

# 定义源目录和目标目录
SOURCE_DIR_DOCKER="/mnt/3.860.ssd/docker"
SOURCE_DIR_KVM="/mnt/3.860.ssd/kvm"
SOURCE_DIR_KVM_CONFIG="/etc/libvirt"  # 假设 KVM 配置文件在这里，如果不对需要修改
DEST_DIR="/mnt/1.870.ssd"
LOG_DIR="/mnt/1.870.ssd/backup_logs"  # 定义日志目录
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")
LOG_FILE="$LOG_DIR/rsync_backup_$TIMESTAMP.log"

# 增量备份 Docker 目录, 不使用 --progress 避免产生大量日志
echo "Starting backup of Docker directory..." >> "$LOG_FILE"
rsync -avh --delete "$SOURCE_DIR_DOCKER" "$DEST_DIR" >> "$LOG_FILE" 2>&1

# 增量备份 KVM 目录
echo "Starting backup of KVM directory..." >> "$LOG_FILE"
rsync -avh --progress --delete "$SOURCE_DIR_KVM" "$DEST_DIR" >> "$LOG_FILE" 2>&1

# 增量备份 KVM 配置文件
echo "Starting backup of KVM configuration files..." >> "$LOG_FILE"
rsync -avh --progress --delete "$SOURCE_DIR_KVM_CONFIG" "$DEST_DIR" >> "$LOG_FILE" 2>&1

# 输出完成信息
echo "Backup completed on $(date)" >> "$LOG_FILE"

# 保留最近的 5 个日志文件，删除旧日志
echo "Cleaning up old log files..." >> "$LOG_FILE"
find "$LOG_DIR" -type f -name "rsync_backup_*.log" | sort -r | tail -n +6 | xargs -r rm -f

# 确认完成
echo "Cleanup completed. Latest 5 logs are kept." >> "$LOG_FILE"
```

此脚本将 **docker**, **KVM 虚拟机文件** 以及 **KVM 的配置文件** 从 `/mnt/3.860.ssd` 备份到 `/mnt/1.870.ssd` 目录下, 将上述脚本重命名为 `backup.sh` 并赋予执行权限, 然后添加到定时任务中:

```bash
# 必须使用 sudo 运行
sudo crontab -e

# 每天凌晨 2 点执行
0 2 * * * /mnt/1.870.ssd/backup.sh
```

> M920x 除了系统盘备份, `/mnt/3.860.ssd` 也会通过 **Active Backup for Business** 备份到 NAS 上, 相当于 2 份备份, 最后一份云端备份由 DS923+ 统一处理.

---

#### Station

Station 作为 AI 实验室使用, 目前只有 2 个 1T 的 m.2 固态, 模型数据和系统是分开的, 像 LLM 这些比较容易在网上获取的数据就没有必要备份了, 所以只需要备份系统盘即可.

在 [Synology NAS](#物理服务器备份) 一节中会使用 **Active Backup for Business** 的 [物理服务器备份功能](#物理服务器备份) 备份 Station 的系统盘.

### macOS 备份

macOS 设备有 3 台:

- Macbook Pro Apple M1 Max
- Mac mini 2018
- Mac mini Apple M2

MBP 是主力机, 其他两台放家里当服务器用, 因为 **AirPort Time Capsule** 只有 2T 的空间, 且备份速度较慢, 所以我打算将 MBP 备份到 DS923+ 上, 而其他 2 台 Mac 备份到 **AirPort Time Capsule**.

#### 系统备份

##### 使用 ABB 备份

我将使用 **Active Backup for Business** 的 macOS 备份功能备份整个 MBP, 具体方式看 [**Windows/macOS 备份**](#Windows/macOS-备份).

##### 使用 Time Machine

另外两台 Mac 直接使用 **AirPort Time Capsule 2T** 备份, 只需要在 macOS 上简单配置即可, 而 NAS 同样可以作为 Time Machine 备份 macOS.

首先打开 **启用通过 SMB 进行 Bonjour Time Machine 播送** (AFP 可能对最新的 macOS 存在兼容性问题, 所以推荐使用 SMB 协议):

![20241229154732_qsi93R7k.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_qsi93R7k.webp)

接着设置 Time Machine 的存储目录, 最好新建一个专门用于 Time Machine 的共享目录, 并启用 **索引** 功能, 后续可以直接使用 Mac Finder 搜索启动的文件和内容.

然后在 macOS 上配置 Time Machine:

![20241229154732_XyeMqjkU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_XyeMqjkU.webp)

推荐使用 [TimeMachineEditor](https://tclementdev.com/timemachineeditor/), 可在特定时间启动 Time Machine 中的备份. 比如可以选择间隔或创建其他类型的计划:

![20241229154732_pgJJBWR8.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_pgJJBWR8.webp)

#### 重要文件备份

使用 [Synology Driver Client](#Synology-Drive-Client) 备份.

### iCloud 数据备份

iCloud 比较重要的就 3 个:

- Surge
- Obsidian
- 照片

对于前 2 个目录直接在 Mac mini 2018 上通过脚本自动备份 (`backup.icloud.sh`) :

```bash
#!/bin/bash

# 它会将 iCloud 中的 Surge 和 Obsidian 目录备份到指定的 Synology Drive 路径，并使用 yyyy-mm-dd 格式的日期作为备份文件夹名

# 定义源目录和目标目录
SOURCE_SURGE="$HOME/Library/Mobile Documents/iCloud~com~nssurge~inc/Documents"
SOURCE_OBSIDIAN="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"

# 这是 Synology Drive 的目录, 会自动同步到 NAS
DEST_SURGE="$HOME/Library/CloudStorage/SynologyDrive-driver/macOS/apps/surge"
DEST_OBSIDIAN="$HOME/Library/CloudStorage/SynologyDrive-driver/Obsidian"

# 获取当前日期，格式为 yyyy-mm-dd
DATE=$(date +%F)

# 创建备份文件夹
SURGE_BACKUP="$DEST_SURGE/$DATE"
OBSIDIAN_BACKUP="$DEST_OBSIDIAN/$DATE"

mkdir -p "$SURGE_BACKUP"
mkdir -p "$OBSIDIAN_BACKUP"

# 开始备份
echo "Backing up Surge to $SURGE_BACKUP..."
rsync -avh --delete "$SOURCE_SURGE/" "$SURGE_BACKUP/"

echo "Backing up Obsidian to $OBSIDIAN_BACKUP..."
rsync -avh --delete "$SOURCE_OBSIDIAN/" "$OBSIDIAN_BACKUP/"

# 打印完成信息
echo "Backup completed: $DATE"
```

**使用 launchd 添加定时任务**:

1. 在 `~/Library/LaunchAgents` 目录下创建一个 `.plist` 文件 (`touch ~/Library/LaunchAgents/xx.xxx.icloud-backup.plist`):

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
     <dict>
       <key>Label</key>
       <string>xx.xxx.icloud-backup</string>
       <key>ProgramArguments</key>
       <array>
         <string>~/Library/CloudStorage/SynologyDrive-driver/DevOps/batch-script/shell/backup/backup.icloud.sh</string>
       </array>
       <key>StartCalendarInterval</key>
       <dict>
         <key>Hour</key>
         <integer>3</integer> <!-- 设置每天凌晨 3 点运行 -->
         <key>Minute</key>
         <integer>0</integer>
       </dict>
       <key>StandardOutPath</key>
       <string>/tmp/backup.log</string>
       <key>StandardErrorPath</key>
       <string>/tmp/backup_error.log</string>
       <key>RunAtLoad</key>
       <true/>
     </dict>
   </plist>
   ```

2. 加载 launchd 配置:

   ```bash
   launchctl load ~/Library/LaunchAgents/xx.xxx.icloud-backup.plist
   ```

3. 检查任务状态:

   ```bash
   launchctl list | grep xx.xxx.icloud-backup
   ```

4. 不用后可以卸载:

   ```bash
   launchctl unload ~/Library/LaunchAgents/xx.xxx.icloud-backup.plist
   ```

> 照片我则使用 **Synology Photos Mobile** 备份到 DS218+, 然后再自动同步到 DS923+.

**其他参考:**

- [使用 Docker 为 iCloud 照片生成本地备份](https://ios.sspai.com/post/90641)

---

### Synology NAS

> 之所以先讲其他设备的备份方式, 是因为它们的备份文件最终都会写入到 DS923+ 中, 最后我只需要对 DS923+ 上的文件进行备份即可.

[Synology NAS 提供多种备份方式](https://kb.synology.com/zh-tw/DSM/tutorial/How_to_back_up_your_Synology_NAS#x_anchor_id12), 他们的对比如下:

| 备份目的地          | Hyper Backup | Snapshot Replication | USB Copy | Cloud Sync                          |
| :------------------ | :----------- | :------------------- | :------- | :---------------------------------- |
| 本地共用资料夹      | 可使用       | 可使用               | 不可使用 | 不可使用                            |
| 外接装置(USB)       | 可使用       | 不可使用             | 可使用   | 不可使用                            |
| 另一台 Synology NAS | 可使用       | 可使用               | 不可使用 | 不可使用                            |
| 档案伺服器          | 可使用       | 不可使用             | 不可使用 | 仅支援 WebDAV 及 OpenStack 资料同步 |
| 公有云              | 可使用       | 不可使用             | 不可使用 | 可使用                              |

**功能总结**:

| 应用程式及系统设定备份      | 可使用   | 不可使用                                    | 不可使用   | 不可使用         |
| --------------------------- | -------- | ------------------------------------------- | ---------- | ---------------- |
| 备份及还原效能              | 低       | 高                                          | 中         | 中               |
| 储存空间利用效率            | 中       | 高                                          | 低         | 低               |
| 备份频率                    | 每小时   | 每 5 分钟(共用资料夹) 每 15 分钟(iSCSI LUN) | 热插拔备份 | 于资料变更时同步 |
| 透过 WriteOnce 保护备份资料 | 不可使用 | 仅支援不可变快照                            | 不可使用   | 不可使用         |

根据上面的功能总结, 我计划的备份方案为:

1. 使用 **Snapshot Replication** 在当前 NAS 为重要共享目录创建快照作为第一层保护, 在手残误删文件时能够快速恢复 (**本地备份**);
2. 在 DS218+ 上使用 **Hyper Backup** 将重要的 APP 配置与数据备份到 DS923+, 同时通过 WebDAV 加密备份到云端, 还原颗粒度可以精确到文件级别 (**不同的存储介质备份**);
3. 在 DS218+ 上使用 **Hyper Backup** 将整个系统备份到 DS923+, 同时通过 WebDAV 加密备份到云端, 以便在系统崩溃或损坏时还原 (**不同的存储介质备份**);
4. 在 DS923+ 上使用 **Hyper Backup** 将所有照片和家庭视频通过 rsync 备份到 Mac mini 2018 连接的 **LaCie 8TB d2 Professional** (**不同的存储介质备份**);
5. 在 DS923+ 上使用 **Hyper Backup** 将重要的 APP 配置与数据备份(包括照片和家庭视频)通过 WebDAV 加密备份到云端 (**云端备份**);
6. 在 DS923+ 上使用 **Active Backup for Business** 整机备份 DS218+ (**不同的存储介质备份**);
7. 在 DS923+ 上使用 **Active Backup for Business** 物理服务器备份功能集中备份 M920x 和 Station 整个系统 (**不同的存储介质备份**);
8. 在 DS923+ 上使用 **Active Backup for Business** 文件服务器备份功能集中备份所有开发板和小主机的重要文件 (**不同的存储介质备份**);
9. 在 DS923+ 上使用外置存储定时备份 **Active Backup for Business** 产生的备份文件 (**不同的存储介质备份**);
10. 其他能够安装 **Synology Drive Client** 的主要设备上, 使用 **Drive** 自带的备份功能备份本机上重要的文件 (**不同的存储介质备份**);

---

#### Snapshot Replication

[**Snapshot Replication**](https://www.synology.cn/zh-cn/dsm/feature/snapshot_replication) 是 Synology 提供的一项数据备份功能，它通过利用 Btrfs 文件系统创建时间点副本，实现数据的块级保护和快速恢复。该功能支持多种复制策略，可灵活部署，并配备便捷的管理工具，帮助我们轻松实现数据的备份和灾难恢复.

在系统支持 Btrfs 文件格式的情况下，建议优先考虑使用快照复制作为备份策略。这种方式可以将备份周期设置得非常短，非常适合处理公共文件夹中同时进行大量编辑的情况。
当遇到问题（例如：不慎删除了大量数据，或是不知道进行了哪些修改）需要恢复文件或整个共享文件夹时，你会非常感激不需要按照一天或两天的时间单位来回溯。
优点是：备份周期越短，恢复时只需还原单个文件或整个文件夹，而且还原速度极快。这样的备份方案在紧急情况下能够大大减轻工作压力。

![20241229154732_m09bLGED.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_m09bLGED.webp)

如果在勾选 **高级-让快照可见** 的选项后, 可在文件管理器中查看已保存的快照, 此目录保存在每个创建了快照的共享目录下, 且不会被其他群晖备份套件备份:

![20241229154732_d7mCWrSi.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_d7mCWrSi.webp)

同时还具备 **复制** 功能, 选择远程服务器作为复制目的地时, 比如另一台 NAS, 即可将快照在另一台 NAS **重现**, 不过我一直卡在循环验证的地方, 暂时并未使用此功能:

![20241229154732_smrtCyCo.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_smrtCyCo.webp)

> Snapshot Replication 属于本地备份, 性能和还原速度都是最优的, 且快照占用的磁盘空间较小.

---

#### Hyper Backup

Hyper Backup 是几个备份套件中功能最全的一个, 除了整机备份, 还能单独备份共享目录和 APP 配置, 所以在 [整机备份](#NAS-整机备份) 的基础上, 我还是用它来单独备份个别共享目录和全部的 APP 配置, 这样我可以在不需要整机还原的情况下单独恢复部分数据或 APP:

![20241229154732_bpGajtWl.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_bpGajtWl.webp)

Hyper Backup 备份 APP 时会一并将对应的共享目录一起备份:

![20241229154732_bQkbLo6V.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_bQkbLo6V.webp)

> 在 DS218+ 上 使用此套件将文件备份到 DS923+, 并加密备份到阿里云盘, 相当于有 2 份备份, 且一份在异地.
>
> Hyper Backup 提供了灵活的方法来选择要备份的共享文件夹、文件夹和文件。可以勾选和取消勾选复选框以选择要备份的内容。有 3 种不同的备份选择可供选择：
>
> ![20241229154732_s5fn82qw.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_s5fn82qw.webp)

---

#### Active Backup for Business

[Active Backup for Business](https://www.synology.cn/zh-cn/dsm/feature/active_backup_business#pc) 是一款功能全面的备份与恢复工具，适合需要集中管理多种设备数据的需求. 目前我正在用它来集中备份多个开发板上的重要文件, Linux 整机备份以及 DS218+ 的整机备份.

##### NAS 整机备份

这个将在 [NAS 整机备份](#NAS-整机备份) 一节中详细介绍, 这里就不再赘述了.

##### Windows/macOS 备份

我目前没有 Windows 主机, 根据 [前面的计划](#macOS-备份), MBP 将使用此功能备份(可以享受万兆内网的速度), 另外 2 台 Mac 将使用 [Time Machine](#系统备份) 备份到 **AirPort Time Capsule 2T**.

macOS 需要下载 **Active Backup for Business Agent**, 在 macOS 端主动连接到 DS923+ 的备份服务器:

![20241229154732_ZfhbpwPy.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ZfhbpwPy.webp)

因为是内网连接, 可以不用管这个 SSL 证书问题, 点击 **仍然继续** 即可. 不过为了避免因为证书到期导致备份失败, 最好直接使用 **Active Backup for Business 证书**:

![20241229154732_a4IEYPy8.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_a4IEYPy8.webp)

启用后会自动在 **控制面板-安全性-证书** 中添加相应的证书:

![20241229154732_VnZMCUOS.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VnZMCUOS.webp)

另一个问题是模版匹配:

![20241229154732_6v2p4f48.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_6v2p4f48.webp)

连接服务器时, 因为 **备份目的地格式不受支持** 而添加失败, 其实不是格式不受支持, **是备份的目的地目录不存在**.

![20241229154732_xKF38i63.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_xKF38i63.webp)

在 DS923+ 的 **Active Backup for Business** 修改模版中的 **目的地**, 默认是 **ActiveBackupforBusiness**, 但是我们的 NAS 根本就没有这个共享目录, 所以出错了(也有可能是我以前把这个目录手动删除了 😂).

![20241229154732_svmFryzc.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_svmFryzc.webp)

更换一个存在且可用的共享目录即可, 添加成功后的 **Agent 信息**:

![20241229154732_ZzsyQIdD.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ZzsyQIdD.webp)

**服务端信息**:

![20241229154732_o6QFY31x.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_o6QFY31x.webp)

后续就是根据自己的情况配置任务了.

---

##### 物理服务器备份

Active Backup for Business 目前支持以下 Linux 系统:

- Debian：10, 11, 12
- Ubuntu：16.04, 18.04, 20.04, 22.04, 24.04
- Architechture: x86_64

连接方式也非常简单:

1. 下载官方的 agent, 这个在 **Active Backup for Business - 物理服务器 - 添加设备** 时会告知下载地址;

2. 修改模版(因为我没有这一步导致连接失败): **Active Backup for Business - 设置 - 模版**, 将 **共享文件夹** 修改成存在的共享目录;

3. 在 Linux 上安装 Agent, 可查看 **README** 的操作指南;

4. 安装完成后使用 **abb-cli -c** 连接 NAS:

   ```bash
   $ abb-cli -c
   Enter server address: NAS 的 IP
   Enter username: NAS 的用户名
   Enter password: 对应的密码
   Connecting...
   The SSL certificate of the Synology NAS is not trusted. To learn how to obtain a valid certificate, please have a registered domain by setting up DDNS (http://sy.to/ddns) and applying for Let's Encrypt (http://sy.to/letsencrypt) certificate. Proceed anyway? [y/n](default: y): y
   Enter a 6-digit verification code xxxxx (2FA code)

   Server address: x.x.x.x
   Username: xxx
   Backup type: Server
   Applied template: Default
   Backup destination: backup
   Source type: System volumes backup
   Restoration privilege: admin, xxx, administrators
   Back up by time: Monday, Tuesday, Wednesday, Thursday, Friday Start at: 03:00(Daily/Weekly)
   Retention policy: Advanced retention policy settings
   Backup window: Disabled
   Data transfer compression: Enable
   Data transfer encryption: Enable
   Bandwidth consumption limit: Disabled
   Compression at backup destination: Enable
   Encryption at backup destination: Disabled
   Backup verification: Disabled
   Pre/post script: Disabled
   Confirm authentication? [y/n](default: y):
   Confirming authentication...
   Successfully connected
   ```

最后在 **Active Backup for Business** 端可修改备份计划:

![20241229154732_uMETHAjv.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_uMETHAjv.webp)

如果是整机还原, 需要使用 Linux 恢复媒体创建一个 [可启动的 USB 恢复驱动器](https://kb.synology.com/en-global/DSM/tutorial/How_do_I_create_a_bootable_USB_drive_for_restoring_Linux):

![20241229154732_PS1X66hN.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_PS1X66hN.webp)

如果只是文件还原, 可使用 **Active Backup for Business Portal** 操作:

![20241229154732_upTgftjF.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_upTgftjF.webp)

##### 文件服务器备份

将开发板连接到 **Active Backup for Business Portal** 集中备份:

![20241229154732_BiIE6axw.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_BiIE6axw.webp)

文件服务器备份使用的是 **rsync**, 且最好使用 root 用户, 不然某些目录由于权限问题无法备份:

![20241229154732_Wu9lAdyl.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Wu9lAdyl.webp)

##### 虚拟机备份

**Active Backup for Business** 只能备份 VMware® vSphere™ 与 Microsoft® Hyper-V® 虚拟机, 所以 [M920x 上的 KVM 虚拟机我只能使用脚本备份](#M920x-备份),

而 Synology Virtual Machine Manager 中的虚拟机可以通过快照来备份, 另一种方式是将虚拟机导出到共享目录, 然后使用其他方式备份虚拟机文件.

---

#### Synology Drive Client

Synology Drive Client 在提供同步功能的同时还具备备份功能, 所以我将主力机上的重要文件使用它备份到 NAS 中, 备份的目的地只能选择当前登录用户的 home 目录:

![20241229154732_sF7Y1PVi.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_sF7Y1PVi.webp)

---

#### DSM 系统冗余

首先需要了解一下 **RAID 的几种类型**:

| RAID 类型 | 磁盘数量   | 数据分布          | 冗余能力                     | 性能 | 最少磁盘要求 |
| --------- | ---------- | ----------------- | ---------------------------- | ---- | ------------ |
| RAID 0    | 2+         | 条带化            | 无                           | 最高 | 2            |
| RAID 1    | 2+（偶数） | 镜像              | 完全                         | 一般 | 2            |
| RAID 5    | 3+         | 条带化+奇偶校验   | 单磁盘故障                   | 较高 | 3            |
| RAID 6    | 4+         | 条带化+双奇偶校验 | 双磁盘故障                   | 较高 | 4            |
| RAID 10   | 4+（偶数） | 镜像+条带化       | 单磁盘故障（每个镜像组）     | 高   | 4            |
| RAID 50   | 6+         | RAID 5 + 条带化   | 单磁盘故障（每个 RAID 5 组） | 较高 | 6            |
| RAID 60   | 8+         | RAID 6 + 条带化   | 双磁盘故障（每个 RAID 6 组） | 较高 | 8            |

> 条带化（Striping）是一种数据分配技术，它将数据分割成小块（通常称为“条带”或“块”），并将这些小块分散存储在多个磁盘上。这种技术在 RAID（独立冗余磁盘阵列）配置中非常常见，尤其是在 RAID 0、RAID 5、RAID 6 和 RAID 10 等级别中。

**说明：**

1. **RAID 0**：速度快，但无任何冗余，适合不关心数据丢失的高性能场景。
2. **RAID 1**：安全性高，写入时需要复制数据，磁盘利用率较低。
3. **RAID 5**：提供奇偶校验，容忍单个磁盘故障，适合平衡性能与冗余需求。
4. **RAID 6**：双重奇偶校验，更高安全性，适用于关键数据保护。
5. **RAID 10（1+0）**：兼顾 RAID 1 的安全性和 RAID 0 的速度。
6. **RAID 50/60**：适合企业级大型存储系统，结合 RAID 0 的性能和 RAID 5/6 的冗余。

参考:

- [RAID 类型](https://zh.wikipedia.org/wiki/RAID)
- [Synology-选择 RAID 类型](https://kb.synology.cn/zh-cn/DSM/help/DSM/StorageManager/storage_pool_what_is_raid?version=7)
- [什么是 Synology Hybrid RAID (SHR)](https://kb.synology.cn/zh-cn/DSM/tutorial/What_is_Synology_Hybrid_RAID_SHR)
- [RAID 计算器](https://www.synology.cn/zh-cn/support/RAID_calculator)

除了上述这些常见的 RAID 类型, 一些硬件和软件厂商还会开发自己的磁盘冗余阵列技术或增强技术：

{% details  🪬 其他厂商的磁盘冗余阵列技术或增强技术 %}

1. **ZFS**（Zettabyte File System）

   - **厂商/开发者**：Sun Microsystems（现属于 Oracle）
   - **特点**：
     - ZFS 集文件系统和卷管理器于一体。
     - 提供类似于 RAID 的多种模式（如 RAID-Z、RAID-Z2、RAID-Z3）。
     - 支持快照、数据完整性校验、重复数据删除（deduplication）。
     - 提供动态条带化，无需固定条带大小。
   - **优势**：
     - 高数据完整性：基于校验码检测和修复数据损坏。
     - 灵活性：支持在线扩展存储池。
   - **适用场景**：家庭 NAS（如 TrueNAS）、企业存储、高可靠性备份。

2. **SHR**（Synology Hybrid RAID）

   - **厂商/开发者**：Synology
   - **特点**：

     - 提供类似于 RAID 的功能，但支持**混合硬盘容量**。
     - 自动优化存储利用率，允许用户使用不同大小的硬盘组合。
     - 支持 1 至 2 块硬盘冗余（类似 RAID 5 或 RAID 6）。

   - **优势**：
     - 易用性：面向普通用户，无需手动配置复杂的 RAID 模式。
     - 灵活性：允许随时添加更大容量的硬盘。
   - **适用场景**：Synology NAS 用户，特别是家庭和小型企业存储系统。

3. UnRAID

   - **厂商/开发者**：Lime Technology
   - **特点**：
     - 与传统 RAID 不同，UnRAID 不做条带化或镜像，而是将数据独立存储在每块硬盘上。
     - 提供一个专用的**奇偶校验盘**用于数据冗余。
     - 支持灵活扩展，允许随时增加硬盘并使用不同容量的硬盘。​
   - **优势**：
     - 数据独立性：即使多块硬盘损坏，未损坏的硬盘数据仍可直接读取。
     - 灵活性：无需所有硬盘容量一致。
   - **适用场景**：家庭媒体服务器、大容量存储需求。

4. HP’s ADG (Advanced Data Guarding)

   - **厂商/开发者**：Hewlett-Packard (HP)
   - **特点**：
     - 类似于 RAID 6，提供双重奇偶校验。
     - 可允许两块磁盘同时故障而不丢失数据。
     - 专为 HP 的企业级存储系统设计。
   - **优势**：
     - 更高的容错性。
     - 专为大型企业的高可用性环境而设计。
   - **适用场景**：企业存储系统（如 HP ProLiant 服务器）。

5. NetApp RAID-DP

   - **厂商/开发者**：NetApp
   - **特点**：
     - 基于 RAID 4（单奇偶校验）改进，提供双奇偶校验（类似 RAID 6）。
     - 专为企业级存储系统和大规模部署优化。
   - **优势**：

     - 提高容错能力，可容忍两块磁盘同时故障。
     - 集成在 NetApp 的 Data ONTAP 操作系统中，支持高效快照和备份。

   - **适用场景**：大规模企业存储和虚拟化环境。

6. VMware VSAN（Virtual SAN）

   - **厂商/开发者**：VMware
   - **特点**：
     - 软件定义存储，将多个服务器的本地存储整合成共享存储池。
     - 提供分布式数据冗余，支持 RAID 1、RAID 5 和 RAID 6 级别的保护。
     - 数据跨节点分布，支持企业级高可用性。
   - **优势**：
     - 高可扩展性，适合超融合基础架构。
     - 与 VMware 环境深度集成。
   - **适用场景**：虚拟化和云计算环境。

7. Dell EMC VxRail

   - **厂商/开发者**：Dell EMC
   - **特点**：
     - VxRail 是 Dell EMC 提供的超融合基础架构，整合计算、存储和网络。
     - 存储采用分布式冗余技术，不直接使用传统 RAID，而是基于对象的存储分布。
   - **优势**：
     - 高扩展性：节点扩展灵活，适合云和企业级存储。
     - 提供企业级容错和冗余。
   - **适用场景**：云计算、超融合数据中心。

8. Windows Storage Spaces

   - **厂商/开发者**：Microsoft
   - **特点**：
     - 提供类似于 RAID 的功能，如条带化（RAID 0）、镜像（RAID 1）和奇偶校验（RAID 5）。
     - 支持混合硬盘容量，允许动态扩展存储池。
   - **优势**：
     - 集成在 Windows 系统中，部署成本低。
     - 易于配置，适合中小型企业和个人用户。
   - **适用场景**：Windows Server 或家庭 Windows 系统上的存储管理。

9. Ceph

   - **厂商/开发者**：社区驱动（开源）
   - **特点**：
     - 分布式存储系统，不依赖传统 RAID。
     - 数据存储在多个节点上，提供高可用性和故障恢复能力。
     - 基于对象存储，支持动态扩展。
   - **优势**：
     - 高扩展性和灵活性。
     - 无需专用硬件，适合大型分布式存储系统。
   - **适用场景**：云存储、超大规模企业环境。

10. IBM GPFS（General Parallel File System）
    - **厂商/开发者**：IBM
    - **特点**：
      - 提供分布式文件系统和并行访问功能。
      - 数据分布在多个磁盘或节点上，提供高可靠性和高性能。
      - 支持自动故障检测和数据修复。
    - **优势**：
      - 高性能和高可靠性。
      - 适合大规模、高吞吐量的存储需求。
    - **适用场景**：企业数据中心、大数据分析、高性能计算（HPC）。

**总结**

现代厂商开发的磁盘冗余技术大多是对传统 RAID 的优化，提供更强的灵活性、扩展性和容错能力。这些技术主要服务于以下需求：

- **家庭级存储**：如 Synology SHR、UnRAID、ZFS;
- **企业级存储**：如 NetApp RAID-DP、Dell EMC VxRail、Ceph;
- **超融合与分布式存储**：如 VMware VSAN、IBM GPFS;

{% enddetails %}

> 因为我的 **DS218+** 只有 2 个盘位, 而 **DS923+** 也只支持 2 块 M.2 的 SSD, 所以索性将他们全部更换为 SSD 并组 RAID1, 至少能保证坏了一块 SSD 的情况下系统仍然能够运行.

---

#### DSM 配置备份

Synology 提供 [DSM 的配置备份](https://kb.synology.cn/zh-cn/DSM/help/DSM/AdminCenter/system_configbackup?version=7), 可以自动备份到你的 Synology 账户中, 且可手动导出备份到本地(**目前在寻找可自动导出备份文件的方法**):

![20241229154732_zlEIvRtE.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_zlEIvRtE.webp)

#### NAS 整机备份

[Hyper Backup](https://www.synology.cn/dsm/feature/hyper_backup) 和 [Active Backup for Business](https://www.synology.cn/zh-cn/dsm/feature/active_backup_business#pc) 都提供了 NAS 整机备份的功能, 它们的区别为:

- 备份方式不同:
  - Active Backup for Business 是作为备份 **目的地** 端的套件(A 备份到 B, 在 B 端操作);
  - Hyper Backup 是作为 **备份源** 为角色的套件(A 备份到 B, 在 A 端操作);
- 还原方式不同:
  - 整机还原([还原步骤](https://kb.synology.cn/zh-cn/DSM/help/HyperBackup/restore?version=7)):
    - 两者都可以;
  - 部分数据还原:
    - Active Backup for Business 直接在远程 NAS 上操作;
    - Hyper Backup 只能在本机操作;
- 数据查看方式不同:
  - Active Backup for Business 能够通过 **Active Backup for Business Portal** 查看共享目录下的任何文件;
  - Hyper Backup 无法友好的查看备份的文件目录与内容;
- 备份数据格式不同:
  - Active Backup for Business 会将 NAS 系统备份为 数据盘.img 和 系统.img 2 个镜像文件, 只能通过 **Active Backup for Business Portal** 查看内部数据;
  - Hyper Backup 备份的是压缩文件.

> 官方推荐的整机备份方式是 **Hyper Backup**, 可以备份 NAS 上的 **共享文件夹**、**应用程序设置** 和 **系统配置**，从而确保整机数据与环境一致性, 以便在系统出现问题需要重装或彻底坏掉后能够恢复到另一台 NAS 上, 但是我会同时使用 **Active Backup for Business** 备份全部的共享数据文件, 以便在数据被误删后能够单独恢复.

---

##### Hyper Backup

在 DS218+ 上创建整机备份任务:

![20241229154732_VUIY1Q8F.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VUIY1Q8F.webp)

任务创建成功后, 可在远端 NAS(DS923+) 的 **Hyper Backup Vault** 查看备份任务:

![20241229154732_U8AJ0dt9.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_U8AJ0dt9.webp)

##### Active Backup for Business

在 DS923+ 上创建整机备份任务(需要在 DS218+ 上安装 Agent):

![20241229154732_haQLMkXU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_haQLMkXU.webp)

备份完成后可通过 **Active Backup for Business Portal** 查看备份的数据:

![20241229154732_Vv4y25dU.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_Vv4y25dU.webp)

> ##### 还原整个系统
>
> **对于已完成首次设置的 Synology NAS 设备**:
>
> 1. 单击 **还原**，然后选择 **整个系统**。您将被重定向到 **控制面板**。
> 2. 单击 **还原系统** 并选择存储备份数据的还原来源。
> 3. 按向导完成还原。
>
> **对于尚未完成首次设置的 Synology NAS 设备**:
>
> 1. 在欢迎页面上单击 **还原系统**。
> 2. 选择存储备份数据的还原来源。
> 3. 按向导完成还原。

![20241229154732_VC4tJUte.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_VC4tJUte.webp)

---

#### 参考

- [備份 Synology NAS 多種解決方案比較](https://www.cjkuo.net/synology-nas-backup/)
- [当你拥有了第二台 NAS，这是你需要了解的数据迁移和同步方式-少数派](https://sspai.com/post/81509)
- [担心群晖硬盘损坏丢失数据？不来试试 Hyper Backup ？](https://post.smzdm.com/p/a8pe67kn/)
- [群晖 NAS 云盘备份神器，使用 Cloud Sync 打通 NAS 与无缝网盘同步](https://post.smzdm.com/p/all247z8/)
- [Synology-企业应用篇](https://post.smzdm.com/p/az59k63n/)
- [群晖 DSM6.1 数据安全三猛将 → 同步、备份、快照，+新兵 USB Copy2.0](https://post.smzdm.com/p/545304/)
- [Synology-Backup Solution Guide 2023](https://cndl.synology.cn/download/Document/Software/WhitePaper/Package/ActiveBackup/All/enu/Synology_Backup_Solution_Guide_2023_enu.pdf)
- [Synology-備份解決方案概覽](https://global.download.synology.com/download/Document/Software/WhitePaper/Os/DSM/All/cht/backup_solution_guide_cht.pdf)

### 冗余备份

因为所有的备份文件都会汇总到 DS923+ 上, 所以最后一道保险就是为 DS923+ 上的文件创建冗余备份.

正好有一个 8TB 的 **LaCie d2 Professional** 闲置, 可以直接用作 DS923+ 的冗余备份.

**LaCie d2 Professional** 通过 type-c 连接到了我的 Mac mini 2018, 具有 10Gb/s 的速度, 在 NAS 上使用 **Hyper Backup** 套件, 合适的远程连接有 rsync 和 WebDAV 2 种, 尝试了在 Mac mini 2018 上分别部署 Rsync Server 和 WebDAV 后, 最终选择了第一种方式.

首先需要了解一下 rsync 基本参数:

```
一般做增量同步时，直接使用 -avz 即可。

rsync参数：
-a           #归档模式传输, 等于-tropgDl
-v           #详细模式输出, 打印速率, 文件数量等。一般默认显示 info=all1，添加 -v 后会显示 info=all2
-z           #传输时进行压缩以提高效率

-r           #递归传输目录及子目录，即目录下得所有目录都同样传输。
-t           #保持文件时间信息
-o           #保持文件属主信息
-p           #保持文件权限
-g           #保持文件属组信息
-l           #保留软连接
-P           #显示同步的过程及传输时的进度等信息
-D           #保持设备文件信息
-L           #保留软连接指向的目标文件
-e           #使用的信道协议,指定替代rsh的shell程序  ssh
--exclude=PATTERN   #指定排除不需要传输的文件模式
--exclude-from=file #文件名所在的目录文件
--bwlimit=100       #限速传输
--partial           #断点续传
--delete            #让目标目录和源目录数据保持一致，当 src 删除某个文件时，dst 会同步删除，默认是仅传输新增的数据，不会删除远端存在但本端不存在的文件
--debug=all4        #开启最高级别的debug，all 表示显示所有信息，4 为 loglevel 的最高级别。
```

基础命令

```
rsync -avz --delete SRC DST
```

**参考资料**:

- https://ss64.com/bash/rsync_options.html

- [Linux 下 Rsync 和 Tar 增量备份梳理](https://www.cnblogs.com/kevingrace/p/6601088.html)

- [备份数据的重要性以及 rsync 的基本使用](https://zhuanlan.zhihu.com/p/88338737)

#### macOS 上搭建 Rsync Server

```bash
$ tree
.
├── rsync													# 二进制文件
├── rsyncd.conf.txt								# rsync 的配置
├── rsyncd.log										# rsync 日志
├── rsyncd.secrets.txt						# 密钥
├── rsyncd_nas.log								# 同步日志
└── start													# 启动脚本
```

**启动脚本**:

```bash
#!/bin/bash

nohup /path/to/rsync -vvv --daemon --no-detach --ipv4 --config=/path/to/rsyncd.conf.txt . > /dev/null 2>&1 &
```

**配置文件(rsync.conf.txt)**:

```bash
port = 8873
log file = /path/to/rsyncd.log
use chroot = no

[NAS]
# 备份的目的地
path = /Volumes/LaCie/Backup/NAS
comment = NAS
log file = /path/to/rsyncd_nas.log
transfer logging = true
read only = false
# 认证的用户
auth users = username
secrets file = /path/to/rsyncd.secrets.txt
```

**认证配置(rsyncd.secrets.txt)**

```bash
username:password
```

在 DS923+ 上配置 **Hyper Backup** :

![20241229154732_pDQp416p.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_pDQp416p.webp)

上面的 Rsync Server 需要在 macOS 启动后手动执行 **start** 脚本启动, 为了减少手动操作, 我们可以通过 macOS 的 launchctl 来管理 Rsync Server 的自启动:

在 `~/Library/LaunchAgents` 下新增 `xx.xxx.rsync.plist` 文件:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>xx.xxx.rsync.plist</string>
    <key>UserName</key>
    <string>xxx</string>
    <key>KeepAlive</key>
    <true/>
    <key>ProgramArguments</key>
    <array>
        <string>./rsync</string>
        <string>-vvv</string>
        <string>--daemon</string>
        <string>--no-detach</string>
        <string>--ipv4</string>
        <string>--config=rsyncd.conf.txt</string>
        <string>.</string>
    </array>
    <key>WorkingDirectory</key>
    <!-- 工作目录, 所以上面的 ProgramArguments 使用的是 ./rsync -->
    <string>~/rsync-server</string>
    <key>RunAtLoad</key>
    <true/>
    <key>OnDemand</key>
    <false/>
    <key>LaunchOnlyOnce</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>~/rsync-server/err.log</string>
    <key>StandardOutPath</key>
    <string>~/rsync-server/out.log</string>
  </dict>
</plist>
```

加载 plist:

```
launchctl load ~/Library/LaunchAgents/xx.xxx.rsync.plist
```

确认服务已运行:

```bash
$ launchctl list | grep xx.xxx.rsync
3130	0	xx.xxx.rsync
```

```bash
$ ps -ef | grep -v grep | grep --color=auto rsync
  501  3130     1   0 10:47AM ??         0:00.09 ./rsync -vvv --daemon --no-detach --ipv4 --config=rsyncd.conf.txt .
```

![20241229154732_GRk3xPdz.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_GRk3xPdz.webp)

**同步日志**:

![20241229154732_7zbndo4b.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_7zbndo4b.webp)

如果需要卸载服务（临时停止并从启动项中移除）:

```bash
launchctl unload ~/Library/LaunchAgents/xx.xxx.rsync.plist
```

**参考**:

- [macOS 设置开机启动任务](https://0clickjacking0.github.io/2020/05/20/macos%E8%AE%BE%E7%BD%AE%E5%BC%80%E6%9C%BA%E5%90%AF%E5%8A%A8%E4%BB%BB%E5%8A%A1/)
- [macOS 实现软件开启自启动](https://www.liangguanghui.com/macos-login-startup/)
- [Creating Launch Daemons and Agents](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html#//apple_ref/doc/uid/10000172i-SW7-BCIEDDBJ)
- [Daemons and Services Programming Guide](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html)
- [Technical Note TN2083: Daemons and Agents](http://developer.apple.com/library/mac/technotes/tn2083/)

---

### 云端备份

最后就是异地备份了, 这里直接使用 **阿里云盘的 WebDAV 服务**.

> 为什么不用 **Cloud Sync** 利用单向同步的方式备份到云端:
>
> 1. **Cloud Sync** 更适合同步数据, 会保留原始的文件路径;
> 2. **Cloud Sync** 一个任务只能选择一个共享目录;
> 3. 没有 **Hyper Backup** 的 **压缩备份**, **块级传输**, **多版本管理** 等高级功能;

**备份到云端**:

Hyper Backup 支持备份到云端, 这里我直接使用 **阿里云盘 WebDAV** 这个第三方套件:

![20241229154732_OjkqZdJm.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_OjkqZdJm.webp)

然后 Hyper Backup 通过 **WevDAV** 备份到阿里云盘:

![20241229154732_4DViff2E.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_4DViff2E.webp)

[**阿里云盘 WebDAV 套件使用教程**](https://imnks.com/3939.html), 获取到 **refresh_token** 后就可直接使用, 还能在 File Station 中通过 **远程连接** 挂载阿里云盘到本地, 可以方便的浏览云盘内容:

![20241229154732_X52qX4Ur.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_X52qX4Ur.webp)

> 我还会使用 阿里云盘 WebDAV 配合 Cloud Sync 下载云盘内容, 工作流为:
>
> 1. 将待下载的文件保存到阿里云盘;
> 2. 然后在 DS923+ 的 Cloud Sync 连接阿里云盘的 WebDAV 服务, 设置为 **单向同步**;
> 3. 云盘内容下载完成后直接在 File Station 挂载的阿里云盘 WebDAV 中删除即可. 除了第一步, 后续流程完全不需要登录到官方的阿里云盘操作;

### 备份时间整理

因为我使用 NAS 作为备份中枢, 且 2 台 NAS 之间存在关联关系, 所以我需要整理备份的时间, 以保证备份的正确性与可用性.

> 还需要考虑到 2 台路由器的重启计划:
>
> - 小米 AX9000 周 2 4 6 的 04:30 定时重启;
> - 小米 6500Pro 周 1 3 5 04:00 定时重启;

#### macOS

| 源文件                   | 备份方式                                   | 目的地                           | 时间                | 备份数量 |
| ------------------------ | ------------------------------------------ | -------------------------------- | ------------------- | -------- |
| 系统卷 [MBP]             | Active Backup for Business(物理服务器备份) | DS923+:/backups/ActiveBackupData | 周 1 3 5 21:00 启动 | 3        |
| 整个磁盘 [MBP]           | Time Machine                               | DS923+:/timemachine              | 周 2 4 6 22:00 启动 | 自动轮转 |
| 其他重要文件 [MBP]       | Synology Drive Client                      | DS923+:/home/Backup              | 每隔 8 小时启动     | 1        |
| 整个磁盘 [Mac mini M2]   | Time Machine                               | AirPort Time Capsule 2T          | 每周                | 自动轮转 |
| 整个磁盘 [Mac mini 2018] | Time Machine                               | AirPort Time Capsule 2T          | 每周                | 自动轮转 |

#### M920x

| 源文件       | 备份方式                                   | 目的地                          | 时间                | 备份数量 |
| ------------ | ------------------------------------------ | ------------------------------- | ------------------- | -------- |
| 系统卷       | Active Backup for Business(物理服务器备份) | DS923+:/backup/ActiveBackupData | 周 1 3 5 12:00 启动 | 3        |
| 3.860.ssd    | Active Backup for Business(物理服务器备份) | DS923+:/backup/ActiveBackupData | 周 2 4 6 12:00 启动 | 3        |
| 3.860.ssd    | [自动化脚本](#M920x-%20备份)               | 1.870.ssd                       | 每天 2 点增量备份   | 1        |
| 其他重要文件 | Active Backup for Business(文件服务器备份) | DS923+:/backup/m920x            | 周 1 3 5 05:20 启动 | 5        |

#### Station

| 源文件       | 备份方式                                   | 目的地                          | 时间            | 备份数量 |
| ------------ | ------------------------------------------ | ------------------------------- | --------------- | -------- |
| 系统卷       | Active Backup for Business(物理服务器备份) | DS923+:/backup/ActiveBackupData | 假日 22:00 启动 | 3        |
| 其他重要文件 | Active Backup for Business(文件服务器备份) | DS923+:/backup/station          | 假日 19:00 启动 | 5        |

#### H28K

| 源文件       | 备份方式                                        | 目的地               | 时间                | 备份数量 |
| ------------ | ----------------------------------------------- | -------------------- | ------------------- | -------- |
| eMMC         | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份) | DS923+:/backups/eMMC | 周 2 08:00 启动     | 3        |
| 其他重要文件 | Active Backup for Business(文件服务器备份)      | DS923+:/backup/H28K  | 周 2 4 6 07:00 启动 | 5        |

#### HK1Box

| 源文件       | 备份方式                                        | 目的地               | 时间                | 备份数量 |
| ------------ | ----------------------------------------------- | -------------------- | ------------------- | -------- |
| eMMC         | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份) | DS923+:/backups/eMMC | 周 3 08:00 启动     | 3        |
| 其他重要文件 | Active Backup for Business(文件服务器备份)      | DS923+:/backup/HA    | 周 1 3 5 09:00 启动 | 5        |

#### NanoPI NEO4

2 个 NEO4, 第二个往后延长 30 分钟执行.

| 源文件                | 备份方式                                        | 目的地                | 时间            | 备份数量 |
| --------------------- | ----------------------------------------------- | --------------------- | --------------- | -------- |
| 系统(eMMC) [NEO4.1]   | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份) | DS923+:/backups/eMMC  | 周 6 19:00 启动 | 3        |
| 其他重要文件 [NEO4.1] | Active Backup for Business(文件服务器备份)      | DS923+:/backup/NEO4.1 | 周 6 20:00 启动 | 3        |
| 系统(eMMC) [NEO4.2]   | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份) | DS923+:/backups/eMMC  | 周 6 19:30 启动 | 3        |
| 其他重要文件 [NEO4.2] | Active Backup for Business(文件服务器备份)      | DS923+:/backup/NEO4.2 | 周 6 20:30 启动 | 3        |

#### 树莓派

4 台树莓派, 每台间隔 30 分钟执行备份任务

| 源文件                | 备份方式                                          | 目的地                    | 时间            | 备份数量 |
| --------------------- | ------------------------------------------------- | ------------------------- | --------------- | -------- |
| 系统(SD 卡) [pi4]     | M920x 定时任务: [通过网络复制脚本](#通过网络复制) | DS923+:/backups/SD/pi4    | 周天 10:00 启动 | 3        |
| 其他重要文件 [pi4]    | Active Backup for Business(文件服务器备份)        | DS923+:/backup/PI4        | 周天 11:00 启动 | 5        |
| 系统(SD 卡) [pi51]    | M920x 定时任务: [通过网络复制脚本](#通过网络复制) | DS923+:/backups/SD/pi51   | 周天 10:30 启动 | 3        |
| 其他重要文件 [pi51]   | Active Backup for Business(文件服务器备份)        | DS923+:/backup/PI51       | 周天 11:30 启动 | 5        |
| 系统(SD 卡) [pi52]    | M920x 定时任务: [通过网络复制脚本](#通过网络复制) | DS923+:/backups/SD/pi52   | 周天 11:00 启动 | 3        |
| 其他重要文件 [pi52]   | Active Backup for Business(文件服务器备份)        | DS923+:/backup/PI52       | 周天 12:00 启动 | 5        |
| 系统(SD 卡) [zero2w]  | M920x 定时任务: [通过网络复制脚本](#通过网络复制) | DS923+:/backups/SD/zero2w | 周天 11:30 启动 | 3        |
| 其他重要文件 [zero2w] | Active Backup for Business(文件服务器备份)        | DS923+:/backup/Zero       | 周天 12:30 启动 | 5        |

#### R2S && R5S

| 源文件               | 备份方式                                                                  | 目的地                     | 时间                | 备份数量 |
| -------------------- | ------------------------------------------------------------------------- | -------------------------- | ------------------- | -------- |
| 系统(SD 卡) [R2S.T]  | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份)                           | DS923+:/backups/eMMC       | 周 1 10:00 启动     | 3        |
| OpenWrt 配置 [R2S.T] | OpenWrt 任务计划: [OpenWrt 自动备份脚本](#OpenWrt-%20备份) + 手动临时备份 | 本地 U 盘 + DS218+:/driver | 周 1 06:00 启动     | 5        |
| 其他重要文件 [R2S.T] | Active Backup for Business(文件服务器备份)                                | DS923+:/backup/R2ST        | 周 1 3 5 14:00 启动 | 5        |
| 系统(SD 卡) [R2S.U]  | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份)                           | DS923+:/backups/eMMC       | 周 1 11:30 启动     | 3        |
| OpenWrt 配置 [R2S.U] | OpenWrt 任务计划: [OpenWrt 自动备份脚本](#OpenWrt-%20备份) + 手动临时备份 | 本地 U 盘 + DS218+:/driver | 周 1 07:00 启动     | 5        |
| 其他重要文件 [R2S.U] | Active Backup for Business(文件服务器备份)                                | DS923+:/backup/R2SU        | 周 1 3 5 15:00 启动 | 5        |
| 系统(SD 卡) [R2S.C]  | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份)                           | DS923+:/backups/eMMC       | 周 1 12:30 启动     | 3        |
| OpenWrt 配置 [R2S.C] | OpenWrt 任务计划: [OpenWrt 自动备份脚本](#OpenWrt-%20备份) + 手动临时备份 | 本地 U 盘 + DS218+:/driver | 周 1 08:00 启动     | 5        |
| 其他重要文件 [R2S.C] | Active Backup for Business(文件服务器备份)                                | DS923+:/backup/R2SC        | 周 1 3 5 16:00 启动 | 5        |
| 系统(SD 卡) [R5S]    | DS923+ 任务计划: [eMMC 备份脚本](#eMMC-%20备份)                           | DS923+:/backups/eMMC       | 周 1 13:30 启动     | 3        |
| OpenWrt 配置 [R5S]   | OpenWrt 任务计划: [OpenWrt 自动备份脚本](#OpenWrt-%20备份) + 手动临时备份 | 本地 U 盘 + DS218+:/driver | 周 1 09:00 启动     | 5        |
| 其他重要文件 [R5S]   | Active Backup for Business(文件服务器备份)                                | DS923+:/backup/R5S         | 周 1 3 5 17:00 启动 | 5        |

#### NAS 快照

| 任务名               | 备份时间       | 源地址           | 目的地                     | 备份数量 |
| -------------------- | -------------- | ---------------- | -------------------------- | -------- |
| DS218-photo-Snap     | 每天 00:00     | DS218:/photo     | DS218:/photo/#snapshot     | 5        |
| DS218-driver-Snap    | 每天 01:00     | DS218:/driver    | DS218:/driver/#snapshot    | 5        |
| DS218-1Panel-Snap    | 每天 20:00     | DS218:/1Panel    | DS218:/1Panel/#snapshot    | 5        |
| DS218-docker-Snap    | 每天 20:10     | DS218:/docker    | DS218:/docker/#snapshot    | 5        |
| DS218-Memos-Snap     | 每天 22:00     | DS218:/Memos     | DS218:/Memos/#snapshot     | 5        |
| DS218-homes-Snap     | 每天 23:00     | DS218:/homes     | DS218:/homes/#snapshot     | 5        |
| DS923-backup-Snap    | 周 1 3 5 00:10 | DS923:/backup    | DS923:/backup/#snapshot    | 3        |
| DS923-backups-Snap   | 周 2 4 6 00:10 | DS923:/backups   | DS923:/backups/#snapshot   | 3        |
| DS923-Developer-Snap | 周天 01:00     | DS923:/Developer | DS923:/Developer/#snapshot | 3        |
| DS923-homes-Snap     | 每天 01:30     | DS923:/homes     | DS923:/homes/#snapshot     | 5        |
| DS923-photo-Snap     | 每天 02:10     | DS923:/photo     | DS923:/photo/#snapshot     | 5        |
| DS923-driver-Snap    | 每天 05:00     | DS923:/driver    | DS923:/driver/#snapshot    | 5        |
| DS923-1Panel-Snap    | 每天 12:00     | DS923:/1Panel    | DS923:/1Panel/#snapshot    | 5        |
| DS923-Memos-Snap     | 每天 13:00     | DS923:/Memos     | DS923:/Memos/#snapshot     | 5        |
| DS923-docker-Snap    | 每天 23:00     | DS923:/docker    | DS923:/docker/#snapshot    | 5        |

#### DS218+

| 任务名          | 备份套件     | 备份时间   | 备份源              | 目的地                            | 备份数量 |
| --------------- | ------------ | ---------- | ------------------- | --------------------------------- | -------- |
| backup.apps     | Hyper Backup | 周 3 14:00 | 所有 APP            | DS923:/backups/DS218.Apps.hbk     | 3        |
| backup.datas    | Hyper Backup | 周 2 14:00 | 部分共享目录        | DS923:/backups/DS218.Datas.hbk    | 3        |
| backup.system   | Hyper Backup | 周 4 14:00 | 整个系统            | DS923:/backups/DS218.System.hbk   | 3        |
| backup.to.cloud | Hyper Backup | 周 5 14:00 | 所有 APP + 重要数据 | 阿里云盘:/backups/DS218.Datas.hbk | 3        |

> **Hyper Backup** 整机备份无法使用 **WebDAV**, 只能是远程 NAS 或 Synology C2 Storage, 所以只能将 APP 和重要数据备份到阿里云盘.

#### DS923+

| 任务名          | 备份套件     | 备份时间   | 备份源                  | 目的地                            | 备份数量 |
| --------------- | ------------ | ---------- | ----------------------- | --------------------------------- | -------- |
| backup.to.Lacie | Hyper Backup | 周天 16:00 | 所有 APP                | Lacie:/Backup/NAS/DS923           | 3        |
| backup.datas    | Hyper Backup | 周 3 16:00 | 部分共享目录            | 阿里云盘:/backups/DS923.Datas.hbk | 3        |
| VMS             | -            | 手动备份   | Virtual Machine Manager | DS923:/backups/NAS.VMs            | 3        |

### 数据备份总结

![data-backup.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/data-backup.drawio.svg)

1. macOS 使用 Time machine 和 ABB 进行整机备份, Synology Drive Client 则用于重要数据数据冗余备份;
2. OpenWrt 使用 ABB 文件备份, 并使用脚本进行整个系统备份;
3. Linux 使用 ABB 的物理服务器和文件备份, 还需要使用脚本在特殊情况下备份;
4. 开发版使用 ABB 的文件备份, 并使用自动化脚本对整个系统备份, 包括 eMMC 和 SD 卡;
5. 2 台 NAS 分别使用快照对重要共享目录进行备份;
6. DS218+ 使用 Hyper Backup 备份数据到 DS923+, 并使用 ABB 进行整机备份;
7. 其他设备的备份文件全部传输到 DS923+;
8. DS923+ 使用 Hyper Backup 备份数据到云盘和外置磁盘;

这一次算是把所有设备的备份全部梳理了一遍, 整个备份系搭建下来, 感觉 DS923+ 承担了所有, 就是不知道它扛不扛得住, 这就要通过时间去验证这套备份体系了.

## 总结

至此, 7 篇关于 HomeLab 的文章算是全部完结了, 我以为花个一周时间应该可以写个七七八八, 但是这几篇文章加起来花了接近一个月的时间, 看来还是太高估自己的能力了, 原因应该是花了大量时间查阅文档以及进行各种测试.

如今基于目前的架构, 应该可以支撑很长一段时间, 只要我不手残或不添置新的设备, 所以 HomeLab 相关的文章应该到此结束了, 或许下一篇 HomeLab 的开始应该就是另一种架构了, 比如全套 [UniFi](https://store.ui.com/us/en) + 机架了, 慢慢折腾吧.

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
