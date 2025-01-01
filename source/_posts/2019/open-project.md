---
title: 开源项目汇总：Spring Cloud生态圈
categories:
  - 新时代码农
tags:
  - Spring Cloud
  - 微服务架构
  - 云原生
  - 企业级解决方案
  - Nacos
  - Feign
  - Hystrix
  - Spring Boot Admin
  - JWT
  - OAuth2
  - API网关
  - Zuul Gateway
  - Moss
  - JetCache
abbrlink: 44d3ec9b
date: 2019-12-22 00:00:00
ai:
  - This is a collection of resources related to the development and implementation
    of various microservices architectures. The resources cover a range from cloud
    platforms featuring service authorization, monitoring tools like Spring Boot Admin,
    load balancing through proxies and gateways, distributed service registration
    with Nacos, API gateway services that handle authentication, authorization, debugging
    interfaces, traffic control and status checks for endpoints. There's also mention
    of OAuth2-based open platforms offering a unified interface management system
    for app-level, platform integrations and third-party partner collaborations. Other
    tools include JWT for secure service interactions, Hystrix for circuit breakers
    to prevent service cascading failures in distributed systems, Seata for distributed
    transaction management across multiple data sources, and other utilities like
    API Boot that streamline RESTful API development.
description: This is a collection of resources related to the development and implementation
  of various microservices architectures. The resources cover a range from cloud platforms
  featuring service authorization, monitoring tools like Spring Boot Admin, load balancing
  through proxies and gateways, distributed service registration with Nacos, API gateway
  services that handle authentication, authorization, debugging interfaces, traffic
  control and status checks for endpoints. There's also mention of OAuth2-based open
  platforms offering a unified interface management system for app-level, platform
  integrations and third-party partner collaborations. Other tools include JWT for
  secure service interactions, Hystrix for circuit breakers to prevent service cascading
  failures in distributed systems, Seata for distributed transaction management across
  multiple data sources, and other utilities like API Boot that streamline RESTful
  API development.
---

## [zuihou-admin-cloud](https://github.com/zuihou/zuihou-admin-cloud)

基于  `SpringCloud(Hoxton.SR1)` + `SpringBoot(2.2.2.RELEASE)`  的 SaaS 型微服务脚手架，具备用户管理、资源权限管理、网关统一鉴权、Xss 防跨站攻击、自动代码生成、多存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，架构清晰，非常适合学习使用。核心技术采用 Nacos、Fegin、Ribbon、Zuul、Hystrix、JWT Token、Mybatis、SpringBoot、Seata、Nacos、Sentinel、 RabbitMQ、FastDFS 等主要框架和中间件。

希望能努力打造一套从  `SaaS基础框架` - `分布式微服务架构` - `持续集成` - `系统监测`  的解决方案。`本项目旨在实现基础能力，不涉及具体业务。`

部署方面，可以采用以下 4 种方式，并会陆续公布 jenkins 集合以下 3 种部署方式的脚本和配置文件：

- IDEA 启动
- jar 部署
- docker 部署
- k8s 部署

### 租户后台 和 开发&运营后台 2 者之间的关系是什么？

A 公司 使用这套 SaaS 脚手架二次开发了一个 OA 或者商城， B 和 C 公司想使用 A 公司开发的这套系统，但土豪公司 B 有钱想要个性化功能，C 公司是个穷逼，不愿意多花钱  
于是，A 公司就在 zuihou-admin-ui（开发&运营后台） 上新建了 租户 B 和租户 C， 并各自新建了账号 b1 和账号 c1， 分别给 B 公司和 C 公司 试用，  
B 公司和 C 公司分别拿着账号， 在 zuihou-ui(租户后台) 上试用， 试用很满意，但土豪 B 公司先要定制功能， 就跟 A 公司签了一个 500W 的定制大单，并要求独立部署在他们自己的服务器  
穷逼 C 公司没钱， 就花了 20W 使用 A 公司部署的云环境， 服务器和数据等都存在 A 公司的云服务器上。

### zuihou-admin-boot 演示地址

| 项目            | 演示地址                                                                                         | 管理员账号       | 普通账号   |
| --------------- | ------------------------------------------------------------------------------------------------ | ---------------- | ---------- |
| 租户后台        | [http://42.202.130.216:10000/zuihou-ui](http://42.202.130.216:10000/zuihou-ui)                   | zuihou/zuihou    | test/zuiou |
| 开发 & 运营后台 | [http://42.202.130.216:10000/zuihou-admin-ui](http://42.202.130.216:10000/zuihou-admin-ui)       | demoAdmin/zuihou | 无         |
| swagger 文档    | [http://42.202.130.216:10000/api/gate/doc.html](http://42.202.130.216:10000/api/gate/doc.html)   | 无               | 无         |
| 定时任务        | [http://42.202.130.216:10000/zuihou-jobs-server](http://42.202.130.216:10000/zuihou-jobs-server) | zuihou/zuihou    | 无         |

### 功能点介绍

1. **服务注册 & 发现与调用：**

   基于 Nacos 来实现的服务注册与发现，使用使用 Feign 来实现服务互调，可以做到使用 HTTP 请求远程调用时能与调用本地方法一样的编码体验，开发者完全感知不到这是远程方法，更感知不到这是个 HTTP 请求。

2. **服务鉴权:**

   通过 JWT 的方式来加强服务之间调度的权限验证，保证内部服务的安全性。

3. **负载均衡：**

   将服务保留的 rest 进行代理和网关控制，除了平常经常使用的 node.js、nginx 外，Spring Cloud 系列的 zuul 和 ribbon，可以帮我们进行正常的网关管控和负载均衡。其中扩展和借鉴国外项目的扩展基于 JWT 的 Zuul 限流插件，方面进行限流。

4. **熔断机制：**

   因为采取了服务的分布，为了避免服务之间的调用 “雪崩”，采用了 Hystrix 的作为熔断器，避免了服务之间的 “雪崩”。

5. **监控：**

   利用 Spring Boot Admin 来监控各个独立 Service 的运行状态；利用 turbine 来实时查看接口的运行状态和调用频率；通过 Zipkin 来查看各个服务之间的调用链等。

6. **链路调用监控：**

   利用 Zipkin 实现微服务的全链路性能监控， 从整体维度到局部维度展示各项指标，将跨应用的所有调用链性能信息集中展现，可方便度量整体和局部性能，并且方便找到故障产生的源头，生产上可极大缩短故障排除时间。有了它，我们能做到：

   > 请求链路追踪，故障快速定位：可以通过调用链结合业务日志快速定位错误信息。 可视化：各个阶段耗时，进行性能分析。 依赖优化：各个调用环节的可用性、梳理服务依赖关系以及优化。 数据分析，优化链路：可以得到用户的行为路径，汇总分析应用在很多业务场景。

7. **数据权限**

   利用基于 Mybatis 的 DataScopeInterceptor 拦截器实现了简单的数据权限

8. **SaaS（多租户）的无感解决方案**

   使用 Mybatis 拦截器实现对所有 SQL 的拦截，修改默认的 Schema，从而实现多租户数据隔离的目的。 并且支持可插拔。

9. **二级缓存**

   采用 J2Cache 操作缓存，第一级缓存使用内存 (Caffeine)，第二级缓存使用 Redis。 由于大量的缓存读取会导致 L2 的网络成为整个系统的瓶颈，因此 L1 的目标是降低对 L2 的读取次数。 该缓存框架主要用于集群环境中。单机也可使用，用于避免应用重启导致的缓存冷启动后对后端业务的冲击。

10. **优雅的 Bean 转换**

    采用 Dozer 组件来对 DTO、DO、PO 等对象的优化转换

11. **前后端统一表单验证**

    严谨的表单验证通常需要 前端 + 后端同时验证， 但传统的项目，均只能前后端各做一次检验， 后期规则变更，又得前后端同时修改。 故在  `hibernate-validator`  的基础上封装了  `zuihou-validator-starter`  起步依赖，提供一个通用接口，可以获取需要校验表单的规则，然后前端使用后端返回的规则， 以后若规则改变，只需要后端修改即可。

12. **防跨站脚本攻击（XSS）**

    - 通过过滤器对所有请求中的 表单参数 进行过滤
    - 通过 Json 反序列化器实现对所有 application/json 类型的参数 进行过滤

13. **当前登录用户信息注入器**

    - 通过注解实现用户身份注入

14. **在线 API**

    由于原生 swagger-ui 某些功能支持不够友好，故采用了国内开源的  `swagger-bootstrap-ui`，并制作了 stater，方便 springboot 用户使用。

15. **代码生成器**

    基于 Mybatis-plus-generator 自定义了一套代码生成器， 通过配置数据库字段的注释，自动生成枚举类、数据字典注解、SaveDTO、UpdateDTO、表单验证规则注解、Swagger 注解等。

16. **定时任务调度器**：

    基于 xxl-jobs 进行了功能增强。（如：指定时间发送任务、执行器和调度器合并项目、多数据源）

17. **大文件 / 断点 / 分片续传**

    前端采用 webupload.js、后端采用 NIO 实现了大文件断点分片续传，启动 Eureka、Zuul、File 服务后，直接打开 docs/chunkUploadDemo/demo.html 即可进行测试。 经测试，本地限制堆栈最大内存 128M 启动 File 服务，5 分钟内能成功上传 4.6G + 的大文件，正式服耗时则会受到用户带宽和服务器带宽的影响，时间比较长。

18. **分布式事务**

    集成了阿里的分布式事务中间件：seata，以  **高效**  并且对业务  **0 侵入**  的方式，解决 微服务 场景下面临的分布式事务问题。

### 项目架构图

![20241229154732_sgdUPRIO.webp](20241229154732_sgdUPRIO.webp)

### 技术栈 / 版本介绍

- 所涉及的相关的技术有：
  - JSON 序列化：Jackson
  - 消息队列：RabbitMQ
  - 缓存：Redis
  - 缓存框架：J2Cache
  - 数据库： MySQL 5.7.9 (驱动 6.0.6)
  - 定时器：采用 xxl-jobs 项目进行二次改造
  - 前端：vue
  - 持久层框架： Mybatis-plus
  - 代码生成器：基于 Mybatis-plus-generator 自定义 [[https://github.com/zuihou/zuihou-generator.git](https://github.com/zuihou/zuihou-generator.git)]
  - API 网关：Zuul
  - 服务注册与发现：Eureka -> Nacos
  - 服务消费：OpenFeign
  - 负载均衡：Ribbon
  - 配置中心：Nacos
  - 服务熔断：Hystrix
  - 项目构建：Maven 3.3
  - 分布式事务： seata
  - 分布式系统的流量防卫兵： Sentinel
  - 监控： spring-boot-admin 2.x
  - 链路调用跟踪： zipkin 2.x
  - 文件服务器：FastDFS 5.0.5 / 阿里云 OSS / 本地存储
  - Nginx
- 部署方面：
  - 服务器：CentOS
  - Jenkins
  - Docker 18.09
  - Kubernetes 1.12

本代码采用 Intellij IDEA (2018.1 EAP) 来编写，但源码与具体的 IDE 无关。

PS: Lombok 版本过低会导致枚举类型的参数无法正确获取参数，经过调试发现因为版本多低后，导致 EnumDeserializer 的 Object obj = p.getCurrentValue (); 取的值为空。

## [microservices-platform](https://github.com/zlt2000/microservices-platform)

### 项目总体架构图

![20241229154732_lCCGFgoH.webp](20241229154732_lCCGFgoH.webp)

### 功能介绍

![20241229154732_NdaIh5EJ.webp](20241229154732_NdaIh5EJ.webp)

### 模块说明

```
central-platform -- 父项目，公共依赖
│  ├─zlt-business -- 业务模块一级工程
│  │  ├─user-center -- 用户中心[7000]
│  │  ├─file-center -- 文件中心[5000]
│  │  ├─code-generator -- 代码生成器[7300]
│  │  ├─search-center -- 搜索中心
│  │  │  ├─search-client -- 搜索中心客户端
│  │  │  ├─search-server -- 搜索中心服务端[7100]
│  │─zlt-commons -- 通用工具一级工程
│  │  ├─zlt-auth-client-spring-boot-starter -- 封装spring security client端的通用操作逻辑
│  │  ├─zlt-common-core -- 封装通用操作逻辑
│  │  ├─zlt-common-spring-boot-starter -- 封装通用操作逻辑
│  │  ├─zlt-db-spring-boot-starter -- 封装数据库通用操作逻辑
│  │  ├─zlt-log-spring-boot-starter -- 封装log通用操作逻辑
│  │  ├─zlt-redis-spring-boot-starter -- 封装Redis通用操作逻辑
│  │  ├─zlt-ribbon-spring-boot-starter -- 封装Ribbon和Feign的通用操作逻辑
│  │  ├─zlt-sentinel-spring-boot-starter -- 封装Sentinel的通用操作逻辑
│  │  ├─zlt-swagger2-spring-boot-starter -- 封装Swagger通用操作逻辑
│  ├─zlt-config -- 配置中心
│  ├─zlt-doc -- 项目文档
│  ├─zlt-gateway -- api网关一级工程
│  │  ├─sc-gateway -- spring-cloud-gateway[9900]
│  │  ├─zuul-gateway -- netflix-zuul[9900]
│  ├─zlt-job -- 分布式任务调度一级工程
│  │  ├─job-admin -- 任务管理器[8081]
│  │  ├─job-core -- 任务调度核心代码
│  │  ├─job-executor-samples -- 任务执行者executor样例[8082]
│  ├─zlt-monitor -- 监控一级工程
│  │  ├─sc-admin -- 应用监控[6500]
│  │  ├─log-center -- 日志中心[6200]
│  ├─zlt-uaa -- spring-security认证中心[8000]
│  ├─zlt-register -- 注册中心Nacos[8848]
│  ├─zlt-web -- 前端一级工程
│  │  ├─back-web -- 后台前端[8066]
│  ├─zlt-transaction -- 事务一级工程
│  │  ├─txlcn-tm -- tx-lcn事务管理器[7970]
│  ├─zlt-demo -- demo一级工程
│  │  ├─txlcn-demo -- txlcn分布式事务demo
│  │  ├─seata-demo -- seata分布式事务demo
│  │  ├─sharding-jdbc-demo -- sharding-jdbc分库分表demo
│  │  ├─rocketmq-demo -- rocketmq和mq事务demo
```

## (open-capacity-platform)[https://gitee.com/owenwangwen/open-capacity-platform]

### **功能介绍**

- 统一安全认证中心
  - 支持 oauth 的四种模式登录
  - 支持用户名、密码加图形验证码登录
  - 支持第三方系统单点登录
- 微服务架构基础支撑
  - 服务注册发现、路由与负载均衡
  - 服务熔断与限流
  - 统一配置中心
  - 统一日志中心
  - 分布式锁
  - 分布式任务调度器
- 系统服务监控中心
  - 服务调用链监控
  - 应用吞吐量监控
  - 服务降级、熔断监控
  - 微服务服务监控
- 能力开放平台业务支撑
  - 网关基于应用方式 API 接口隔离
  - 网关基于应用限制调用次数
  - 下游服务基于 RBAC 权限管理，实现细粒度控制
  - 代码生成器中心
  - 网关聚合服务内部 Swagger 接口文档
  - 统一跨域处理
  - 统一异常处理
- docker 容器化部署
  - 基于 rancher 的容器化部署
  - 基于 docker 的 elk 日志监控
  - 基于 docker 的服务动态扩容

### 代码结构

![20241229154732_6fabptft.webp](20241229154732_6fabptft.webp)

## [mall](https://github.com/macrozheng/mall)

### 项目介绍

mall 项目是一套电商系统，包括前台商城系统及后台管理系统，基于 SpringBoot+MyBatis 实现，采用 Docker 容器化部署。前台商城系统包含首页门户、商品推荐、商品搜索、商品展示、购物车、订单流程、会员中心、客户服务、帮助中心等模块。后台管理系统包含商品管理、订单管理、会员管理、促销管理、运营管理、内容管理、统计报表、财务管理、权限管理、设置等模块。

### 系统架构图

![20241229154732_I6pbMYqL.webp](20241229154732_I6pbMYqL.webp)

## [spring-boot-plus](https://github.com/geekidea/spring-boot-plus)

### 主要特性

1. 集成 spring boot 常用开发组件集、公共配置、AOP 日志等
2. 集成 mybatis plus 快速 dao 操作
3. 快速生成后台代码: entity/param/vo/controller/service/mapper/xml
4. 集成 swagger2，可自动生成 api 文档
5. 集成 jwt、shiro/spring security 权限控制
6. 集成 redis、spring cache、ehcache 缓存
7. 集成 rabbit/rocket/kafka mq 消息队列
8. 集成 druid 连接池，JDBC 性能和慢查询检测
9. 集成 spring boot admin，实时检测项目运行情况
10. 使用 assembly maven 插件进行不同环境打包部署,包含启动、重启命令，配置文件提取到外部 config 目录

### 项目架构

![20241229154732_ghNYKhGb.webp](20241229154732_ghNYKhGb.webp)

## [carefree-mongodb-spring-boot-starter](https://github.com/kweny/carefree-mongodb-spring-boot-starter)

<https://zhuanlan.zhihu.com/p/45033950>

## [Micro-Service-Skeleton](https://github.com/babylikebird/Micro-Service-Skeleton)

<https://blog.csdn.net/w1054993544/article/details/78932614>

## [pig](https://gitee.com/log4j/pig)

### 特性

- 基于 Spring Cloud Hoxton 、Spring Boot 2.2、 OAuth2 的 RBAC 权限管理系统
- 基于数据驱动视图的理念封装 element-ui，即使没有 vue 的使用经验也能快速上手
- 提供对常见容器化支持 Docker、Kubernetes、Rancher2 支持
- 提供 lambda 、stream api 、webflux 的生产实践

### 结构

```
pig-ui  -- https://gitee.com/log4j/pig-ui

pig
├── pig-auth -- 授权服务提供[3000]
├── pig-codegen -- 图形化代码生成[5002]
└── pig-common -- 系统公共模块
     ├── pig-common-core -- 公共工具类核心包
     ├── pig-common-log -- 日志服务
     ├── pig-common-security -- 安全工具类
     └── pig-common-swagger -- 接口文档
├── pig-register -- Nacos Server[8848]
├── pig-gateway -- Spring Cloud Gateway网关[9999]
├── pig-monitor -- Spring Boot Admin监控 [5001]
└── pig-upms -- 通用用户权限管理模块
     └── pig-upms-api -- 通用用户权限管理系统公共api模块
     └── pig-upms-biz -- 通用用户权限管理系统业务处理模块[4000]

```

## [prex](https://gitee.com/kaiyuantuandui/prex)

Prex 基于 Spring Boot 2.1.8 、Spring Cloud Greenwich.SR3、Spring Cloud Alibaba、Spring Security 、Spring cloud Oauth2 、Vue 的前后端分离的的 RBAC 权限管理系统，项目支持数据权限管理，支持后端配置菜单动态路由，第三方社交登录，努力做最简洁的后台管理系统

### 技术栈

- 基于 Spring Boot 2.1.8 、Spring Cloud、Spring Cloud Alibaba、Spring Security、OAuth2 的 RBAC 权限管理系统。
- 基于 Nacos 做注册中心和配置中心。
- 基于 Sentinel 做方法限流和阻塞处理。
- 基于 Vue 前端框架 和最新 Ant Design 界面。
- 基于 Mybatis Plus 简化开发、数据隔离等。
- 项目均使用 Lambda 、Stream Api 的风格编码。
- 使用 Spring Social 三方登录。
- 提供 Spring Cloud Admin 做项目可视化监控。
- 基于 Swagger 提供统一 Api 管理。

### 基本功能

- 用户管理：该功能主要完成系统用户配置，提供用户基础配置 (用户名、手机号邮箱等) 以及部门角色等。
- 角色管理：权限菜单分配，以部门基础设置角色的数据权限范围。
- 菜单管理：后端配置实现菜单动态路由，支持多级菜单，操作权限，按钮权限标识等。
- 部门管理：配置系统组织架构，树形表格展示，可随意调整上下级。
- 岗位管理：根据部门配置所属职位
- 租户管理：提供统一认证对权限管理平台，按照租户进行数据隔离 (微服务版暂不开放)。
- 社交账号管理：可以对绑定 Prex 系统对社交账号进行查看和解绑。
- 字典管理：对系统中经常使用的一些较为固定的数据进行维护，如：状态 (正常 / 异常)，性别 (男 / 女) 等。
- 日志管理：可以删除和查看用户操作的日志。
- 异常日志：记录异常日志，方便开发人员定位错误。

### 项目特点

- 前后端分离的微服务架构
- 使用 Nacos、Sentinel、SpringCloud 等最新流行组件和 UI
- 可直接集成到企业微服务项目中
- 使用 Gateway 进行高性能的网关路由
- 独立的 UPMS 系统
- 使用 JWT 进行 Token 管理
- 提供插拔式密码和客户端两种模式到授权方式
- 对日志操作、短信、邮件、Redis、资源服务、Swagger 均提供插拔式使用
- 代码大量采用中文注释，极其简洁风格，上手快、易理解
- 采用 RESTFul API 规范开发
- 统一异常拦截，友好的错误提示
- 基于注解 + Aop 切面实现全方位日记记录系统
- 基于 Mybatis 拦截器 + 策略模式实现数据权限控制
- 提供解决前后分离第三方社交登录方案
- Spring Social 集成 Security 实现第三方社交登录
- 基于 Mybatis-Plus 实现 SaaS 多租户功能 (微服务版暂不开放)

## [Nepxion](https://github.com/Nepxion)

## [FEBS-Cloud](https://github.com/wuyouzhuguli/FEBS-Cloud)

FEBS Cloud 是一款使用 Spring Cloud Hoxton.RELEASE、Spring Cloud OAuth2 & Spring Cloud Alibaba 构建的低耦合权限管理系统，前端（FEBS Cloud Web）采用 vue element admin 构建。FEBS 意指：**F**ast，**E**asy use，**B**eautiful 和  **S**afe。该系统具有如下特点：

1. 前后端分离架构，客户端和服务端纯 Token 交互；
2. 认证服务器与资源服务器分离，方便接入自己的微服务系统；
3. 微服务防护，客户端请求资源只能通过微服务网关获取；
4. 集成 Prometheus，SpringBootAdmin，多维度监控微服务；
5. 集成 Spring Cloud Alibaba Nacos 服务治理和集中配置管理；
6. 网关限流，网关黑名单限制，网关日志（WebFlux 编程实践）；
7. ~~集成 Zipkin，方便跟踪 Feign 调用链~~，集成 Skywalking APM；
8. 集成 ELK，集中管理日志，便于问题分析；
9. 微服务 Docker 化，使用 Docker Compose 一键部署；
10. 支持 Kubernetes 集群部署；
11. 提供详细的使用文档和搭建教程；
12. 前后端请求参数校验，Excel 导入导出，代码生成等。

### 文档与教程

项目导入及使用文档：[https://www.kancloud.cn/mrbird/spring-cloud/1263681](https://www.kancloud.cn/mrbird/spring-cloud/1263681)。  
项目从零搭建到部署教程：[https://www.kancloud.cn/mrbird/spring-cloud/1263685](https://www.kancloud.cn/mrbird/spring-cloud/1263685)。  
Kubernetes 集群部署脚本：[https://github.com/wuyouzhuguli/FEBS-Cloud-K8S](https://github.com/wuyouzhuguli/FEBS-Cloud-K8S)。  
分布式事务方案（RocketMQ、TX-LCN、Seata）：[https://www.kancloud.cn/mrbird/spring-cloud/1456142](https://www.kancloud.cn/mrbird/spring-cloud/1456142)。

## [Spring Cloud Alibaba 组件使用](https://github.com/helloworlde/spring-cloud-alibaba-component)

### Nacos

> Nacos 是一个配置和注册中心，类似 Spring Cloud Config 和 Eureka、ZooKeeper、Consul

- [Spring Boot 使用 Nacos 作为配置中心](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/boot-config/README.md)
- [Spring Cloud 使用 Nacos 作为配置中心](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-config/README.md)
- [Spring Cloud 使用 Nacos 作为服务注册中心](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-discovery/README.md)

### Sentinel

> Sentinel 是一个流量控制框架，支持流量控制，熔断降级，系统负载保护，类似 Hystrix、resilience4j

- [Spring Cloud 使用 Sentinel 作为限流降级工具](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/sentinel-nacos-config/README.md)

### OSS

> spring-cloud-starter-alicloud-oss 是用于阿里云 OSS 的 SpringBoot Starter，通过封装 SDK 实现对 OSS 的操作

- [Spring Cloud 使用阿里云 OSS](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-oss/README.md)

### Dubbo

> Dubbo 是一个远程调用框架，用于实现方法的远程调用

推荐使用 ZooKeeper 作为注册中心，当前使用 Nacos 会有各种问题

- [Spring Cloud 使用 Dubbo 实现远程调用，Nacos 作为注册中心](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-dubbo-nacos/README.md)
- [Spring Cloud 使用 Dubbo 实现远程调用，ZooKeeper 作为注册中心](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-dubbo-zk/README.md)

### Seata

> Seata 是一个分布式事务框架，可以通过 Seata 框架的注解实现非侵入性的分布式事务

- [Spring Cloud 使用 Seata 实现分布式事务 - MyBatis](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-mybatis/README.md)
- [Spring Cloud 使用 Seata 实现分布式事务 - JPA](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-jpa/README.md)
- [Spring Cloud 使用 Seata 实现分布式事务 - Mybatis/Nacos](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-nacos/README.md)
- [Spring Cloud 使用 Seata 实现分布式事务 - Mybatis/Nacos/Dubbo](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-dubbo-nacos/README.md)
- [Spring Cloud 使用 Seata 实现分布式事务 - Mybatis/Eureka/Feign](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-eureka/README.md)
- [Spring Cloud 使用 Seata 实现分布式事务 - Mybatis 多数据源](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-multi-datasource/README.md)
- [Spring Cloud 使用 Seata 实现分布式事务 - Mybatis 多数据源 & MyBatisPlus](https://github.com/helloworlde/spring-cloud-alibaba-component/blob/master/cloud-seata-multi-datasource-mybatis-plus/README.md)

MyBatis 和 JPA 通过 Seata 实现分布式事务都需要注入  `io.seata.rm.datasource.DataSourceProxy`, 不同的是，MyBatis 还需要额外注入  `org.apache.ibatis.session.SqlSessionFactory`

## [cloud-platform](https://gitee.com/geek_qi/cloud-platform)

### 架构摘要

1. 服务鉴权  
   通过 JWT 的方式来加强服务之间调度的权限验证，保证内部服务的安全性。
2. 监控  
   利用 Spring Boot Admin 来监控各个独立 Service 的运行状态；利用 Hystrix Dashboard 来实时查看接口的运行状态和调用频率等。
3. 负载均衡  
   将服务保留的 rest 进行代理和网关控制，除了平常经常使用的 node.js、nginx 外，Spring Cloud 系列的 zuul 和 ribbon，可以帮我们进行正常的网关管控和负载均衡。其中扩展和借鉴国外项目的扩展基于 JWT 的 Zuul 限流插件，方面进行限流。
4. 服务注册与调用  
   基于 Nacos 来实现的服务注册与调用，在 Spring Cloud 中使用 Feign, 我们可以做到使用 HTTP 请求远程服务时能与调用本地方法一样的编码体验，开发者完全感知不到这是远程方法，更感知不到这是个 HTTP 请求。
5. 熔断机制  
   因为采取了服务的分布，为了避免服务之间的调用 “雪崩”，采用了 Hystrix 的作为熔断器，避免了服务之间的 “雪崩”。

## [open-cloud](https://github.com/liuyadu/open-cloud)

### 简介

搭建基于 OAuth2 的开放平台、为 APP 端、应用服务提供统一接口管控平台、为第三方合作伙伴的业务对接提供授信可控的技术对接平台

- 分布式架构，Nacos (服务注册 + 配置中心) 统一管理
- 统一 API 网关（参数验签、身份认证、接口鉴权、接口调试、接口限流、接口状态、接口外网访问）
- 统一 oauth2 认证协议

## [api-boot](https://gitee.com/minbox-projects/api-boot)

## [Moss](https://github.com/SpringCloud/Moss)

[集成 jetcache](https://www.jianshu.com/p/c3a3a2aee709)  
<https://github.com/bounce5733/eagle-gateway>  
<https://github.com/zhoutaoo/SpringCloud>  
<https://gitee.com/wugou/springcloud-gateway-nacos>  
<https://github.com/alibaba/sca-best-practice>  
<https://github.com/chillzhuang/SpringBlade>  
<https://github.com/chillzhuang/blade-tool>  
<https://github.com/lets-mica/mica>  
<https://github.com/xkcoding/scaffold>  
<https://github.com/xiiiblue/zen-scaffold>  
<https://github.com/MyHerux/spring-boot-2.x-scaffold>  
<https://github.com/sofastack/sofa-tracer>
