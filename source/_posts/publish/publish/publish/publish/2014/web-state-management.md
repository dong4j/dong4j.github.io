---
title: Web 应用状态管理
keywords:
  - Spring
categories:
  - Spring
tags:
  - Spring
abbrlink: "25473362"
date: 2014-07-05 00:00:00
---

Web 服务器一旦发出响应,一个请求响应过程就结束了.  
当再次发出请求时,Web 服务器不记得曾就做过的请求,也不记得给用户发出过响应.,这就是 http 的无状态模式

当需要跨多个请求需要保留与客户端会话状态时,我们有 4 种解决方案

## 表单隐藏字段

`<input type="hidden" name="userName" value="…">`  
作用:

1. 对用户在网上的访问进行会话跟踪
2. 为服务器提供预定义的输入
3. 存储动态产生的网页的上下文信息

缺点: 只有当每个网页是动态生成的才有效

## Cookie

将数据已键值对的形式通过响应保存在客户端  
方法:

1. Cookie(name,value)
2. get/setComment(String comment): 注释
3. get/setDomain(String domainPattern): 得到/设置应用 Cookie 的域
4. setMaxAge(int lifetime) 设置过期时间,默认为负数,表示在关闭浏览器后过期
5. getMaxAge()
6. get/setName(String name)
7. get/setValue(String value)

将 Cookie 发送到客户端的步骤

1. 创建一个或多个 Cookie
2. 使用 setXXX 方法设置 Cookie 的可选属性
3. 使用 HttpServletResponse 对象的 addCookie() 方法将 Cookie 插入到响应头中

读取客户端传递过来的 Cookie 的步骤

1. 使用 HttpServletRequset 对象的 getCookie 方法返回一个 Cookie 对象数组
2. Servlet 遍历该数组 (getName()),直到找到名称相匹配的 Cookie 值

## Session

在服务器端为客户端创建一个唯一的 Session 对象,用于存放数据.  
在创建 Session 对象的同时,服务器会为该对象创建一个唯一的 SesionID,存储在客户端的 Cookie 当中

HttpSession 接口中的方法

1. get/setAttribute(String key,Object obj)
2. removeAttribute(String key)
3. getCreationTime() : 返回第一次创建会话的时间
4. getLastAccessedTime() : 返回容器最后一次得到该会话 ID 的请求时间
5. get/setMaxInactiveInterval(int time) : 存活时间
6. invalidate(): 结束会话
7. getId()

### 会话超时管理

结束会话的 3 种情况

1. 服务器重启或崩溃
2. 调用 invalidate() 方法
3. 会话超时

在 web.xml 中设置会话时间  
单位是分钟

```xml
<session-config>
	<session-timeout>15</session-timeout>
</session-config>
```

在程序中设置超时时间的单位是秒

### Application 和 Session 域范围的属性

Application

```java
ServletContext sc = this.getServletConfig().getServletContext();
```

### Session 持久化

Tomcat 提供的 2 个类来管理 Session 对象

1. StandardManager(默认)
   - 当服务器关闭或应用重新加载的时候在 work/Catalina/localhost/web/应用名 下创建名为 session.ser 的文件,将 session 信息写入,当宠幸加载或重启时读取这个文件,然后删除
2. PersistentManager

## URL 重写

由于 Session 依赖于 Cookie,当浏览器关闭 Cookie 时将不能使用 Cookie 和 Session,当这种情况发生时,URL 重写就派上用场了.  
URL 重写是将 SessionID 写入到 URL 当中,就不需要 Cookie 保存 SessionID

URL;jsessionid=id;

重定向中使用 URL 重写

```java
HttpSession session = requset.getSession();
String url = resquest.encodeRedirectURL("/aa/bb.html");
request.sendRedirect(url);
```

encodeURL() 是本应用级别的，encodeRedirectURL() 是跨应用的。

1. response.encodeRedirectURL(url) 是一个进行 URL 重写的方法， 使用这个方法的作用是为了在原来的 url 后面追加上 Jsessionid 。 目的是保证即使在客户端浏览器禁止了 cookie 的情况下，服务器端仍然能够对其进行事务跟踪.
2. response.sendRedirect(url) 是一个 url 重定向的方法， 服务器端的通过该方法，“告诉”客户端的浏览器去访问 url 所指向的资源

## 总结

Http 协议使用的是无状态连接
相当于每一个请求都是来自于新客户
服务器不保存客户的信息

解决方案

1. 表单隐藏字段 hidden
   缺点 :
   类型被限制,只能使用字符串
   要一层一层的传递,对不需要使用信息的网页也需要使用 hidden

2. Cookie (客户端)

```java
Cookie cookie = new Cookie("cool","tiger");
addCookie();
```

3. Session (服务端)
   SessionID 存到客户端的 Cookie 中

4. URL 重写
   把 SessionID 加到 URL 后面
