---
title: Spring Boot 入门指南：从基础到实践
keywords:
  - Spring Boot
  - main类位置
  - 构造器注入
  - 开发者工具
  - 配置文件
  - 环境选择
  - 日志配置
categories:
  - 新时代码农
tags:
  - Spring Boot
  - main类位置
  - 构造器注入
  - 开发者工具
  - 配置文件
  - 环境选择
  - 日志配置
abbrlink: f2cb7e19
date: 2014-08-17 00:00:00
ai:
  - 本文探讨了Spring Boot应用中main类放置位置的建议。建议将main类放在所有类所在包的顶层，以便于使用@ComponentScan和@SpringBootApplication注解，简化配置。同时，文章还介绍了构造器注入、开发者工具（如devtools）的使用，以及配置文件和环境选择等高级特性。此外，还提到了Spring
    Boot的一些调试和管理特性，例如远程调试、自定义Banner、Application事件监听器和Admin特性等。最后，本文简要描述了日志配置的选择和定制方法。
description: 本文探讨了Spring Boot应用中main类放置位置的建议。建议将main类放在所有类所在包的顶层，以便于使用@ComponentScan和@SpringBootApplication注解，简化配置。同时，文章还介绍了构造器注入、开发者工具（如devtools）的使用，以及配置文件和环境选择等高级特性。此外，还提到了Spring
  Boot的一些调试和管理特性，例如远程调试、自定义Banner、Application事件监听器和Admin特性等。最后，本文简要描述了日志配置的选择和定制方法。
---

## Spring Boot 为什么建议将 main 类放在所有类所在包的顶层

> 通常建议将应用的 main 类放到其他类所在包的顶层 (root package)，并 将 @EnableAutoConfiguration 注解到你的 main 类上，这样就隐式地定义了一个 基础的包搜索路径（search package），以搜索某些特定的注解实体（比如 @Service，@Component 等） 。例如，如果你正在编写一个 JPA 应用，Spring 将 搜索 @EnableAutoConfiguration 注解的类所在包下的 @Entity 实体。

采用 root package 方式，你就可以使用 @ComponentScan 注解而不需要指 定 basePackage 属性，也可以使用 @SpringBootApplication 注解，只要将 main 类放到 root package 中。

@SpringBootApplication 等同于**以默认属性**使用一下注解:

1. @EnableAutoConfiguration
2. @ComponentScan 扫描所有 Spring 组件 (@Component , @Service , @Repository , @Controller)，包括 @Configuration 类。
3. @Configuration

**自定义属性**  
@SpringBootApplication(exclude = {}, excludeName = {}, scanBasePackages = {}, scanBasePackageClasses = {})

## 构造器注入

1. @Autowired 可省略
2. 注入的 bean 可以为 final

```java
@Service
public class DatabaseAccountService implements AccountService {
	private final RiskAssessor riskAssessor;
	@Autowired
	public DatabaseAccountService(RiskAssessor riskAssessor) {
		this.riskAssessor = riskAssessor;
	}
}
```

## 开发者工具

```xml
<!-- 热部署 -->
<!-- devtools可以实现页面热部署（即页面修改后会立即生效，这个可以直接在application.properties文件中配置spring.thymeleaf.cache=false来实现） -->
<!-- 实现类文件热部署（类文件修改后不会立即生效），实现对属性文件的热部署。 -->
<!-- 即devtools会监听classpath下的文件变动，并且会立即重启应用（发生在保存时机），注意：因为其采用的虚拟机机制，该项重启是很快的 -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-devtools</artifactId>
  <!-- optional=true,依赖不会传递，该项目依赖devtools；之后依赖boot项目的项目如果想要使用devtools，需要重新引入 -->
  <optional>true</optional>
</dependency>
```

application.properties 配置

```
#添加那个目录的文件需要restart
spring.devtools.restart.additional-paths=src/main/java
#排除那个目录的文件不需要restart
spring.devtools.restart.exclude=static/**,public/**
```

> 在运行一个完整的，打包过的应用时，开发者工具（devtools）会被自动禁用。 如果应用使用 java -jar 或特殊的类加载器启动，都会被认为是一个产品级的应 用（production application），从而禁用开发者工具。为了防止 devtools 传递到项 目中的其他模块，设置该依赖级别为 optional 是个不错的实践

**Spring Loaded 或 JRebel 项目**

<http://blog.csdn.net/JE_GE/article/details/53326525>  
<http://blog.csdn.net/isea533/article/details/70495714>

## spring boot 远程调试

## FailureAnalyzer

<https://docs.spring.io/spring-boot/docs/2.0.0.M5/reference/htmlsingle/#howto-failure-analyzer>

## 自定义 Banner

## 自定义 SpringApplication

```java
public static void main(String[] args) {
		SpringApplication app = new SpringApplication(MySpringConfig.uration.class);
		app.setBannerMode(Banner.Mode.OFF);
		app.run(args);
	}
```

## Application 事件和监听器

## Admin 特性

> 通过设置 spring.application.admin.enabled 属性可以启用管理相关的 （admin-related）特性，这将暴露 SpringApplicationAdminMXBean 到平台 的 MBeanServer ，你可以使用该特性远程管理 Spring Boot 应用，这对任何 service 包装器（wrapper）实现也有用。

注 通过 local.server.port 可以获取该应用运行的 HTTP 端口。启用该特性时需 要注意 MBean 会暴露一个方法去关闭应用。

## Application 属性文件

1. 当前目录下的 /config 子目录。
2. 当前目录。
3. classpath 下的 /config 包。
4. classpath 根路径（root）。

## 配置文件

通过设置启动参数来选择环境, 只需要打一次包, 就可以在不同环境运行

## 日志

Spring Boot 默认日志框架为 logback, 默认控制台输出

根据日志配置文件的名称选择日志系统

| 日志系统                | 定制配置                                                            |
| ----------------------- | ------------------------------------------------------------------- |
| Logback                 | logback-spring.xml logback-spring.groovy logback.xml logback.groovy |
| Log4j                   | log4j.properties log4j.xml                                          |
| Log4j2                  | log4j2-spring.xml log4j2.xml                                        |
| JDK (Java Util Logging) | logging.properties                                                  |
