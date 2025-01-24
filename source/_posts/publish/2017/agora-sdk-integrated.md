---
title: 声网Agora SDK集成教程：Java客户端API详解
keywords:
  - 实时互动
  - 低代码应用平台
  - 声网
  - 语音通话
  - 视频通话
  - 直播
  - IM
  - 媒体流加速
  - 水晶球
  - 互动白板
  - 实时录制
  - 凤鸣AI引擎
  - Status Page
  - 灵动课堂
  - 灵隼物联网云平台
categories:
  - 新时代码农
tags:
  - 实时互动
  - 低代码应用平台
  - 声网
  - 语音通话
  - 视频通话
  - 直播
  - IM
  - 媒体流加速
  - 水晶球
  - 互动白板
  - 实时录制
  - 凤鸣AI引擎
  - Status Page
  - 灵动课堂
  - 灵隼物联网云平台
abbrlink: 7ef4d1ad
date: 2017-11-22 00:00:00
ai:
  - 声网主要提供实时互动基础能力和扩展能力，以及低代码应用平台。其产品解决低延迟、高可靠性的实时互动需求，支持海量用户同时在线，保障数据安全。业务场景包括手机端和PC端的语音聊天，支持呼叫功能、群组管理等。声网客户端API涵盖账号消息系统和频道系统，提供登录、发送消息、加入/离开频道等功能。SDK集成示例涵盖Android、Web、iOS平台。
description: 声网主要提供实时互动基础能力和扩展能力，以及低代码应用平台。其产品解决低延迟、高可靠性的实时互动需求，支持海量用户同时在线，保障数据安全。业务场景包括手机端和PC端的语音聊天，支持呼叫功能、群组管理等。声网客户端API涵盖账号消息系统和频道系统，提供登录、发送消息、加入/离开频道等功能。SDK集成示例涵盖Android、Web、iOS平台。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover)

## 声网主要产品

声网主要提供以下几类产品：

**1. 实时互动基础能力**：

- **语音通话**： 一对一，多人实时语音通话。
- **视频通话**： 一对一，多人实时视频通话。
- **直播**： 提供低延时、强同步、大并发、高质量的互动直播能力。
- **实时消息**： 超低延迟的全球信令与消息云服务。
- **即时通讯 IM**： 单聊、群聊、聊天室、系统通知等 IM 功能。
- **媒体流加速**： 具备 QoS 保障的全球端到端加速服务。

**2. 实时互动扩展能力**：

- **水晶球**： 实时监控、告警通知、通话调查、数据洞察。
- **互动白板**： H5 课件、动态 PPT、轨迹与音视频同步。
- **实时录制**： 云端录制、本地服务端录制、页面录制。
- **凤鸣 AI 引擎**： 新一代音频技术智能引擎，包括空间音频、AI 降噪、虚拟声卡等功能。
- **Status Page**： 集中展示声网主要产品及服务的综合服务质量及可用性信息。

**3. 低代码应用平台**：

- **灵动课堂**： 15 分钟上线自由品牌互动教学平台。
- **灵隼物联网云平台**： 「耳聪目明」智能硬件音视频体验升级。

## 主要解决的问题

声网产品主要解决以下问题：

- **低延迟、高可靠**： 提供低延迟、高可靠的实时互动能力，满足各类实时互动应用的需求。
- **可扩展性**： 产品支持海量用户同时在线，可扩展性强，满足不同规模的应用需求。
- **安全性**： 产品具备数据安全保障和个人隐私保护机制，确保用户数据安全。
- **易用性**： 产品提供丰富的 API 和开发文档，方便开发者快速集成和使用。
- **定制化**： 产品支持定制化开发，满足不同场景的个性化需求。

## 业务场景

手机端和 PC 端需要进行语音聊天, 主要功能为:

1. Web 端

   - 呼叫功能
     - 弹出新窗口, 呼叫按钮置灰
     - 实时监控呼叫
     - 我的车辆呼叫
     - 第三方货主派车呼叫
     - 司机管理呼叫
     - 货主接收抢单呼叫
     - 运单作业呼叫
   - 呼叫记录
     - 呼出记录
     - 呼入记录(查)

2. 客户端接口

   - 建群
   - 解散群
   - 添加成员
   - 成员列表
   - 验证消息
   - 踢人
   - 群列表
   - 用户 id 加密
   - 声网 证书 token 处理

3. 日志
   - 群组管理记录
   - 呼叫记录(写入)

## 声网名词解释

关键词:

**App ID**

开发者在我们官网注册后，可以创建多个项目，每一个项目对应的唯一标识就是 App ID。 如果有人非法获取了你的 App ID，他将可以在 Agora 提供的 SDK 中使用你的 App ID，如果他知道你的频道名字，甚至有可能干扰你正常的通话。

所以建议仅在测试阶段或对安全性要求不高的场景里使用 App ID。

使用不同 App ID 的应用程序是不能互通的。如果已在通话中，用户必须调用 leaveChannel() 退出当前通话，才能进入下一个频道

**Dynamic Key**

当项目准备正式上线运营，建议开发者采用 Dynamic Key，这是一个更为安全的用户身份验证方案。针对不同的服务，Dynamic Key 有不同的名称:

1. Channel Key 用于加入频道;
2. Signaling Key 用于登录信令系统;

**App Certificate**

将您的 App Certificate 保存在服务器端，且对任何客户端均不可见。
通常 App Certificate 在启用一小时后生效。

当项目的 App Certificate 被启用后，您必须使用 Dynamic Key。例如: 在启用 App Certificate 前，您可以使用 App ID 加入频道。但启用了 App Certificate 后，您必须使用 Channel Key 加入频道。

**channel**

标识通话的频道名称，长度在 64 字节以内的字符串

可以理解为房间名

要进行语音或者视频, 不同的用户都必须在同一个 channel 中

![20241229154732_jLP435rJ.webp](https://cdn.dong4j.site/source/image/20241229154732_jLP435rJ.webp)

**channel key**

安全要求不高: 将值设为 null
安全要求高: 将值设置为 Channel Key。 如果你已经启用了 App Certificate, 请务必使用 Channel Key。

**UID**

用户位移表示

同一个频道里不能出现两个相同的 UID。如果你的 App 支持多设备同时登录，即同一个用户账号可以在不同的设备上同时登录 (例如微信支持在 PC 端和移动端同时登录)，请保证传入的 UID 不相同。 例如你之前都是用同一个用户标识作为 UID, 建议从现在开始加上设备 ID, 以保证传入的 UID 不相同 。如果你的 App 不支持多设备同时登录，例如在电脑上登录时，手机上会自动退出，这种情况下就不需要在 UID 上添加设备 ID。

**信令 和 通信**

> 频道，可以理解成通讯的房间，信令和通信中的频道是一个意思，只不过，信令是确认进入房间，通信是在房间内聊天。

https://dev.agora.io/cn/question/1780

**群组**

**通话统计**

### App 的用户之间要建立和发起一个呼叫，整个流程是怎样的？

以 A 呼叫 B 为例，一般呼叫流程如下:

1. A 向信令服务器发起呼叫请求。

2. 信令服务器检查 B 是否在线:

- 如不在线，向 A 返回 B 不在线错误。
- 如在线，信令服务器生成频道名，返回给 A；并向 B 投递呼叫信令。

3. A 收到信令服务器返回的频道名，准备加入语音频道。此时为加快进频道速度，可以提前进入频道待命:

- A 调用 muteLocalAudioStream(true) 和 muteLocalVideoStream(true)（如有视频功能）禁止发送音视频数据。
- 调用 joinChannel 进入频道。

4. B 收到信令服务器投递过来的 A 的呼叫请求。

- B 响铃。 为加快进频道速度，可以提交进入频道待命。
- B 调用 muteLocalAudioStream(true) 和 muteLocalVideoStream(true)（如有视频功能）禁止发送音视频数据。

5. A 调用 joinChannel 进入频道:
   - 如 B 拒绝请求:
     - B 调用 leaveChannel 退出频道
     - B 向信令服务器返回拒绝应答
     - 信令服务器向 A 返回 B 拒绝应答信令
     - A 调用 leaveChannel 退出频道
   - 如 B 接受请求:
     - B 调用 muteLocalAudioStream(false) 和 muteLocalVideoStream(false) 开始发送音视频数据
       - B 向信令服务器返回接受应答信令
       - 调用 muteLocalAudioStream(false) 和 muteLocalVideoStream(false) 开始发送音视频数据

![20241229154732_2cqjFJCm.webp](https://cdn.dong4j.site/source/image/20241229154732_2cqjFJCm.webp)

呼叫失败或者成功, 客户端需要调用 xxx 接口写日志

![20241229154732_GzUptBTW.webp](https://cdn.dong4j.site/source/image/20241229154732_GzUptBTW.webp)

![20241229154732_OPhFa2GG.webp](https://cdn.dong4j.site/source/image/20241229154732_OPhFa2GG.webp)

客户端呼叫 货主 (TMS/货主 app) 需要发起 2 个呼叫, 当一方接通时, 回调中关闭另一个呼叫 4

## 声网客户端 API

### 账号消息系统

#### 登录

```java
public void login(String appId,String account,String token,int uid,String deviceID);

public void login2(String appId,String account,String token,int uid,String deviceID,int retry_time_in_s, int retry_count);
```

#### 登出

```java
public void logout();
```

#### 检查当前是否在线 (isOnline)

```java
public int isOnline();
```

#### 发送点对点消息 (messageInstantSend)

```java
public void messageInstantSend(String account,int uid,String msg,String msgID);
```

#### 设置用户属性 (set_attr)

```java
public void set_attr(String name,String value);
```

#### 获取自己的属性 (get_attr)

```java
public void get_attr(String name);
```

#### 获取自己的全部属性 (get_attr_all)

```java
public void get_attr_all();
```

#### 获取某个用户的属性 (get_user_attr)

```java
public void get_user_attr(String account,String name);

```

#### 获取某个用户的所有属性 (get_user_attr_all)

```java
public void get_user_attr_all(String account);
```

### 频道系统

### 加入频道 (channelJoin)

```java
public void channelJoin(String channelID);
```

让用户加入指定频道。用户一次只能加入一个频道。如加入指定频道时已在其他频道中，将自动从其他频道退出。

用户加入频道成功后，自己将收到回调 onChannelJoined，其他同一频道内用户将收到回调 onChannelUserJoined。用户加入失败后，自己将收到回调 onChannelJoinFailed。

#### 离开频道 (channelLeave)

```java
public void channelLeave(String channelID);
```

#### 查询频道用户数 (channelQueryUserNum)

```java
public void channelQueryUserNum(String channelID);
```

#### 设置频道属性 (channelSetAttr)

```java
public void channelSetAttr(String channelID,String name,String value);
```

#### 删除频道属性 (channelDelAttr)

```java
public void channelDelAttr(String channelID,String name);
```

#### 删除所有频道属性 (channelClearAttr)

```java
public void channelClearAttr(String channelID);
```

#### 发送频道消息 (messageChannelSend)

```java
public void messageChannelSend(String channelID,String msg,String msgID);
```

### 呼叫系统

#### 发起呼叫 (channelInviteUser)

```java
public void channelInviteUser(String channelID,String account,int uid);

public void channelInviteUser2(String channelID,String account,String extra);
```

该方法用于发起呼叫，即邀请某用户加入某个频道。呼叫和加入频道，是两个独立的过程。用户必须自己再另行加入频道，用户可以选择：先加入频道，再发送呼叫邀请或先发送呼叫邀请，对方接受后再加入频道。如果呼叫失败，会回调 onInviteFailed。可能的原因有：

1. 对方不在线；
2. 本端网络不通；
3. 服务器异常

#### 接受呼叫 (channelInviteAccept)

```java
public void channelInviteAccept(String channelID,String account,int uid);
```

#### 拒绝呼叫 (channelInviteRefuse)

```java
public void channelInviteRefuse(String channelID,String account,int uid);
```

#### 结束呼叫 (channelInviteEnd)

```java
public void channelInviteEnd(String channelID,String account,int uid);
```

## 声网 SDK 集成

### API demo

**Android**

```java
RtcEngine rtcEngine = RtcEngine.create(mContext, appId, mEngineEventHandler.mRtcEventHandler);
rtcEngine.joinChannel(null, channel, "Extraoptional data", uid);
mRtcEngine.leaveChannel();
```

**Web**

```javascript
var client = AgoraRTC.createRtcClient();
client.init(
  appId,
  function () {
    client.join(appId, channel, undefined, successCallback, errorCallback);
  },
  errorCallback
);
```

**iOS**

```javascript
let engine = AgoraRtcEngineKit.sharedEngineWithAppId("AppId", delegate: self)
engine.enableVideo()
engine.joinChannelByKey(nil, channelName: "channelName", info: nil, uid: 0, joinSuccess: nil)
```
