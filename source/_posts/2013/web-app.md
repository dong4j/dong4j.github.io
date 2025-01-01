---
title: Web app开发：成本与体验的权衡之道
keywords:
  - 社交化在线商店
  - Android 客户端
  - iOS 客户端
  - Java 后台
  - Web app 开发
  - Native App
  - 数据交互
  - Redis 搭建
  - SVN 版本控制
categories:
  - 新时代码农
tags:
  - 社交化在线商店
  - Android 客户端
  - iOS 客户端
  - Java 后台
  - Web app 开发
  - Native App
  - 数据交互
  - Redis 搭建
  - SVN 版本控制
abbrlink: 390ff665
date: 2013-01-03 00:00:00
ai:
  - 本文讲述了作者在开发一个社交化的在线商店过程中遇到的挑战和解决方案。文章首先介绍了项目的技术架构，包括 Android 和 iOS 客户端、Java 后台以及前端
    Web app 的开发。接着分析了 Native App 和 Web App 的区别，强调了 Native App 在用户体验和功能实现上的优势，同时也指出了其更新成本高和维护复杂的问题。随后，作者详细描述了
    Java Web 开发与 Web app 数据交互的区别，并举例说明了客户端登录流程的具体实现。最后，文章讨论了在开发过程中遇到的两个问题：Windows
    下搭建 Redis 服务器和 SVN 版本控制问题，并提供了相应的解决方法。
description: 本文讲述了作者在开发一个社交化的在线商店过程中遇到的挑战和解决方案。文章首先介绍了项目的技术架构，包括 Android 和 iOS 客户端、Java
  后台以及前端 Web app 的开发。接着分析了 Native App 和 Web App 的区别，强调了 Native App 在用户体验和功能实现上的优势，同时也指出了其更新成本高和维护复杂的问题。随后，作者详细描述了
  Java Web 开发与 Web app 数据交互的区别，并举例说明了客户端登录流程的具体实现。最后，文章讨论了在开发过程中遇到的两个问题：Windows 下搭建
  Redis 服务器和 SVN 版本控制问题，并提供了相应的解决方法。
---

最近在做一个社交化的在线商店, 有 Android 和 iOS 客户端, 后台使用 java, 我主要负责接口设计和实现.
目前产品已经上线, 现在主要是前端的业务流程优化, 后台的优化和需求更改. 客户端使用 Web app + Native app 的形式.
对于菜鸟级我的来说, 以前的小项目都是 10 多张表就搞定了, 现在这个项目有 170 多张表, 想来要完全熟悉全部的业务流程需要花写功夫了.
以前都是写的 Java Web 项目, 现在一下来写 Web app 项目有点不习惯, 主要是测试有点麻烦. 接下来, 我将写写来对项目的总体认识以及 Web app 开发和 Java Web 开发的区别 (其实也没多大区别), 算是做一个总结吧.

### Web app 和 Native app 的区别

**Native App：**

1. 开发成本非常大。一般使用的开发语言为 Java、C++、Objective-C。
2. 更新体验较差、同时也比较麻烦。每一次发布新的版本，都需要做版本打包，且需要用户手动更新（有些应用程序即使不需要用户手动更新，但是也需要有一个恶心的提示）。
3. 非常酷。因为 Native app 可以调用 iOS 中的 UI 控件以 UI 方法，它可以实现 Web app 无法实现的一些非常酷的交互效果。
4. Native app 是被 Apple 认可的。Native app 可以被 Apple 认可为一款可信任的独立软件，可以放在 Apple Stroe 出售，但是 Web app 却不行。

**Web App：**

1. 开发成本较低。使用 Web 开发技术就可以轻松的完成 Web app 的开发。
2. 升级较简单。升级不需要通知用户，在服务端更新文件即可，用户完全没有感觉。
3. 维护比较轻松。和一般的 Web 一样，维护比较简单，它其实就是一个站点。

Web app 说白了就是一个针对 iPhone、Android 优化后的 Web 站点，它使用的技术无非就是 HTML 或 HTML5、CSS3、JavaScript，服务端技术 Java、PHP、ASP。

说到这里, 我曾经想过, 为什么不直接写一个 Java Web 项目, 然后做一个 Web app 直接访问这个网站, 只要网站是响应式的, 这样就不需要做多少更改让手机和 PC 都能以较好的方式访问, 不用针对手机特定来开发一款 app.  
但是查了下资料, 这种方式有很多弊端:

1. 最最重要的一点, 这种 app 其实就是一个浏览器, 虽然开发速度快, 但是不可能通过 AppStore 的审核, 国内几个较大的 Android 市场也通过不了;
2. 做 app 就是做良心, 给人以最好的用户体验, 如果网络环境不佳的话, 就是一个大白页, 用户体验值为 0;
3. 因为 CSS 和 JS 资源不在本地, 需要远程载入, 如果使用比较大的前端框架, 如 bootstrap 之类时, 加上现在 4G 的普及, 用户使用 app 逛下商城, 买买东西, 一套房子就没用了….
4. 在网页中经常使用的 jQuery 框架在 webview 里的速度并不理想, 再如果不是 ajax 的网页请求, 每次操作都要条抓和网页渲染, 想想我也是醉了.

所以说为了尽快上线而不管用户体验的老板都不是司机. 我们公司的老板还行, 没用使用这种方式, 而是使用 Hrbird app(老板声音有点像杰森 · 斯坦森, 不知道是不是嗨歌嗨到嗓子哑了….)

### Java Web 与 Web app 数据交互的区别

对于 Java Web 开发, 客户端向服务器发出请求, 给上一些参数, 然后查询数据库, 返回数据到前台, 这个流程也同样适用于 Web app, 只是 Web app 更多的是直接返回 json 格式的数据.  
我们常说的 app 接口开发, 对于初学者, 可能一下就想到了 interface(其实我也是这么想的), 但是这是不准确的.  
比如现在我负责的接口开发, 是要负责从 Controller 到 Service 到数据库最后返回 json 数据这么一整条流程的开发. 当用户点击 app 上一个按钮或者查看详细信息时, app 会调用我们写好的接口 (其实说白了就是一 URL), 然后经过 DispatcherServlet 根据 URL 调用特定的 Controller 进行处理, 最后返回 json 数据给 app.

**举个最简单的例子, 用户登录.**  
一个 web 系统, 用户通过浏览器把用户名密码传递到 web 服务端, 也就是后台, 那么这里就有个 URL 比如叫 `XXX\user\login.action?userid=zhangsan&pwd=123`
然后你后台就能获取到 userid 和 pwd 然后就能返回给浏览器成功与否.  
同样的道理,  
app 调用 `XXX\user\login.action?userid=zhangsan&pwd=123`  
你后台一样能获取到 userid 和 pwd 那么你就可以给安卓 APP 返回信息告诉他登录成功与否.  
所以这里所谓的接口, 就是一个 URL ,

接口返回 json 或 xml 就可以了，然后你开发的当然是知道接口的 url 了，还有接口的传参，这样就可以让前端调用了。  
告诉前端，你的 url 地址，需要给这个接口传什么参数，返回参数是什么（返回他们可以测试得到，不过最好还是先告诉他们），字段说明，这样就可以交互了.

### 说说客户端的登录

来公司的第一天就看的实现登录的代码, 与 Java web 最大的区别就是一般 web 是使用 session 验证登录状态，而 app 则使用 token 来验证登录状态（token 是自己定义的一个和用户 ID 相关的加密字符串，传入后台后从数据库查询用户信息）。还有如果对安全性要求较高，app 传输数据时可能会对数据进行加密，而 web 一般没有这一步，web 的加密一般是使用 https。

#### 不安全的方式

**在 app 中保存登录数据, 每次调用接口时传输**  
为了偷懒, 程序员什么都干得出来. 在用户登录之后, 直接把用户名和密码保存在本地, 然后每次调用后端接口时作为参数传递, 但是这种方式及其不安全, 随便那个嗅探器就可以把用户名密码弄到手, 如果用户习惯所有的地方都使用同一用户名和密码, 那么黑客通过撞库的方式能把用户的所有信息一锅端 (这也是为什么不要使用公共场合的 wifi).

#### 安全的登录方式

**登录时请求一次 token, 之后用 token 调用接口 (公司就是这么搞的)**  
大体的流程:

1. 用户输入电话号码和密码
2. 在数据库中查询有无此电话号码, 没有则提示错误; 有则再验证密码是否正确;
3. 如果登录成功, 调用 api 生成 token(使用 Base64 加密, 使用 URLEncoder 解决中文参数问题) ;
4. 将 key = 客户 ID,value=token 放入 redis 缓存
5. 返回客户信息

以后用户请求时, 都会带上 token 这个参数, 当 token 过时后将跳转到登录界面重新登录

### 遇到的问题

#### 在 windows 下搭建 redis 服务器

项目中用到了 redis 作用缓存服务器, 以前从来没有使用过, 所以学习了下载 windows 下搭建 redis 服务器.  
redis 是一个开源的、使用 C 语言编写的、支持网络交互的、可基于内存也可持久化的 Key-Value 数据库。这里就不做过多介绍了, 有兴趣可以去百度一下.

由于 Redis 官网不支持 windows 的, 只是 Microsoft Open Tech group 在 GitHub 上开发了一个 Win64 的版本, 项目地址是：  
[https://github.com/MSOpenTech/redis](https://github.com/MSOpenTech/redis)

打开以后，可以直接使用浏览器下载，或者 git 克隆。  
可以在项目主页右边找到 zip 包下载  
下载解压，没什么好说的，在解压后的 bin 目录下有以下这些文件：

```
redis-benchmark.exe         #基准测试
redis-check-aof.exe         # aof
redis-check-dump.exe        # dump
redis-cli.exe               # 客户端
redis-server.exe            # 服务器
redis.windows.conf          # 配置文件
```

启动服务器命令: redis-server redis.windows.conf  
可以写一个批处理命令, 以后直接双击启动, 关闭 cmd 窗口就关闭了服务器

我第一次启动报错了

> redis-server.exe redis.windows.conf  
> [7736] 10 Aug 21:39:42.974 #  
> The Windows version of Redis allocates a large memory mapped file for sharing  
> the heap with the forked process used in persistence operations. This file  
> will be created in the current working directory or the directory specified by  
> the ‘dir’ directive in the .conf file. Windows is reporting that there is  
> insufficient disk space available for this file (Windows error 0x70).
>
> You may fix this problem by either reducing the size of the Redis heap with  
> the –maxheap flag, or by starting redis from a working directory with  
> sufficient space available for the Redis heap.
>
> Please see the documentation included with the binary distributions for more  
> details on the –maxheap flag.
>
> Redis can not continue. Exiting.

根据提示，是 maxheap 标识有问题, 打开配置文件 redis.windows.conf , 搜索 maxheap , 然后直接指定好内容即可.

```
.......
#
# maxheap <bytes>
maxheap 1024000000
.......
```

再次启动服务器  
![20241229154732_5mnRTEhd.webp](20241229154732_5mnRTEhd.webp)

然后使用自带的客户端工具进行测试  
![20241229154732_mA8ER0ZT.webp](20241229154732_mA8ER0ZT.webp)

成功了, 玩儿去吧

#### svn 版本控制问题

整个工程使用 Maven, 并使用 svn 进行版本控制, 但是当导入工程时报 svn 错误, 开始怀疑配置不正确, 进入 intellij 的 svn 设置, 去掉所有的复选框  
![20241229154732_baVEVepE.webp](20241229154732_baVEVepE.webp)

还是报错, 查询资料后发现 1.8 使用了命令工具（command line client tools）默认安装 SVN 时是未安装此客户端的。  
![20241229154732_8P0pRg2X.webp](20241229154732_8P0pRg2X.webp)

重新安装乌龟, 然后把命令工具选上, svn 配置不变, 都不勾选, 然后重启 IDEA 就可以了.
