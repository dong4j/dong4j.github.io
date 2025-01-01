---
title: 基于 Spring 的 Token 鉴权系统搭建教程
keywords:
  - REST
  - Token
  - 身份鉴权
  - 移动端
  - Spring
  - 安全
categories:
  - 新时代码农
tags:
  - REST
  - Token
  - 身份鉴权
  - 移动端
  - Spring
  - 安全
abbrlink: '18363420'
date: 2014-05-17 00:00:00
ai:
  - REST是一种软件架构风格，通过URL对资源进行操作，而Token用于移动端登录身份鉴权，与Session相比更安全且符合无状态设计。文章介绍了Token的交互流程、程序示例和Spring框架下的实现方式，包括TokenModel类、RedisTokenManager接口及其在Controller中的应用。还讨论了登录请求的安全性问题以及Token生成方式的多样性。
description: REST是一种软件架构风格，通过URL对资源进行操作，而Token用于移动端登录身份鉴权，与Session相比更安全且符合无状态设计。文章介绍了Token的交互流程、程序示例和Spring框架下的实现方式，包括TokenModel类、RedisTokenManager接口及其在Controller中的应用。还讨论了登录请求的安全性问题以及Token生成方式的多样性。
---

### 什么是 REST

REST (Representational State Transfer) 是一种软件架构风格。它将服务端的信息和功能等所有事物统称为资源，客户端的请求实际就是对资源进行操作，它的主要特点有： - 每一个资源都会对应一个独一无二的 url - 客户端通过 HTTP 的 GET、POST、PUT、DELETE 请求方法对资源进行查询、创建、修改、删除操作 - 客户端与服务端的交互必须是无状态的

### 使用 Token 进行身份鉴权

网站应用一般使用 Session 进行登录用户信息的存储及验证，而在移动端使用 Token 则更加普遍。它们之间并没有太大区别，Token 比较像是一个更加精简的自定义的 Session。Session 的主要功能是保持会话信息，而 Token 则只用于登录用户的身份鉴权。所以在移动端使用 Token 会比使用 Session 更加简易并且有更高的安全性，同时也更加符合 RESTful 中无状态的定义。

### 交互流程

1. 客户端通过登录请求提交用户名和密码，服务端验证通过后生成一个 Token 与该用户进行关联，并将 Token 返回给客户端。
2. 客户端在接下来的请求中都会携带 Token，服务端通过解析 Token 检查登录状态。
3. 当用户退出登录、其他终端登录同一账号（被顶号）、长时间未进行操作时 Token 会失效，这时用户需要重新登录。

### 程序示例

服务端生成的 Token 一般为随机的非重复字符串，根据应用对安全性的不同要求，会将其添加时间戳（通过时间判断 Token 是否被盗用）或 url 签名（通过请求地址判断 Token 是否被盗用）后加密进行传输。在本文中为了演示方便，仅是将 User Id 与 Token 以 `_` 进行拼接。

```java
/**
 * Token 的 Model 类，可以增加字段提高安全性，例如时间戳、url 签名
 */
public class TokenModel {

    // 用户 id
    private long userId;

    // 随机生成的 uuid
    private String token;

    public TokenModel (long userId, String token) {
        this.userId = userId;
        this.token = token;
    }

    public long getUserId () {
        return userId;
    }

    public void setUserId (long userId) {
        this.userId = userId;
    }

    public String getToken () {
        return token;
    }

    public void setToken (String token) {
        this.token = token;
    }
}
```

Redis 是一个 Key-Value 结构的内存数据库，用它维护 User Id 和 Token 的映射表会比传统数据库速度更快，这里使用 Spring-Data-Redis 封装的 TokenManager 对 Token 进行基础操作：

```java
/**
 * 对 token 进行操作的接口
 */
public interface TokenManager {

    /**
     * 创建一个 token 关联上指定用户
     * @param userId 指定用户的 id
     * @return 生成的 token
     */
    public TokenModel createToken (long userId);

    /**
     * 检查 token 是否有效
     * @param model token
     * @return 是否有效
     */
    public boolean checkToken (TokenModel model);

    /**
     * 从字符串中解析 token
     * @param authentication 加密后的字符串
     * @return
     */
    public TokenModel getToken (String authentication);

    /**
     * 清除 token
     * @param userId 登录用户的 id
     */
    public void deleteToken (long userId);

}

/**
 * 通过 Redis 存储和验证 token 的实现类
 */
@Component
public class RedisTokenManager implements TokenManager {

    private RedisTemplate redis;

    @Autowired
    public void setRedis (RedisTemplate redis) {
        this.redis = redis;
        // 泛型设置成 Long 后必须更改对应的序列化方案
        redis.setKeySerializer (new JdkSerializationRedisSerializer ());
    }

    public TokenModel createToken (long userId) {
        // 使用 uuid 作为源 token
        String token = UUID.randomUUID ().toString ().replace ("-", "");
        TokenModel model = new TokenModel (userId, token);
        // 存储到 redis 并设置过期时间
        redis.boundValueOps (userId).set (token, Constants.TOKEN_EXPIRES_HOUR, TimeUnit.HOURS);
        return model;
    }

    public TokenModel getToken (String authentication) {
        if (authentication == null || authentication.length () == 0) {
            return null;
        }
        String [] param = authentication.split ("_");
        if (param.length != 2) {
            return null;
        }
        // 使用 userId 和源 token 简单拼接成的 token，可以增加加密措施
        long userId = Long.parseLong (param [0]);
        String token = param [1];
        return new TokenModel (userId, token);
    }

    public boolean checkToken (TokenModel model) {
        if (model == null) {
            return false;
        }
        String token = redis.boundValueOps (model.getUserId ()).get ();
        if (token == null || !token.equals (model.getToken ())) {
            return false;
        }
        // 如果验证成功，说明此用户进行了一次有效操作，延长 token 的过期时间
        redis.boundValueOps (model.getUserId ()).expire (Constants.TOKEN_EXPIRES_HOUR, TimeUnit.HOURS);
        return true;
    }

    public void deleteToken (long userId) {
        redis.delete (userId);
    }
}
```

RESTful 中所有请求的本质都是对资源进行 CRUD 操作，所以登录和退出登录也可以抽象为对一个 Token 资源的创建和删除，根据该想法创建 Controller：

```java
/**
 * 获取和删除 token 的请求地址，在 Restful 设计中其实就对应着登录和退出登录的资源映射
 */
@RestController
@RequestMapping ("/tokens")
public class TokenController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private TokenManager tokenManager;

    @RequestMapping (method = RequestMethod.POST)
    public ResponseEntity login (@RequestParam String username, @RequestParam String password) {
        Assert.notNull (username, "username can not be empty");
        Assert.notNull (password, "password can not be empty");

        User user = userRepository.findByUsername (username);
        if (user == null || // 未注册
                !user.getPassword ().equals (password)) { // 密码错误
            // 提示用户名或密码错误
            return new ResponseEntity (ResultModel.error (ResultStatus.USERNAME_OR_PASSWORD_ERROR), HttpStatus.NOT_FOUND);
        }
        // 生成一个 token，保存用户登录状态
        TokenModel model = tokenManager.createToken (user.getId ());
        return new ResponseEntity (ResultModel.ok (model), HttpStatus.OK);
    }

    @RequestMapping (method = RequestMethod.DELETE)
    @Authorization
    public ResponseEntity logout (@CurrentUser User user) {
        tokenManager.deleteToken (user.getId ());
        return new ResponseEntity (ResultModel.ok (), HttpStatus.OK);
    }

}
```

这个 Controller 中有两个自定义的注解分别是`@Authorization`和`@CurrentUser`，其中`@Authorization`用于表示该操作需要登录后才能进行：

```java
/**  * 在 Controller 的方法上使用此注解，该方法在映射时会检查用户是否登录，未登录返回 401 错误  * @author ScienJus  * @date 2015/7/31.  */ @Target (ElementType.METHOD) @Retention (RetentionPolicy.RUNTIME) public @interface Authorization { }/**
 * 在 Controller 的方法上使用此注解，该方法在映射时会检查用户是否登录，未登录返回 401 错误
 */
@Target (ElementType.METHOD)
@Retention (RetentionPolicy.RUNTIME)
public @interface Authorization {
}
```

这里使用 Spring 的拦截器完成这个功能，该拦截器会检查每一个请求映射的方法是否有`@Authorization`注解，并使用 TokenManager 验证 Token，如果验证失败直接返回 401 状态码（未授权）：

```java
/**
 * 自定义拦截器，判断此次请求是否有权限
 */
@Component
public class AuthorizationInterceptor extends HandlerInterceptorAdapter {

    @Autowired
    private TokenManager manager;

    public boolean preHandle (HttpServletRequest request,
                             HttpServletResponse response, Object handler) throws Exception {
        // 如果不是映射到方法直接通过
        if (!(handler instanceof HandlerMethod)) {
            return true;
        }
        HandlerMethod handlerMethod = (HandlerMethod) handler;
        Method method = handlerMethod.getMethod ();
        // 从 header 中得到 token
        String authorization = request.getHeader (Constants.AUTHORIZATION);
        // 验证 token
        TokenModel model = manager.getToken (authorization);
        if (manager.checkToken (model)) {
            // 如果 token 验证成功，将 token 对应的用户 id 存在 request 中，便于之后注入
            request.setAttribute (Constants.CURRENT_USER_ID, model.getUserId ());
            return true;
        }
        // 如果验证 token 失败，并且方法注明了 Authorization，返回 401 错误
        if (method.getAnnotation (Authorization.class) != null) {
            response.setStatus (HttpServletResponse.SC_UNAUTHORIZED);
            return false;
        }
        return true;
    }
}
```

`@CurrentUser`注解定义在方法的参数中，表示该参数是登录用户对象。这里同样使用了 Spring 的解析器完成参数注入：

```java
/**
 * 在 Controller 的方法参数中使用此注解，该方法在映射时会注入当前登录的 User 对象
 */
@Target (ElementType.PARAMETER)
@Retention (RetentionPolicy.RUNTIME)
public @interface CurrentUser {
}

/**
 * 增加方法注入，将含有 CurrentUser 注解的方法参数注入当前登录用户
 */
@Component
public class CurrentUserMethodArgumentResolver implements HandlerMethodArgumentResolver {

    @Autowired
    private UserRepository userRepository;

    @Override
    public boolean supportsParameter (MethodParameter parameter) {
        // 如果参数类型是 User 并且有 CurrentUser 注解则支持
        if (parameter.getParameterType ().isAssignableFrom (User.class) &&
                parameter.hasParameterAnnotation (CurrentUser.class)) {
            return true;
        }
        return false;
    }

    @Override
    public Object resolveArgument (MethodParameter parameter, ModelAndViewContainer mavContainer, NativeWebRequest webRequest, WebDataBinderFactory binderFactory) throws Exception {
        // 取出鉴权时存入的登录用户 Id
        Long currentUserId = (Long) webRequest.getAttribute (Constants.CURRENT_USER_ID, RequestAttributes.SCOPE_REQUEST);
        if (currentUserId != null) {
            // 从数据库中查询并返回
            return userRepository.findOne (currentUserId);
        }
        throw new MissingServletRequestPartException (Constants.CURRENT_USER_ID);
    }
}
```

### 一些细节

- 登录请求一定要使用 HTTPS，否则无论 Token 做的安全性多好密码泄露了也是白搭
- Token 的生成方式有很多种，例如比较热门的有 JWT（JSON Web Tokens）、OAuth 等。
