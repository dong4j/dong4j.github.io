![random-pic-api](https://api.dong4j.site/pc?spm={{spm}})

## 配置管理，最容易被做烂的事
  
在所有研发底座的能力中，配置管理是最"不起眼"的。它不产生业务价值，不影响接口性能，甚至改坏了也不会马上出问题——配置错误可能在被调用到的时候才暴露。

但正因为它不起眼，它也是最容易被做烂的。框架迭代了两年，不同的人在不同的时期添加不同的配置项，大家的命名习惯、组织方式、使用方式各不相同，最后就形成了一种"配置腐化"。

我接手的时候，框架的配置状况大概是这样的：

有的配置用 `@Value` 注入：

```java
@Value("${spring.data.redis.enable:true}")
private boolean enable;
```

有的配置用 `@ConfigurationProperties`，但前缀混乱。开关配置一部分叫 `enable`，一部分叫 `enabled`：

```yaml
secret:
  mybatis:
    enable: false        # 这里是 enable

gateway:
  log:
    access:
      enabled: false     # 这里是 enabled
```

业务方写配置的时候，得先在脑子里检索——这个模块到底用的是 `enable` 还是 `enabled`？检索不出来，就得去翻文档或者源码。这额外的几秒钟认知负担，在几十个配置项之间反复出现。

有些配置项之间互相依赖，但没有显式约束。比如 Redis 集群模式下必须配置 `cluster.nodes`，但如果忘了配，启动时不报错，等到第一次做集群操作时才发现连不上。

更让我难受的是配置的粒度问题。短信服务商类型用的居然是字符串：

```yaml
sms:
  type: ryd
```

有人写 `ryd`，有人写 `RYD`，有人写 `rongyida`——同一种东西三种写法，排查问题的时候光定位配置不一致就要花半天。

## 第一步：统一入口

整改第一步，所有配置改用 `@ConfigurationProperties`，不再用 `@Value`。

为什么？不是 `@Value` 不能用，而是框架的配置体量决定了 `@ConfigurationProperties` 的收益更大。

`@Value` 的优势是轻量——一个注解就搞定。但它没法做结构化表达，没法校验，IDE 不提示。

`@ConfigurationProperties` 把这些短板全补上了。以缓存组件为例，原来散落在四五个类里的 `@Value` 全部收敛到一个类中：

```java
@Data
@ConfigurationProperties(prefix = "framework.cache")
@Validated
public class CacheProperties {

    private boolean enabled = true;

    @NotNull(message = "缓存实现类型不能为空")
    private String implementation = "redisson";

    private String keyPrefix = "";

    @DurationMin(seconds = 1)
    private Duration defaultExpiration = Duration.ofHours(1);

    private Pool pool = new Pool();
    private Redisson redisson = new Redisson();
    private Jedis jedis = new Jedis();

    @Data
    public static class Pool {
        @Min(1) private int maxActive = 20;
        @Min(0) private int maxIdle = 10;
        @Min(0) private int minIdle = 5;
        @DurationMin(millis = 100)
        private Duration maxWait = Duration.ofSeconds(10);
    }

    @Data
    public static class Redisson {
        private String mode = "single";
        @NotEmpty private String address;
        private String password;
        private int database = 0;
    }
}
```

完成后，使用者在 yaml 里输入 `framework.cache.`，IDE 自动补全所有可配置项。不需要翻文档，不需要记 key。

如果配置值不合法——比如 `maxActive = -1`——启动阶段就抛异常，而不是等到运行时才发现连接池创建失败。这就是"快速失败"原则：**运行时暴露的问题越少，系统的可靠性越高**。

短信服务商类型这种 String 配置，改成枚举：

```java
@Data
@ConfigurationProperties(prefix = "framework.sms")
public class SmsProperties {
    private SmsProvider provider = SmsProvider.RYD;   // 枚举，杜绝拼写错误
}

public enum SmsProvider {
    RYD, TYFO
}
```

开发者输入 `framework.sms.provider=` 的时候，IDE 只提示 `ryd` 和 `tyfo` 两个合法值。想输错都很难。

## 第二步：配置校验

校验不是可选项。想想这些场景：

-   有人把 `maxActive` 设成 `-1` → 启动时不报错，运行时创建连接池失败；
-   有人把 `redis.address` 留空 → NullPointerException 在第一次缓存操作时才发生；
-   有人设了 `mode=cluster` 但没配 `cluster.nodes` → 运行时连接失败。

这些都可以用 JSR 303 注解在编译阶段发现：

```java
@Data
@ConfigurationProperties(prefix = "framework.cache")
@Validated
public class CacheProperties {

    @AssertTrue(message = "集群模式必须配置 cluster.nodes")
    public boolean isClusterNodesValid() {
        if ("cluster".equals(redisson.getMode())) {
            return redisson.getCluster() != null 
                && !redisson.getCluster().getNodes().isEmpty();
        }
        return true;
    }
}
```

启动时如果校验不通过，Spring Boot 直接拒绝启动，把问题暴露在最早期。

## 第三步：Spring Boot 配置加载顺序里的坑

配置统一之后，下一个问题是这些配置放在哪。框架在从 2.x 往 3.x 升级的过程中，遇到了一个经典的配置加载顺序问题。

在 Spring Cloud 2020+ 版本中，`bootstrap.yml` 被废弃了，所有配置统一放在 `application.yml` 中。这本身是个好的简化方向，但有一个坑：`spring.config.import` 的执行时机早于 profile 文件的加载。

这意味着你**不能**把 `spring.profiles.active` 相关的 Nacos 地址放到 `application-test.yml` 这种 profile 文件中：

```yaml
# application.yml
spring:
  profiles:
    active: test
  config:
    import: nacos:share-config.yaml              # 此时还没加载 application-test.yml！

# application-test.yml
spring:
  cloud:
    nacos:
      server-addr: 10.0.0.1:8848                 # 这个配得太晚了，Nacos 加载已经结束了
```

正确的做法是把所有 profile 相关的 Nacos 配置都放在 `application.yml` 中，用 `spring.config.activate.on-profile` 做条件激活：

```yaml
# application.yml
spring:
  profiles:
    active: local
  application:
    name: @project.artifactId@
  config:
    import:
      - nacos:share-config.yaml?refreshEnabled=false&group=DEFAULT_GROUP
      - nacos:${spring.application.name}.yaml?refreshEnabled=true&group=DEFAULT_GROUP

---
spring:
  config:
    activate:
      on-profile: local
  cloud:
    nacos:
      server-addr: 127.0.0.1:8848
      config:
        namespace: local
      discovery:
        namespace: local

---
spring:
  config:
    activate:
      on-profile: dev
  cloud:
    nacos:
      server-addr: nacos-dev.internal:8848
      config:
        namespace: dev
      discovery:
        namespace: dev
```

这个文件虽然长了点，但它是**可预测的**——你看一眼就知道 local 环境连哪个 Nacos，dev 环境连哪个 Nacos。不会出现"local 环境配置在 `application-local.yml` 里，但 `application-local.yml` 加载太晚导致 Nacos 连不上"的问题。

很多人被这个问题坑过。排查起来极其痛苦——没有报错，Nacos 也不连，所有 Nacos 配置都不生效，但你找不到原因。所以我把这个写成了一条铁律：**不要把 `spring.cloud.nacos.*` 配置单独放到 profile 文件中**。

## 第四步：共享配置分层

配置整理好之后，还要解决"共享"的问题。十几个微服务，有些配置是共通的——日志格式、Feign 超时、MyBatis 配置、数据库连接池配置。如果每个服务抄一遍，改一次得改十几个地方。

我们的做法是用 Nacos 的共享配置：

```yaml
# share-config.yaml —— 放在 Nacos 中，所有服务共用
spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      initial-size: 5
      min-idle: 5
      max-active: 20
      max-wait: 60000

feign:
  sentinel:
    enabled: true

mybatis-plus:
  mapper-locations: classpath*:com/xxx/**/*Dao.xml
  configuration:
    map-underscore-to-camel-case: true
```

每个服务在自己的 Nacos 配置中只写自己特有的东西：

```yaml
# user-service.yaml
server:
  port: 9003
  servlet:
    contextPath: /user/api

spring:
  datasource:
    druid:
      url: jdbc:postgresql://${db-address}/user_service?currentSchema=public
```

三层配置优先级：**服务专属配置 > 共享配置 > 框架默认值**。服务可以覆写共享配置中的任意值。

还有一个容易忽视的点：共享配置中**不应该有安全敏感信息的默认值**。比如 SM2 密钥，框架不应该提供默认的，而是要业务方显式配置。如果一个框架提供了 SM2 默认密钥，绝大多数业务方不会去改，那加密就成了摆设。

```yaml
# 共享配置中这样写就够了
secret:
  sm2:
    privateKey:    # 留空，强制业务方显式配置
    publicKey:     # 留空
```

这不是给使用者制造麻烦，这是保护他们。

---

配置管理这篇已经是第五篇了。回顾一下这几篇文章串起来的逻辑：先从整体架构切入（第一篇），然后落到工程规范（第二篇），接着深入 Response 和异常处理的设计细节（第三篇），再到缓存组件的接口和实现重构（第四篇），这篇讲配置管理的系统性优化。下一篇，我们聊代码质量保障——Checkstyle、PMD、SonarQube 怎么在一个项目型组织中落地，不是理想化的"工具选型"，而是真实地面对"历史代码太多、团队成员抵触"的现实。