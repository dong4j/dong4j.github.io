---
title: SpringBoot 退出服务时调用自定义销毁方法的两种方式
keywords:
  - SpringBoot
  - DisposableBean
  - '@PreDestroy'
  - 容器销毁
categories:
  - 新时代码农
tags:
  - SpringBoot
  - DisposableBean
  - '@PreDestroy'
  - 容器销毁
abbrlink: 442823ed
date: 2016-06-11 00:00:00
ai:
  - 本文介绍了在SpringBoot应用中如何在工作容器退出时执行特定操作的方法，包括通过实现DisposableBean接口和使用@PreDestroy注解两种方式。并通过代码示例展示了这两种方法的具体使用。文章还提供了关于如何在命令行启动并正确地终止应用的技巧。
description: 本文介绍了在SpringBoot应用中如何在工作容器退出时执行特定操作的方法，包括通过实现DisposableBean接口和使用@PreDestroy注解两种方式。并通过代码示例展示了这两种方法的具体使用。文章还提供了关于如何在命令行启动并正确地终止应用的技巧。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://cover.dong4j.ink:1024)

我们在工作中有时候可能会遇到这样场景，需要在退出容器的时候执行某些操作。SpringBoot 中有两种方法可以供我们来选择（其实就是 spring 中我们常用的方式。只是 destory-method 是在 XML 中配置的，SpringBoot 是去配置化。所以这里就不提这种方式了），一种是实现 DisposableBean 接口，一种是使用@PreDestroy 注解。OK，下面我写两个例子看一下：

## DisposableBean 接口

我们可以通过实现这个接口来在容器退出的时候执行某些操作。例子如下：

```java

@Component
public class TestImplDisposableBean implements DisposableBean, ExitCodeGenerator {

    @Override
    public void destroy() throws Exception {

        System.out.println("<<<<<<<<<<<我被销毁了......................>>>>>>>>>>>>>>>");
        System.out.println("<<<<<<<<<<<我被销毁了......................>>>>>>>>>>>>>>>");
    }

    @Override
    public int getExitCode() {

        return 5;
    }
}

```

## @PreDestroy 注解

我们可以在需要的类的方法上添加这个注解，同样可以满足我们的需求。

```java
@Component
public class TestAnnotationPreDestroy {

    @PreDestroy
    public void destory() {

        System.out.println("我被销毁了、、、、、我是用的@PreDestory的方式、、、、、、");
        System.out.println("我被销毁了、、、、、我是用的@PreDestory的方式、、、、、、");
    }
}

```

## TIPS：

退出你可以通过 Ide 中的功能来退出。这里我启动的时候是在 CMD 中用 jar 启动的，启动命令如下：java -jar LearnSpringBoot-0.0.1-SNAPSHOT.jar，所以我在这里退出的时候是用的 Ctrl+C 来执行的退出操作。如果你用的 mvn spring-boot:run 来启动运行的话，可能不会执行销毁的操作。
