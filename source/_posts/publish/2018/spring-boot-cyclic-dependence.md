---
title: Springboot 循环依赖解决办法
categories:
  - Java
tags:
  - Springboot
  - shiro
  - 循环依赖
  - 解决方案
  - 懒加载
abbrlink: 62ae7a01
date: 2018-06-11 00:00:00
ai:
  - 在使用SpringBoot进行项目开发时遇到了引入shiro后出现的依赖循环报错问题。通过排查发现存在服务之间的循环调用导致的问题。解决方法包括：一、重构代码以消除耦合；二、在配置文件中为互相依赖的服务添加lazy-init属性；三、在注入bean时使用@Lazy注解延迟加载其中一个bean，从而解决了循环依赖错误。
description: 在使用SpringBoot进行项目开发时遇到了引入shiro后出现的依赖循环报错问题。通过排查发现存在服务之间的循环调用导致的问题。解决方法包括：一、重构代码以消除耦合；二、在配置文件中为互相依赖的服务添加lazy-init属性；三、在注入bean时使用@Lazy注解延迟加载其中一个bean，从而解决了循环依赖错误。
---

最近在使用 Spingboot 做项目的时候，在引入 shiro 后，启动项目一直报错

```lua
Error creating bean with name 'debtServiceImpl': Bean with name 'debtServiceImpl' has been injected into other beans [repayBillServiceImpl,investServiceImpl,receiveBillServiceImpl] in its raw version as part of a circular reference, but has eventually been wrapped. This means that said other beans do not use the final version of the bean. This is often the result of over-eager type matching - consider using 'getBeanNamesOfType' with the 'allowEagerInit' flag turned off, for example.
```

后来在网上找了半天说是依赖循环，检查了一下代码，确实存在循环依赖的现象，但是项目快要上线，再去改代码逻辑是来不及了，于是各种找解决方案，终于算是找到了。

首先说一下什么是依赖循环，比如：我现在有一个 ServiceA 需要调用 ServiceB 的方法，那么 ServiceA 就依赖于 ServiceB，那在 ServiceB 中再调用 ServiceA 的方法，就形成了循环依赖。Spring 在初始化 bean 的时候就不知道先初始化哪个 bean 就会报错。

```
public class ClassA {
    @Autowired
    ClassB classB;
}
public class ClassB {
    @Autowired
    ClassA classA;
}
```

那如何解决循环依赖，当然最好的方法是重构你的代码，进行解耦，但是重构不是一时的事情，那就使用下面的方法：

第一种：

```xml
<bean id="ServiceDependent1" class="org.xyz.ServiceDependent1" lazy-init="true">
    <constructor-arg ref="Service"/>
</bean>
<bean id="ServiceDependent2" class="org.xyz.ServiceDependent2" lazy-init="true">
    <constructor-arg ref="Service"/>
</bean>
```

在你的配置文件中，在互相依赖的两个 bean 的任意一个加上 lazy-init 属性。

第二种：

```java
@Autowired
@Lazy
private ClassA classA;
@Autowired
@Lazy
private ClassB classB;
```

在你注入 bean 时，在互相依赖的两个 bean 上加上@Lazy 注解也可以。

以上两种方法都能延迟互相依赖的其中一个 bean 的加载，从而解决循环依赖的问题。
