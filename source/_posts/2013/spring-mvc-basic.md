---
title: 探索Spring MVC注解驱动：从基础到高级
keywords:
  - Spring 配置
  - 多配置文件
  - 注解驱动
  - 自动扫描
  - RequestMapping
  - 数据绑定
  - 类型转换
  - 输入验证
  - 文件上传
  - 拦截器
categories:
  - 新时代码农
tags:
  - Spring 配置
  - 多配置文件
  - 注解驱动
  - 自动扫描
  - RequestMapping
  - 数据绑定
  - 类型转换
  - 输入验证
  - 文件上传
  - 拦截器
abbrlink: aab1eaf1
date: 2013-04-12 00:00:00
ai:
  - 本文探讨了Spring框架中多配置文件的处理方法，包括使用逗号和通配符分隔配置文件以及如何开启注解驱动和自动扫描。文章还介绍了如何在Spring中使用@RequestMapping注解来处理HTTP请求，并讨论了数据绑定、类型转换和输入验证等方面。最后，文章简单提及了文件上传和拦截器的相关内容。
description: 本文探讨了Spring框架中多配置文件的处理方法，包括使用逗号和通配符分隔配置文件以及如何开启注解驱动和自动扫描。文章还介绍了如何在Spring中使用@RequestMapping注解来处理HTTP请求，并讨论了数据绑定、类型转换和输入验证等方面。最后，文章简单提及了文件上传和拦截器的相关内容。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover)

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
