---
title: 《Log4j 2 官方文档》多余性（Additivity）
keywords:
  - Log4j2
  - Logger配置
  - 日志级别控制
  - Trace日志
categories:
  - 新时代码农
tags:
  - Log4j2
  - Logger配置
  - 日志级别控制
  - Trace日志
abbrlink: d6e26bb5
date: 2014-08-10 00:00:00
ai:
  - 本文介绍如何在Log4j2中配置专门的Logger来输出特定组件的TRACE级别日志，同时避免影响其他组件的日志输出。文章通过XML配置文件展示了如何为com.foo.Bar组件创建一个独立的Logger实例，并关闭了其父Logger（Root
    Logger）的自动性（additivity），以防止重复输出日志。此外，还说明了如何在配置中添加Console Appender以及设置日志格式。
description: 本文介绍如何在Log4j2中配置专门的Logger来输出特定组件的TRACE级别日志，同时避免影响其他组件的日志输出。文章通过XML配置文件展示了如何为com.foo.Bar组件创建一个独立的Logger实例，并关闭了其父Logger（Root
  Logger）的自动性（additivity），以防止重复输出日志。此外，还说明了如何在配置中添加Console Appender以及设置日志格式。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

如果我们希望输出 `com.foo.Bar` 的 TRACE 等级的日志，而不像影响其他日志的输出。简单的改变日志等级是不能达到我们想要的目的；但是修改也很简单，只要我们添加一个新的 Logger 定义就可以达到目标。

```xml
<Logger name="com.foo.Bar" level="TRACE"/>
<Root level="ERROR">
  <AppenderRef ref="STDOUT">
</Root>
```

这个配置达到了我们想要的目标，所有 `com.foo.Bar` 的日志都会被输出，而其他组件的日志仅仅会输出 `ERROR` 等级的日志。

在上面的例子，所有 `com.foo.Bar` 的日志都会被输出到控制台。这是因为为 `com.foo.Bar`  配置的 `Logger` 没有设定任何的 `Appender`。

请看如下的配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="com.foo.Bar" level="trace">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="error">
      <AppenderRef ref="Console"/>
    </Root>
  </Loggers>
</Configuration>
```

将会输出

```
17:13:01.540 [main] TRACE com.foo.Bar - entry
17:13:01.540 [main] TRACE com.foo.Bar - entry
17:13:01.540 [main] ERROR com.foo.Bar - Did it again!
17:13:01.540 [main] TRACE com.foo.Bar - exit (false)
17:13:01.540 [main] TRACE com.foo.Bar - exit (false)
17:13:01.540 [main] ERROR MyApp - Didn't do it.
```

注意 `com.foo.bar` 的 `TRACE` 日志被输出了两次。

首先 `com.foo.Bar` 关联的 `Logger` 执行了一次，直接输出到控制台。接下来这个 `Logger` 的父节点，也就是 `Root Logge`r 执行了另一次输出，这是因为日志在 `com.foo.Bar` 已经被输出，所以也会被父自动输出到控制台。这就是**多余性**，有的时候**多余性**的确是非常便捷的功能（前面的例子，我们增加了一个 `Logger`，但是没有设置 `Appender`，但是却正常工作了），有的时候却不是很方便，因此这个功能在 `Logger` 中是可以通过 `additivity` 的属性进行关闭的（设置成 false）。

> 译者注：
>
> 首先 Additivity 的确不知道该翻译成什么更合适，感觉什么“附加性”“额外性”都不是很合适，最后觉得“多余性”更贴切些，如果有好的建议望指正。
>
> 其次这个**多余性**的特点，个人认为主要是让我们使用 `Log4j2` 的时候不用为每一个 Logger 指定 `Appender` 方便配置；当然如果想单独指定 `Appender`，`Log4j2` 也是支持的。而且可以设置开关。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="com.foo.Bar" level="trace" additivity="false">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="error">
      <AppenderRef ref="Console"/>
    </Root>
  </Loggers>
</Configuration>
```

上面配置的输出（译者的输出）：

```
16:41:37.116 [main] TRACE com.foo.Bar - Enter
16:41:37.118 [main] ERROR com.foo.Bar - Did it again!
16:41:37.119 [main] TRACE com.foo.Bar - Exit with(false)
16:41:37.119 [main] ERROR com.foo.MyApp - Didn't do it.
```

一旦一个日志输出到一个 `Logger`，这个 `Logger` 的 `additivity` 设置为 `false`，那么这个日志不会再继续向父 `Logger` 进行传递，忽略其他 `Logger` 的 `additivity` 的设置。
