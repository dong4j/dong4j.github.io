---
title: 树莓派直播新选择：打造你的个人流媒体服务器
keywords:
  - 树莓派
  - 直播
  - RTSP
  - 流媒体服务器
  - ZLMediaKit
categories:
  - 新时代码农
tags:
  - 树莓派
  - 直播
  - RTSP
  - 流媒体服务器
  - ZLMediaKit
description: 本文介绍了一种利用树莓派和大方摄像头结合RTSP协议，通过流媒体服务器实现直播间搭建的方法。文章详细介绍了直播架构，包括推流工具如ffmpeg和OBS
  studio、拉流工具如ffplay和ijkplayer等，以及多种流媒体服务器的选择和部署方法。重点推荐了ZLMediaKit作为流媒体服务器，并提供了详细的安装配置步骤和API使用示例。
abbrlink: 5e9872c3
date: 2023-11-30 00:00:00
ai:
  - 本文介绍了一种利用树莓派和大方摄像头结合RTSP协议，通过流媒体服务器实现直播间搭建的方法。文章详细介绍了直播架构，包括推流工具如ffmpeg和OBS studio、拉流工具如ffplay和ijkplayer等，以及多种流媒体服务器的选择和部署方法。重点推荐了ZLMediaKit作为流媒体服务器，并提供了详细的安装配置步骤和API使用示例。
---

## 1. 背景

在 [[pi-dafang-monitor|树莓派 + 大方摄像头 打造婴儿监控]] 中简单介绍了通过刷大方摄像头第三方固件来解锁更多功能, 比如 RTSP, MQTT 等, 这里我们就使用 RTSP 结合树莓派来打造一个直播间.

## 2. 直播架构

复杂的架构图:

![20241229154732_uyt57iIf.webp](20241229154732_uyt57iIf.webp)

简单的架构图:

![zhibo.drawio.svg](zhibo.drawio.svg)

### 2.1 推流工具

- ffmpeg：https://www.ffmpeg.org/download.html
- OBS studio：https://obsproject.com/download

### 2.2 拉流工具

- ffplay 播放器: https://www.ffmpeg.org/download.html 。
- cutv www.cutv.com/demo/live_test.swf flash 播放器。
- vlc 播放器。
- ijkplayer (基于 ffplay): 一个基于 FFmpeg 的开源 Android/iOS 视频播放器。开源，API 易于集成；编译配置可裁剪，方便控制安装包大小；支持硬件加速解码，更加省电简单易用，指定拉流 URL，自动解码播放.。

### 2.3 流媒体服务器

- SRS ：一款国人开发的优秀开源流媒体服务器系统。普通 C++ 语法，底层使用协程编写。
- BMS ：也是一款流媒体服务器系统，但不开源，是 SRS 的商业版，比 SRS 功能更多。作者也是目前 SRS 的作者，这个是目前 SRS 作者在上一家公司 (guanzhiyun) 的产物。
- nginx ：免费开源 web 服务器，也常用来配置流媒体服务器，集成 Rtmp_module 即可。C 语言编写。
- zlmediakit：开源，国人开发的优秀流媒体服务器，使用 C++11 多线程编写。
- Red5：是 java 写的一款稳定的开源的 rtmp 服务器。

## 3. 环境搭建

![aaa.drawio.svg](aaa.drawio.svg)

### 3.1 推流工具

直接使用 大方摄像头的 RTSP 协议推流, 地址为: `rtsp://192.168.31.128:8554/unicast`

使用 VLC 验证一下:

![20241229154732_jh1kKfzc.webp](20241229154732_jh1kKfzc.webp)

完全没问题, 内网播放非常流畅.

### 3.2 流媒体服务器

#### 3.2.1 ZLMediaKit

https://docs.zlmediakit.com/zh/

![20241229154732_3iL0oAds.webp](20241229154732_3iL0oAds.webp)

**ZLMediaKit** 是一套高性能的流媒体服务框架，目前支持 rtmp、rtsp、hls、http-flv 等流媒体协议，支持 linux、macos、windows 三大 PC 平台和 ios、android 两大移动端平台。

**主要功能:**

1. 基于 C++11 开发，避免使用裸指针，代码稳定可靠，性能优越。
2. 支持多种协议(RTSP/RTMP/HLS/HTTP-FLV/WebSocket-FLV/GB28181/HTTP-TS/WebSocket-TS/HTTP-fMP4/WebSocket-fMP4/MP4),支持协议互转。
3. 使用多路复用/多线程/异步网络 IO 模式开发，并发性能优越，支持海量客户端连接。
4. 代码经过长期大量的稳定性、性能测试，已经在线上商用验证已久。
5. 支持 linux、macos、ios、android、windows 全平台。
6. 支持画面秒开、极低延时(500 毫秒内，最低可达 100 毫秒)。
7. 提供完善的标准 C API,可以作 SDK 用，或供其他语言调用。
8. 提供完整的 MediaServer 服务器，可以免开发直接部署为商用服务器。
9. 提供完善的 restful api 以及 web hook，支持丰富的业务逻辑。
10. 打通了视频监控协议栈与直播协议栈，对 RTSP/RTMP 支持都很完善。
11. 全面支持 H265/H264/AAC/G711/OPUS。

> 总结: 同时支持 rtsp/rtmp 推拉流，而且支持 h265 的推拉流（推流端要支持 265 的 ffmpeg/拉流播放端也要支持 265 的播放器），支持各种格式拉流，使用者众多

#### 3.2.2 Monibuca

https://m7s.live/#ui

![20241229154732_x3jiipX8.webp](20241229154732_x3jiipX8.webp)

Monibuca 是一个开源的流媒体服务器开发框架，适用于快速定制化开发流媒体服务器，可以对接 CDN 厂商，作为回源服务器，也可以自己搭建集群部署环境。 丰富的内置插件提供了流媒体服务器的常见功能，例如 rtmp server、http-flv、视频录制、QoS 等。除此以外还内置了后台 web 界面，方便观察服务器运行的状态。 也可以自己开发后台管理界面，通过 api 方式获取服务器的运行信息。 Monibuca 提供了可供定制化开发的插件机制，可以任意扩展其功能。

![20241229154732_uYMVXrO1.webp](20241229154732_uYMVXrO1.webp)

**主要功能:**

1. 针对流媒体服务器独特的性质进行的优化，充分利用 Golang 的 goroutine 的性质对大量的连接的读写进行合理的分配计算资源，以及尽可能的减少内存 Copy 操作。使用对象池减少 Golang 的 GC 时间。
2. 专为二次开发而设计，基于 Golang 语言，开发效率更高；独创的插件机制，可以方便用户定制个性化的功能组合，更高效率的利用服务器资源。
3. 功能强大的仪表盘可以直观的看到服务器运行的状态、消耗的资源、以及其他统计信息。用户可以利用控制台对服务器进行配置和控制。点击右上角菜单栏里面的演示，可以看到演示控制台界面。
4. 纯 Go 编写，不依赖 cgo，不依赖 FFMpeg 或者其他运行时，部署极其方便，对服务器的要求极为宽松。

> 总结: 支持自定义插件, 扩展新功能非常方便, 缺点就是部分插件收费.

#### 3.2.3 SRS

https://ossrs.net/lts/zh-cn/

![20241229154732_Ihggdcre.webp](20241229154732_Ihggdcre.webp)

SRS(Simple Realtime Server)是一个简单高效的实时视频服务器，支持 RTMP、WebRTC、HLS、HTTP-FLV、SRT 等多种实时流媒体协议。

SRS 作为当前非常普遍的运营级解决方案，具备非常全面的功能，包括集群、协议网关、CDN 功能等，主要功能如下：

1. SRS 定位是运营级的互联网直播服务器集群，追求更好的概念完整性和最简单实现的代码。
2. SRS 提供了丰富的接入方案将 RTMP 流接入 SRS， 包括推送 RTMP 到 SRS、推送 RTSP/UDP/FLV 到 SRS、拉取流到 SRS。 SRS 还支持将接入的 RTMP 流进行各种变换，譬如将 RTMP 流转码、流截图、 转发给其他服务器、转封装成 HTTP-FLV 流、转封装成 HLS、 转封装成 HDS、转封装成 DASH、录制成 FLV/MP4。
3. SRS 包含支大规模集群如 CDN 业务的关键特性， 譬如 RTMP 多级集群、源站集群、VHOST 虚拟服务器 、 无中断服务 Reload、HTTP-FLV 集群。
4. SRS 还提供丰富的应用接口， 包括 HTTP 回调、安全策略 Security、HTTP API 接口、 RTMP 测速。
5. SRS 在源站和 CDN 集群中都得到了广泛的应用 Applications。

> 总结: 支持 rtmp 推流，早期版本支持 rtsp 推流，不知道为何移除了。支持部分格式拉流，不支持 ws-flv 拉流，使用者众多

#### 3.2.4 EasyDarwin

https://www.easydarwin.org/

![20241229154732_Gu71mfT9.webp](20241229154732_Gu71mfT9.webp)

**EasyDarwin** 是由国内开源流媒体团队维护和迭代的一整套开源流媒体视频平台框架，Golang 开发，从 2012 年 12 月创建并发展至今，包含有单点服务的开源流媒体服务器，和扩展后的流媒体云平台架构的开源框架，开辟了诸多的优质开源项目，能更好地帮助广大流媒体开发者和创业型企业快速构建流媒体服务平台，更快、更简单地实现最新的移动互联网(安卓、iOS、H5、微信)流媒体直播与点播的需求，尤其是安防行业与互联网行业的衔接。

**主要功能:**

1. 基于 Golang 语言开发维护。
2. 支持 Windows、Linux、macOS 三大系统平台部署。
3. 支持 RTSP 推流分发（推模式转发）。
4. 支持 RTSP 拉流分发（拉模式转发）。
5. 服务端录像、检索、回放。
6. 支持关键帧缓存、秒开画面。
7. Web 后台管理。
8. 分布式负载均衡。

> 总结: 只支持 rtsp 推拉流，默认端口 5541，不支持其他格式拉流，如果仅仅是监控摄像头使用，非常方便，有个网页管理后台，不会过期可以一直用，缺点是功能单一，只能在他的后台查看视频流，或者用播放器播放.

**上述 4 种流媒体服务对比:**

![20241229154732_kgiruT3T.webp](20241229154732_kgiruT3T.webp)

#### 3.2.5 MediaMTX

https://github.com/bluenviron/mediamtx

_MediaMTX_（以前称为*rtsp-simple-server*）是一个即用型、零依赖的实时媒体服务器和媒体代理，允许发布、读取、代理和记录视频和音频流。它被设想为一种“媒体路由器”，将媒体流从一端路由到另一端。

**主要功能:**

- 将直播流发布到服务器
- 从服务器读取直播流
- 流自动从一种协议转换为另一种协议
- 在不同的路径中同时提供多个流
- 将流记录到磁盘
- 验证用户身份；使用内部或外部身份验证
- 将读取器重定向到其他 RTSP 服务器（负载平衡）
- 通过 API 查询和控制服务器
- 在不断开现有客户端连接的情况下重新加载配置（热重载）
- 读取 Prometheus 兼容的指标
- 当客户端连接、断开连接、读取或发布流时运行挂钩（外部命令）
- 与 Linux、Windows 和 macOS 兼容，不需要任何依赖项或解释器，它是单个可执行文件

> 总结: 同时支持 rtsp/rtmp 推拉流，拉流还支持 hls/webrtc 两种方式，最新版本还支持了 srt 方式。推出来的 hls/webrtc 可以直接嵌入个 iframe 网页播放，没有任何依赖，如果希望直接在网页中播放无依赖，强烈推荐用 mediamtx

#### 3.2.6 Nginx-rtmp-module

https://github.com/arut/nginx-rtmp-module

Nginx 本身是一个非常出色的 HTTP 服务器,FFMPEG 是非常好的音视频解决方案.这两个东西通过一个 nginx 的模块 nginx-rtmp-module,组合在一起即可以搭建一个功能相对比较完善的流媒体服务器. 这个流媒体服务器可以支持 RTMP 和 HLS(Live Http Stream)。

**主要特性:**

1. 支持 RTMP、HLS、MPEG-DASH
2. 支持 RTMP、HLS 点播
3. 可将直播视频分段存储
4. 支持 H.264 视频编解码、AAC 音频编解码
5. 支持 FFmpeg 命令内嵌
6. 支持回调 HTTP
7. 可使用 HTTP 对直播进行删除、录播等控制
8. 具有强大的缓冲功能，可确保在效率与码率间达到平衡
9. 支持多种操作系统（Linux、MacOS、Windows）

> 总结: 只支持 rtmp 推拉流，默认端口 1935，不支持其他格式拉流，功能极其单一，不推荐。

流媒体服务器直接选择了相对比较熟悉的 **ZLMediaKit**, 能够比较方便的将 RTSP 协议转换成其他各种协议.

### 3.3 ZLMediaKit 部署

使用 docker 一键安装部署:

```yaml
version: "3.3"
services:
  app:
    image: "zlmediakit/zlmediakit:master"
    container_name: zlmediakit
    restart: unless-stopped
    environment:
      - MODE=standalone
      - TZ=Asia/Shanghai
    ports:
      - "1935:1935"
      - "8080:80"
      - "7443:443"
      - "8554:554"
      - "10000:10000"
      - "10000:10000/udp"
      - "8000:8000/udp"
      - "9000:9000/udp"
    volumes:
      - ./data/media/bin:/opt/media/bin
      - ./data/media/conf:/opt/media/conf
```

![20241229154732_WXm0i7BP.webp](20241229154732_WXm0i7BP.webp)

有上面的 WEB 管理端是使用了 [此项目](https://github.com/1002victor/zlm_webassist), 直接放在 zlm 的 www 根目录下即可.

#### 3.3.1 按需拉流

使用 API 将 RTSP 流注册到 ZLM:

```bash
curl 'http://192.168.31.11:8080/index/api/addStreamProxy?vhost=192.168.31.11&secret=AmcwaLke5ELUbJCgO46M47MR4qPiefqt&app=live1&stream=test1&url=rtsp://192.168.31.128:8554/unicast'

{
	"code" : 0,
	"data" :
	{
		"key" : "192.168.31.11/live1/test1"
	}
}
```

然后根据 ZLM 的 [URL 播放地址说明](https://github.com/ZLMediaKit/ZLMediaKit/wiki/%E6%92%AD%E6%94%BEurl%E8%A7%84%E5%88%99), 我们选择使用 mp4 在浏览器进行播放:

`http://192.168.31.11:8080/live1/test1.live.mp4`
