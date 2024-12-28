---
title: 日志重构
categories:
  - Java
tags:
  - Java
abbrlink: b3fe09a9
date: 2018-10-29 00:00:00
---

> 现有架构日志存在的问题

1. 关键逻辑无日志埋点
2. 日志级别规范
3. 生产环境日志级别不正确, 不规范
4. 日志配置不统一
5. 日志框架不统一
6. 日志打语句不规范

因此针对以上问题, 对整个项目中的日志进行规范管理

## 统一日志配置

新框架中统一使用 `log4j2` 日志框架来进行日志管理

具有的功能:

1. 根据不同的环境输出不同的日志级别
   1. 开发环境, 输出等级为 debug
   2. 测试和生成环境, 输出等级为 info
2. 开发环境, 只输出到 console
3. 测试和生产环境, 输出到 /usr/logs/app_name/port/all.log, 关闭 console 输出
4. 按天压缩日志
5. 自动删除 30 天以前的日志
6. 统一输出格式
7. 动态修改日志等级

## 现有日志修改

现在的代码暂时不能全部迁移到新框架, 考虑到现在各个模块使用的日志配置不统一, 日志配置不合理, 这里规范一下日志相关的配置

### 统一配置格式

由于老项目中一部分使用 log4j, 另一部分又使用了 log4j2 日志框架,  
配置文件一部分是 xml, 另一部分又是 properties.

为了以后迁移方便, 这里统一全部改成 xml 的配置形式.

日志框架暂时不需要改动, 因为需要改动的依赖太多, 因此这里会分 log4j.xml 和 log4j2.xml 2 种配置分别说明.

已修改的日志配置的模块有:

| 模块名            | 原日志配置       | 现日志配置 |
| ----------------- | ---------------- | ---------- |
| migu-game-service | log4j2.xml       | log4j2.xml |
| callout-tool      | log4j.xml        | log4j.xml  |
| redis-cache       | log4j.properties | log4j.xml  |
| IavpProxy         | log4j.properties | log4j.xml  |
| async-tool        | log4j.xml        | log4j.xml  |

log4j.xml 和 log4j2.xml 的配置方式不相同, 可以参考已修改的配置将还未修改的模块修改.

### 统一输出格式

log4j.xml 配置

```xml
<param name="ConversionPattern" value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%5p] - [%t] %c :: %m%n"/>
```

log4j2.xml 配置

```xml
<Property name="FILE_LOG_PATTERN">%date{yyyy-MM-dd HH:mm:ss.SSS} ${LOG_LEVEL_PATTERN} - [%t] %c{1.} :: %m%n
```

大概是这个样子

```java
2018-08-21 17:12:10.651 [ INFO] - [main] com.xxxx.msearch.toolsframework.main.Main :: 开始读取配置文件
2018-08-21 17:12:11.276 [ INFO] - [main] com.xxxx.msearch.toolsframework.main.Main :: org.quartz.threadPool.class=org.quartz.simpl.SimpleThreadPool
2018-08-21 17:12:11.277 [ INFO] - [main] com.xxxx.msearch.toolsframework.main.Main :: org.quartz.threadPool.threadCount=2
2018-08-21 17:12:11.277 [ INFO] - [main] com.xxxx.msearch.toolsframework.main.Main :: org.quartz.threadPool.threadPriority=5
```

> 日志必须显示 `日志等级`, 时间精确到毫秒

以前也说过, 显示日志等级,可以配合插件来高亮不同日志等级, 还可以设置声音提示.  
显示日志等级也有利于在现网搜索特定级别的日志.

以后直接给运维说需要某段时间特定等级或关键字的日志, 要是运维直接扔全部的日志过来, 麻烦把下面的脚本发给他

```shell
# sed -n '/开始时间/,/结束时间/p' all.log |grep '关键字' | > snippet.log
sed -n '/2018-08-21 16:27:57.569/,/2018-08-21 16:36:14.604/p' all.log |grep 'INFO' | > snippet.log
```

## 统一输出路径

具体配置需要查看已修改的模块

log4j.xml

```xml
<param name="File" value="/usr/logs/callout-tool/all.log" />
```

log4j2.xml

```xml
<property name="LOG_DEFAULT_FOLDER">/usr/logs</property>
```

测试环境和生成环境日志配置统一输出到文件, 且文件统一保存在一个日志目录下

以前的方式是将日志保存在 tomcat 的 log 目录下或者通过 JVM 启动的日志保存在启动目录下  
这样不好统一管理日志, 每次查看日志时, 还得记住哪个 tomcat 下是哪个应用.  
因此考虑将日志全部统一管理在同一个目录下, 通过应用名区分日志.

> 1.应用名配置使用 '-' 分隔, 全部采用小写

不要用大写, linux 下还得按个大小写切换键, 麻烦

```java
async-tool
iavp-proxy
migu-game-service
redis-cache
service-meeting
```

**请按照上面的命名方式命名应用名**

> 2.本地开发时需要修改为自己电脑的一个保存路径

log4j.xml

```xml
<param name="File" value="你的本机路径/应用名/all.log" />
```

log4j2.xml

```xml
<property name="LOG_DEFAULT_FOLDER">你的本机路径</property>
```

新框架中不需要这样修改, 能根据不同的环境选择输出路径;

已修改的模块日志配置默认全部输出到 `/usr/logs/` 目录下, 如果是本地开发时, 没有这个目录肯定会报错. 因此需要修改为你本地的一个目录

**如果是 windows, 路径需要转义**

比如我会建立一个专门的日志目录, 将所有的软件日志, 开发日志都输出到这个目录下, 能方便的管理日志

![image_source/2018/logging-reconstruct/15348458268711.jpg](15348458268711.webp)

推荐大家也采用这种方式

> 3.本地开发时, 需要修改日志等级

现在的日志配置针对 2 种环境

**本地开发环境**

本地开发时, 需要查看 DEBUG 信息, 且只用输出到 console

**现网环境**

现网部署时, 最低日志等级为 INFO 就好, 不需要输出 debug 级别日志, 且只需要输出到文件

log4j.xml

```xml
<log4j:configuration>

    <!-- 日志输出到控制台 -->
    <appender name="console" class="org.apache.log4j.ConsoleAppender">
        <!-- 日志输出格式 -->
        <layout class="org.apache.log4j.PatternLayout">
            <param name="ConversionPattern" value="%d{yyyy-MM-dd HH:mm:ss.SSS} [%5p] - [%t] %c :: %m%n"/>
        </layout>

        <!--过滤器设置输出的级别-->
        <filter class="org.apache.log4j.varia.LevelRangeFilter">
            <!-- 设置日志输出的最小级别 本地开发时 设置为 DEBUG, 默认为 INFO-->
            <param name="levelMin" value="INFO"/>
            <!-- 设置日志输出的最大级别 -->
            <param name="levelMax" value="ERROR"/>
        </filter>
    </appender>

    ...

    <!-- 自定义第三方类的日志等级, 添加不需要输出的日志 -->
    <log name="org.apache.zookeeper.ClientCnxn">
        <level value="ERROR"/>
    </log>
    <!-- 本地开发时, 修改为 DEBUG 默认为 INFO -->
    <log name="com.xxx">
        <level value ="INFO"/>
    </log>

    <!-- 根log的设置，若代码中未找到指定的log，则会根据继承机制，使用根log-->
    <root>
        <appender-ref ref="console"/>
        <!-- 本地开发时, 不需要输出到文件 -->
        <!-- <appender-ref ref="dailyRollingAppender"/> -->
    </root>

</log4j:configuration>
```

log4j2.xml

```xml
<!-- 对包进行更详细的配置 -->
<Asynclog name="com.xxx" level="INFO">
    <!-- 开发时, 注释掉 RollingFile , 只需要输出到 Console, 且修改为 DEBUG 级别 -->
    <appender-ref ref="Console"/>
    <appender-ref ref="RollingFile"/>
</Asynclog>

<asyncRoot level="INFO">
    <!-- 各应用自行调整，日志输出至文件，自动按时间、按文件大小进行归档 ,生产环境调默认为INFO -->
    <appender-ref level="INFO" ref="RollingFile"/>
    <!-- 日志输出至Console，仅在IDE开发时打开方便开发人员，部署到服务器之后必须置为OFF，level设置为OFF表示禁用Console控制台日志输出 -->
    <appender-ref level="INFO" ref="Console"/>
</asyncRoot>
```

以上需要修改的配置, 在新框架中都不需要手动修改

### 日志配置修改方式

其他未修改的模块, 只需要参考已修改的模块配置, 直接拷贝后, 需要修改的地方:

1. 应用名
2. 日志输出路径, 统一为 /usr/logs/应用名
3. start.sh

start.sh 中会根据 properties 中的日志配置保存日志文件, 这里统一后, 不使用这种方式, 将日志相关配置全部迁移到 log4j.xml/log4j2.xml 中, 因此需要注释掉 start.sh 对日志的相关配置, 具体可参考已修改的模块

## 日志最佳实践

现有代码存在的最大问题就是排查问题时, 没有日志可看, 不得不加入日志后再部署再看问题, 这样就很尴尬

**合理的日志等级以及日志埋点能够快速定位问题**

针对现在代码中存在的问题和以后的迁移工作, 在做需求开发时, 尽量按照以下方式修改日志相关的代码.

### 删除 printStackTrace()

**删除所有的 printStackTrace() 方法 , 改用日志输出**

e.printStackTrace 会直接输出到 System.err (如果是 tomcat 部署, 就会输出到 catalina.out)

我们的所有日志配置全部通过 log4j.xml 或者 log4j2.xml 控制,

```java
try {
	// do something
} catch (Exception e) {
   // todo 删除 printStackTrace(), 改用 log.error 输出
	e.printStackTrace();
}
```

### 使用 slf4j api

### 正确使用 error 日志级别

```java
public void error(String msg, Throwable t);
```

错误的做法:

```java
# 框架会发现最后一个参数是多余的，并查看其是否是一个异常对象，如果是则输出堆栈，否则忽略
log.error("Failed to format {}", s, e);
```

### 使用 占位符 代替 连接符, 提高效率

```java
log.info("解析错误,错误码:" + status);
```

替换为

```java
log.info("解析错误,错误码: {}", status);
```

## 基本的日志编码规范

> 以下是规范的日志写法, 希望以后开发时, 注意以下几点

1. 获取 log, 日志对象名统一使用 **log**  
   如果有父类, 统一在父类中获取 log

```java
protected log log = logFactory.getlog(getClass());
```

    如果没有父类, 在当前类中获取 log

```java
private static final log log = logFactory.getlog(类名.class);
```

可以使用 live templates 快速输入, 需要自己设置

![image_source/2018/logging-reconstruct/15357304426490.jpg](15357304426490.webp)

以上方式是没有使用 lombok 插件的情况, 如果使用, 直接在类上加 `@Slf4j` 即可, 然后使用 `log` 对象打印日志

> 如果使用新框架, 可以使用 `Logs` 工具类打印日志

2. 输出 Exceptions 的全部 Throwable 信息，因为 log.error(msg) 和 log.error(msg,e.getMessage()) 这样的日志输出方法会丢失掉最重要的 StackTrace 信息。

```java
void foo(){
        try{
            // do something
        } catch (Exception e) {
            log.error(e.getMessage()); // 错误
            log.error("Bad things", e.getMessage()); // 错误
            log.error("Bad things", e); // 正确
            // error 允许拼接字符串, 因为 error 毕竟没有 info 和 debug 多, 而且需要输出参数信息时, 也只有这种方式
            log.error("Bad things " + user, e);
        }
}
```

3. **不允许**记录日志后又抛出异常，因为这样会多次记录日志，只允许记录一次日志.

```java
void foo() throw LogException {
        try{
            // do something
        } catch (NoUserException e) {
             log.error("No user available", e);
             // 这里抛出异常后, 上级又会处理一次异常
             throw new UserServiceException("Nouseravailable", e);
        }
}
```

4. **不允许**出现 System print(包括 System.out.println 和 System.error.println) 语句
5. **不允许**出现 printStackTrace

```java
void foo() throw LogException {
        try{
            // do something
        } catch (NoUserException e) {
            e.printStackTrace(); // 错误
            log.error("No user available", e);
        }
}
```

6. 使用 slf4j 代替 log4j

   **slf4j 中的占位符—不再需要冗长的级别判断**

   在 log4j 中，为了提高运行效率，往往在输出信息之前，还要进行级别判断，以避免无效的字符串连接操作。如下：

```java
if (log.isDebugEnabled()){
        log.debug("debug：" + name);
}
```

    slf4j 巧妙的解决了这个问题：先传入带有占位符的字符串，同时把其他参数传入，在 slf4j 的内容部实现中，如果级别合适再去用传入的参数去替换字符串中的占位符，否则不用执行。

```java
log.info("{} is {}", new String[]{“x",“y"});
```

7. 不在循环中打印日志

```java
void read() {
        while (hasNext()) {
            try {
                readData();
            } catch {Exception e) {
                // this isn’t recommend
                log.error("error reading data", e);
            }
        }
}
```

如果 readData() 抛出异常并且 hasNext() 返回 true，这段代码就会不停在打印日志

```java
void read() {
        int exceptionsThrown = 0;
        while (hasNext()) {
            try {
                readData();
            } catch {Exception e) {
                    if (exceptionsThrown < THRESHOLD) {
                        log.error(“error reading data", e);
                        exceptionsThrown++;
                    } else {
                        // Now the error won’t choke the system.
                    }
            }
        }
}
```

还有一个方法就是把日志操作从循环中去掉，在另外的地方进行打印，只记录第一个或者最后一个异常就好了
