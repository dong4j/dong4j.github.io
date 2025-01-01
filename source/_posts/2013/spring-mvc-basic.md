---
title: 探索Spring MVC注解驱动：从基础到高级
keywords:
  - Spring
categories:
  - 新时代码农
tags:
  - Spring配置
  - 注解配置
  - 数据绑定
  - 类型转换
  - 输入验证
abbrlink: aab1eaf1
date: 2013-04-12 00:00:00
ai:
  - 本文介绍了如何在Spring框架中使用多个配置文件进行处理。通过逗号分隔配置文件、利用通配符和注解驱动等方式来优化配置。阐述了RequestMapping注解的应用场景，包括value、params与method属性，并且讲解了请求处理方法可接受的HTTP相关组件如HttpServletRequest,
    HttpServletResponse以及Session等。同时，详细讨论了数据绑定过程，包括基本数据类型、字符串数组、Bean绑定及List绑定的方法。另外，还涉及了不同类型转换的需求通过@InitBinder和Converter实现，以及输入验证的重要工具Hibernate
    Validator的使用。文章最后提及了文件上传的基础知识和拦截器的概念，特别是HandlerInterceptor的使用场景与特性，包括perHandler、postHandler和alterCompletion方法，并简述了它们的主要用途。
description: 本文介绍了如何在Spring框架中使用多个配置文件进行处理。通过逗号分隔配置文件、利用通配符和注解驱动等方式来优化配置。阐述了RequestMapping注解的应用场景，包括value、params与method属性，并且讲解了请求处理方法可接受的HTTP相关组件如HttpServletRequest,
  HttpServletResponse以及Session等。同时，详细讨论了数据绑定过程，包括基本数据类型、字符串数组、Bean绑定及List绑定的方法。另外，还涉及了不同类型转换的需求通过@InitBinder和Converter实现，以及输入验证的重要工具Hibernate
  Validator的使用。文章最后提及了文件上传的基础知识和拦截器的概念，特别是HandlerInterceptor的使用场景与特性，包括perHandler、postHandler和alterCompletion方法，并简述了它们的主要用途。
---

多个 Spring 配置文件处理

1.  采用逗号将多个配置文件分开
2.  使用通配符

开启注解:
`<mvc:annotation-driven>`
开启自动扫描
`<context:component-scan base-package="包"`

使用 Annotation 不用使用继承父类或者实现接口

RequestMapping

1. value
2. params -->对请求参数进行过滤
3. method -->代表请求方式 通过提交方式进行过滤请求

请求处理方法可以接受参数
HttpServletRequest
HttpServletRespones
HttpServletSession

@RequsetParam 注解

restful
representational state transfer
表现层状态转移

请求处理方法可以返回的值

## 数据绑定

1. 基本数据类型,String String[]绑定
   - 只需要让 jsp 中的 name 值和 controller 中的属性名相同即可
2. 绑定到一个 Bean 当中去
   - 只要保证 Bean 中属性的名字和表单数据的 name 一样
3. List 绑定

## 类型转换

@InitBinber
Converter-->类型转换器

## 输入验证

Hibernate Validator

## 文件上传

## 拦截器

实现 HandlerInterceptor

1. perHandler -->Controller 前
2. postHandler -->Controller 后
3. alterCompletion -->一般进行一些清理工作

继承 HandlerInterptorAdaptor
