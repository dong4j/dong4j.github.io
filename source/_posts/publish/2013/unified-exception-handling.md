---
title: 5分钟掌握：RESTful API的异常处理艺术
keywords:
  - SpringMVC
  - 异常处理
  - HandlerExceptionResolver
  - ExceptionHandler
  - RESTEasy
  - ExceptionMapper
categories:
  - 新时代码农
tags:
  - SpringMVC
  - 异常处理
  - HandlerExceptionResolver
  - ExceptionHandler
  - RESTEasy
  - ExceptionMapper
abbrlink: 954087b4
date: 2013-06-22 00:00:00
ai:
  - 本文探讨了在Spring MVC和RESTEasy框架中的异常处理方法。Spring MVC提供了SimpleMappingExceptionResolver、HandlerExceptionResolver以及@ExceptionHandler注解来实现异常处理。RESTEasy则通过ExceptionMapper接口来进行通用异常处理。文章详细介绍了这些方法的实现方式，并给出了示例代码。
description: 本文探讨了在Spring MVC和RESTEasy框架中的异常处理方法。Spring MVC提供了SimpleMappingExceptionResolver、HandlerExceptionResolver以及@ExceptionHandler注解来实现异常处理。RESTEasy则通过ExceptionMapper接口来进行通用异常处理。文章详细介绍了这些方法的实现方式，并给出了示例代码。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover)

## SpringMVC

### SimpleMappingExceptionResolver

在 Spring 的配置文件 applicationContext.xml 中增加以下内容：

```xml
<bean class="org.springframework.web.servlet.handler.SimpleMappingExceptionResolver">
    <!-- 定义默认的异常处理页面，当该异常类型的注册时使用 -->
    <property name="defaultErrorView" value="error"></property>
    <!-- 定义异常处理页面用来获取异常信息的变量名，默认名为 exception -->
    <property name="exceptionAttribute" value="ex"></property>
    <!-- 定义需要特殊处理的异常，用类名或完全路径名作为 key，异常也页名作为值 -->
    <property name="exceptionMappings">
        <props>
            <prop key="cn.basttg.core.exception.BusinessException">error-business</prop>
            <prop key="cn.basttg.core.exception.ParameterException">error-parameter</prop>

            <!-- 这里还可以继续扩展对不同异常类型的处理 -->
        </props>
    </property>
</bean>
```

使用 SimpleMappingExceptionResolver 进行异常处理，具有集成简单、有良好的扩展性、对已有代码没有入侵性等优点，但该方法仅能获取到异常信息，若在出现异常时，对需要获取除异常以外的数据的情况不适用。

### HandlerExceptionResolver

1. 增加 HandlerExceptionResolver 接口的实现类 MyExceptionHandler，代码如下：

```java
public class MyExceptionHandler implements HandlerExceptionResolver {
    private static final Logger LOGGER = LoggerFactory.getLogger(MyExceptionHandler.class);
    public ModelAndView resolveException(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) {
        try(PrintWriter writer = new PrintWriter(response.getWriter(), true)){
            if (ex instanceof DataValidateException) {
                writer.println(ex.getMessage());
            } else if (ex instanceof RuntimeException){
                writer.println(ex.getMessage());
                LOGGER.error("Errors.OPTION_ERROR", ex);
            }
        } catch (IOException e) {
            LOGGER.error("getWriter error ", e);
        }
        return null;
    }
}

```

2. 在 Spring 的配置文件 applicationContext.xml 中增加以下内容：

```xml
<bean id="exceptionHandler" class="com.xxx.server.web.interceptor.MyExceptionHandler"/>
```

使用实现 HandlerExceptionResolver 接口的异常处理器进行异常处理，具有集成简单、有良好的扩展性、对已有代码没有入侵性等优点，同时，在异常处理时能获取导致出现异常的对象，有利于提供更详细的异常处理信息

### @ExceptionHandler

1. 增加 BaseController 类，并在类中使用 @ExceptionHandler 注解声明异常处理，代码如下：

```java
@ExceptionHandler
    public String exp(HttpServletRequest request, HttpServletResponse response, Exception ex) {
        try(PrintWriter writer = new PrintWriter(response.getWriter(), true)){
            if (ex instanceof DataValidateException) {
                writer.println(ex.getMessage());
            } else if (ex instanceof SSDBHelperException){
                writer.println(Errors.OPTION_ERROR);
            } else {
                // 未知异常都报服务器异常
                writer.println(RespCode.EX_SERVER_INNER.getMessage());
                LOGGER.error("Errors.OPTION_ERROR", ex);
            }
        } catch (IOException e) {
            LOGGER.error("getWriter error ", e);
        }
        return null;
    }
```

2. 修改代码，使所有需要异常处理的 Controller 都继承该类，如下所示，修改后的 TestController 类继承于 BaseController

使用 @ExceptionHandler 注解实现异常处理，具有集成简单、有扩展性好（只需要将要异常处理的 Controller 类继承于 BaseController 即可）、不需要附加 Spring 配置等优点，但该方法对已有代码存在入侵性（需要修改已有代码，使相关类继承于 BaseController），在异常处理时不能获取除异常以外的数据

### @ControllerAdvice

全局异常处理类

```java
@ControllerAdvice
public class GlobalExceptionHandler {
 private Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

 @ResponseBody  # 返回 json 数据
 @ExceptionHandler(Exception.class)
 public Object handleException(Exception e) {
     logger.error(ExceptionUtils.getFullStackTrace(e));  // 记录错误信息
     String msg = e.getMessage();
     if (msg == null || msg.equals("")) {
         msg = "服务器出错";
     }
     JSONObject jsonObject = new JSONObject();
     jsonObject.put("message", msg);
     return jsonObject;
 }
}
```

@ExceptionHandler 表示该方法可以处理的异常，可以多个，比如  
@ExceptionHandler({ NullPointerException.class, DataAccessException.class})  
也可以针对不同的异常写不同的方法。@ExceptionHandler(Exception.class) 可以处理所有的异常类型。

#### @ControllerAdvice 和 @PropertySource

##### @ControllerAdvice

@ ControllerAdvice 是一个 @ Component，用于定义 @ ExceptionHandler 的，@InitBinder 和 @ModelAttribute 方法，适用于所有使用 @ RequestMapping 方法。 Spring4 之前，@ ControllerAdvice 在同一调度的 Servlet 中协助所有控制器。Spring4 已经改变：@ ControllerAdvice 支持配置控制器的子集，而默认的行为仍然可以利用。

在 Spring4 中， @ControllerAdvice 通过 annotations(), basePackageClasses(), basePackages() 方法定制用于选择控制器子集：

```java
@ControllerAdvice(annotations = RestController.class)
class ApiExceptionHandlerAdvice {

    /**
     * Handle exceptions thrown by handlers.
     */
    @ExceptionHandler(value = Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    @ResponseBody
    public ApiError exception(Exception exception, WebRequest request) {
        return new ApiError(Throwables.getRootCause(exception).getMessage());
    }
}
```

##### @PropertySource

Spring 4 是和 @Configuration 协同，提供一个增加 name/value 属性的配置方式。

```java
@Configuration
@**PropertySource**("classpath:/datasource.properties")
public class DefaultDataSourceConfig implements DataSourceConfig {

    @Autowired
    private Environment env;

    @Override
    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName(env.getRequiredProperty("dataSource.driverClassName"));
        dataSource.setUrl(env.getRequiredProperty("dataSource.url"));
        dataSource.setUsername(env.getRequiredProperty("dataSource.username"));
        dataSource.setPassword(env.getRequiredProperty("dataSource.password"));
        return dataSource;
    }
}
```

## RESTEasy

RESTEasy 是 JBoss 提供的一个 Restful 基础框架，使用它我们可以很方便的构建我们的 Restful 服务，而且它也完全符合  [Java](http://lib.csdn.net/base/java "Java 知识库")  的 JAX-RS2.0 标准，很多第三方 Restful 框架也都是基于 RESTEasy 开发的。

在任何框架中都不可避免的涉及到异常处理，Restful 框架也是如此。按照我们一般传统异常处理方式，在 Restful 的最外层，我们一般会对所有的业务调用都加上 try catch，以免异常被用户接收到，比如我们有这么一个 Restful 服务：

```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.Response;
import org.jboss.resteasy.spi.validation.ValidateRequest;

@Path("/rest")
public class UserApi
{
    @Autowire
    UserService userService;
    @Path("/users/{id}")
    @GET
    @ValidateRequest
    public Response getUserBId  ( @PathParam("id") String id ) throws RuntimeException
    {
        try{
            User user=userService.getUser(id);
        } catch(IllegalArgumentException e) {
            //if exception occured
            return Response.status(Status.BAD_REQUEST).entity(exception.getMessage()).build();
        } catch(Exception e) {
            //if exception occured
            return Response.status(Status.BAD_REQUEST).entity(exception.getMessage()).build();
        }
        //if success
        return Response.ok().entity("User with ID " + id + " found !!").build();
    }
}
```

上面 UserApi 接口中的 getUserBId() 方法调用了 userService.getUser() 服务，这个服务会抛出一些异常，UserApi 需要捕获异常并返回客户的一个错误的响应。还有一点我们一般会在 API 层 catch 一个 Exception 异常，也就是捕获所有可能发生的异常情况，以免前端出现不友好的错误提示。

这么做也没什么问题，但是我们的接口不只是一个，每个接口需要进行 try catch 来处理异常，这么做显然不符合我们的编程思想，我们希望把所有异常集中到一个地方处理。

如果我们的 Restful 框架是基于 RESTEasy 的，那么我们就可以使用 ExceptionMapper 来实现一个通用异常处理类。

### ExceptionMapper

ExceptionMapper 是 provider 的一个协议，它会将 Java 的异常映射到 Response 对象。所以要进行通用异常处理，我们只需要写一个类来实现 ExceptionMapper 接口，并把它声明为一个 provider 即可：

```java
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Provider
public class MyApplicationExceptionHandler implements ExceptionMapper<MyApplicationException>
{
    @Override
    public Response toResponse(Exception exception)
    {
        return Response.status(Status.BAD_REQUEST).entity(exception.getMessage()).build();
    }
}
```

上面的 ExceptionMapper 的实现已经写好了，下面我们写个 Restful API 来 [测试](http://lib.csdn.net/base/softwaretest "软件测试知识库") 下：

```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.Response;
import org.jboss.resteasy.spi.validation.ValidateRequest;

@Path("/rest")
public class UserApi
{
    @Autowire
    UserService userService;
    @Path("/users/{id}")
    @GET
    @ValidateRequest
    public Response getUserBId  ( @PathParam("id") String id ) throws RuntimeException
    {
        try{
            User user=userService.getUser(id);
        } catch(IllegalArgumentException e) {
           throw new RuntimeException("id is not a number !!");
        }
        return Response.ok().entity("User with ID " + id + " found !!").build();
    }
}
```

在这个接口中，我们并没有对异常做特殊处理，也没有 catch 一个 Exception 异常，仅仅是把异常抛出，而所有的异常处理都集中在了 MyApplicationExceptionHandler 中。
