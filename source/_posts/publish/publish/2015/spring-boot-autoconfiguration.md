---
title: Spring Boot 自动配置
keywords:
  - Spring
categories:
  - Spring
tags:
  - Spring
description: " "
abbrlink: 6961d5da
date: 2015-09-20 00:00:00
---

spring boot 之所以能够自动配置 bean，是通过基于条件来配置 Bean 的能力实现的。

常用的条件注解如下

```
1. @ConditionalOnBean：当容器里存在指定的Bean的条件下
2. @ConditionalOnClass：当前类路径下存在指定的类的条件下
3. @ConditionalOnExpression：基于SpEL表达式作为判断条件
4. @ConditionalOnJava：基于JVM版本作为判断条件
5. @ConditionalOnJndi：在JNDI存在的条件下查找指定的位置
6. @ConditionalOnMissingBean：当容器里没有指定的Bean的条件下
7. @ConditionalOnMissingClass：当前类路径下没有指定的类的条件下
8. @ConditionalOnNotWebApplication：当前项目不是web项目的条件下
9. @ConditionalOnProperty：指定的属性是否有指定的值的条件下
10. @ConditionalOnResource：类路径下是否有指定的值
11. @ConditionalOnSingleCandidate：指定Bean在容器中只有一个，或者虽然有多个但是指定首选的Bean
12. @ConditionalOnWebApplication：当前项目是Web项目的条件下
```

这些注解都组合了@Conditional 注解，只是使用了不同的条件。

接下来我们自己写一个自动配置，并且封装成 starter pom。

首先创建 maven 工程，导入以下依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-autoconfigure</artifactId>
    <version>1.3.8.RELEASE</version>
</dependency>
```

创建 AuthorProperties 类，作为配置信息的载体

```java
import org.springframework.boot.context.properties.ConfigurationProperties;
@ConfigurationProperties(prefix="author")//指定配置内容的前缀
public class AuthorProperties {
    private static final String NAME = "微儿博客";
    private static final int AGE = 18;
    private String name = NAME;//默认为微儿博客
    private int age = AGE;//默认为18
}
```

创建 AuthorService 类，作为 Bean

```java
public class AuthorService {
    private String name;
    private int age;
}
```

创建配置类 AuthorServiceAutoConfiguration，负责配置 Bean

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration//声明配置类
@EnableConfigurationProperties(AuthorProperties.class)
@ConditionalOnClass(AuthorService.class)//类路径下存在AuthorService类的条件下
@ConditionalOnProperty(prefix="author",value="enabled",matchIfMissing=true)//在前缀为author的配置为enabled的情况下，即author=enabled,没有配置默认为enabled
public class AuthorServiceAutoConfiguration {

    @Autowired
    private AuthorProperties authorProperties;

    @Bean
    @ConditionalOnMissingBean(AuthorService.class)//容器中没有AuthorService的Bean的条件下配置该Bean
    public AuthorService authorService(){
        AuthorService authorService = new AuthorService();
        authorService.setName(authorProperties.getName());
        authorService.setAge(authorProperties.getAge());
        return authorService;
    }
}
```

若想自动配置生效，需要注册自动配置类。在 src/main/resources 下创建 META-INF/spring.factories 文件，并写入以下内容：

```lua
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.springboot.springboot_starter_hello.AuthorServiceAutoConfiguration
```

若有多个自动配置类，则用 "," 隔开，此处`\` 是为了换行后仍能读到属性。

以上操作完成后执行 maven install。

然后在 Spring Boot 项目中引入该依赖：

```xml
<dependency>
    <groupId>com.springboot</groupId>
    <artifactId>springboot-starter-hello</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</dependency>
```

新建 AutoConfig 类：

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.springboot.springboot_starter_hello.AuthorService;

@SpringBootApplication
@RestController
public class AutoConfig {

    @Autowired
    private AuthorService authorService;

    @RequestMapping("/")
    public String who(){
        return authorService.who();
    }

    public static void main(String[] args) {
        SpringApplication.run(AutoConfig.class, args);
    }
}
```

运行该类，访问 localhost:8080,出现如下结果：name: 微儿博客,age:18

接下来在 src/main/resources 下新建 application.properties 文件，写入以下内容：

```
author.name=weare
author.age=19
```

重新运行 AutoConfig 类：name:weare,age:19
