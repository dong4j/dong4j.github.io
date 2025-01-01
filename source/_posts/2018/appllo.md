---
title: Apollo配置中心的使用心得分享：从入门到进阶
categories:
  - Java
tags:
  - Apollo
  - 配置管理
  - 分布式系统
abbrlink: a2959ba3
date: 2018-11-02 00:00:00
ai:
  - Apollo配置中心系统设计和功能介绍
description: Apollo配置中心系统设计和功能介绍
---

之前一直学习 SpringCloud, 对于配置中心，一直也是采用的 Spring Cloud Config,但是用久了，发现很多地方满足不了要求，同时也感觉很 low(个人看法勿喷)。在学习 Spring cloud config  的时候也有听到过携程的 apollo，但一直没时间去弄。直到昨天看了一张图，如下：使我下定决心去看看携程的 apollo 配置中心。

这张图也算是综合对比了 spring cloud config,netflix archaius, ctrip apollo, disconf, hawk 等配置中心的功能点。综合比较下来携程 apollo 更具有优势。

# 二、简单介绍携程 Apollo 配置中心

# 1、What is Apollo

## 1.1 背景

随着程序功能的日益复杂，程序的配置日益增多：各种功能的开关、参数的配置、服务器的地址……

对程序配置的期望值也越来越高：配置修改后实时生效，灰度发布，分环境、分集群管理配置，完善的权限、审核机制……

在这样的大环境下，传统的通过配置文件、数据库等方式已经越来越无法满足开发人员对配置管理的需求。

Apollo 配置中心应运而生！

## 1.2 Apollo 简介

Apollo（阿波罗）是携程框架部门研发的开源配置管理中心，能够集中化管理应用不同环境、不同集群的配置，配置修改后能够实时推送到应用端，并且具备规范的权限、流程治理等特性。

Apollo 支持 4 个维度管理 Key-Value 格式的配置：

1. application (应用)
2. environment (环境)
3. cluster (集群)
4. namespace (命名空间)

同时，Apollo 基于开源模式开发，开源地址：[https://github.com/ctripcorp/apollo](https://github.com/ctripcorp/apollo)

## 1.3 配置基本概念

既然 Apollo 定位于配置中心，那么在这里有必要先简单介绍一下什么是配置。

按照我们的理解，配置有以下几个属性：

- **配置是独立于程序的只读变量**
  - 配置首先是独立于程序的，同一份程序在不同的配置下会有不同的行为。
  - 其次，配置对于程序是只读的，程序通过读取配置来改变自己的行为，但是程序不应该去改变配置。
  - 常见的配置有：DB Connection Str、Thread Pool Size、Buffer Size、Request Timeout、Feature Switch、Server Urls 等。
- **配置伴随应用的整个生命周期**
  - 配置贯穿于应用的整个生命周期，应用在启动时通过读取配置来初始化，在运行时根据配置调整行为。
- **配置可以有多种加载方式**
  - 配置也有很多种加载方式，常见的有程序内部 hard code，配置文件，环境变量，启动参数，基于数据库等
- **配置需要治理**
  - 权限控制
    - 由于配置能改变程序的行为，不正确的配置甚至能引起灾难，所以对配置的修改必须有比较完善的权限控制
  - 不同环境、集群配置管理
    - 同一份程序在不同的环境（开发，测试，生产）、不同的集群（如不同的数据中心）经常需要有不同的配置，所以需要有完善的环境、集群配置管理
  - 框架类组件配置管理
    - 还有一类比较特殊的配置 - 框架类组件配置，比如 CAT 客户端的配置。
    - 虽然这类框架类组件是由其他团队开发、维护，但是运行时是在业务实际应用内的，所以本质上可以认为框架类组件也是应用的一部分。
    - 这类组件对应的配置也需要有比较完善的管理方式。

# 2、Why Apollo

正是基于配置的特殊性，所以 Apollo 从设计之初就立志于成为一个有治理能力的配置管理平台，目前提供了以下的特性：

- **统一管理不同环境、不同集群的配置**
  - Apollo 提供了一个统一界面集中式管理不同环境（environment）、不同集群（cluster）、不同命名空间（namespace）的配置。
  - 同一份代码部署在不同的集群，可以有不同的配置，比如 zk 的地址等
  - 通过命名空间（namespace）可以很方便的支持多个不同应用共享同一份配置，同时还允许应用对共享的配置进行覆盖
- **配置修改实时生效（热发布）**
  - 用户在 Apollo 修改完配置并发布后，客户端能实时（1 秒）接收到最新的配置，并通知到应用程序
- **版本发布管理**
  - 所有的配置发布都有版本概念，从而可以方便地支持配置的回滚
- **灰度发布**
  - 支持配置的灰度发布，比如点了发布后，只对部分应用实例生效，等观察一段时间没问题后再推给所有应用实例
- **权限管理、发布审核、操作审计**
  - 应用和配置的管理都有完善的权限管理机制，对配置的管理还分为了编辑和发布两个环节，从而减少人为的错误。
  - 所有的操作都有审计日志，可以方便的追踪问题
- **客户端配置信息监控**
  - 可以在界面上方便地看到配置在被哪些实例使用
- **提供 Java 和.Net 原生客户端**
  - 提供了 Java 和.Net 的原生客户端，方便应用集成
  - 支持 Spring Placeholder, Annotation 和 Spring Boot 的 ConfigurationProperties，方便应用使用（需要 Spring 3.1.1+）
  - 同时提供了 Http 接口，非 Java 和.Net 应用也可以方便的使用
- **提供开放平台 API**
  - Apollo 自身提供了比较完善的统一配置管理界面，支持多环境、多数据中心配置管理、权限、流程治理等特性。
  - 不过 Apollo 出于通用性考虑，对配置的修改不会做过多限制，只要符合基本的格式就能够保存。
  - 在我们的调研中发现，对于有些使用方，它们的配置可能会有比较复杂的格式，而且对输入的值也需要进行校验后方可保存，如检查数据库、用户名和密码是否匹配。
  - 对于这类应用，Apollo 支持应用方通过开放接口在 Apollo 进行配置的修改和发布，并且具备完善的授权和权限控制
- **部署简单**
  - 配置中心作为基础服务，可用性要求非常高，这就要求 Apollo 对外部依赖尽可能地少
  - 目前唯一的外部依赖是 MySQL，所以部署非常简单，只要安装好 Java 和 MySQL 就可以让 Apollo 跑起来
  - Apollo 还提供了打包脚本，一键就可以生成所有需要的安装包，并且支持自定义运行时参数

# 3、Apollo at a glance

## 3.1 基础模型

如下即是 Apollo 的基础模型：

1. 用户在配置中心对配置进行修改并发布
2. 配置中心通知 Apollo 客户端有配置更新
3. Apollo 客户端从配置中心拉取最新的配置、更新本地配置并通知到应用

![20241229154732_DkK2ypQG.webp](20241229154732_DkK2ypQG.webp)

## 3.2 界面概览

![20241229154732_a2KZU0KU.webp](20241229154732_a2KZU0KU.webp)

上图是 Apollo 配置中心中一个项目的配置首页

- 在页面左上方的环境列表模块展示了所有的环境和集群，用户可以随时切换。
- 页面中央展示了两个 namespace(application 和 FX.apollo) 的配置信息，默认按照表格模式展示、编辑。用户也可以切换到文本模式，以文件形式查看、编辑。
- 页面上可以方便地进行发布、回滚、灰度、授权、查看更改历史和发布历史等操作

## 3.3 添加/修改配置项

用户可以通过配置中心界面方便的添加/修改配置项：

![20241229154732_qPwTCUq9.webp](20241229154732_qPwTCUq9.webp)

输入配置信息：

![20241229154732_AJURlBSS.webp](20241229154732_AJURlBSS.webp)

## 3.4 发布配置

通过配置中心发布配置：

![20241229154732_l6UchSjE.webp](20241229154732_l6UchSjE.webp)

填写发布信息：

![20241229154732_S2vDJqCJ.webp](20241229154732_S2vDJqCJ.webp)

## 3.5 客户端获取配置（Java API 样例）

配置发布后，就能在客户端获取到了，以 Java API 方式为例，获取配置的示例代码如下。更多客户端使用说明请参见 [Java 客户端使用指南](https://github.com/ctripcorp/apollo/wiki/Java%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97)。

```
Config config = ConfigService.getAppConfig();
Integer defaultRequestTimeout = 200;
Integer requestTimeout =
         config.getIntProperty("request.timeout",defaultRequestTimeout);

```

## 3.6 客户端监听配置变化（Java API 样例）

通过上述获取配置代码，应用就能实时获取到最新的配置了。

不过在某些场景下，应用还需要在配置变化时获得通知，比如数据库连接的切换等，所以 Apollo 还提供了监听配置变化的功能，Java 示例如下：

```
Config config = ConfigService.getAppConfig();
config.addChangeListener(new ConfigChangeListener() {
    @Override
    public void onChange(ConfigChangeEvent changeEvent) {
        for (String key : changeEvent.changedKeys()) {
            ConfigChange change = changeEvent.getChange(key);
            System.out.println(String.format(
                "Found change - key: %s, oldValue: %s, newValue: %s, changeType: %s",
                change.getPropertyName(), change.getOldValue(),
                change.getNewValue(), change.getChangeType()));
        }
    }
});

```

## 3.7 Spring 集成样例

Apollo 和 Spring 也可以很方便地集成，只需要标注 `@EnableApolloConfig` 后就可以通过 `@Value` 获取配置信息：

```
@Configuration
@EnableApolloConfig
public class AppConfig {}

```

```
@Component
public class SomeBean {
    @Value("${request.timeout:200}")
    private int timeout;

    @ApolloConfigChangeListener
    private void someChangeHandler(ConfigChangeEvent changeEvent) {
        if (changeEvent.isChanged("request.timeout")) {
            refreshTimeout();
        }
    }
}

```

# 4、Apollo in depth

通过上面的介绍，相信大家已经对 Apollo 有了一个初步的了解，并且相信已经覆盖到了大部分的使用场景。

接下来会主要介绍 Apollo 的 cluster 管理（集群）、namespace 管理（命名空间）和对应的配置获取规则。

## 4.1 Core Concepts

在介绍高级特性前，我们有必要先来了解一下 Apollo 中的几个核心概念：

1. **application (应用)**

   - 这个很好理解，就是实际使用配置的应用，Apollo 客户端在运行时需要知道当前应用是谁，从而可以去获取对应的配置
   - 每个应用都需要有唯一的身份标识 - appId，我们认为应用身份是跟着代码走的，所以需要在代码中配置，具体信息请参见 [Java 客户端使用指南](https://github.com/ctripcorp/apollo/wiki/Java%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97)。

2. **environment (环境)**

   - 配置对应的环境，Apollo 客户端在运行时需要知道当前应用处于哪个环境，从而可以去获取应用的配置
   - 我们认为环境和代码无关，同一份代码部署在不同的环境就应该能够获取到不同环境的配置
   - 所以环境默认是通过读取机器上的配置（server.properties 中的 env 属性）指定的，不过为了开发方便，我们也支持运行时通过 System Property 等指定，具体信息请参见 [Java 客户端使用指南](https://github.com/ctripcorp/apollo/wiki/Java%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97)。

3. **cluster (集群)**

   - 一个应用下不同实例的分组，比如典型的可以按照数据中心分，把上海机房的应用实例分为一个集群，把北京机房的应用实例分为另一个集群。
   - 对不同的 cluster，同一个配置可以有不一样的值，如 zookeeper 地址。
   - 集群默认是通过读取机器上的配置（server.properties 中的 idc 属性）指定的，不过也支持运行时通过 System Property 指定，具体信息请参见 [Java 客户端使用指南](https://github.com/ctripcorp/apollo/wiki/Java%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97)。

4. **namespace (命名空间)**

   - 一个应用下不同配置的分组，可以简单地把 namespace 类比为文件，不同类型的配置存放在不同的文件中，如数据库配置文件，rpc 配置文件，应用自身的配置文件等
   - 应用可以直接读取到公共组件的配置 namespace，如 DAL，RPC 等
   - 应用也可以通过继承公共组件的配置 namespace 来对公共组件的配置做调整，如 DAL 的初始数据库连接数

## 4.2 自定义 Cluster

> 【本节内容仅对应用需要对不同集群应用不同配置才需要，如没有相关需求，可以跳过本节】

比如我们有应用在 A 数据中心和 B 数据中心都有部署，那么如果希望两个数据中心的配置不一样的话，我们可以通过新建 cluster 来解决。

### 4.2.1 新建 Cluster

新建 Cluster 只有项目的管理员才有权限，管理员可以在页面左侧看到“添加集群”按钮。

![20241229154732_KiFCrigs.webp](20241229154732_KiFCrigs.webp)

点击后就进入到集群添加页面，一般情况下可以按照数据中心来划分集群，如 SHAJQ、SHAOY 等。

不过也支持自定义集群，比如可以为 A 机房的某一台机器和 B 机房的某一台机创建一个集群，使用一套配置。

![20241229154732_D5ZfQpSc.webp](20241229154732_D5ZfQpSc.webp)

### 4.2.2 在 Cluster 中添加配置并发布

集群添加成功后，就可以为该集群添加配置了，首选需要按照下图所示切换到 SHAJQ 集群，之后配置添加流程和 [3.2 添加/修改配置项](http://nobodyiam.com/2016/07/09/introduction-to-apollo/#section-2) 一样，这里就不再赘述了。

![20241229154732_c01v9OMS.webp](20241229154732_c01v9OMS.webp)

### 4.2.3 指定应用实例所属的 Cluster

Apollo 会默认使用应用实例所在的数据中心作为 cluster，所以如果两者一致的话，不需要额外配置。

如果 cluster 和数据中心不一致的话，那么就需要通过 System Property 方式来指定运行时 cluster：

- -Dapollo.cluster=SomeCluster
- 这里注意 `apollo.cluster` 为全小写

## 4.3 自定义 Namespace

> 【本节仅对公共组件配置或需要多个应用共享配置才需要，如没有相关需求，可以跳过本节】

如果应用有公共组件（如 hermes-producer，cat-client 等）供其它应用使用，就需要通过自定义 namespace 来实现公共组件的配置。

### 4.3.1 新建 Namespace

以 hermes-producer 为例，需要先新建一个 namespace，新建 namespace 只有项目的管理员才有权限，管理员可以在页面左侧看到“添加 Namespace”按钮。

![20241229154732_HkmfFyMH.webp](20241229154732_HkmfFyMH.webp)

点击后就进入 namespace 添加页面，Apollo 会把应用所属的部门作为 namespace 的前缀，如 FX。

![20241229154732_Kpuh1aBK.webp](20241229154732_Kpuh1aBK.webp)

### 4.3.2 关联到环境和集群

Namespace 创建完，需要选择在哪些环境和集群下使用

![20241229154732_JT15Rl8C.webp](20241229154732_JT15Rl8C.webp)

### 4.3.3 在 Namespace 中添加配置项

接下来在这个新建的 namespace 下添加配置项

![20241229154732_5Q0Vo9yD.webp](20241229154732_5Q0Vo9yD.webp)

添加完成后就能在 FX.Hermes.Producer 的 namespace 中看到配置。

![20241229154732_ii3xtcBo.webp](20241229154732_ii3xtcBo.webp)

### 4.3.4 发布 namespace 的配置

![20241229154732_FOxrOgXT.webp](20241229154732_FOxrOgXT.webp)

### 4.3.5 客户端获取 Namespace 配置

对自定义 namespace 的配置获取，稍有不同，需要程序传入 namespace 的名字。更多客户端使用说明请参见 [Java 客户端使用指南](https://github.com/ctripcorp/apollo/wiki/Java%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97)。

```
Config config = ConfigService.getConfig("FX.Hermes.Producer");
Integer defaultSenderBatchSize = 200;
Integer senderBatchSize = config.getIntProperty("sender.batchsize", defaultSenderBatchSize);

```

### 4.3.6 客户端监听 Namespace 配置变化

```
Config config = ConfigService.getConfig("FX.Hermes.Producer");
config.addChangeListener(new ConfigChangeListener() {
  @Override
  public void onChange(ConfigChangeEvent changeEvent) {
    System.out.println("Changes for namespace " + changeEvent.getNamespace());
    for (String key : changeEvent.changedKeys()) {
      ConfigChange change = changeEvent.getChange(key);
      System.out.println(String.format(
        "Found change - key: %s, oldValue: %s, newValue: %s, changeType: %s",
        change.getPropertyName(), change.getOldValue(),
        change.getNewValue(), change.getChangeType()));
     }
  }
});

```

### 4.3.7 Spring 集成样例

```
@Configuration
@EnableApolloConfig("FX.Hermes.Producer")
public class AppConfig {}

```

```
@Component
public class SomeBean {
    @Value("${request.timeout:200}")
    private int timeout;

    @ApolloConfigChangeListener("FX.Hermes.Producer")
    private void someChangeHandler(ConfigChangeEvent changeEvent) {
        if (changeEvent.isChanged("request.timeout")) {
            refreshTimeout();
        }
    }
}

```

## 4.4 配置获取规则

> 【本节仅当应用自定义了集群或 namespace 才需要，如无相关需求，可以跳过本节】

在有了 cluster 概念后，配置的规则就显得重要了。

比如应用部署在 A 机房，但是并没有在 Apollo 新建 cluster，这个时候 Apollo 的行为是怎样的？

或者在运行时指定了 cluster=SomeCluster，但是并没有在 Apollo 新建 cluster，这个时候 Apollo 的行为是怎样的？

接下来就来介绍一下配置获取的规则。

### 4.4.1 应用自身配置的获取规则

当应用使用下面的语句获取配置时，我们称之为获取应用自身的配置，也就是应用自身的 application namespace 的配置。

```
Config config = ConfigService.getAppConfig();

```

对这种情况的配置获取规则，简而言之如下：

1. 首先查找运行时 cluster 的配置（通过 apollo.cluster 指定）
2. 如果没有找到，则查找数据中心 cluster 的配置
3. 如果还是没有找到，则返回默认 cluster 的配置

图示如下：

![20241229154732_BMEnbzMK.webp](20241229154732_BMEnbzMK.webp)

所以如果应用部署在 A 数据中心，但是用户没有在 Apollo 创建 cluster，那么获取的配置就是默认 cluster（default）的。

如果应用部署在 A 数据中心，同时在运行时指定了 SomeCluster，但是没有在 Apollo 创建 cluster，那么获取的配置就是 A 数据中心 cluster 的配置，如果 A 数据中心 cluster 没有配置的话，那么获取的配置就是默认 cluster（default）的。

### 4.4.2 公共组件配置的获取规则

以**_FX.Hermes.Producer_**为例，hermes producer 是 hermes 发布的公共组件。当使用下面的语句获取配置时，我们称之为获取公共组件的配置。

```
Config config = ConfigService.getConfig("FX.Hermes.Producer");

```

对这种情况的配置获取规则，简而言之如下：

1. 首先获取当前应用下的**_FX.Hermes.Producer_** namespace 的配置
2. 然后获取 hermes 应用下**_FX.Hermes.Producer_** namespace 的配置
3. 上面两部分配置的并集就是最终使用的配置，如有 key 一样的部分，以当前应用优先

图示如下：

![20241229154732_eZawyyZs.webp](20241229154732_eZawyyZs.webp)

通过这种方式，就实现了对框架类组件的配置管理，框架组件提供方提供配置的默认值，应用如果有特殊需求，可以自行覆盖。

## 4.5 总体设计

![20241229154732_ePfZQkEn.webp](20241229154732_ePfZQkEn.webp)

上图简要描述了 Apollo 的总体设计，我们可以从下往上看：

- Config Service 提供配置的读取、推送等功能，服务对象是 Apollo 客户端
- Admin Service 提供配置的修改、发布等功能，服务对象是 Apollo Portal（管理界面）
- Config Service 和 Admin Service 都是多实例、无状态部署，所以需要将自己注册到 Eureka 中并保持心跳
- 在 Eureka 之上我们架了一层 Meta Server 用于封装 Eureka 的服务发现接口
- Client 通过域名访问 Meta Server 获取 Config Service 服务列表（IP+Port），而后直接通过 IP+Port 访问服务，同时在 Client 侧会做 load balance、错误重试
- Portal 通过域名访问 Meta Server 获取 Admin Service 服务列表（IP+Port），而后直接通过 IP+Port 访问服务，同时在 Portal 侧会做 load balance、错误重试
- 为了简化部署，我们实际上会把 Config Service、Eureka 和 Meta Server 三个逻辑角色部署在同一个 JVM 进程中

### 4.5.1 Why Eureka

为什么我们采用 Eureka 作为服务注册中心，而不是使用传统的 zk、etcd 呢？我大致总结了一下，有以下几方面的原因：

- 它提供了完整的 Service Registry 和 Service Discovery 实现
  - 首先是提供了完整的实现，并且也经受住了 Netflix 自己的生产环境考验，相对使用起来会比较省心。
- 和 Spring Cloud 无缝集成
  - 我们的项目本身就使用了 Spring Cloud 和 Spring Boot，同时 Spring Cloud 还有一套非常完善的开源代码来整合 Eureka，所以使用起来非常方便。
  - 另外，Eureka 还支持在我们应用自身的容器中启动，也就是说我们的应用启动完之后，既充当了 Eureka 的角色，同时也是服务的提供者。这样就极大的提高了服务的可用性。
  - **这一点是我们选择 Eureka 而不是 zk、etcd 等的主要原因，为了提高配置中心的可用性和降低部署复杂度，我们需要尽可能地减少外部依赖。**
- Open Source
  - 最后一点是开源，由于代码是开源的，所以非常便于我们了解它的实现原理和排查问题。

## 4.6 客户端设计

![20241229154732_KmL6Rzxj.webp](20241229154732_KmL6Rzxj.webp)

上图简要描述了 Apollo 客户端的实现原理：

1. 客户端和服务端保持了一个长连接，从而能第一时间获得配置更新的推送。
2. 客户端还会定时从 Apollo 配置中心服务端拉取应用的最新配置。

   - 这是一个 fallback 机制，为了防止推送机制失效导致配置不更新
   - 客户端定时拉取会上报本地版本，所以一般情况下，对于定时拉取的操作，服务端都会返回 304 - Not Modified
   - 定时频率默认为每 5 分钟拉取一次，客户端也可以通过在运行时指定 System Property: `apollo.refreshInterval` 来覆盖，单位为分钟。

3. 客户端从 Apollo 配置中心服务端获取到应用的最新配置后，会保存在内存中
4. 客户端会把从服务端获取到的配置在本地文件系统缓存一份

   - 在遇到服务不可用，或网络不通的时候，依然能从本地恢复配置

5. 应用程序可以从 Apollo 客户端获取最新的配置、订阅配置更新通知

### 4.6.1 配置更新推送实现

前面提到了 Apollo 客户端和服务端保持了一个长连接，从而能第一时间获得配置更新的推送。

长连接实际上我们是通过 Http Long Polling 实现的，具体而言：

- 客户端发起一个 Http 请求到服务端
- 服务端会保持住这个连接 30 秒
- 如果在 30 秒内有客户端关心的配置变化，被保持住的客户端请求会立即返回，并告知客户端有配置变化的 namespace 信息，客户端会据此拉取对应 namespace 的最新配置
- 如果在 30 秒内没有客户端关心的配置变化，那么会返回 Http 状态码 304 给客户端
- 客户端在服务端请求返回后会自动重连

考虑到会有数万客户端向服务端发起长连，在服务端我们使用了 async servlet(Spring DeferredResult) 来服务 Http Long Polling 请求。

## 4.7 可用性考虑

配置中心作为基础服务，可用性要求非常高，下面的表格描述了不同场景下 Apollo 的可用性：

| 场景                     | 影响                                  | 降级                                  | 原因                                                                                       |
| :----------------------- | :------------------------------------ | :------------------------------------ | :----------------------------------------------------------------------------------------- |
| 某台 config service 下线 | 无影响                                |                                       | Config service 无状态，客户端重连其它 config service                                       |
| 所有 config service 下线 | 客户端无法读取最新配置，Portal 无影响 | 客户端重启时,可以读取本地缓存配置文件 |                                                                                            |
| 某台 admin service 下线  | 无影响                                |                                       | Admin service 无状态，Portal 重连其它 admin service                                        |
| 所有 admin service 下线  | 客户端无影响，portal 无法更新配置     |                                       |                                                                                            |
| 某台 portal 下线         | 无影响                                |                                       | Portal 域名通过 slb 绑定多台服务器，重试后指向可用的服务器                                 |
| 全部 portal 下线         | 客户端无影响，portal 无法更新配置     |                                       |                                                                                            |
| 某个数据中心下线         | 无影响                                |                                       | 多数据中心部署，数据完全同步，Meta Server/Portal 域名通过 slb 自动切换到其它存活的数据中心 |

# 5、Contribute to Apollo

Apollo 从开发之初就是以开源模式开发的，所以也非常欢迎有兴趣、有余力的朋友一起加入进来。

服务端开发使用的是 Java，基于 Spring Cloud 和 Spring Boot 框架。客户端目前提供了 Java 和.Net 两种实现。
