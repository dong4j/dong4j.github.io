---
title: SSO单点登录优化：Shiro认证过程详解与代码封装技巧
categories:
  - 新时代码农
tags:
  - Shiro
  - 登录逻辑优化
  - UsernamePasswordToken
  - 认证过程
  - 模块封装
abbrlink: 205ef910
date: 2018-10-09 00:00:00
ai:
  - 文章介绍了如何通过封装登录逻辑到模块中作为插件来优化代码，并详细解释了Shiro认证过程中的各个阶段。包括收集实体/凭据信息、提交凭证消息、执行认证和处理认证结果，以及登出操作。此外，文章还解析了SimpleAuthenticationInfo的使用方式及内部实现原理。
description: 文章介绍了如何通过封装登录逻辑到模块中作为插件来优化代码，并详细解释了Shiro认证过程中的各个阶段。包括收集实体/凭据信息、提交凭证消息、执行认证和处理认证结果，以及登出操作。此外，文章还解析了SimpleAuthenticationInfo的使用方式及内部实现原理。
---

多个模块有登录需求, 但是代码都是相互拷贝, 没有做统一处理

## 优化方案

将登录逻辑封装成模块, 作为插件提供服务

## shiro 认证过程

### 1. 收集实体/凭据信息

```java
UsernamePasswordToken token = new UsernamePasswordToken(username, password, true);
```

UsernamePasswordToken 支持最常见的用户名/密码的认证机制。同时，由于它实现了 Rarraydsj@163.comemberMeAuthenticationToken 接口，我们可以通过令牌设置“记住我”的功能。  
但是，“已记住”和“已认证”是有区别的：  
 已记住的用户仅仅是非匿名用户，你可以通过 subject.getPrincipals() 获取用户信息。但是它并非是认证通过的用户，当你访问需要认证用户的功能时，你仍然需要重新提交认证信息。  
 这一区别可以参考淘宝网站，网站会默认记住登录的用户，再次访问网站时，对于非敏感的页面功能，页面上会显示记住的用户信息，但是当你访问网站账户信息时仍然需要再次进行登录认证

### 2. 提交实体/凭据消息

```java
SecurityUtils.getSubject().login(token);
```

### 3. 认证

如果自定义 Realm 实现, 但执行第二步中的 login() 时, 会回调 `doGetAuthenticationInfo()`

```java
protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authcToken) throws AuthenticationException {
	// 获取基于用户名和密码的令牌
	// 实际上这个 token 是从 LoginController 里面 SecurityUtils.getSubject().login(token) 传过来的
	UsernamePasswordToken token = (UsernamePasswordToken) authcToken;
	String username = token.getUsername();
	if (!StringUtils.isEmpty(username)) {
		// 从数据库中查询用户用信息
		LoginModel model = authorityService.getLoginModel(username);
		// 原来没有判断 model 是否为 null 的语句, 会造成 model.getPassword() 语句 空指针异常
		if(model != null){
			// 此处无需比对,比对的逻辑 Shiro 会做, 我们只需返回一个和令牌相关的正确的验证信息
			return new SimpleAuthenticationInfo(StringUtils.upperCase(username), model.getPassword(), getName());
		}
	}
	return null;
}
```

### 4. 认证处理

```java
try {
		SecurityUtils.getSubject().login(token);
} catch (AuthenticationException e) {
	model.addAttribute("message", "用户名或密码错误或用户已被禁用");
	return "login";
}
```

发生异常时, 给出提示信息, 返回到登录页面

如果 login 方法执行完毕且没有抛出任何异常信息，那么便认为用户认证通过。之后在应用程序任意地方调用 SecurityUtils.getSubject() 都可以获取到当前认证通过的用户实例，使用 subject.isAuthenticated() 判断用户是否已验证都将返回 true.  
相反，如果 login 方法执行过程中抛出异常，那么将认为认证失败

### 4. 登出操作

登出操作可以通过调用 subject.logout() 来删除你的登录信息，如：

```
SecurityUtils.getSubject().logout();
```

### SimpleAuthenticationInfo

SimpleAuthenticationInfo 这里原理很简单，又有一些值得挖掘的东西。

```java
//此处使用的是user对象，不是username
SimpleAuthenticationInfo authenticationInfo = new SimpleAuthenticationInfo(
        user,
        user.getPassword(),
        getName()
);
```

这个东西是在 realm 中的，第一个参数 user，这里好多地方传的时候都是 user 对象，但是都在备注用户名。可是我如果传入 username，就会报类型转换问题。

但是在开涛大神的博客中，无状态的 shiro 里，那边给出的例子是传 username。我自己测试的，可以传 username，也可以传 user 对象，仅限他那边一段代码。网上有文章说，这里其实是 user 和 username 的集合，后端是分两个字段接收的。由于时间的问题，没有深入里了解这块，传 user 对象是 OK 的。

第二个字段是 user.getPassword()，注意这里是指从数据库中获取的 password。

第三个字段是 realm，即当前 realm 的名称。

看了几篇文章介绍说，这块对比逻辑是先对比 username，但是 username 肯定是相等的，所以真正对比的是 password。从这里传入的 password（这里是从数据库获取的）和 token（filter 中登录时生成的）中的 password 做对比，如果相同就允许登录，不相同就抛出异常。

如果验证成功，最终这里返回的信息 authenticationInfo 的值与传入的第一个字段的值相同（我这里传的是 user 对象）。
