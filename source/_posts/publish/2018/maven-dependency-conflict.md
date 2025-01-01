---
title: Java开发者的痛：如何避免和解决常见的Jar包冲突问题
categories:
  - 新时代码农
tags:
  - Java
  - JAR包冲突
  - Maven
  - 依赖管理
abbrlink: a65dfb13
date: 2018-07-15 00:00:00
ai:
  - 本文深入探讨了Java应用程序中的JAR包冲突问题，分析了导致这类问题的本质原因和常见表象。文章指出，JAR包冲突主要分为两类：第一类是由于依赖管理中不同版本的同名JAR包导致的；第二类则是由于多个不同JAR包中存在同名类导致的加载顺序问题。文章详细解释了Maven的仲裁机制、JAR包的加载顺序以及这些因素如何导致冲突。同时，文章还提供了针对这些问题排查和解决的策略，包括良好的依赖管理习惯和使用冲突检测插件等方法来有效避免和解决JAR包冲突问题。
description: 本文深入探讨了Java应用程序中的JAR包冲突问题，分析了导致这类问题的本质原因和常见表象。文章指出，JAR包冲突主要分为两类：第一类是由于依赖管理中不同版本的同名JAR包导致的；第二类则是由于多个不同JAR包中存在同名类导致的加载顺序问题。文章详细解释了Maven的仲裁机制、JAR包的加载顺序以及这些因素如何导致冲突。同时，文章还提供了针对这些问题排查和解决的策略，包括良好的依赖管理习惯和使用冲突检测插件等方法来有效避免和解决JAR包冲突问题。
keywords:
  - Java
  - JAR包冲突
  - Maven
  - 依赖管理
---

Jar 包冲突是老生常谈的问题，几乎每一个 Java 程序猿都不可避免地遇到过，并且也都能想到通常的原因一般是同一个 Jar 包由于 maven 传递依赖等原因被引进了多个不同的版本而导致，可采用依赖排除、依赖管理等常规方式来尝试解决该问题，但这些方式真正能彻底解决该冲突问题吗？答案是否定的。笔者之所以将文章题目起为 “重新看待”，是因为之前对于 Jar 包冲突问题的理解仅仅停留在前面所说的那些，直到在工作中遇到的一系列 Jar 包冲突问题后，才发现并不是那么简单，对该问题有了重新的认识，接下来本文将围绕 Jar 包冲突的问题本质和相关的解决方案这两个点进行阐述。

# Jar 包冲突问题

## 一、冲突的本质

Jar 包冲突的本质是什么？Google 了半天也没找到一个让人满意的完整定义。其实，我们可以从 Jar 包冲突产生的结果来总结，在这里给出如下定义（此处如有不妥，欢迎拍砖  -）：

> **Java 应用程序因某种因素，加载不到正确的类而导致其行为跟预期不一致。**

具体来说可分为两种情况：1）应用程序依赖的同一个 Jar 包出现了多个不同版本，并选择了错误的版本而导致 JVM 加载不到需要的类或加载了错误版本的类，为了叙述的方便，笔者称之为**第一类 Jar 包冲突问题**；2）同样的类（类的全限定名完全一样）出现在多个不同的依赖 Jar 包中，即该类有多个版本，并由于 Jar 包加载的先后顺序导致 JVM 加载了错误版本的类，称之为**第二类 Jar 包问题**。这两种情况所导致的结果其实是一样的，都会使应用程序加载不到正确的类，那其行为自然会跟预期不一致了，以下对这两种类型进行详细分析。

### 1.1 同一个 Jar 包出现了多个不同版本

随着 Jar 包迭代升级，我们所依赖的开源的或公司内部的 Jar 包工具都会存在若干不同的版本，而版本升级自然就避免不了类的方法签名变更，甚至于类名的更替，而我们当前的应用程序往往依赖特定版本的某个类  **M** ，由于 maven 的传递依赖而导致同一个 Jar 包出现了多个版本，当 maven 的仲裁机制选择了错误的版本时，而恰好类  **M**  在该版本中被去掉了，或者方法签名改了，导致应用程序因找不到所需的类  **M**  或找不到类  **M**  中的特定方法，就会出现第一类 Jar 冲突问题。可总结出该类冲突问题发生的以下三个必要条件：

- 由于 maven 的传递依赖导致依赖树中出现了同一个 Jar 包的多个版本
- 该 Jar 包的多个版本之间存在接口差异，如类名更替，方法签名更替等，且应用程序依赖了其中有变更的类或方法
- maven 的仲裁机制选择了错误的版本

### 1.2 同一个类出现在多个不同 Jar 包中

同样的类出现在了应用程序所依赖的两个及以上的不同 Jar 包中，这会导致什么问题呢？我们知道，同一个类加载器对于同一个类只会加载一次（多个不同类加载器就另说了，这也是解决 Jar 包冲突的一个思路，后面会谈到），那么当一个类出现在了多个 Jar 包中，假设有  **A** 、 **B** 、 **C**  等，由于 Jar 包依赖的路径长短、声明的先后顺序或文件系统的文件加载顺序等原因，类加载器首先从 Jar 包  **A**  中加载了该类后，就不会加载其余 Jar 包中的这个类了，那么问题来了：如果应用程序此时需要的是 Jar 包  **B**  中的类版本，并且该类在 Jar 包  **A**  和  **B**  中有差异（方法不同、成员不同等等），而 JVM 却加载了 Jar 包  **A**  的中的类版本，与期望不一致，自然就会出现各种诡异的问题。

从上面的描述中，可以发现出现不同 Jar 包的冲突问题有以下三个必要条件：

- 同一个类  **M**  出现在了多个依赖的 Jar 包中，为了叙述方便，假设还是两个： **A**  和  **B**
- Jar 包  **A**  和  **B**  中的该类  **M**  有差异，无论是方法签名不同也好，成员变量不同也好，只要可以造成实际加载的类的行为和期望不一致都行。如果说 Jar 包  **A**  和  **B**  中的该类完全一样，那么类加载器无论先加载哪个 Jar 包，得到的都是同样版本的类  **M** ，不会有任何影响，也就不会出现 Jar 包冲突带来的诡异问题。
- 加载的类  **M**  不是所期望的版本，即加载了错误的 Jar 包

## 二、冲突的产生原因

### 2.1 maven 仲裁机制

当前 maven 大行其道，说到第一类 Jar 包冲突问题的产生原因，就不得不提  [maven 的依赖机制](https://link.jianshu.com/?t=https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)了。传递性依赖是 Maven2.0 引入的新特性，让我们只需关注直接依赖的 Jar 包，对于间接依赖的 Jar 包，Maven 会通过解析从远程仓库获取的依赖包的 pom 文件来隐式地将其引入，这为我们开发带来了极大的便利，但与此同时，也带来了常见的问题——版本冲突，即同一个 Jar 包出现了多个不同的版本，针对该问题 Maven 也有一套仲裁机制来决定最终选用哪个版本，但** Maven 的选择往往不一定是我们所期望的**，这也是产生 Jar 包冲突最常见的原因之一。先来看下 Maven 的仲裁机制：

- 优先按照依赖管理元素中指定的版本声明进行仲裁，此时下面的两个原则都无效了
- 若无版本声明，则按照 “短路径优先” 的原则（Maven2.0）进行仲裁，即选择依赖树中路径最短的版本
- 若路径长度一致，则按照 “第一声明优先” 的原则进行仲裁，即选择 POM 中最先声明的版本

从 maven 的仲裁机制中可以发现，除了第一条仲裁规则（这也是解决 Jar 包冲突的常用手段之一）外，后面的两条原则，对于同一个 Jar 包不同版本的选择，maven 的选择有点 “一厢情愿” 了，也许这是 maven 研发团队在总结了大量的项目依赖管理经验后得出的两条结论，又或者是发现根本找不到一种统一的方式来满足所有场景之后的无奈之举，可能这对于多数场景是适用的，但是**它不一定适合我——当前的应用**，因为每个应用都有其特殊性，该依赖哪个版本，maven 没办法帮你完全搞定，如果你没有规规矩矩地使用来进行依赖管理，就注定了逃脱不了第一类 Jar 包冲突问题。

### 2.1 Jar 包的加载顺序

对于第二类 Jar 包冲突问题，即多个不同的 Jar 包有类冲突，这相对于第一类问题就显得更为棘手。为什么这么说呢？在这种情况下，两个不同的 Jar 包，假设为  **A**、 **B**，它们的名称互不相同，甚至可能完全不沾边，如果不是出现冲突问题，你可能都不会发现它们有共有的类！对于 A、B 这两个 Jar 包，maven 就显得无能为力了，因为 maven 只会为你针对同一个 Jar 包的不同版本进行仲裁，而这俩是属于不同的 Jar 包，超出了 maven 的依赖管理范畴。此时，当 A、B 都出现在应用程序的类路径下时，就会存在潜在的冲突风险，即 A、B 的加载先后顺序就决定着 JVM 最终选择的类版本，如果选错了，就会出现诡异的第二类冲突问题。

那么 Jar 包的加载顺序都由哪些因素决定的呢？具体如下：

- Jar 包所处的加载路径，或者换个说法就是加载该 Jar 包的类加载器在 JVM 类加载器树结构中所处层级。由于 JVM 类加载的双亲委派机制，层级越高的类加载器越先加载其加载路径下的类，顾名思义，引导类加载器（bootstrap ClassLoader，也叫启动类加载器）是最先加载其路径下 Jar 包的，其次是扩展类加载器（extension ClassLoader），再次是系统类加载器（system ClassLoader，也就是应用加载器 appClassLoader），Jar 包所处加载路径的不同，就决定了它的加载顺序的不同。比如我们在 eclipse 中配置 web 应用的 resin 环境时，对于依赖的 Jar 包是添加到`Bootstrap Entries`中还是`User Entries`中呢，则需要仔细斟酌下咯。
- 文件系统的文件加载顺序。这个因素很容易被忽略，而往往又是因环境不一致而导致各种诡异冲突问题的罪魁祸首。因 tomcat、resin 等容器的 ClassLoader 获取加载路径下的文件列表时是不排序的，这就依赖于底层文件系统返回的顺序，那么当不同环境之间的文件系统不一致时，就会出现有的环境没问题，有的环境出现冲突。例如，对于 Linux 操作系统，返回顺序则是由 iNode 的顺序来决定的，如果说测试环境的 Linux 系统与线上环境不一致时，就极有可能出现典型案例：测试环境怎么测都没问题，但一上线就出现冲突问题，规避这种问题的最佳办法就是尽量保证测试环境与线上一致。

## 三、冲突的表象

Jar 包冲突可能会导致哪些问题？通常发生在编译或运行时，主要分为两类问题：一类是比较直观的也是最为常见的错误是抛出各种运行时异常，还有一类就是比较隐晦的问题，它不会报错，其表现形式是应用程序的行为跟预期不一致，分条罗列如下：

- **java.lang.ClassNotFoundException**，即 java 类找不到。这类典型异常通常是由于，没有在依赖管理中声明版本，maven 的仲裁的时候选取了错误的版本，而这个版本缺少我们需要的某个 class 而导致该错误。例如 httpclient-4.4.jar 升级到 httpclient-4.36.jar 时，类 org.apache.http.conn.ssl.NoopHostnameVerifier 被去掉了，如果此时我们本来需要的是 4.4 版本，且用到了 NoopHostnameVerifier 这个类，而 maven 仲裁时选择了 4.6，则会导致 ClassNotFoundException 异常。
- **java.lang.NoSuchMethodError**，即找不到特定方法，第一类冲突和第二类冲突都可能导致该问题——加载的类不正确。若是第一类冲突，则是由于错误版本的 Jar 包与所需要版本的 Jar 包中的类接口不一致导致，例如 antlr-2.7.2.jar 升级到 antlr-2.7.6.Jar 时，接口 antlr.collections.AST.getLine() 发生变动，当 maven 仲裁选择了错误版本而加载了错误版本的类 AST，则会导致该异常；若是第二类冲突，则是由于不同 Jar 包含有的同名类接口不一致导致，**典型的案例**：Apache 的 commons-lang 包，2.x 升级到 3.x 时，包名直接从 commons-lang 改为 commons-lang3，部分接口也有所改动，由于包名不同和传递性依赖，经常会出现两种 Jar 包同时在 classpath 下，org.apache.commons.lang.StringUtils.isBlank 就是其中有差异的接口之一，由于 Jar 包的加载顺序，导致加载了错误版本的 StringUtils 类，就可能出现 NoSuchMethodError 异常。
- **java.lang.NoClassDefFoundError**，**java.lang.LinkageError**  等，原因和上述雷同，就不作具体案例分析了。
- **没有报错异常，但应用的行为跟预期不一致**。这类问题同样也是由于运行时加载了错误版本的类导致，但跟前面不同的是，冲突的类接口都是一致的，但具体实现逻辑有差异，当我们加载的类版本不是我们需要的实现逻辑，就会出现行为跟预期不一致问题。这类问题通常发生在我们自己内部实现的多个 Jar 包中，由于包路径和类名命名不规范等问题，导致两个不同的 Jar 包出现了接口一致但实现逻辑又各不相同的同名类，从而引发此问题。

# 解决方案

## 一、问题排查和解决

1. 如果有异常堆栈信息，根据错误信息即可定位导致冲突的类名，然后在 eclipse 中`CTRL+SHIFT+T`或者在 idea 中`CTRL+N`就可发现该类存在于多个依赖 Jar 包中
2. 若步骤 1 无法定位冲突的类来自哪个 Jar 包，可在应用程序启动时加上 JVM 参数`-verbose:class`或者`-XX:+TraceClassLoading`，日志里会打印出每个类的加载信息，如来自哪个 Jar 包
3. 定位了冲突类的 Jar 包之后，通过`mvn dependency:tree -Dverbose -Dincludes=<groupId>:<artifactId>`查看是哪些地方引入的 Jar 包的这个版本
4. 确定 Jar 包来源之后，如果是第一类 Jar 包冲突，则可用 **排除不需要的 Jar 包版本或者在依赖管理**  中申明版本；若是第二类 Jar 包冲突，如果可排除，则用排掉不需要的那个 Jar 包，若不能排，则需考虑 Jar 包的升级或换个别的 Jar 包。当然，除了这些方法，还可以从类加载器的角度来解决该问题，可参考博文——[如果 jar 包冲突不可避免，如何实现 jar 包隔离](https://www.shop988.com/blog/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0jar%E5%8C%85%E9%9A%94%E7%A6%BB.html)，其思路值得借鉴。

## 二、有效避免

从上一节的解决方案可以发现，当出现第二类 Jar 包冲突，且冲突的 Jar 包又无法排除时，问题变得相当棘手，这时候要处理该冲突问题就需要较大成本了，所以，最好的方式是**在冲突发生之前能有效地规避之**！就好比数据库死锁问题，死锁避免和死锁预防就显得相当重要，若是等到真正发生死锁了，常规的做法也只能是回滚并重启部分事务，这就捉襟见肘了。那么怎样才能有效地规避 Jar 包冲突呢？

### 2.1 良好的习惯：依赖管理

对于第一类 Jar 包冲突问题，通常的做法是用排除不需要的版本，但这种做法带来的问题是每次引入带有传递性依赖的 Jar 包时，都需要一一进行排除，非常麻烦。maven 为此提供了集中管理依赖信息的机制，即依赖管理元素，对依赖 Jar 包进行统一版本管理，一劳永逸。通常的做法是，在 parent 模块的 pom 文件中尽可能地声明所有相关依赖 Jar 包的版本，并在子 pom 中简单引用该构件即可。

来看个示例，当开发时确定使用的 httpclient 版本为 4.5.1 时，可在父 pom 中配置如下：

```
<properties>
  <httpclient.version>4.5.1</httpclient.version>
</properties>
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpclient</artifactId>
      <version>${httpclient.version}</version>
    </dependency>
  </dependencies>
</dependencyManagement>

```

然后各个需要依赖该 Jar 包的子 pom 中配置如下依赖：

```xml
dependencies>
  <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
  </dependency>
</dependencies>
```

### 2.2 冲突检测插件

对于第二类 Jar 包冲突问题，前面也提到过，其核心在于同名类出现在了多个不同的 Jar 包中，如果人工来排查该问题，则需要逐个点开每个 Jar 包，然后相互对比看有没同名的类，那得多么浪费精力啊？！好在这种费时费力的体力活能交给程序去干。**maven-enforcer-plugin**，这个强大的 maven 插件，配合** extra-enforcer-rules**  工具，能自动扫描 Jar 包将冲突检测并打印出来，汗颜的是，笔者工作之前居然都没听过有这样一个插件的存在，也许是没遇到像工作中这样的冲突问题，算是涨姿势了。其原理其实也比较简单，通过扫描 Jar 包中的 class，记录每个 class 对应的 Jar 包列表，如果有多个即是冲突了，故不必深究，我们只需要关注如何用它即可。

在**最终需要打包运行的应用模块 pom**  中，引入 maven-enforcer-plugin 的依赖，在 build 阶段即可发现问题，并解决它。比如对于具有 parent pom 的多模块项目，需要将插件依赖声明在应用模块的 pom 中。这里有童鞋可能会疑问，为什么不把插件依赖声明在 parent pom 中呢？那样依赖它的应用子模块岂不是都能复用了？这里之所以强调 “打包运行的应用模块 pom”，是因为冲突检测针对的是最终集成的应用，关注的是应用运行时是否会出现冲突问题，而每个不同的应用模块，各自依赖的 Jar 包集合是不同的，由此而产生的列表也是有差异的，因此只能针对应用模块 pom 分别引入该插件。

先看示例用法如下：

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-enforcer-plugin</artifactId>
  <version>1.4.1</version>
  <executions>
    <execution>
      <id>enforce</id>
      <configuration>
        <rules>
          <dependencyConvergence/>
        </rules>
      </configuration>
      <goals>
        <goal>enforce</goal>
      </goals>
    </execution>
    <execution>
      <id>enforce-ban-duplicate-classes</id>
      <goals>
        <goal>enforce</goal>
      </goals>
      <configuration>
        <rules>
          <banDuplicateClasses>
            <ignoreClasses>
              <ignoreClass>javax.*</ignoreClass>
              <ignoreClass>org.junit.*</ignoreClass>
              <ignoreClass>net.sf.cglib.*</ignoreClass>
              <ignoreClass>org.apache.commons.logging.*</ignoreClass>
              <ignoreClass>org.springframework.remoting.rmi.RmiInvocationHandler</ignoreClass>
            </ignoreClasses>
            <findAllDuplicates>true</findAllDuplicates>
          </banDuplicateClasses>
        </rules>
        <fail>true</fail>
      </configuration>
    </execution>
  </executions>
  <dependencies>
    <dependency>
      <groupId>org.codehaus.mojo</groupId>
      <artifactId>extra-enforcer-rules</artifactId>
      <version>1.0-beta-6</version>
    </dependency>
  </dependencies>
</plugin>
```

maven-enforcer-plugin 是通过很多预定义的标准规则（[standard rules](https://link.jianshu.com/?t=http://maven.apache.org/enforcer/enforcer-rules/index.html)）和用户自定义规则，来约束 maven 的环境因素，如 maven 版本、JDK 版本等等，它有很多好用的特性，具体可参见[官网](https://link.jianshu.com/?t=http://maven.apache.org/enforcer/maven-enforcer-plugin/)。而 Extra Enforcer Rules 则是* MojoHaus*  项目下的针对 maven-enforcer-plugin 而开发的提供额外规则的插件，这其中就包含前面所提的重复类检测功能，具体用法可参见[官网](https://link.jianshu.com/?t=http://www.mojohaus.org/extra-enforcer-rules/)，这里就不详细叙述了。

# 典型案例

## 第一类 Jar 包冲突

这类 Jar 包冲突是最常见的也是相对比较好解决的，已经在[三、冲突的表象](https://www.jianshu.com/p/100439269148#%E4%B8%89%E3%80%81%E5%86%B2%E7%AA%81%E7%9A%84%E8%A1%A8%E8%B1%A1)这节中列举了部分案例，这里就不重复列举了。

## 第二类 Jar 包冲突

### Spring2.5.6 与 Spring3.x

Spring2.5.6 与 Spring3.x，从单模块拆分为多模块，Jar 包名称（artifactId）也从 spring 变为 spring-submoduleName，如
spring-context、spring-aop 等等，并且也有少部分接口改动（Jar 包升级的过程中，这也是在所难免的）。由于是不同的 Jar 包，经 maven 的传递依赖机制，就会经常性的存在这俩版本的 Spring 都在 classpath 中，从而引发潜在的冲突问题。
