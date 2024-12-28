---
title: HomeLab 硬件篇：构建基石-自托管硬件的选购与实践
cover: /images/cover/homelab-hardware.webp
ai: true
swiper_index: 3
top_group_index: 3
tags:
  - HomeLab
categories:
  - HomeLab
abbrlink: cc96
date: 2020-04-10 00:00:00
main_color:
---

![封面图](/images/cover/homelab-hardware.webp)

## 简介

在打造个人云端实验室（HomeLab）的过程中，硬件选择是至关重要的第一步。它们不仅是实验的基础设施，也是整个系统稳定性和性能的保证。本篇将重点探讨如何在预算范围内，选择具有高稳定性、良好性价比、可扩展性以及兼容性的硬件。

以下是我在挑选硬件时需要考虑的关键因素：

1. **稳定性**：我将优先考虑那些可靠性高的硬件产品，避免因频繁故障而导致的维护成本和工作中断。
2. **性价比**：在确保硬件能满足基本需求的前提下，我会寻找性价比最高的选项。毕竟，资金是有限的资源，需要合理分配。
3. **可扩展性**：为了未来的发展和可能的升级，我倾向于选择那些能够轻松扩展的硬件解决方案。
4. **兼容性**：为了避免后期使用中的不兼容问题，我将选择那些在市场上得到广泛认可的、具有良好兼容性的组件。

在选择硬件时，我特别看重稳定性。我不想频繁地处理各种硬件故障，这不仅影响工作效率，也可能导致宝贵的数据丢失。因此，我排除了集成所有功能的“全功能一体机”（All In One）方案(这类方案又叫 **All In Boom**)。这类产品虽然在某些方面可能看起来很有吸引力，但它们往往牺牲了性能和升级的可能性。

相反，我会将服务部署到多个独立的服务器上。这种分布式架构意味着即使一台服务器出现故障，也不会影响到其他服务的正常运行。这种方法不仅提高了系统的可靠性，也确保了数据的安全和连续性。

在接下来的内容中，我们将详细探讨如何在实际操作中选择合适的硬件组件，并分享一些实际操作的案例和实践经验。让我们一起探索自托管硬件选购的奥秘，为构建一个稳定、高效的个人云端实验室打下坚实的基础。

**相关文章:**

1. {% post_link homelab-guide '先导篇' %} ：我的 HomeLab 概要;
2. 硬件篇 ：介绍我所拥有的硬件设备;
3. {% post_link homelab-network '网络篇' %} ：包括网络环境、异地组网与网络安全;
4. {% post_link homelab-service '服务篇' %} ：使用 Docker 搭建的各类服务;
5. {% post_link homelab-data '数据篇' %} ：包括数据存储方案、备份方案和数据恢复方案;
6. {% post_link homelab-data-sync 'HomeLab数据同步：构建高效的数据同步网络' %};
7. {% post_link homelab-data-backup 'HomeLab数据备份：打造坚实的数据安全防线' %};

## 硬件清单

### 主机

|          硬件           |                      型号                       | 数量 |                     备注                     |
| :---------------------: | :---------------------------------------------: | :--: | :------------------------------------------: |
|           MBP           |             16 寸/M1 Pro Max 64G/4T             |  1   |                    主力机                    |
|      Mac mini 2018      |             i7/64G 内存/1T/万兆电口             |  1   |     原来的主力机, 现在沦为下载机与服务器     |
|      Mac mini 2023      |            M2/16G 内存/256G/万兆电口            |  1   |          缓存服务器, 小模型的试验机          |
| ThinkStation M920x Tiny |           i7/64G 内存/4.5T/双万兆光口           |  1   | 主要的服务器, 大部分 Docker 和虚拟机的寄主机 |
|       台式组装机        | 双路 E5 2680V4/256G 内存/2T/万兆电口/2080Ti+P40 |  1   |                    炼丹炉                    |

因为工作的原因, 从 2015 购买第一台 MBP 开始便一发不可收拾, 陆陆续续购买了 Apple 全家桶, 一是因为 macOS 非常适合开发, 二是简约的系统和完美的工业设计.
后来因为组建 HomeLab 和 AI 的爆火, 开始购买 X86 硬件与显卡, 组装了第一台家用服务器, 但是因为耗电量巨大, 不是 24 小时开机运行.
后续入手了联想的 M920X 准系统, 后续持续升级到现在的配置, 安装了 Ubuntu Server, 主要用于跑一些大型服务与重要数据的容灾备份.

#### MackBook Pro

![image_source/2020/homelab-hardware/mbp.jpg](mbp.webp)

这是我的第二台 MBP, 在如今 LLM 爆发的 AI 元年, 很庆幸买了 64G 内存的版本, 得益于 [llama.cpp](https://github.com/ggerganov/llama.cpp) 这样的优秀框架，即使在 CPU 上也能相对流畅地运行大型模型。

不得不说 Apple 从 Intel CPU 升级到 Apple Silicon, 给我最直观的感受就是基本上只有在跑 LLM 时才会稍微感受到一点温度, 其他时候都冷手.

目前，LLM（大型语言模型）正处于百花齐放的阶段，从自然语言交互到图像和语音生成，再到多模态处理，各领域的 LLM 应用层出不穷。然而，对于个人用户来说，部署 LLM 仍需要不小的硬件投入，尤其是在端侧，隐私问题和计算资源的高要求都未能很好地解决。如果未来能在树莓派这样的开发板上顺畅运行 LLM，那将是一个让每个人都可以轻松拥有、私密且低成本的个人化 LLM 时代美好时代。

#### Mac mini 2018

Mac mini 2018 是我第一台 Mac 主机, 主要看重它能够更换内存, 因此买了最小的 8G 版本, 然后升级到了 64G 内存, 不得不说但是的内存条跳水真的太夸张了, 第一条 32G 内存买成接近 3000, 隔了 3 个月购买第二张 32G 内存时, 降价到 1000+, 我只能用 "早买早享受" 来安慰自己了.

![image_source/2020/homelab-hardware/mini1.JPEG](mini1.webp)

内部结构, 看着赏心悦目

![image_source/2020/homelab-hardware/mini2.JPEG](mini2.webp)

![image_source/2020/homelab-hardware/mini3.JPEG](mini3.webp)

一条超贵的 32G 内存条.

后续再次入手了一台同型号的 Mac mini 2018, 放在公司作为开发主力机, 还购买了 Blackmagic eGPU, 因为当时 Mac mini 2018 带 2 台 4K 显示器略微吃力, 在 Blackmagic eGPU 的加持下, IDEA 的流畅度大大增加.

![image_source/2020/homelab-hardware/WechatIMG28.jpg](WechatIMG28.webp)

我只能说 Intel 芯片发热太严重了, 陆陆续续更换了多个外置散热, 最离谱的是还用过半导体散热方案, 不开散热一会就开始烫手, Apple Silicon YYDS...

![image_source/2020/homelab-hardware/Blackmagic-eGPU.png](Blackmagic-eGPU.webp)

当 Mac mini M1 上市后, 还在观望, 查看了大量测试视频后, 决定后期购买 M2 芯片的 Mac mini, 因此出掉了一台 Mac mini 2018, Blackmagic eGPU 则卖给了朋友, 剩下的 Mac mini 2018 就当留作 Apple Intel CPU 的最后一代的见证(其实是 M 系列芯片上市后, Intel 系列的 Mac mini 降价太严重, 犹豫之后还是留下来当服务器用).

#### Mac mini M2

Mac mini M2 的配置是: 16G 内存 + 256G SSD + 万兆电口, 但是应该是最具性价比的 M 系列小主机, 对于开发者来说, 内存比闪存更重要, 且当时也有更换闪存的成功案例, 因此想着后期能够直接更换更大的闪存且比官网便宜太多, 就购买了 256G 的版本.

![image_source/2020/homelab-hardware/m21.jpg](m21.webp)

忽略杂乱的线, 前面显示器一盖就什么都看不到了(更乱的线还在后面 😂, 桌搭的博客安排上)

目前 Mac mini M2 主要用作缓存服务器, 且因为统一内存的架构, 还能跑一跑 GGUF 格式的小模型. 目前还没有完全用起来, 等更换了闪存后再开始重度使用(256G 闪存被阉割且真的太小了, 目前都不敢安装太多的 APP, 且 LLM 的模型文件还得放到 NAS 上才敢跑一下).

#### ThinkStation M920x Tiny

![image_source/2020/homelab-hardware/m920x1.jpg](m920x1.webp)

具体硬件参数:

- CPU: i7-8700
- 内存: `32G *2`
- 磁盘: M.2 512G 系统盘 + 1T `SSD * 4`
- 网卡: Intel X520-DA2 双万兆 10G 光口网卡 + 板载千兆 I219 电口网卡 + USB 转 2.5G 电口网卡 + USB 蓝牙 & WiFi 模块

系统选择了 Ubuntu Server, 而不是 PVE 或者 ESXi 的原因是 ThinkStation M920x Tiny 定位是单机服务器, 主要满足个人需求:

- 几乎所有服务都可以使用 Docker 运行，开销小;
- 容器调用显卡比虚拟机调用显卡容易很多; 更何况这台 M920x 没装显卡;
- 虚拟化支持是集成在 Linux 内核中的，任何发行版都可以安装 KVM/QEMU 来跑虚拟机;
- 随着使用时间的增加，虚拟机的资源总是需要重新调整，而像文件系统这类的资源调整起来很麻烦;
- 不需要虚拟诸如 OpenWrt, NAS 等系统, 我更倾向于购买专门的硬件来跑这类独立系统;

所以我目前就是 Ubuntu + Docker + KVM/QEMU，Docker 里跑着四十多个服务，共用文件系统和显卡，偶尔有跑其他内核系统的需求就在 KVM/QEMU 里开个虚拟机, 简单而不失优雅.

![image_source/2020/homelab-hardware/20241115_e9NwlC34.png](20241115_e9NwlC34.webp)

目前只跑了 4 个虚拟机, WAF 作为防火墙是所有外网流量的第二层入口, 负责代理局域网的其他服务, 如果出现问题可以快速熔断.

其他 2 个虚拟机作为实验机, 使用纯净的系统避免因为端口冲突导致启动失败等问题出现(寄主机已经启动了太多的 Docker 容器, 管理端口确实有点麻烦, 用新的虚拟机直接 docker-compose 启动即可, 避免升级时 git pull 的冲突).

#### 台式组装机

![image_source/2020/homelab-hardware/station4.jpg](station4.webp)

严重光污染警告!!!

具体硬件参数:

- CPU: 双路 E5 2680V4;
- 内存: 256G ECC 内存(全部插满, 要的就是这种满足感);
- 磁盘: `1T SSD * 2` (后期会考虑扩充 HDD 硬盘);
- 显卡: 2080Ti + P40;
- 网卡: 板载双千兆电口网卡 + PCIe 转万兆电口网卡 + PCIe 转 2.5G 电口网卡 + USB 蓝牙 & WiFi 模块;

早期是真的想组装一台属于自己的服务器, 考虑过机架服务器, 便宜是真便宜, 奈何噪音机器体积都无法接受, 放家里肯定不合适.

所以选择了支持双路的华南主板, 搭配 2 颗 E5 2680V4, 性价比还是挺高的.

后续继续捡垃圾, 内存条全部插满, 系统也从 Windows 11 换成了 Ubuntu Server 22.04(E5 跑 Windows 11 卡的我怀疑人生).

存储倒是没有太多的要求, 所以直接搭配了 2 条 1T SSD, 后期在考虑扩展吧.

传统的封闭式机箱没有找到满意的, 索性就去咸鱼定制了一款开放型机箱, 看着还不错, 就是灰尘不好打理.

因为插了 2 张显卡, 这个耗电量着实有点吃不消, 目前也只会在测试最新模型时才会开机, 其他时间都在吃灰.

2080Ti 咸鱼二手购入, 但是 1800, 现在有魔改 22G 的版本, 后续可以尝试一下.
跑模型非常吃显存, 因此后续又购入了 Tesla P40, 24G 显存可以自己训练 Lora 模型了.

因为散热问题导致宕机过几次, 因此对 2080Ti 进行了魔改, 加装了散热钢板并改成了水冷, 目前跑模型还能压得住.

Tesla P40 因为是服务器上使用的不具备主动散热, 因此去咸鱼上改了个散热, 目前用下来还勉强够用, 不过不是特别推荐, 一是速度太慢了, 二是有可能不被模型支持.

##### 接入米家

为了方便的开关机, 加装了一张 WiFi 开机卡, 接入米家后可直接语音开关机.

![image_source/2020/homelab-hardware/20241117_cLBxdgBf.png](20241117_cLBxdgBf.webp)

### 群晖 NAS

|  硬件  |                                型号                                 | 数量 |                  备注                  |
| :----: | :-----------------------------------------------------------------: | :--: | :------------------------------------: |
| DS218+ |             10G 内存/2T SSD 组 Raid1/千兆电口+2.5G 电口             |  1   | 主要用于 Drive 数据同步, 跑轻量 Docker |
| DS923+ | 36G 内存/2T SSD 组 Raid1 作为系统盘/ 6T + 8T + `10T*2` HDD/万兆电口 |  1   |  重要数据备份,影音服务, Docker 寄主机  |

#### DS218+

![image_source/2020/homelab-hardware/218.png](218.webp)

从 2019 年入手第一台 DS218+ 开始, 便入了 NAS 的坑, 原来 NAS 还能这么好玩, 最开始购买的 `6*6` T HDD 硬盘因为断电损坏了一块, 导致现在对 HDD 的选择非常谨慎.

目前 DS218+ 主要通过 Synology Drive 来同步文件, 因为有公网 IP 的加持, 围绕 Drive 搭建了全平台的数据同步方案, 目前使用下来非常省心.

为了提高 DS218+ 的数据同步效率, 且我也不需要特别大的 HHD, 因此索性将 HDD 全部更换为 SSD, 并组了 Raid1 来保证数据安全.

#### USB 2.5G 网卡

DS218+ 使用了 USB 转 2.5G 网卡将网络升级到了 2.5G, [这里](https://www.iplaysoft.com/synology-nas-25g.html) 是详细的教程, 不过现在通过第三方的套件更加方便:

![image_source/2020/homelab-hardware/2.5G.png](2.5G.webp)

需要在套件中心添加第三方套件来源:

![image_source/2020/homelab-hardware/kits.png](kits.webp)

套件地址汇总:

- spk7: spk7.imnks.com
- synocommunity: https://packages.synocommunity.com/
- 云梦: https://spk.520810.xyz:666
- 4sag: https://spk.4sag.ru/

#### DS923+

![image_source/2020/homelab-hardware/923.png](923.webp)

而 DS923+ 作为重要数据的备份从机, 会对 DS218+ 进行全盘备份, 同时跑一些影音服务, Docker 寄主机. 值得说明的是, DS923+ 官网说只支持 32G 内存, 试测是可以最大支持到 64G 的, 目前只购买了一张 32G ECC 内存, 加上原来的 4G 一共 36G.

[DS923+ 支持 SSD 作为存储盘](https://post.smzdm.com/p/all3nvl8/), 可是坑爹的是只能使用官网的 M.2, 不过开源的 [Synology HDD db](https://github.com/007revad/Synology_HDD_db) 可以完美的绕过这个问题,

需要在 DSM 更新后重新运行该脚本。如果 DSM 设置为自动更新，则最佳选项是在 Synology 每次启动时运行该脚本，而最佳方法是设置计划任务以在启动时运行该脚本:

![image_source/2020/homelab-hardware/m.2.png](m.2.webp)

还有其他几个项目可以尝试:

- [Synology enable M2 volume](https://github.com/007revad/Synology_enable_M2_volume)
- [Synology M2 volume](https://github.com/007revad/Synology_M2_volume)

#### 万兆网卡

DS923+ 官网 10G 网卡:

![image_source/2020/homelab-hardware/20241115_f5ZJCup0.png](20241115_f5ZJCup0.webp)

我选择 DS923+ 的原因就是支持万兆网卡, 为后期全屋万兆打下基础, 但是官方的网卡实在太贵, 抵得上 `1/5` 的 DS923+ 的价格了, 直到兼容的网卡出现, 400+ 的价格果断下手:

![image_source/2020/homelab-hardware/20241115_2oEL0IHV.png](20241115_2oEL0IHV.webp)

现在 DS923+ 与 Mac mini 2018 通过 `HYWS-SGT0204S` 万兆交换机直连, 拷贝速度非常满意, 后期考虑将书房的主要设备全部升级到万兆(现在就差全口万兆交换机和雷电 4 转万兆扩展坞了, 还在犹豫全光口还是电口, 大概率会全光口, 发热量比电口小的多, 但是部分设备只能用电口, 因此还要增加光转电接口的成本).

![image_source/2020/homelab-hardware/20241115_AyNwKmup.png](20241115_AyNwKmup.webp)

跑满了理论速度.

![image_source/2020/homelab-hardware/WechatIMG27.jpg](WechatIMG27.webp)

`HYWS-SGT0204S` 交换机只有 2 个万兆光口, 分别通过万兆光转电模块连接 DS923+ 和 Mac mini 2018, 发热量也是不小, 因此额外增加了散热风扇和散热片, 效果非常好.

#### 链路聚合

![image_source/2020/homelab-hardware/20241116_7dCSQwsQ.png](20241116_7dCSQwsQ.webp)

因为购买了独立的万兆网卡, 自带的 2 个千兆网卡就可以玩玩链路聚合了, 不过因为没有连接到具备网管功能的交换机上, 目前也就只能算个自娱自乐, 还不具备带宽翻倍的效果.

可以参考以下链接来学习相关知识:

- [SMB3 多通道和链路聚合的区别](https://kb.synology.cn/zh-cn/DSM/tutorial/smb3_multichannel_link_aggregation)
- [nas 开启链路聚合，提升多设备访问带宽](https://post.smzdm.com/p/apm8p5mw/)

我的目的是实现提升多设备并发访问的效率, 理论上只需要添加一台具备网管功能的交换机即可(目前硬件已经有了, 但是需要改造线路, 后面再折腾吧).

### 硬路由

|          硬件           |        型号        | 数量 |                    备注                    |
| :---------------------: | :----------------: | :--: | :----------------------------------------: |
|       小米 AX9000       | 电信拨号, 主路由器 |  1   |      1G 宽带接入, 2.5G 网口用作局域网      |
|       小米 AX1800       | AX9000 Mesh 路由器 |  2   |    书房和主卧各一个, 增加 WiFi 覆盖面积    |
|      小米 6500Pro       | 联通拨号, 主路由器 |  1   |      1G 宽带接入, 2.5G 网口用作局域网      |
|     小米路由器 R3D      | 6500Pro 二级路由器 |  1   |       淘汰下来的, 1T 硬盘当下载机用        |
|     小米路由器 R1D      | 6500Pro 二级路由器 |  1   |       淘汰下来的, 1T 硬盘当下载机用        |
| AirPort Time Capsule 2T |   AX9000 子路由    |  1   | 关闭了 WiFi, 用作 macOS 系统备份, 网口拓展 |
|     Airport Express     |   AX9000 子路由    |  1   |     关闭了 WiFi, 只用作 AirPlay2 放歌      |

家里是电信联通双千兆宽带入户, 电信作为主网, 用作家庭主要上网宽带; 联通作为辅网, 用作下载与物联设备联网, 互不干涉, 冗余设计.

#### AX9000

![image_source/2020/homelab-hardware/ax9000.jpg](ax9000.webp)

AX9000 是可以跑 Docker 的, 且能够通过 Docker 获取 root 权限, 但是尝试过后发现不是特别稳定, 所以还原成了. 专业的事情还是让专业的设备来干吧.

![image_source/2020/homelab-hardware/20241115_tzGZHfcC.png](20241115_tzGZHfcC.webp)

目前带了差不多快 40 个终端设备, 稳定性还是可以的.

#### AX1800

AX1800 通过有线与 AX9000 进行 Mesh 组网, 一个放在主卧, 另一个放在书房, 一是作为 WiFi 热点, 二是作为 Lan 扩展, 下级再连接交换机为开发板提供有线接入.

#### 6500Pro

![image_source/2020/homelab-hardware/6500pro.jpg](6500pro.webp)

购买 6500Pro 是看上了它内置的中枢网关, 家里大部分智能设备是小米旗下的, 基本上节省了一台网关的钱, 但是性能有点差强人意, 一是延迟较高, 二是散热设计非常不合理, 如果有意购买 6500Pro 的朋友, 可以先看看这个 [测评](https://www.bilibili.com/video/BV1zx4y147WQ?t=339.8), 后面可能会考虑进行改造.

![image_source/2020/homelab-hardware/20241115_7nZ4JqX2NNfbRpir.png](20241115_7nZ4JqX2NNfbRpir.webp)

6500Pro 主要作为智能家居设备接入, 因此专门开了一个 `ihome.device` 的 2.4GHz 的频段, 并且另外开设了一个访客网络, 供来访的朋友使用.

#### 小米路由器 R3D && R1D

![image_source/2020/homelab-hardware/r3d2.jpg](r3d2.webp)

![image_source/2020/homelab-hardware/r1d1.jpg](r1d1.webp)

2 款路由器都比较经典, 自带 1T HDD 且具有 SMBA 功能, 完全可以当轻 NAS 是用, 期间获取过 root 权限, 但是硬件素质太差, 不具备太大的可玩性.

不知道从何开始, 喜欢上折腾散热了, 能加装散热的设备通通不放过, 它两本身的散热一般, 夏天稍有点热, 现在的外加散热还是有点用, 但不是太多.

#### AirPort Time Capsule 2T & Airport Express

![image_source/2020/homelab-hardware/atc.jpg](atc.webp)
![image_source/2020/homelab-hardware/Airport_Express.jpg](Airport_Express.webp)

2 款停产许久的产品, AirPort Time Capsule 2T 还是多年前去万象城人肉提回来的, 2T 的备份备份 3 台 macOS, 勉强够用吧, 另外作为千兆网口的扩展.

Airport Express 后面咸鱼入手的, 也就拿来 AirPlay2 放歌用, 没有其他用途了.

![image_source/2020/homelab-hardware/20241116_nDQD8t3Z.png](20241116_nDQD8t3Z.webp)

感觉 Apple 路由器设置还是蛮方便的.

#### IPV6

两款主路由器都支持开启 IPV6, 且在外网能够正常通过 IPV6 访问家里的设备, 但是目前是关闭状态, 因为有部分服务还没有来得及设置安全认证, 总觉得直接暴露到公网会有安全问题(IPV6 因为长度的问题想要暴力猜测可能没那么容易, 奈何我绑定了域名, 这不一 Ping 就知道设备的唯一地址了, 还是先用 IPV4 吧, 至少能通过端口转发控制暴露出去的服务).

#### 为什么不用猫棒代替光猫

经常看到有视频介绍 `猫棒+ 2.5G 路由器` 代替光猫突破千兆, 我并没有采用这种方案, 主要原因是:

- 猫棒发热量巨大, 降低了稳定性;
- 为了从 930Mbps 突破到 1100Mbps+, 额外购买猫棒和其他硬件, 我觉得性价比不是特别高;

#### 为什么不考虑多线多拨、负载均衡、宽带叠加

同样会有大量视频推荐多线多拨、负载均衡、宽带叠加等实现 1+1 = 2 的网速, 但是这些方案我没有考虑的原因是:

- 大多数运营商不支持多拨, 或者多拨也不会叠加网速, 我主要考虑稳定性;
- 网速快不代表体验好, 联通宽带延迟比电信宽带延迟高, 我可以按需使用不同的宽带, 避免延迟不可控;
- IP 乱跳: 我的电信和联通宽带都有公网 IP, 用上述方法肯定会导致出口 IP 随机变化, 当然可以通过配置解决, 但是会增加额外的硬件成本和配置复杂度;
- 我目前根本用不到这么快的网速, 上述方式目前只停留在测速上, 对我来说没有实际应用场景;
- 因为会存在单点问题, 并不想使用一个设备去承载 2 条宽带;

目前考虑的是双宽带主从冗余, 各司其职, 且另一个关键的原因是需要通过 Wireguard 进行异地组网, 会分别通过不同的宽带接入到家中的局域网, 因此不想更改目前的网络架构.

### 软路由

| 硬件 |       型号       | 数量 |                 备注                 |
| :--: | :--------------: | :--: | :----------------------------------: |
| R2S  | 电信&联通 旁路由 |  3   | 轻量 Docker 容器, 广告过滤, 异地组网 |
| R5S  | 电信&联通 旁路由 |  1   | 轻量 Docker 容器, 广告过滤, 异地组网 |
| H28K | 电信&联通 旁路由 |  1   | 轻量 Docker 容器, 广告过滤, 异地组网 |

OpenWrt 又是一个打开新世界大门的伟大开源项目, 从未想过还能随心所欲的配置网络, 不过在配置的过程中也遇到了不少坑.

购买软路由的朋友, 怎么使用应该都知道吧, 所以这部分就不展开说了.

#### R2S

最开始入手的 R2S, 小巧的外形加铝合金材质, 怎么看怎么喜欢, 后来加上了风扇, 通过温控脚本控制风扇转速.

刚开始因为对 OpenWtr 不是特别熟悉, 不知道 Lan 口还能改成 Wan 口, 就只作为电信宽带的子路由使用, 部署 Wireguard 后只能访问电信的局域网, 因此后面捡漏购买了另一个 R2S, 作为联通宽带的 Wireguard 服务器.

随着折腾的不断深入, 尝试将 Lan 口修改为 Wan 口, 现在 R2S 能够同时接入电信和联通宽带, 权当作为冗余吧, 也没有出掉多余的 R2S.

![image_source/2020/homelab-hardware/r2st.jpg](r2st.webp)

放在书房桌面上, 作为电信的二级路由, 联通作为冗余宽带接入.

![image_source/2020/homelab-hardware/r2su.jpg](r2su.webp)

放在弱电箱, 作为联通的二级路由, 电信作为冗余宽带接入.

![image_source/2020/homelab-hardware/r2sc.jpg](r2sc.webp)

第三台 R2S 放在公司使用, 主要也是作为 Wireguard 服务器, 与家里的设备进行异地组网.

值得说明的是, R2S 的 Wan 口是通过 USB3.0 转换的, 测试过最多跑到 600M+, 但是因为使用场景的不同, 我目前对这个速率还不是那么敏感, 所以也没有升级的必要.

##### 将 Lan 改成 Wan 接口

R2S 主要作为旁路由使用, 因此并不需要设备与 Lan 直接, 所以多出来的 Lan 口可以用来做 Wan 口, 这样就可以同时接入电信和联通宽带了.

但是会存在网卡优先级的问题, 可以通过网关跃点解决:

![image_source/2020/homelab-hardware/20241116_264lyTxU.png](20241116_264lyTxU.webp)

具体的配置方式会在网络篇中详细说明.

##### 温控脚本

我安装的固件并没有官方的温控脚本, 不过按照 [教程](https://github.com/coolsnowwolf/lede/issues/5681) 完美实现了温控.

```shell
curl -o /usr/bin/start-rk3328-pwm-fan.sh https://github.com/friendlyarm/friendlywrt/blob/master-v19.07.1/target/linux/rockchip-rk3328/base-files/usr/bin/start-rk3328-pwm-fan.sh \
curl -o /etc/init.d/fa-rk3328-pwmfan https://github.com/friendlyarm/friendlywrt/blob/master-v19.07.1/target/linux/rockchip-rk3328/base-files/etc/init.d/fa-rk3328-pwmfan \
chmod +x /usr/bin/start-rk3328-pwm-fan.sh  /etc/init.d/fa-rk3328-pwmfan \
/etc/init.d/fa-rk3328-pwmfan enable \
/etc/init.d/fa-rk3328-pwmfan start
```

#### R5S

![image_source/2020/homelab-hardware/r5s.jpg](r5s.webp)

加上了散热风扇, 但是温控还没有搞定, 不过引出了 PWM 接口, 后续折腾的时候不用再拆机器了, 直接通过 PWM 取电, 替换现在的 USB.

还为 R5S 添加了 256G 的 M.2 SSD, 作用轻量服务器, 4G 的内存不能白白浪费了.

#### H28K

非常喜欢这种小巧的铝合金机身, 因此忍不住又买了 H28K 4G 版本, 不过目前也仅仅是作为 Wireguard 服务器, 连 Docker 容器都还没有 🤣.

![image_source/2020/homelab-hardware/h28k1.jpg](h28k1.webp)

![image_source/2020/homelab-hardware/h28k2.jpg](h28k2.webp)

因为 H28K 没有 PWM 接口, 就自己焊接了一个 USB 来驱动风扇, 感觉还行 😎.

### 交换机

|         硬件         |               型号               | 数量 |               备注               |
| :------------------: | :------------------------------: | :--: | :------------------------------: |
|  TP-Link TL-SH1005   |   电信&联通 `2.5G*5口 交换机`    |  2   |         弱电箱出口交换机         |
| 兮克 SKS1200-8GPY1XF | 电信 `2.5G*8口 + 1万兆口 交换机` |  1   |          书房入口交换机          |
|       DX-1009N       | 联通 `2.5G*8口 + 1万兆口 交换机` |  1   |          书房入口交换机          |
|  TP-Link TL-SG2008D  |      电信 `千兆*8口 交换机`      |  1   |  二级交换机, 主要用于连接开发板  |
|  TP-Link TL-SG1008D  |      联通 `千兆*8口 交换机`      |  1   |  二级交换机, 主要用于连接开发板  |
|   iKuai IK-J3005D    |   电信&联通 `千兆*5口 交换机`    |  2   |          书房临时交换机          |
|    HYWS-SGT0204S     | 联通 `2.5G*4口 + 万兆*2口交换机` |  1   | mac mini 2018 和 DS923+ 万兆直连 |

交换机陆陆续续换了好多款, 主要是从 千兆升级到 2.5G, 到现在的 2.5G 混合万兆网口. 后续会考虑为书房添加联通万兆交换机, 将主要设备进行万兆直连, 主要包括:

- MBP: 通过雷电 4 转万兆光口;
- Mac mini 2018: 自带万兆电口;
- Mac mini M2: 自带万兆电口;
- DS923+: 已升级到万兆电口;
- M920X: 自带 2 个万兆光口;
- 组装机: 自带 1 个万兆电口;

因此购买一个 8 光口的万兆交换机绰绰有余, 然后根据需要购买万兆光转电模块直连.

#### TL-SH1005

![image_source/2020/homelab-hardware/TL-SH1005.png](TL-SH1005.webp)

弱电箱电信玩光猫光纤接入, 通过预埋的网线与对面电视柜中的 AX9000 连接并拨号上网, 在通过另一根预埋的网线接回到 `TL-SH1005` 交换机, 然后再接入到其他房间.

联通宽带接入就相对简单许多, 因为光猫, 6500Pro 还有交换机都在弱电箱附近, 直接通过短距离有线连接即可, 同样是光纤入户, 路由器拨号.

还好装修时预埋了多条网线: 客厅电视柜 3 根, 主卧和书房 2 根, 次卧 1 根.

如果埋少了恐怕整个 HomeLab 又是另一种架构了.

#### SKS1200-8GPY1XF & DX-1009N

![image_source/2020/homelab-hardware/SKS1200-8GPY1XF.png](SKS1200-8GPY1XF.webp)

![image_source/2020/homelab-hardware/DX-1009N.png](DX-1009N.webp)

2 个交换机先后从咸鱼购买, 没有去细究具体参数, 本着捡垃圾的原则, 捡便宜的买就行.

从书房的 2 个网口分别接入电信和联通网络, 为书房其他设备提供有线网络接入 (基本上每台设备都具备双网口, 为了将冗余做到极致, 单网口的也要整个 USB 转 2.5G 网卡).

#### IK-J3005D

![image_source/2020/homelab-hardware/IK-J3005D.png](IK-J3005D.webp)

先后买了 2 个, 放在桌面上做临时的交换机, 小巧占地方.

![image_source/2020/homelab-hardware/IK-J3005D2.jpg](IK-J3005D2.webp)

#### HYWS-SGT0204S

![image_source/2020/homelab-hardware/HYWS-SGT0204S.png](HYWS-SGT0204S.webp)

后来 2.5G 网口不够了, 且为了将 Mac mini 2018 与 DS923+ 进行万兆直连, 新增了这个交换机.

后续考虑换成全万兆交换机, 把主要设备全部升级到万兆互联.

### 影音硬件

|     硬件     |      型号      | 数量 |         备注         |
| :----------: | :------------: | :--: | :------------------: |
| Apple TV 4K  |      64G       |  1   |       客厅电视       |
|   HomePod    |     第一代     |  1   |       书房音箱       |
| HomePod mini |     第二代     |  2   |       客厅音箱       |
|   无源音箱   |      组装      |  2   | 安装在书桌下, 听个响 |
| 飞傲 K5 Pro  |   K5Pro ESS    |  1   |     搭配耳机使用     |
|   斐讯 T1    | 2G RAM+16G ROM |  1   |      Android TV      |

#### Apple TV 4K

![image_source/2020/homelab-hardware/appletv.jpg](appletv.webp)

配合 VidHub 播放 NAS 电影, 最新支持 Surge TV 版本, 偶尔看见 Youtube, 用的不是特别多.

![image_source/2020/homelab-hardware/VidHub.png](VidHub.webp)

#### HomePod & HomePod mini

![image_source/2020/homelab-hardware/homepod.jpg](homepod.webp)

第一代的 HomePod, 听说第二代阉割了, 所以一直没有打算换二代, 目前配合桌下的无源音箱, 桌上桌下齐响, 环绕感还是挺强的.

![image_source/2020/homelab-hardware/homepodmini1.jpg](homepodmini1.webp)
![image_source/2020/homelab-hardware/homepodmini2.jpg](homepodmini2.webp)

HomePod Mini 放在客厅沙发后面当 Apple TV 4K 的音源输出, 偶尔全屋 Airplay 播放, 感觉还是挺不错的.

#### 无源音箱

![image_source/2020/homelab-hardware/621731716248.jpg](621731716248.webp)

![image_source/2020/homelab-hardware/641731716250.jpg](641731716250.webp)

全套咸鱼购买, 自己组装

#### 飞傲 K5 Pro

![image_source/2020/homelab-hardware/631731716249.jpg](631731716249.webp)

烧过一段时间 Hi-Fi, 后面出掉了随时设备, 就留下了这个和 WH-1000XM4 配合使用.

#### 斐讯 T1

![image_source/2020/homelab-hardware/m21.jpg](m21.webp)

中间那个黑色黑子就是 T1, 刷了第三方 YYF 固件. 屏幕和 Mac mini M2 共用, 使用绿联的 KVM 切换视频输入.

![image_source/2020/homelab-hardware/lvlian-kvm.jpg](lvlian-kvm.webp)

坑的地方是没有适配 Apple Silicon 的 macOS 系统, 因为我买了 2 个, Apple Intel CPU 就能很好的适配.

现在也在吃灰, 后面看能不能折腾下刷成 Armbian 系统玩玩.

### 云服务器

|  硬件  |  型号   | 数量 |              备注               |
| :----: | :-----: | :--: | :-----------------------------: |
| 阿里云 | 2 核 2G |  1   | 固定公网 ip, 博客服务, 异地组网 |

很多折腾的前提的要有一个固定公网 IP, 虽然现在也能通过 DDNS 来实现通过域名访问家中的服务, 但是经不起便宜啊, 99 元/年的价格, 怎么看怎么划算, 一口气买了 2 年.

### 其他硬件

|         硬件          |       型号        | 数量 |              备注              |
| :-------------------: | :---------------: | :--: | :----------------------------: |
|    树莓派 Zero 2W     |     512M 内存     |  1   |             开发板             |
|       树莓派 4B       |      8G 内存      |  1   |             开发板             |
|       树莓派 5B       |      8G 内存      |  2   |             开发板             |
|      NanoPI NEO4      | 1G 内存/ 32G eMMC |  2   |             开发板             |
|        HK1 Box        | 32GB 闪存/4G 内存 |  1   |         Home Assistant         |
| LaCie d2 Professional |        8T         |  1   |              冷备              |
|          UPS          | APC Back-UPS 650  |  1   | 作为 DS923+ 和开发板的备用电源 |

#### 树莓派

![image_source/2020/homelab-hardware/pi51.jpg](pi51.webp)

![image_source/2020/homelab-hardware/pi52.jpg](pi52.webp)

感觉到了某个阶段, 编写软件已经无法满足好奇心了, 所以陆续买了几个树莓派玩一些新奇的东西, 通过软件控制硬件感觉非常酷, 目前主要玩儿的是工作相关的, 比如流媒体服务.

#### NanoPI NEO4

![image_source/2020/homelab-hardware/neo41.jpg](neo41.webp)

![image_source/2020/homelab-hardware/neo42.jpg](neo42.webp)

RK3399 的发热量是真的大, 所以买了几个树莓派小风扇并加装了散热片. 开发板就买过 NanoPi 和树莓派, 其他家的还没尝试过, 但是现在还是更喜欢树莓派(资料多, 社区活跃).

应该能看到其中一台连接了摄像头, 因为资料的问题还没驱动起来.

#### HK1 Box

![image_source/2020/homelab-hardware/mbox1.jpg](mbox1.webp)

![image_source/2020/homelab-hardware/mbox2.jpg](mbox2.webp)

咸鱼购买, 刷了 Armbian, 通过 Docker 安装 Home Assistant, 以前经常死机, 后来在 UART 接口焊接了排线并安装了散热风扇, 现在稳定运行.

#### LaCie d2 Professional

![image_source/2020/homelab-hardware/lacie.png](lacie.webp)

通过 雷雳 3 和 Mac mini 2018 连接, 通过 rsync 定时备份 DS923+ 的重要数据.

#### UPS

![image_source/2020/homelab-hardware/ups.jpg](ups.webp)

服役了几年, 主要是保护 DS923+, 最近更换过一次电池, 加装了电压显示模块.

## 总结

本篇文章罗列了个人拥有的硬件设备, 因为稳定性考虑, 更倾向是用独立硬件运行特定的系统, 取代 **All in One** 的方案, 网络方面也是独立分开, 互相冗余.

这个还是要看实际需求, 我需要重度依赖家中的 NAS 和其他服务, 花了大量去设计容错方案.

最后贴一下书房的总耗电量(设备应该启动了 80% 左右的情况下):

![image_source/2020/homelab-hardware/WechatIMG67.jpg](WechatIMG67.webp)

更多内容敬请期待...

<!--
https://nerdyarticles.com/my-homelab-a-general-overview/
https://chriskirby.net/setting-up-and-leveling-up-your-homelab-a-comprehensive-guide/

{% details mode:close 怎样才能订阅你博客的更新？ %}
订阅 RSS 啊！
{% enddetails %}
-->

**相关文章:**

1. {% post_link homelab-guide '先导篇' %} ：我的 HomeLab 概要;
2. {% post_link homelab-hardware '硬件篇' %} ：介绍我所拥有的硬件设备;
3. {% post_link homelab-network '网络篇' %} ：包括网络环境、异地组网与网络安全;
4. {% post_link homelab-service '服务篇' %} ：使用 Docker 搭建的各类服务;
5. {% post_link homelab-data '数据篇' %} ：包括数据存储方案、备份方案和数据恢复方案;
6. {% post_link homelab-data-sync 'HomeLab数据同步：构建高效的数据同步网络' %};
7. {% post_link homelab-data-backup 'HomeLab数据备份：打造坚实的数据安全防线' %};
8. {% post_link homelab-upgrade-to-10g 'HomeLab 网络续集：升级 10G 网络-再战 10 年' %};
9. {% post_link nat-guide 'NAT 内网穿透详解：揭秘网络连接背后的奥秘' %};
