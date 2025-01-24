---
title: 深入理解Spring Profiles：定制化配置的艺术
categories:
  - 新时代码农
tags:
  - Spring
  - Bean
  - Profile
  - Configuration
abbrlink: 278e3e03
date: 2019-12-02 00:00:00
ai:
  - 本文介绍了如何在Spring框架中利用Profile功能来管理不同环境下Bean的配置。文章首先解释了从Spring 3.1开始支持根据不同profile（如开发、测试和产品）动态加载Bean的概念。接着详细说明了如何使用`@Profile`注解将Bean绑定到特定profile，以及如何在XML配置文件中声明profile。然后讨论了几种设置和激活profile的方法，包括通过WebApplicationInitializer接口、ConfigurableEnvironment、web.xml配置、JVM参数、环境变量以及Maven
    Profile等。最后，文章以一个示例说明了如何在测试中使用`@ActiveProfiles`注解指定profile，并在Spring Boot环境下展示了如何使用profile-specific
    profiles文件来为不同环境配置不同的数据库连接信息。
description: 本文介绍了如何在Spring框架中利用Profile功能来管理不同环境下Bean的配置。文章首先解释了从Spring 3.1开始支持根据不同profile（如开发、测试和产品）动态加载Bean的概念。接着详细说明了如何使用`@Profile`注解将Bean绑定到特定profile，以及如何在XML配置文件中声明profile。然后讨论了几种设置和激活profile的方法，包括通过WebApplicationInitializer接口、ConfigurableEnvironment、web.xml配置、JVM参数、环境变量以及Maven
  Profile等。最后，文章以一个示例说明了如何在测试中使用`@ActiveProfiles`注解指定profile，并在Spring Boot环境下展示了如何使用profile-specific
  profiles文件来为不同环境配置不同的数据库连接信息。
keywords:
  - Spring
  - Bean
  - Profile
  - Configuration
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## 1. 概述

这篇文章将阐述怎么在 Spring 中使用 Profile

从 Spring 3.1 开始，我们能够将 bean 映射到不同的 profile 上，如 dev, test, prod 等。

我们也能够根据环境 (environment) 来激活不同的 profile，从而加载我们需要的 bean。

## 2. 在 Bean 上使用  `@Profile`

我们先从简单的例子开始，看看怎么把 bean 绑定到不同的 profile 上。

使用  `@Profile`  注解，我们可以将 bean 绑定到指定的 profile 上。这个注解支持绑定一个或多个 profile。

试想这样一个场景：我们有一个 bean，只在开发环境需要，线上环境不需要。那么我们可以通过注解将这个 bean 绑定到  `dev profile`  上。这样，这个 bean 只会存在于开发环境，而在其他环境中不会被加载。如下所示：

```java
@Component
@Profile("dev")
public class DevDatasourceConfig

```

上面的写法是指绑定 bean 到  `dev profile`。如果想绑定 bean 到除  `dev`  以外的 profile 呢。可以使用  **NOT 操作符**。如下所示：

```java
@Component
@Profile("!dev")
public class DevDatasourceConfig
```

> 译者注：  
> `@Profile`  的声明如下：
>
> ```
> public @interface Profile {
>    String[] value();
> }
>
> ```
>
> `value`  是个数组，支持多个值。绑定多个 profile，如下所示：
>
> ```
> @Profile(value = {"dev", "test"})
>
> ```

## 3. 在 XML 中声明 Profile

除了使用  `@Profile`  注解，还可以在 XML 中绑定 profile。

`<bean>`  标签有个  `profiles`  属性。多个 profile 之间使用逗号分隔：

`profile还是profiles？？？`

```xml
<beans profile="dev">
    <bean id="devDatasourceConfig"
      class="org.baeldung.profiles.DevDatasourceConfig" />
</beans>

```

## 4. 设置 profile

上面只是将 bean 和 profile 进行了绑定，下一步需要设置和激活 profile，才能使不同的 bean 被注册到容器中。方法有很多种，下面是一些例子：

### 4.1 使用  `WebApplicationInitializer` interface

这是一种编程的方式 (与之对应是配置方式)

在 web 应用中，`WebApplicationInitializer`  可以被用来配置  `ServletContext`。

> 译者注：  
> `WebApplicationInitializer`  在 spring-web 中

方法如下：

```java
@Configuration
public class MyWebApplicationInitializer
  implements WebApplicationInitializer {

    @Override
    public void onStartup(ServletContext servletContext) throws ServletException {

        servletContext.setInitParameter(
          "spring.profiles.active", "dev");
    }
}

```

> 译者注：  
> 这种方式，直接把要绑定的 profile 硬编码到代码中，是非常不优雅，也不方便的。

### 4.2 使用  `ConfigurableEnvironment`

你也可以直接在环境中设置 profile:

```java
@Autowired
private ConfigurableEnvironment env;
...
env.setActiveProfiles("someProfile");
```

> 译者注：  
> 问题同 4.1

### 4.3 在  `web.xml`  中配置

```xml
<context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/app-config.xml</param-value>
</context-param>
<context-param>
    <param-name>spring.profiles.active</param-name>
    <param-value>dev</param-value>
</context-param>
```

> 译者注：  
> 问题同 4.1，4.2。 本人不赞成任何硬编码的方式

### 4.4 通过 JVM 参数设置

profile 的名字还可以通过 JVM 参数的方式设置。在启动的时候，添加类似如下参数：

`-Dspring.profiles.active=dev`

> 译者注：  
> 如  `java -jar xxx.jar -Dspring.profiles.active=dev`

### 4.5 通过环境变量设置

通过设置环境变量，也是可以的：

`export spring_profiles_active=dev`

### 4.6 Maven Profile

Spring profile 也可以结合 maven profile 使用，通过设置  `spring.profiles.active`  属性：

```xml
<profiles>
    <profile>
        <id>dev</id>
        <activation>
            <activeByDefault>true</activeByDefault>
        </activation>
        <properties>
            <spring.profiles.active>dev</spring.profiles.active>
        </properties>
    </profile>
    <profile>
        <id>prod</id>
        <properties>
            <spring.profiles.active>prod</spring.profiles.active>
        </properties>
    </profile>
</profiles>
```

同时，还需要在  `application.properties`(如果使用 spring boot 的话) 中添加如下设置：

```java
spring.profiles.active=@spring.profiles.active@

```

另外，还需要再  `pom.xml`  文件中添加如下配置：

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <filtering>true</filtering>
        </resource>
    </resources>
    ...
</build>
```

> 译者注：  
> 在  `pom.xml`  中添加的配置，意思是开启占位符替换。可参考：[Maven Filtering](https://maven.apache.org/plugins/maven-resources-plugin/examples/filter.html)

结合使用 maven profile 后，就可以在打包的时候激活某个 profile:

```shell
mvn clean package -Pprod
```

> 译者注：  
> 个人认为，结合 maven profile 的这种办法，灵活度最高，也最方便，推荐。

### 4.7 Test 中使用  `@ActiveProfiles`

在 test 时，如何指定 profile 呢？也很简单，通过  `@ActiveProfiles`  注解就可以了。

> @ActiveProfiles("dev")

## 5. 默认 profile

如果不指定任何 profile，那么这个 bean 就属于  `default` profile

当没有任何 profile 被激活时，spring 也支持设置默认 profile。就是通过  `spring.profiles.default`  参数。

## 6. 获取被激活的 profile

一旦 profile 被激活，我们就可以通过  `Environment`，在运行时获取这些 profile 的信息：

```java
public class ProfileManager {
    @Autowired
    Environment environment;

    public void getActiveProfiles() {
        for (final String profileName : environment.getActiveProfiles()) {
            System.out.println("Currently active profile - " + profileName);
        }
    }
}
```

## 7. 使用 Profile 的例子

理论总是抽象的，下面我们通过一些例子来深入理解。

试想这样一个场景：我们要分别针对开发环境和线上环境，对 datasource 进行设置。我们先创建一个  `DatasourceConfig`  接口。这个接口需要在两个环境中都被实现。

```java
public interface DatasourceConfig {
    public void setup();
}
```

开发环境的实现：

```java
@Component
@Profile("dev")
public class DevDatasourceConfig implements DatasourceConfig {
    @Override
    public void setup() {
        System.out.println("Setting up datasource for DEV environment. ");
    }
}
```

线上环境的实现：

```java
@Component
@Profile("production")
public class ProductionDatasourceConfig implements DatasourceConfig {
    @Override
    public void setup() {
       System.out.println("Setting up datasource for PRODUCTION environment. ");
    }
}
```

下面我们写个单元测试，并注入  `DatasourceConfig`。那么我们通过设置不同的 profile，就会分别注入  `DevDatasourceConfig` bean 和  `ProductionDatasourceConfig` bean。

```java
public class SpringProfilesTest {
    @Autowired
    DatasourceConfig datasourceConfig;

    public void setupDatasource() {
        datasourceConfig.setup();
    }
}
```

当  `dev` profile 被激活的时候，会有如下输出：

> Setting up datasource for DEV environment.

## 8. 在 Spring Boot 中使用 Profile

Spring Boot 除了支持所有的 profile 配置，还有提供一些额外功能。

`spring.profiles.active`  的初始化可以在配置文件中设定:

```java
spring.profiles.active=dev
```

当然也可以在程序中设定：

```java
SpringApplication.setAdditionalProfiles("dev");
```

还可以在 pom.xml 文件中的  `spring-boot-maven-plugin`  中配置：

```xml
<plugins>
    <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <configuration>
            <profiles>
                <profile>dev</profile>
            </profiles>
        </configuration>
    </plugin>
    ...
</plugins>
```

用 maven 启动，可执行命令:

```shell
mvn spring-boot:run
```

但是 Spring Boot 带来的最重要的特性是  **profile-specific profiles**  文件，这些文件的命名方式需要遵循  `applications-{profile}.properties`  的格式。

举个例子：我们可以在开发环境和线上环境使用不同的数据库。如开发环境使用 h2，线上环境使用 mysql。那么，我们分别需要创建如下两个文件：

**application-production.properties**

```java
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/db
spring.datasource.username=root
spring.datasource.password=root
```

**application-dev.properties**

```java
spring.datasource.driver-class-name=org.h2.Driver
spring.datasource.url=jdbc:h2:mem:db;DB_CLOSE_DELAY=-1
spring.datasource.username=sa
spring.datasource.password=sa
```

如果激活的 profile 是  `dev`，则  **application-dev.properties**  配置文件会被自动加载。如果激活的 profile 是  `production`，则  **application-production.properties**  配置文件会被加载。

通过这种方式，我们就很容易地针对不同环境，配置不同的配置文件。
