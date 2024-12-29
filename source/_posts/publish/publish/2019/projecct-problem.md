---
title: 项目中存在的问题
categories:
  - Java
tags:
  - Java
abbrlink: 6dc04ed2
date: 2019-08-20 00:00:00
---

### Maven 相关问题

> 由于未统一管理多个模块的 jar 依赖, 每个模块都各自为政;  
> 模块之间的配置相互拷贝, 有用的没用的都拷了;  
> 升级版本麻烦, 每个相关模块都得改版本.

![20241229154732_FDHGxHtL.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_FDHGxHtL.webp)

**1. 重复的依赖**

redis-cache 模块的 pom.xml

![20241229154732_ugonm1Ts.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ugonm1Ts.webp)

![20241229154732_1fVuV7vs.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_1fVuV7vs.webp)

**2. 重复的插件**

mamagesystem 模块的 pom.xml

![20241229154732_0GDyIBF8.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_0GDyIBF8.webp)

**3. 依赖冲突**

mamagesystem 模块的 pom.xml

![20241229154732_lWO9h9OG.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_lWO9h9OG.webp)  
**4. 重复的配置**

![20241229154732_h4IF53kV.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_h4IF53kV.webp)

#### 导致的问题

有可能导致出现以下几种异常:

1. java.lang.ClassNotFoundException
2. java.lang.NoSuchMethodError
3. java.lang.NoClassDefFoundError

#### 解决方案

> 所有模块使用一个父模块来管理  
> 将重复配置迁移到 parent pom.xml 中;  
> 使用 `dependencyManagement` 来统一管理 jar 依赖;  
> 使用 `pluginManagement` 统一管理插件依赖;  
> 所有 jar 依赖的版本全部使用 `properties` 管理;  
> 使用 `excludes` 排除冲突的 jar 包;

## 代码问题

### 1. 代码不规范

<!-- 没有规矩不成方圆, 没有规范写不出漂亮的代码 -->

1. 格式化风格不统一

   _会造成大量代码冲突_

   一个项目组应该使用统一的格式化风格 (google-java-style)

2. 编码不统一

   _造成不同开发平台的同学乱码_

3. 命名不规范;

   _不符合 Javaer 的核心价值观, 审美观_

   **变量名:** 方法名你不用驼峰命名法, 你用下划线分隔, 你咋不去写 Python 呢

### 2. 代码无注释

<!-- 代码及注释, 好的代码不需要注释, 写了一段很好的代码, 命名也很容易理解也很规范, 逻辑清楚, 就是很牛逼的一段代码, 一段时间后, 再来看, 恩, 这是一段很牛逼的代码, 就是看不懂…. -->

1. 类注释

对已有的类添加注释

    ```java
    /**
     * <p>Company: xxxx公司 </p>
     * <p>Description: callout 号码解析处理类</p>
     *
     * @author xxx
     * @date 2018-05-31  21:40
     */
     ```

新建类时自动添加

    ```java
    /**
     * <p>Company: xxxx公司 </p>
     * <p>Description: ${description}</p>
     *
     * @author     dong4j
     * @date       ${YEAR}-${MONTH}-${DAY} ${HOUR}:${MINUTE}
     * @email      dong4j@gmail.com
     */
     ```

2. 方法注释

   ```java
   /**
    * 根据规则将数据插入相应的表
    *
    * @param batchOfTask the batch of task		                批次任务详情
    * @param telNos      the tel nos			                zip 包中处理后的号码
    * @throws InterruptedException the interrupted exception   sleep 失败时抛出此异常
    */
   ```

3. 代码注释

   成员变量用 `/** 注释 */`
   行注释放在代码上一行, 不要使用行尾注释
   大段代码注释后 建议使用

   ```java
   //<editor-fold desc="Description">
   多行注释代码
   //</editor-fold>
   ```

   或者

   ```java
   //region Description
   多行注释代码
   //endregion
   ```

### 3. 开发文档不全

应该为每个模块添加一个 `readme.md` 和 `changelog.md` 文件  
`readme.md` 用于记录该模块的一些基本信息, 比如用到的技术, 功能, 使用方法, 部署方式等;  
`changelog.md` 用于记录该模块的更新记录;

**便于维护与交接**

### 4. 代码的优化

**1. String 拼接**

```java
List<CoreSong> listSong = coreSongService.findTopicRingBoxByParam(params);
if (listSong != null && listSong.size() > 0) {
    for (CoreSong c : listSong) {
        taskSongIds += c.getId() + "|";
    }
    model.addAttribute("listSong", listSong);
}
```

<!--JDK1.5 之前-->

<!--JDK1.5 之后-->

**2. 日志相关**

**logger.error 的错误用法**

![20241229154732_kGZ5xPz5.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_kGZ5xPz5.webp)

**logger.error 的正确使用姿势**

![20241229154732_45ESzjrR.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_45ESzjrR.webp)

**使用 printStackTrace()**

![20241229154732_mSA1vWPz.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_mSA1vWPz.webp)  
**不使用 printStackTrace()**

![20241229154732_sAgeQ39m.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_sAgeQ39m.webp)

> 应用中不可直接使用日志系统（Log4j, Logback）中的 API  
> 而是使用 SLF4J 中的 API，使用门面模式的日志框架，有利于维护和各个类的日志处理方式统一

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

...
private static final Logger logger = LoggerFactory.getLogger(Abc.class);
```

**建议使用 log4j2 日志代替 log4j**

日志拼接的耗时对比

```java
@Test
public void testLog1() {
    String[]  traceIds  = {"天王盖地虎", "小鸡炖蘑菇"};
    StopWatch stopwatch = new StopWatch();
    stopwatch.start();
    for (int i = 0; i < 10000000; i++) {
        log.info("traceId[1] = " + traceIds[0] +
                 "traceId[1] = " + traceIds[1] +
                 "traceId[1] = " + traceIds[0] +
                 "traceId[1] = " + traceIds[1]);
    }
    stopwatch.stop();
    System.out.println(stopwatch.prettyPrint());
}

@Test
public void testLog2() {
    String[]  traceIds  = {"天王盖地虎", "小鸡炖蘑菇"};
    StopWatch stopwatch = new StopWatch();
    stopwatch.start();
    for (int i = 0; i < 10000000; i++) {
        if (log.isInfoEnabled()) {
            log.info("traceId[1] = " + traceIds[0] +
                     "traceId[1] = " + traceIds[1] +
                     "traceId[1] = " + traceIds[0] +
                     "traceId[1] = " + traceIds[1]);
        }
    }
    stopwatch.stop();
    System.out.println(stopwatch.prettyPrint());
}

@Test
public void testLog3() {
    String[]  traceIds  = {"天王盖地虎", "小鸡炖蘑菇"};
    StopWatch stopwatch = new StopWatch();
    stopwatch.start();
    for (int i = 0; i < 10000000; i++) {
        log.info("traceId[1] = {}, traceId[1] = {}, traceId[1] = {}, traceId[1] = {}",
                 traceIds[0], traceIds[1],
                 traceIds[0], traceIds[1]);
    }
    stopwatch.stop();
    System.out.println(stopwatch.prettyPrint());
}
```

```java
StopWatch '': running time (millis) = 1268
-----------------------------------------
ms     %     Task name
-----------------------------------------
01268  100%

StopWatch '': running time (millis) = 22
-----------------------------------------
ms     %     Task name
-----------------------------------------
00022  100%

StopWatch '': running time (millis) = 38
-----------------------------------------
ms     %     Task name
-----------------------------------------
00038  100%
```

## 推荐的工具

### Markdown 工具

Mac 下有很多这种工具, 目前使用 MWeb;

Windowns 的话, 建议使用 Typora, 配合 PicGo 上传图片;

### Chrome 插件

**1. 流程图制作工具**

![20241229154732_UO1YJr9v.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_UO1YJr9v.webp)  
**2. Imagus**

鼠标悬浮停留在图片上，自动弹出放大图片，不用再在新链接中打开看大图了。

**3. SimpleExtManager**

![20241229154732_EiDncgsn.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_EiDncgsn.webp)  
**4. Octotree**

同类插件 `GitCodeTree`

![20241229154732_RUf9YYSd.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_RUf9YYSd.webp)

**5. Session Buddy**

下班了, 资料没看完, 可以保存下来

![20241229154732_HVHOpUjd.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_HVHOpUjd.webp)

### Intellij IDEA 插件

**1. JRebel for IntelliJ**

热部署插件，Java WEB 开发必备，节省生命。**墙裂推荐**

**2. Lombok Plugin**

使用注解自动生成代码，偷懒者必备。

**3. RestfulToolkit**

Java WEB 开发必备，再也不用全局搜索 RequestMapping 了

![20241229154732_hp123tER.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_hp123tER.webp)

直接搜索 RequestMapping

![20241229154732_dWncftDM.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_dWncftDM.webp)

**4. Translation**

翻译插件，很好用。 **墙裂推荐**

![20241229154732_GcBDf7PW.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_GcBDf7PW.webp)

**5. Grep Console**

高亮 log 不同级别日志，看日志的时候一目了然。

![20241229154732_kTuQuaqO.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_kTuQuaqO.webp)

**6. GenerateSerialVersionUID**

Alt + Insert 生成 serialVersionUID

**7. Alibaba Java Coding Guidelines**

阿里巴巴规范

**8. Rainbow Brackets**

彩虹括号。自动给代码块内花括号和括号加色，让视野更加注意在代码上。

![20241229154732_EOEuuP5M.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_EOEuuP5M.webp)

**9. Maven Helper**

Maven 插件，安装后可查看依赖以及冲突，一目了然。

![20241229154732_l9LObZVr.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_l9LObZVr.webp)

**12. zookeeper**

就是太慢了, 没有用异步接口, 经常卡住

![20241229154732_SEm37MkN.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_SEm37MkN.webp)

**13. GenerateAllSetter**

new POJO 类的快速生成 set 方法

```java
User user = new User();
// then alt+enter on User
// will generate following
user.setName("");
user.setPassword("");
```

### 终端工具

**1. zsh**

1. 大小写字母自动更正
2. 更强大的 tab 补全
3. 智能的切换目录
4. 命令选项补齐
5. kill 进程号补齐

**2. oh my zsh**

1. 主题
2. 插件
