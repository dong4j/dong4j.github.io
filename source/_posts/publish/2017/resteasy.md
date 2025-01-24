---
title: RESTEasy入门：JAX-RS实践指南
keywords:
  - RestEasy
  - JAX-RS
  - WebServices
  - Java
categories:
  - 新时代码农
tags:
  - RestEasy
  - JAX-RS
  - WebServices
  - Java
description: RESTEasy是一个由JBoss提供的开源项目，用于构建RESTful Web Services和Java应用程序。它完全遵循JAX-RS规范并通过了JCP认证。RESTEasy支持与多种框架集成，如EJB、Seam、Guice、Spring等，并提供自动实现GZIP解压缩的功能。JAX-RS是一个Java
  API，用于创建RESTful Web Services。它使用Java SE 5的注释来简化Web服务的开发和部署，并提供了各种注解来定义资源类和方法，如@Path、@GET、@PUT、@POST等。
abbrlink: 9659e30c
date: 2017-03-03 00:00:00
ai:
  - RESTEasy是一个由JBoss提供的开源项目，用于构建RESTful Web Services和Java应用程序。它完全遵循JAX-RS规范并通过了JCP认证。RESTEasy支持与多种框架集成，如EJB、Seam、Guice、Spring等，并提供自动实现GZIP解压缩的功能。JAX-RS是一个Java
    API，用于创建RESTful Web Services。它使用Java SE 5的注释来简化Web服务的开发和部署，并提供了各种注解来定义资源类和方法，如@Path、@GET、@PUT、@POST等。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://cover.dong4j.ink:1024)

**RESTEasy**

RESTEasy 是 JBoss 的一个开源项目，提供各种框架帮助你构建 RESTful Web Services 和 RESTful Java 应用程序。它是 JAX-RS 规范的一个完整实现并通过 JCP 认证。作为一个 JBOSS 的项目，它当然能和 JBOSS 应用服务器很好地集成在一起。但是，它也能在任何运行 JDK5 或以上版本的 Servlet 容器中运行。RESTEasy 还提供一个 RESTEasy JAX-RS 客户端调用框架。能够很方便与 EJB、Seam、Guice、Spring 和 Spring MVC 集成使用。支持在客户端与服务器端自动实现 GZIP 解压缩。

RESTEasy  项目是  JAX-RS  的一个实现，集成的一些亮点：

- 不需要配置文件，只要把 JARs 文件放到类路径里面，添加  @Path  标注就可以了。
- 完全的把 RESTEeasy 配置作为 Seam 组件来看待。
- HTTP 请求由 Seam 来提供，不需要一个额外的 Servlet。
- Resources 和 providers 可以作为 Seam components (JavaBean or EJB)，具有全面的 Seam injection,lifecycle, interception, 等功能支持。
- 支持在客户端与服务器端自动实现 GZIP 解压缩。

**JAX-RS:**
Java API for RESTful Web Services 是一个 Java 编程语言的应用程序接口, 支持按照 表象化状态转变 (REST) 架构风格创建 Web 服务 Web 服务 [1]. JAX-RS 使用了 Java SE 5 引入的 Java 标注来简化 Web 服务客户端和服务端的开发和部署。

JAX-RS 提供了一些标注将一个资源类，一个 POJOJava 类，封装为 Web 资源。标注包括：

1. @Path，标注资源类或方法的相对路径
2. @GET，@PUT，@POST，@DELETE，标注方法是用的 HTTP 请求的类型
3. @Produces，标注返回的 MIME 媒体类型
4. @Consumes，标注可接受请求的 MIME 媒体类型
5. @PathParam，@QueryParam，@HeaderParam，@CookieParam，@MatrixParam，@FormParam, 分别标注方法的参数来自于 HTTP 请求的不同位置，例如 @PathParam 来自于 URL 的路径，@QueryParam 来自于 URL 的查询参数，@HeaderParam 来自于 HTTP 请求的头信息，@CookieParam 来自于 HTTP 请求的 Cookie。

## 配置

web.xml 配置

```xml
<web-app>
    <display-name>Archetype Created Web Application</display-name>
    <servlet>
        <servlet-name>Resteasy</servlet-name>
        <servlet-class>
            org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher
        </servlet-class>
        <init-param>
            <param-name>javax.ws.rs.Application</param-name>
            <param-value>com.restfully.shop.services.ShoppingApplication</param-value>
        </init-param>
    </servlet>
    <servlet-mapping>
        <servlet-name>Resteasy</servlet-name>
        <url-pattern>/*</url-pattern>
    </servlet-mapping>
</web-app>
```

使用 ServletContextListener 来配置

```xml
<web-app>
   <listener>
      <listener-class>
         org.jboss.resteasy.plugins.server.servlet.ResteasyBootstrap
      </listener-class>
   </listener>
  <!-- ** INSERT YOUR LISTENERS HERE!!!! -->
   <servlet>
      <servlet-name>Resteasy</servlet-name>
      <servlet-class>
         org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher
      </servlet-class>
   </servlet>
   <servlet-mapping>
      <servlet-name>Resteasy</servlet-name>
      <url-pattern>/resteasy/*</url-pattern>
   </servlet-mapping>
</web-app>
```

使用 ServletFilter 来配置

```xml
<web-app>
    <filter>
        <filter-name>Resteasy</filter-name>
        <filter-class>
            org.jboss.resteasy.plugins.server.servlet.FilterDispatcher
        </filter-class>
        <init-param>
            <param-name>javax.ws.rs.Application</param-name>
            <param-value>com.restfully.shop.services.ShoppingApplication</param-value>
        </init-param>
    </filter>
    <filter-mapping>
        <filter-name>Resteasy</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
</web-app>
```

与 Spring 集成

```xml
<web-app>
   <display-name>Archetype Created Web Application</display-name>
   <listener>
      <listener-class>org.jboss.resteasy.plugins.server.servlet.ResteasyBootstrap</listener-class>
   </listener>
   <listener>
      <listener-class>org.jboss.resteasy.plugins.spring.SpringContextLoaderListener</listener-class>
   </listener>
   <servlet>
      <servlet-name>Resteasy</servlet-name>
      <servlet-class>org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher</servlet-class>
   </servlet>
   <servlet-mapping>
      <servlet-name>Resteasy</servlet-name>
      <url-pattern>/*</url-pattern>
   </servlet-mapping>
</web-app>
```

## 使用 @Path,@Get,@Post 等标注

```java
@Path("/library")
public class Library {
   @GET
   @Path("/books")
   public String getBooks() {...}
   @GET
   @Path("/book/{isbn}")
   public String getBook(@PathParam("isbn") String id) {
      // search my database and get a string representation and return it
   }
   @PUT
   @Path("/book/{isbn}")
   public void addBook(@PathParam("isbn") String id, @QueryParam("name") String name) {...}
   @DELETE
   @Path("/book/{id}")
   public void removeBook(@PathParam("id") String id {...}
}
```

以下操作都是针对 library 这个资源的

1. GET http://myhost.com/services/library/books 意思为获得所有的 books 调用的方法为 getBooks
2. GET http://myhost.com/services/library/book/333 意思为获得 ID 为 333 的 book 调用的方法为 getBook
3. PUT http://myhost.com/services/library/book/333 新增一个 ID 为 333 的 book 调用的方法为 addBook
4. DELETE http://myhost.com/services/library/book/333 删除一个 ID 为 333 的 book 调用的方法为 removeBook

**@Path **
这个标注可以在类上也可以在方法上, 如果**类和方法上都有的话, 那么方法上的路径是级联的**如上面例子的 / library/book/
@Path 和使用正则表达式匹配路径
@Path 不仅仅接收简单的路径表达式, 也可以使用正则表达式:

```java
@Path("/resources)
public class MyResource {
   @GET
   @Path("{var:.*}/stuff")
   public String get() {...}
}
```

如下操作就能获得该资源:
GET /resources/stuff
GET /resources/foo/stuff
GET /resources/on/and/on/stuff

表达式的格式为:

`"{" variable-name [ ":" regular-expression] "}"`

正则表达式部分是可选的, 当未提供时, 则会匹配一个默认的表达式 "(`[]*`)"

@Path("/resources/{var}/stuff")

会匹配如下路径:
GET /resources/foo/stuff
GET /resources/bar/stuff

下面的则不会匹配
GET /resources/a/bunch/of/stuff

**@QueryParam**
@QueryParam 这个标注是给通过? 的方式传参获得参数值的, 如:

`GET /books?num=5&index=1`

```java
@GET
   public String getBooks(@QueryParam("num") int num,@QueryParam("index") int index) {
   ...
   }
```

这里同上面的 @PathParam, 参数类型可以是任意类型

**@HeaderParam**
这个标注时用来获得保存在 HttpRequest 头里面的参数信息的, 如:

```java
@PUT
public void put(@HeaderParam("Content-Type") MediaType contentType, ...)
```

这里同上面的 @PathParam, 参数类型可以是任意类型

**@CookieParam**
用来获取保存在 Cookie 里面的参数, 如:

```java
@GET
public String getBooks(@CookieParam("sessionid") int id) {
   ...
}
```

**@FormParam**
用来获取 Form 中的参数值, 如:
页面代码:

```html
<form method="POST" action="/resources/service">
  First name:
  <input type="text" name="firstname" />
  <br />
  Middle name:
  <input type="text" name="middlename" />
  Last name:
  <input type="text" name="lastname" />
</form>
```

后台代码

```java
@Path("/")
public class NameRegistry {
   @Path("/resources/service")
   @POST
   public void addName(@FormParam("firstname") String first, @FormParam("lastname") String last) {...}
}
```

标注了 @FormParam, 会把表达里面的值自动映射到方法的参数上去.
如果要取得 Form 里面的所有属性, 可以通过在方法上增加一个 MultivaluedMap<String, String> form 这样的对象来获得, 如下:

```java
@Path("/resources/service")
   @POST
   public void addName(@FormParam("firstname") String first, @FormParam("lastname") String last,MultivaluedMap<String, String> form) {...}
```

**@Form**
上面已经说的几种标注都是一个属性对应一个参数的, 那么如果属性多了, 定义的方法就会变得不好阅读, 此时最好有个东西能够把上面的几种自动标注自动封装成一个对象,@Form 这个标注就是用来实现这个功能的, 如:

```java
public class MyForm {
   @FormParam("stuff")
   private int stuff;
   @HeaderParam("myHeader")
   private String header;
   @PathParam("foo")
   public void setFoo(String foo) {...}
}
```

**@POST**

```java
@Path("/myservice")
public void post(@Form MyForm form) {...}
```

**@DefaultValue**
在以上标注使用的时候, 有些参数值在没有值的情况下如果需要有默认值, 则使用这个标注, 如:

```java
@GET
public String getBooks(@QueryParam("num") @DefaultValue("10") int num) {...}
```

## 满足 JAX-RS 规范的 Resource Locators 和子资源

资源处理类定义的某个方法可以处理某个请求的一部分, 剩余部分由子资源处理类来处理, 如:

```java
@Path("/")
public class ShoppingStore {
   @Path("/customers/{id}")
   public Customer getCustomer(@PathParam("id") int id) {
      Customer cust = ...; // Find a customer object
      return cust;
   }
}
public class Customer {
    @GET
    public String get() {...}
    @Path("/address")
    public String getAddress() {...}
}
```

当我们发起 GET /customer/123 这样的请求的时候, 程序会先调用 ShoppingStore 的 getCustomer 这个方法, 然后接着调用 Customer 里面的 get 方法

当我们发起 GET /customer/123/address 这样的请求的时候, 程序会先调用 ShoppingStore 的 getCustomer 这个方法, 然后接着调用 Customer 里面的 getAddress 方法

## JAX-RS Content Negotiation

**@Consumes**
我们从页面提交数据到后台的时候, 数据的类型可以是 text 的, xml 的, json 的, 但是我们在请求资源的时候想要请求到同一个资源路径上面去, 此时怎么来区分处理呢? 使用 @Consumes 标注, 下面的例子将说明:

```java
 @Consumes("text/*")
@Path("/library")
public class Library {
         @POST
         public String stringBook(String book) {...}
         @Consumes("text/xml")
         @POST
         public String jaxbBook(Book book) {...}
}
```

当客户端发起请求的时候, 系统会先找到所有匹配路径的方法, 然后根据 content-type 找到具体的处理方法, 比如:

```
POST /library
content-type: text/plain
```

就会执行上面的 **stringBook** 这个方法, 因为这个方法上面没有标注 @ Consumes, 程序找了所有的方法没有找到标注 @ Consumes(“text/plain”) 这个类型的, 所以就执行这个方法了. 如果请求的 content-type=xml, 比如:

```
POST /library
content-type: text/xml
```

此时就会执行 jaxbBook 这个方法

**@Produces**
当服务器端实行完成相关的逻辑需要返回对象的时候, 程序会根据 @Produces 返回相应的对象类型

```java
@Produces("text/*")
@Path("/library")
public class Library {
         @GET
         @Produces("application/json")
         public String getJSON() {...}
         @GET
         public String get() {...}
}
```

如果客户端发起如下请求

```
GET /library
```

那么则会调用到 get 方法并且返回的格式是 json 类型的
这些标注能不能写多个呢? 答案是可以的, 但是系统只认第一个
