---
title: macOS 上使用 IDEA 搭建 SSM 项目
keywords:
  - Spring
  - Spring MVC
  - Hibernate
  - Java
  - Web开发
  - 数据库操作
  - 项目搭建
  - IntelliJ IDEA
  - Tomcat
categories:
  - 新时代码农
tags:
  - Spring
  - Spring MVC
  - Hibernate
  - Java
  - Web开发
  - 数据库操作
  - 项目搭建
  - IntelliJ IDEA
  - Tomcat
abbrlink: 23cbb67c
date: 2015-12-16 00:00:00
ai:
  - 本文详细介绍了使用Spring+Spring MVC+Hibernate等技术栈搭建项目的过程。首先讲解了在IntelliJ IDEA中新建项目的步骤，包括创建项目视图、配置文件和结构等。然后介绍了项目中各层包的功能，如controller、dao、domain、dto、qo、rowmapper、schedulejob和服务等。接着，文章重点讲解了Dao层代码中对适配器设计模式的应用，以及HibernateTemplateDao类的实现细节。最后，文章还介绍了如何配置Tomcat服务器并部署项目。
description: 本文详细介绍了使用Spring+Spring MVC+Hibernate等技术栈搭建项目的过程。首先讲解了在IntelliJ IDEA中新建项目的步骤，包括创建项目视图、配置文件和结构等。然后介绍了项目中各层包的功能，如controller、dao、domain、dto、qo、rowmapper、schedulejob和服务等。接着，文章重点讲解了Dao层代码中对适配器设计模式的应用，以及HibernateTemplateDao类的实现细节。最后，文章还介绍了如何配置Tomcat服务器并部署项目。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover)

项目搭建采用技术栈为：Spring+Spring MVC+Hibernate+Jsp+Gradle ＋ tomcat+mysql5.6

搭建环境文档目录结构说明：

1. 使用 Intellj Idea 搭建项目过程详解
2. 项目各配置文件讲解及部署
3. 各层包功能讲解 & 项目搭建完毕最终效果演示图
4. 项目中重要代码讲解
5. 配置 tomcat 运行环境
6. webapp 文件夹下分层详解

### **1. 使用 Intellj Idea 搭建项目过程详解**

**1.1 打开 Intellj Idea**

![20241229154732_UmUYAM5B.webp](https://cdn.dong4j.site/source/image/20241229154732_UmUYAM5B.webp)

**1.2 操作 Intellj Idea 工具栏 新建项目**

![20241229154732_dQUO0QRI.webp](https://cdn.dong4j.site/source/image/20241229154732_dQUO0QRI.webp)

![20241229154732_4hecK3or.webp](https://cdn.dong4j.site/source/image/20241229154732_4hecK3or.webp)

![20241229154732_OQM0gIFM.webp](https://cdn.dong4j.site/source/image/20241229154732_OQM0gIFM.webp)

![20241229154732_pjRYBW6i.webp](https://cdn.dong4j.site/source/image/20241229154732_pjRYBW6i.webp)

![20241229154732_HiyaFYc8.webp](https://cdn.dong4j.site/source/image/20241229154732_HiyaFYc8.webp)

![20241229154732_XTyTDehX.webp](https://cdn.dong4j.site/source/image/20241229154732_XTyTDehX.webp)

![20241229154732_uWlJZ4Oz.webp](https://cdn.dong4j.site/source/image/20241229154732_uWlJZ4Oz.webp)

需要说明的是，最初创建的项目视图是不完整的，包括 webapp 文件夹下没有 web.xml，以及 src 包下缺少 Java 文件夹 (放置 java 源代码文件)，Resources 文件夹（放置项目配置文件）。

我们继续做以下操作，使得项目的结构符合 web 应用项目的层级标准。

![20241229154732_w031AEdD.webp](https://cdn.dong4j.site/source/image/20241229154732_w031AEdD.webp)

出现如下视图：

![20241229154732_xQkY98hW.webp](https://cdn.dong4j.site/source/image/20241229154732_xQkY98hW.webp)

![20241229154732_jXXkzc48.webp](https://cdn.dong4j.site/source/image/20241229154732_jXXkzc48.webp)

接下来：单击 main 文件夹按照如下操作：

![20241229154732_FpSXWcZK.webp](https://cdn.dong4j.site/source/image/20241229154732_FpSXWcZK.webp)

屏幕快照 2016-11-20 下午 4.44.33.png

![20241229154732_cSVKsRzs.webp](https://cdn.dong4j.site/source/image/20241229154732_cSVKsRzs.webp)

点击 ok，再按照上图操作操作一遍，输入文件名为 **resources**

最终的结构图如下图所示：

![20241229154732_kSY0ppsp.webp](https://cdn.dong4j.site/source/image/20241229154732_kSY0ppsp.webp)

### **2. 项目各配置文件讲解及部署**

完成了项目的初始化结构创建，接下来我们需要来创建配置文件。

首先是 resources 文件夹下的配置文件

**2.1resources 下资源文件截图:(最终配置的结果)**

![20241229154732_ETRD79L5.webp](https://cdn.dong4j.site/source/image/20241229154732_ETRD79L5.webp)

**2.2 data-access-applicationContext.xml**

主要管理数据库访问组件

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context.xsd
       ">

    <!-- 配置自动扫描的包 -->
    <context:component-scan base-package="com.fxmms" use-default-filters="false">
        <context:include-filter type="regex" expression="com.fxmms.*.*.dao.*"/>
        <context:include-filter type="regex" expression="com.fxmms.*.dao.*"/>
    </context:component-scan>

    <!-- 配置数据源 -->
    <context:property-placeholder location="classpath:db.properties"/>
    <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
        <property name="driverClassName" value="${jdbc.driverClass}"/>
        <property name="url" value="${jdbc.jdbcUrl}"/>
        <property name="username" value="${jdbc.user}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>

    <!--配置hibernate SessionFactory-->
    <bean id="sessionFactory"
          class="org.springframework.orm.hibernate4.LocalSessionFactoryBean">
        <property name="dataSource" ref="dataSource"></property>
        <property name="hibernateProperties">
            <props>
                <prop key="hibernate.dialect">${dataSource.hibernate.dialect}</prop>
                <prop key="hibernate.show_sql">${dataSource.hibernate.show_sql}</prop>
                <prop key="hibernate.format_sql">true</prop>
                <!--负责自动创建数据表，基本上不能打开注释，否则所有的数据库中表信息都会被删除，重新创建-->
                <!-- <prop key="hibernate.hbm2ddl.auto">create</prop> -->
            </props>
        </property>
        <!-- <property name="hibernate.jdbc.batch_size" value="50"></property> -->
        <property name="packagesToScan">
            <list>
                <value>com.fxmms.*.*.domain</value>
                <value>com.fxmms.*.domain</value>
            </list>
        </property>
    </bean>

    <!--jdbcTemplate start -->
    <bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
        <property name="dataSource" ref="dataSource"></property>
    </bean>
    <!--Spring JDBC 中操作 LOB 数据 -->
    <bean id="lobHandler" class="org.springframework.jdbc.support.lob.DefaultLobHandler"
          lazy-init="true"></bean>
    <!-- 配置JPA部分 -->
    <!-- 配置JPA的EntityManagerFactory -->
    <!-- <bean id="entityManagerFactory"
           class="org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean">
         <property name="dataSource" ref="dataSource"></property>
         <property name="jpaVendorAdapter">
             <bean class="org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter"></bean>
         </property>
         <property name="packagesToScan" value="com.fxmms"></property>
         <property name="jpaProperties">
             <props>
                 <prop key="hibernate.ejb.naming_strategy">org.hibernate.cfg.ImprovedNamingStrategy</prop>
                 <prop key="hibernate.hbm2ddl.auto">update</prop>
                 <prop key="hibernate.show_sql">true</prop>
                 <prop key="hibernate.format_sql">true</prop>
                 <prop key="hibernate.dialect">org.hibernate.dialect.MySQL5InnoDBDialect</prop>

                 <prop key="hibernate.cache.use_second_level_cache">true</prop>
                 <prop key="hibernate.cache.region.factory_class">org.hibernate.cache.ehcache.EhCacheRegionFactory
                 </prop>
                 <prop key="hibernate.cache.use_query_cache">true</prop>
             </props>
         </property>
         <!–使用二級緩存–>
         <property name="sharedCacheMode" value="ENABLE_SELECTIVE"></property>
     </bean>

     <!– 配置事务 –>
     <bean id="transactionManager" class="org.springframework.orm.jpa.JpaTransactionManager">
         <property name="entityManagerFactory" ref="entityManagerFactory"></property>
     </bean>-->

    <!-- <!– 配置SpringData部分 –>
     <jpa:repositories base-package="com.fxmms"
                       entity-manager-factory-ref="entityManagerFactory">

     </jpa:repositories>-->
</beans>
```

**2.3 service-applicationContext.xml**

主要管理业务逻辑组件，包括对数据库访问的事务控制，以及定时任务。

```
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:task="http://www.springframework.org/schema/task"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
  http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
  http://www.springframework.org/schema/aop
  http://www.springframework.org/schema/aop/spring-aop.xsd
  http://www.springframework.org/schema/tx
  http://www.springframework.org/schema/tx/spring-tx.xsd
        http://www.springframework.org/schema/task
        http://www.springframework.org/schema/task/spring-task.xsd">

    <aop:aspectj-autoproxy/>

    <!--设置定时任务-->
    <task:annotation-driven/>
    <context:component-scan base-package="com.fxmms.www" use-default-filters="false">
        <context:include-filter type="annotation" expression="org.springframework.stereotype.Service"/>
    </context:component-scan>

    <!-- enable the configuration of transactional behavior based on annotations -->
    <tx:annotation-driven transaction-manager="txManager"/>

    <bean id="txManager" class="org.springframework.orm.hibernate4.HibernateTransactionManager">
        <property name="sessionFactory" ref="sessionFactory"/>
    </bean>

</beans>
```

**2.4default-servlet.xml**

设置 springmvc-applicationContext.xml, 前端控制器将请求转发到相应的 controller 层中的处理方法上。

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context
       http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/mvc
       http://www.springframework.org/schema/mvc/spring-mvc.xsd">
    <!---->
    <mvc:annotation-driven>
        <!--json解析-->
        <mvc:message-converters>
            <bean class="org.springframework.http.converter.StringHttpMessageConverter"/>
            <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"/>
        </mvc:message-converters>
    </mvc:annotation-driven>
    <context:component-scan base-package="com.fxmms.www.controller">
        <context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
    </context:component-scan>
    <!--因为web.xml中defaultDispatcherServlet对所有请求进行了拦截，所以对一些.css .jpg .html .jsp也进行了拦截，所以此配置项
    保证对对静态资源不拦截-->
    <mvc:default-servlet-handler/>
    <!--视图解析器-->
    <bean id="viewResolver"
          class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
    <!--配置文件上上传-->
    <bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
        <property name="defaultEncoding" value="utf-8"/>
        <property name="maxUploadSize" value="10485760000"/>
        <property name="maxInMemorySize" value="40960"/>
    </bean>
</beans>
```

**2.5 spring-security.xml**

设置 spring－security 权限控制配置文件，项目中权限的控制统一在此配置文件中配置，包括从数据库中获取用户的相关信息，以及配置相应 pattern 的请求过滤规则。

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:sec="http://www.springframework.org/schema/security"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-3.2.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/security
        http://www.springframework.org/schema/security/spring-security-3.2.xsd">
    <!--    <sec:http pattern="/**/*.jpg" security="none"></sec:http>
        <sec:http pattern="/**/*.jpeg" security="none"></sec:http>
        <sec:http pattern="/**/*.gif" security="none"></sec:http>
        <sec:http pattern="/**/*.png" security="none"></sec:http>s
        <sec:http pattern="/getCode" security="none" /><!– 不过滤验证码 –>
        <sec:http pattern="/test/**" security="none"></sec:http><!– 不过滤测试内容 –>-->
    <!--spring security 权限管理配置文件-->
    <context:component-scan base-package="com.fxmms.common.security">
    </context:component-scan>
    <context:property-placeholder location="classpath:db.properties"></context:property-placeholder>
    <!--权限控制-->
    <sec:http auto-config="true" use-expressions="true">
        <sec:intercept-url pattern="/superadmin/**" access="hasRole('superadmin')"/>
        <sec:intercept-url pattern="/admin/**" access="hasRole('admin')"/>
        <sec:intercept-url pattern="/customer/**" access="hasRole('customer')"/>
        <!--自定义登陆页面,权限验证失败页面，登录成功页面-->
        <sec:form-login login-page="/login.jsp" authentication-failure-url="/login.jsp" login-processing-url="/j_spring_security_check"
                        authentication-success-handler-ref="loginSuccessHandler"/>
        <!--用户权限不一致出现的权限不可得情况，默认情况下跳转到403页面-->
        <sec:access-denied-handler ref="accessDeniedServletHandler" />
        <sec:logout logout-success-url="/login.jsp" />
    </sec:http>

    <sec:authentication-manager>
        <sec:authentication-provider>
            <!--配置从数据库查询用户权限  and isDelete = 0 and enable = 1-->
            <sec:jdbc-user-service data-source-ref="dataSource"
                                   users-by-username-query="select userName,password,enable  from mms_admin where userName=? and isDelete = 0 and enable = 1"
                                   authorities-by-username-query="select userName,role from mms_admin where username=?"
            ></sec:jdbc-user-service>
        </sec:authentication-provider>
    </sec:authentication-manager>
</beans>
```

**2.6 db.properties**

数据库访问配置文件

```
jdbc.user=root
jdbc.password=feixun*123
jdbc.driverClass=com.mysql.jdbc.Driver
#jdbc.jdbcUrl=jdbc:mysql://localhost/fxmms?useUnicode=true&characterEncoding=UTF-8
jdbc.jdbcUrl=jdbc:mysql://222.73.156.132:13306/fxmms?useUnicode=true&characterEncoding=UTF-8

jdbc.initPoolSize=5
jdbc.maxPoolSize=20
dataSource.hibernate.dialect=org.hibernate.dialect.MySQL5Dialect
#######################
##      local        ##
#######################
dataSource.hibernate.show_sql=true
```

**2.7 log4j.properties**

配置项目日志文件，日志输出模式为 Console

```
###########################################################################
# Properties file for the log4j logger system
#
#  Note: During the uPortal build, the file at /properties/Logger.properties is copied
#  to the log4j standard location /WEB-INF/classes/log4j.properties .  This means that editing the file
#  at /properties/Logger.properties in a deployed uPortal will have no effect.
#
# Please read the instructions for the Log4J logging system at
# http://jakarta.apache.org/log4j/ if you want to modify this.

###########################################################################
# You should probably replace the word "debug" with "info" in the
# following line after everything is running.  This will turn off
# the tons of debug messages, and leave only INFO, WARN, ERROR, etc.
#
log4j.rootLogger=info, stdout

# Console output
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d{mm:ss,SSS} %p [%l] - <%m>%n
```

**2.8 web.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">
    <!--配置需要加载的spring配置文件，这些文件中的配置的类都是被<context:component-scan>扫描到的，比如@Repository @Component
    @Service @Controller等-->
    <context-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>classpath:data-access-applicationContext.xml;classpath:spring-security.xml;classpath:service-applicationContext.xml</param-value>
    </context-param>
    <!--配置日志监听 ，如果配置文件报红，没有关系可以正常运行，这个与idea的验证规则有关-->
    <context-param>
        <param-name>log4jConfigLocation</param-name>
        <param-value>classpath:log4j.properties</param-value>
    </context-param>
    <listener>
        <listener-class>org.springframework.web.util.Log4jConfigListener</listener-class>
    </listener>

    <listener>
        <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
    </listener>

   <!--配置权限过滤器，注意必须配置在springmvc 之前，因为对用户访问资源的权限判断与控制是在访问特定url之前发生的-->
    <filter>
        <filter-name>springSecurityFilterChain</filter-name>
        <filter-class>org.springframework.web.filter.DelegatingFilterProxy</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>springSecurityFilterChain</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>

    <!-- 配置字符编码过滤器  必须配置在所有过滤器的最前面 -->
    <filter>
        <filter-name>CharacterEncodingFilter</filter-name>
        <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
        <init-param>
            <param-name>encoding</param-name>
            <param-value>UTF-8</param-value>
        </init-param>
        <init-param>
            <param-name>forceEncoding</param-name>
            <param-value>true</param-value>
        </init-param>
    </filter>

    <filter-mapping>
        <filter-name>CharacterEncodingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    <!--超级管理员 -->
  <!-- <filter>
        <filter-name>superAdminFilter</filter-name>
        <filter-class>com.fxmms.filter.SuperAdminFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>superAdminFilter</filter-name>
        <url-pattern>/fxmms/superadmin/*</url-pattern>
    </filter-mapping>

    <filter>
        <filter-name>adminFilter</filter-name>
        <filter-class>com.fxmms.filter.AdminFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>adminFilter</filter-name>
        <url-pattern>/fxmms/admin/*</url-pattern>
    </filter-mapping>

    <filter>
        <filter-name>customerFilter</filter-name>
        <filter-class>com.fxmms.filter.CustomerFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>customerFilter</filter-name>
        <url-pattern>/fxmms/customer/*</url-pattern>
    </filter-mapping>

    <servlet>
        <servlet-name>LoginServlet</servlet-name>
        <servlet-class>com.fxmms.servlet.LoginServlet</servlet-class>
    </servlet>
    <servlet>
        <servlet-name>InvalidateServlet</servlet-name>
        <servlet-class>com.fxmms.servlet.InvalidateServlet</servlet-class>
    </servlet>-

    <servlet-mapping>
        <servlet-name>LoginServlet</servlet-name>
        <url-pattern>/loginServlet</url-pattern>
    </servlet-mapping>
    <servlet-mapping>
    <servlet-name>InvalidateServlet</servlet-name>
    <url-pattern>/invalidateServlet</url-pattern>
    </servlet-mapping>-->

    <!-- 配置看可以把POST请求转为PUT，DELETE请求的Filter -->
    <filter>
        <filter-name>HiddenHttpMethodFilter</filter-name>
        <filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>HiddenHttpMethodFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    <!--配置中央控制器，对所有请求进行拦截并做请求路径，与处理请求桩模块之间的映射-->
    <servlet>
        <servlet-name>defaultDispatcherServlet</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation
            </param-name>
            <param-value>classpath:default-servlet.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <!--这里是拦截所有-->
    <servlet-mapping>
        <servlet-name>defaultDispatcherServlet</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

**2.9 build.gradle**

项目构建脚本

```
group 'com.fxmms'
version '1.0-SNAPSHOT'

apply plugin: 'java'
apply plugin: 'idea'
apply plugin: 'war'
sourceCompatibility = 1.8

repositories {
    maven { url "http://maven.aliyun.com/nexus/content/groups/public/" }
    mavenLocal()
    jcenter()
    maven { url "http://repo.maven.apache.org/maven2/"}
    maven { url 'https://repo.spring.io/libs-milestone'}
    mavenCentral()
}

dependencies {
    testCompile group: 'junit', name: 'junit', version: '4.12'
    // servlet-api
    compile group: 'javax.servlet', name: 'servlet-api', version: '2.5'
    //spring相关
    compile group: 'org.springframework', name: 'spring-webmvc', version: '4.3.3.RELEASE'
    compile group: 'org.springframework', name: 'spring-orm', version: '4.3.3.RELEASE'
    compile group: 'org.springframework', name: 'spring-aspects', version: '4.3.3.RELEASE'
    compile group: 'org.springframework.security', name: 'spring-security-config', version: '3.2.0.RELEASE'
    compile group: 'org.springframework.security', name: 'spring-security-taglibs', version: '3.2.0.RELEASE'
    compile 'org.springframework.security:spring-security-web:3.2.0.RELEASE'
    //hibernate相关
    compile 'org.hibernate:hibernate-core:4.3.6.Final'
    //c3p0连接池
    compile group: 'org.hibernate', name: 'hibernate-c3p0', version: '4.3.6.Final'
    //ehcahe二级缓存
    compile group: 'org.hibernate', name: 'hibernate-ehcache', version: '4.3.6.Final'
    //mysql
    compile group: 'mysql', name: 'mysql-connector-java', version: '5.1.39'
    //springData
    compile group: 'org.springframework.data', name: 'spring-data-jpa', version: '1.10.3.RELEASE'
    // https://mvnrepository.com/artifact/log4j/log4j日志
    compile group: 'log4j', name: 'log4j', version: '1.2.17'
    //json解析相关
    compile group: 'com.fasterxml.jackson.core', name: 'jackson-databind', version: '2.5.4'
    compile group: 'com.fasterxml.jackson.core', name: 'jackson-core', version: '2.5.4'
    //迅雷接口有关jar 包
    compile 'org.apache.httpcomponents:httpclient:4.4'
    compile 'org.json:json:20141113'
    compile group: 'org.apache.clerezza.ext', name: 'org.json.simple', version: '0.4'
    //https://mvnrepository.com/artifact/org.apache.commons/commons-io 读取文件相关
    compile group: 'org.apache.commons', name: 'commons-io', version: '1.3.2'
    // https://mvnrepository.com/artifact/org.apache.poi/poi 文件读取相关 apache-poi
    compile group: 'org.apache.poi', name: 'poi', version: '3.9'
    // https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml 解决execl 版本差异
    compile group: 'org.apache.poi', name: 'poi-ooxml', version: '3.9'
    // https://mvnrepository.com/artifact/commons-io/commons-io 文件上传
    compile group: 'commons-io', name: 'commons-io', version: '1.3.1'
    // https://mvnrepository.com/artifact/commons-fileupload/commons-fileupload
    compile group: 'commons-fileupload', name: 'commons-fileupload', version: '1.2.2'
}
```

### **3. 各层包功能讲解 & 项目搭建完毕最终效果演示图**

**3.1 项目中各层包功能讲解**

项目中 Java 源代码层级结构如下图所示：

![20241229154732_XHVuaqIU.webp](https://cdn.dong4j.site/source/image/20241229154732_XHVuaqIU.webp)

对于 www 包中的各分层，我们对照上图重点说明：

controller: 用于路由各种 http 访问，其中可以实现对前台页面参数的对象化绑定，这个功能的实现是依赖于 spring mvc 中的参数绑定功能，以及返回向前端页面返回数据。也可以实现基于 Restful 风格 API 的编写。

dao：用于实现对数据库的操作，包中的代码继承并实现自 common 中的 dao 层代码，采用的是类的适配器模式实现的，这里的代码值得细细品味，可以说是整个项目的灵魂所在之处。

domain: 项目的实体类都存在于这个包中，其中的类与数据库表相对应。

dto: 实现了序列化的数据传输层对象，用于接收前台参数，并封装成 dto 对象传输至后台，也负责从数据库中查询数据的封装。

qo: 模糊查询对象所在的包，用于封装 QBC 动态查询参数。

rowmapper：用于对应 jdbcTemplate 查询数据库返回对象的数据集，并将数据集依照此对象进行封装。

schedulejob：定时任务类所在的包，其中类要加上 @Service 注解，因为定时任务注解配置在 service-applicationContext.xml 中，包扫描组件的规则是只扫描有 @Service 注解的组件类

service: 业务逻辑层，主要完成业务逻辑的书写，其中调用了 dao 实现类中的方法，并且每个有关于数据库操作的方法上都加上了 @Transaction 注解，@Transaction 是 Spring Framework 对 AOP 的另一种区别于拦截器的自定义注解实现。

### **4. 项目中重要代码讲解**

主要讲解一下 Dao 层中代码对适配器设计模式的应用：

**4.1 首先看下 commom 层中 BaseDao.java**

```
package com.fxmms.common.dao;

import com.fxmms.common.ro.Dto;
import com.fxmms.common.ro.DtoResultWithPageInfo;
import com.fxmms.common.ro.PageQo;
import org.hibernate.Criteria;
import org.springframework.stereotype.Repository;

import java.io.Serializable;
import java.util.List;
import java.util.Map;

/**
 *
 * @param <T>
 * @usage  数据库公共操作接口
 */
@Repository
public interface BaseDao<T> {

 /**
  *
  *
  * @param id
  * @usage 根据id获取数据库中唯一纪录，封装成java对象并返回
  * @return T
  */
 public T getById(Serializable id);

 /**
  *
  *
  * @param id
  * @usage 根据id懒加载数据库中唯一纪录，封装成java对象并返回
  * @return T
  */
 public T load(Serializable id);

 /**
  *
  *
  * @param columnName
  *
  * @param value
  *
  * @usage 根据列名，以及对应的值获取数据库中惟一纪录，封装成Java对象并返回
  *
  * @return
  */
 public T getByUniqueKey(String columnName, Object value);

 /**
  *
  *
  * @param nameValuePairs
  *
  * @return T
  */
 public T getUniqueResult(Map<String, Object> nameValuePairs);

 /**
  *
  *
  * @param columnName
  *
  * @param value
  *
  * @param sort
  *
  * @param order
  *            asc/desc
  * @return List<T>
  */
 public List<T> getListByColumn(String columnName, Object value,
                                   String sort, String order);

 public List<T> getListByColumn(String columnName, Object value);

 /**
  * ͨ
  *
  * @param nameValuePairs
  *
  * @param sort
  *
  * @param order
  *            asc/desc
  * @return List<T>
  */
 public List<T> getListByColumns(Map<String, Object> nameValuePairs,
                                    String sort, String order);

 public List<T> getListByColumns(Map<String, Object> nameValuePairs);

 /**
  *
  *
  * @return List<T>
  */
 public List<T> getAll();

 /**
  *
  *
  * @param t
  * @return Serializable id
  */
 public Serializable save(T t);

 /**
  *
  *
  * @param t
  */
 public void update(T t);

 /**
  *
  *
  * @param t
  */
 public void delete(T t);

 /**
  * QBC
  * @return
  */
 public Criteria createCriteria();

 /**
  * @param <E>
  * @param <D>
  * @param criteria
  * @param pageNo
  * @param pageSize
  * @param dtoClazz
  * @return
  */
 public <E, D extends Dto> DtoResultWithPageInfo<D> queryPageListByCriteria(
            Criteria criteria, int pageNo, int pageSize, Class<D> dtoClazz);

 /**
  * @param <E>
  * @param <D>
  * @param criteria
  * @param qo
  * @param class1
  * @return
  */
 public <E, D extends Dto> DtoResultWithPageInfo<D> queryPageListByCriteriaWithQo(PageQo qo, Class<D> dtoClazz);

}
```

其中定义了一些对数据库的抽象公共操作方法，代码中有注释，可以对照理解。

**4.2 看下 HibernateTemplateDao.java 对 BaseDao.java 的抽象实现**

```
package com.fxmms.common.dao.hib;

import com.fxmms.common.dao.BaseDao;
import com.fxmms.common.ro.Dto;
import com.fxmms.common.ro.DtoResultWithPageInfo;
import com.fxmms.common.ro.PageInfo;
import com.fxmms.common.ro.PageQo;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.criterion.Order;
import org.hibernate.criterion.Projections;
import org.hibernate.criterion.Restrictions;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Repository;
import org.springframework.util.StringUtils;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 *
 * @param <T>
 * @usage 应用数据访问的灵魂，抽象出各种模型类进行数据库访问的公共操作。
 *        主要使用到QBC动态查询。主要思想是利用反射。
 */
@Repository
public abstract class HibernateTemplateDao<T> implements BaseDao<T> {
 protected static final Log log = LogFactory
   .getLog(HibernateTemplateDao.class);
    //通过反射，可以实现对不同类对应的数据表的操作
 protected abstract Class<?> getEntityClass();

 protected SessionFactory sessionFactory;

 @Autowired
 @Qualifier("sessionFactory")
 public void setSessionFactory(SessionFactory sessionFactory) {
  this.sessionFactory = sessionFactory;
 }

 public Session getSession() {
  return sessionFactory.getCurrentSession();
 }

 public Session openNewSession() {
  return sessionFactory.openSession();
 }

 @Override
 @SuppressWarnings("unchecked")
 public T getById(Serializable id) {
  return (T) getSession().get(getEntityClass(), id);
 }

 @Override
 @SuppressWarnings("unchecked")
 public T getByUniqueKey(String columnName, Object value) {
  return (T) getSession().createCriteria(getEntityClass())
    .add(Restrictions.eq(columnName, value)).uniqueResult();
 }

 @Override
 @SuppressWarnings("unchecked")
 public List<T> getListByColumn(String columnName, Object value,String sort,String order) {
  Criteria criteria = getSession().createCriteria(getEntityClass());
  criteria.add(Restrictions.eq(columnName, value));
  if(StringUtils.hasText(sort) && StringUtils.hasText(order)){
   if("asc".equals(order)){
    criteria.addOrder(Order.asc(sort));
   }else if("desc".equals(order)){
    criteria.addOrder(Order.desc(sort));
   }
  }
  List<T> list = criteria.list();
  return list;
 }

 @Override
 @SuppressWarnings("unchecked")
 public List<T> getListByColumn(String columnName, Object value) {
  Criteria criteria = getSession().createCriteria(getEntityClass());
  criteria.add(Restrictions.eq(columnName, value));
  List<T> list = criteria.list();
  return list;
 }

 @Override
 @SuppressWarnings("unchecked")
 public List<T> getListByColumns(Map<String, Object> nameValuePairs,String sort,String order){
  Criteria criteria = getSession().createCriteria(getEntityClass());
  for (Map.Entry<String, Object> entry : nameValuePairs.entrySet()) {
   criteria.add(Restrictions.eq(entry.getKey(), entry.getValue()));
  }
  if(StringUtils.hasText(sort) && StringUtils.hasText(order)){
   if("asc".equals(order)){
    criteria.addOrder(Order.asc(sort));
   }else if("desc".equals(order)){
    criteria.addOrder(Order.desc(sort));
   }
  }
  List<T> list = criteria.list();
  return list;
 }

 @Override
 @SuppressWarnings("unchecked")
 public List<T> getListByColumns(Map<String, Object> nameValuePairs){
  Criteria criteria = getSession().createCriteria(getEntityClass());
  for (Map.Entry<String, Object> entry : nameValuePairs.entrySet()) {
   criteria.add(Restrictions.eq(entry.getKey(), entry.getValue()));
  }
  List<T> list = criteria.list();
  return list;
 }
 @Override
 @SuppressWarnings("unchecked")
 public List<T> getAll() {
  return getSession().createCriteria(getEntityClass()).list();
 }

 @Override
 @SuppressWarnings("unchecked")
 public T getUniqueResult(Map<String, Object> nameValuePairs) {
  Criteria criteria = getSession().createCriteria(getEntityClass());
  for (Map.Entry<String, Object> entry : nameValuePairs.entrySet()) {
   criteria.add(Restrictions.eq(entry.getKey(), entry.getValue()));
  }
  return (T) criteria.uniqueResult();
 }

 @Override
 @SuppressWarnings("unchecked")
 public T load(Serializable id){
  return (T) getSession().load(getEntityClass(), id);
 }

 @Override
 public Serializable save(T t) {
  return getSession().save(t);
 }

 @Override
 public void update(T t) {
  Session session = this.getSession();
  session.update(t);
  //强制刷新缓存中数据至数据库中，防止大批量数据更新之后出现脏数据
  session.flush();
 }

 @Override
 public void delete(T t) {
  this.getSession().delete(t);
 }

 /**
  * QO  DtoResultWithPageInfo<dtoClazz>list+ҳϢ
  *
  * @param page
  * @param pageSize
  * @param qo
  * @param dtoClazz
  * @return
  */
/* public <Q extends QueryObject, D extends Dto> DtoResultWithPageInfo<D> queryPageListByQueryObject(
   int page, int pageSize,Q qo, Class<D> dtoClazz){
  Criteria criteria = QueryObjectHelper.buildCriteria(qo, getSession());
  return queryPageListByCriteria(criteria, page, pageSize, dtoClazz);
 }*/

 /**
  * QO List<dtoClazz>
  * @param qo
  * @param dtoClazz
  * @return
  */
 /*public <Q extends QueryObject,E, D extends Dto> List<D> queryListByQueryObject(
   Q qo, Class<D> dtoClazz){
  Criteria criteria = QueryObjectHelper.buildCriteria(qo, getSession());
  @SuppressWarnings("unchecked")
  List<E> list = criteria.list();
  List<D> resultsDtoList = new ArrayList<D>();
  for(E entity:list){
   try {
    D dto = dtoClazz.newInstance();
    BeanUtils.copyProperties(entity, dto);
    resultsDtoList.add(dto);
   } catch (InstantiationException e) {
    log.error("dtoʵ쳣ExMsg==>"+e.getMessage());
   } catch (IllegalAccessException e) {
    log.error("dtoʵ쳣ExMsg==>"+e.getMessage());
   }
  }
  return resultsDtoList;
 }*/

 /**
  * queryPageListByCriteria
  *
  * ͨcriteria  DtoResultWithPageInfo<dtoClazz>list+ҳϢ
  *
  * @param criteria
  *            ѯ
  * @param pageNo
  *            ǰҳ
  * @param pageSize
  *            ÿҳʾ
  * @param dtoClass
  *            ݴݶclass
  *
  */
 /*public <E, D extends Dto> DtoResultWithPageInfo<D> queryPageListByCriteria(
   Criteria criteria, int pageNo, int pageSize, Class<D> dtoClazz) {

  PageInfo pageInfo = getInstancePageInfoWithCriteria(criteria, pageNo,
    pageSize);
  criteria.setProjection(null);// ͶӰ
  criteria.setFirstResult(pageInfo.getFirstResultNum());
  criteria.setMaxResults(pageInfo.getPageSize());
  @SuppressWarnings("unchecked")
  List<E> resultsList = criteria.list();
  List<D> resultsDtoList = new ArrayList<D>();
  for (E result : resultsList) {
   D dto;
   try {
    dto = dtoClazz.newInstance();
    try {
     BeanUtils.copyProperties(result, dto);
    } catch (Exception e) {
     log.error("ҳѯ쳣bean쳣");
     e.printStackTrace();
    }
   } catch (InstantiationException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   } catch (IllegalAccessException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   }
   resultsDtoList.add(dto);
  }
  DtoResultWithPageInfo<D> resultWithPageInfo = new DtoResultWithPageInfo<D>(
    resultsDtoList, pageInfo);
  return resultWithPageInfo;
 }*/

 /**
  * ͨcriteria  List<dtoClazz>
  *
  * @param criteria
  * @param dtoClazz
  * @return
  */
 /*public <E, D extends Dto> List<D> queryListByCriteria(
   Criteria criteria,Class<D> dtoClazz) {

  @SuppressWarnings("unchecked")
  List<E> resultsList = criteria.list();
  List<D> resultsDtoList = new ArrayList<D>();
  for (E result : resultsList) {
   D dto;
   try {
    dto = dtoClazz.newInstance();
    try {
     BeanUtils.copyProperties(result, dto);
    } catch (Exception e) {
     log.error("ҳѯ쳣bean쳣");
     e.printStackTrace();
    }
   } catch (InstantiationException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   } catch (IllegalAccessException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   }
   resultsDtoList.add(dto);
  }
  return resultsDtoList;
 }*/

 /*public DataTablePageList queryDataTablePageListByCriteria(
   Criteria criteria, String displayStart, String displayLength) {
  // ܼ¼
  long totalRecords = 0L;
  criteria.setProjection(Projections.rowCount());
  totalRecords = (Long) criteria.uniqueResult();

  //
  criteria.setProjection(null);
  criteria.setFirstResult(Integer.parseInt(displayStart));
  criteria.setMaxResults(Integer.parseInt(displayLength));

  @SuppressWarnings("rawtypes")
  List resultsList = criteria.list();

  DataTablePageList dtpl = new DataTablePageList(
    String.valueOf((int) totalRecords), resultsList);
  return dtpl;
 }
 */

 /**
  * @param criteria
  * @param pageNo
  * @param pageSize
  * @return
  *//*
 private PageInfo getInstancePageInfoWithCriteria(Criteria criteria,
   int pageNo, int pageSize) {
  long totalQuantity = 0L;
  criteria.setProjection(Projections.rowCount());
  totalQuantity = (Long) criteria.uniqueResult();
  PageInfo pageInfo = PageInfo.getInstance(pageNo, pageSize,
    totalQuantity);
  return pageInfo;
 }*/

 @Override
 public Criteria createCriteria() {
  // TODO Auto-generated method stub
  return getSession().createCriteria(getEntityClass());
 }

 /**
  * queryPageListByCriteria
  *
  * ͨcriteria  DtoResultWithPageInfo<dtoClazz>list+ҳϢ
  *
  * @param criteria
  *            ѯ
  * @param pageNo
  *            ǰҳ
  * @param pageSize
  *            ÿҳʾ
  * @param dtoClass
  *            ݴݶclass
  * ص DtoResultWithPageInfo
  *
  * Ϊ queryPageListByCriteria
  */
 @Override
 public <E, D extends Dto> DtoResultWithPageInfo<D> queryPageListByCriteria(
   Criteria criteria, int pageNo, int pageSize, Class<D> dtoClazz) {
      //˷ĵãpageinfoѾfirstResult  maxresult
  PageInfo pageInfo = getInstancePageInfoWithCriteria(criteria, pageNo,
    pageSize);

  criteria.setProjection(null);// ͶӰ
  criteria.setFirstResult(pageInfo.getFirstResultNum());
  criteria.setMaxResults(pageInfo.getPageSize());
  @SuppressWarnings("unchecked")
  List<E> resultsList = criteria.list();
  List<D> resultsDtoList = new ArrayList<D>();
  for (E result : resultsList) {
   D dto;
   try {
    dto = dtoClazz.newInstance();
    try {
     BeanUtils.copyProperties(result, dto);
    } catch (Exception e) {
     log.error("ҳѯ쳣bean쳣");
     e.printStackTrace();
    }
   } catch (InstantiationException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   } catch (IllegalAccessException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   }
   resultsDtoList.add(dto);
  }
  DtoResultWithPageInfo<D> resultWithPageInfo = new DtoResultWithPageInfo<D>(
    resultsDtoList, pageInfo);
  return resultWithPageInfo;
 }

 /**
  * queryPageListByCriteriaWithQo
  *
  * ͨcriteria  DtoResultWithPageInfo<dtoClazz>list+ҳϢ
  *
  * @param criteria
  *            ѯ
  * @param pageNo
  *            ǰҳ
  * @param pageSize
  *            ÿҳʾ
  * @param dtoClass
  *            ݴݶclass
  * ص DtoResultWithPageInfo
  *
  * Ϊ queryPageListByCriteria
  */
 @Override
 public <E, D extends Dto> DtoResultWithPageInfo<D> queryPageListByCriteriaWithQo(PageQo qo, Class<D> dtoClazz) {
      //˷ĵãpageinfoѾfirstResult  maxresult
  Criteria criteria = this.createCriteria();
  qo.add(criteria);
  PageInfo pageInfo = getInstancePageInfoWithCriteria(criteria, qo.getPage(),qo.getRows());

  criteria.setProjection(null);// ͶӰ
  criteria.setFirstResult(pageInfo.getFirstResultNum());
  criteria.setMaxResults(pageInfo.getPageSize());
  @SuppressWarnings("unchecked")
  List<E> resultsList = criteria.list();
  List<D> resultsDtoList = new ArrayList<D>();
  for (E result : resultsList) {
   D dto;
   try {
    dto = dtoClazz.newInstance();
    try {
     BeanUtils.copyProperties(result, dto);
    } catch (Exception e) {
     log.error("ҳѯ쳣bean쳣");
     e.printStackTrace();
    }
   } catch (InstantiationException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   } catch (IllegalAccessException e) {
    log.error("ҳѯ쳣dtoʼ쳣");
    e.printStackTrace();
    dto = null;
   }
   resultsDtoList.add(dto);
  }
  DtoResultWithPageInfo<D> resultWithPageInfo = new DtoResultWithPageInfo<D>(
    resultsDtoList, pageInfo);
  return resultWithPageInfo;
 }

 /**
  * ͨѯʼҳϢ
  *
  * @param criteria
  * @param pageNo
  * @param pageSize
  * @return
  */
 private PageInfo getInstancePageInfoWithCriteria(Criteria criteria,
  int pageNo, int pageSize) {
   long totalQuantity = 0L;
         //  ܵtotalQuality
  criteria.setProjection(Projections.rowCount());
  totalQuantity = (Long) criteria.uniqueResult();

  PageInfo pageInfo = PageInfo.getInstance(pageNo, pageSize,
    totalQuantity);
  return pageInfo;
 }
}
```

这个方法是极为重要的 **protected abstract Class getEntityClass();**

后续介绍，现在暂时有个印象。

在 www 中的 dao 层有与各具体类 (数据表) 相对应的数据库操作实现：

![20241229154732_tHo8ryx3.webp](https://cdn.dong4j.site/source/image/20241229154732_tHo8ryx3.webp)

上图声明了三个具体类对应的接口声明：AdminDao、MacDao、TaskDao。

对应三个接口有三个具体的实现类：AdminDaoImpl、MacDaoImpl、TaskDaoImpl。

我们以与 Admin 类相关的 dao 层操作为例：

**Admin.java**

```
package com.fxmms.www.domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;

/**
 * Created by mark on 16/11/2.
 * @usage 管理员实体类，与数据库中表相对应
 */
@Entity
@Table(name = "mms_admin")
public class Admin {
    @Id
    @GeneratedValue(generator = "increment")
    @GenericGenerator(name = "increment", strategy = "increment")
    @Column
    private int id;
    @Column
    private String userName;
    @Column
    private String password;
    @Column
    private String role;
    @Column
    private int enable;
    @Column
    private int isDelete;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public int getEnable() {
        return enable;
    }

    public void setEnable(int enable) {
        this.enable = enable;
    }

    public int getIsDelete() {
        return isDelete;
    }

    public void setIsDelete(int isDelete) {
        this.isDelete = isDelete;
    }
}
```

AdminDao.java

```
package com.fxmms.www.dao;

import com.fxmms.common.dao.BaseDao;
import com.fxmms.www.domain.Admin;

/**
 * Created by mark on 16/10/31.
 * @usage 操作管理员数据库访问接口
 */
public interface AdminDao extends BaseDao<Admin> {

}
```

**AdminDaoImpl.java**

```
package com.fxmms.www.dao.hib;

import com.fxmms.common.dao.hib.HibernateTemplateDao;
import com.fxmms.www.dao.AdminDao;
import com.fxmms.www.domain.Admin;

/**
 * Created by mark on 16/11/2.
 * @usage 使用适配器模式，将common层中定义的公共访问数据库方法实现嫁接到Admin类的接口中。
 */
public class AdminDaoImpl extends HibernateTemplateDao<Admin> implements AdminDao {

    @Override
    protected Class<?> getEntityClass() {
        // TODO Auto-generated method stub
        return Admin.class;
    }
}
```

可以看到，在具体类相关的数据库操作实现类中，我们只需要实现 HibernateTemplateDao 中抽象方法 protected Class getEntityClass()；即可。

给我们的感觉就是这个方法的实现是画龙点睛之笔。

回过头去看，在 HibernateTemplateDao 类中所有与数据库操作有关的方法：

例如：

```
@Override
 @SuppressWarnings("unchecked")
 public T getByUniqueKey(String columnName, Object value) {
  return (T) getSession().createCriteria(getEntityClass())
    .add(Restrictions.eq(columnName, value)).uniqueResult();
 }
```

getEntityClass() 方法最终都会被具体的类所实现。这个设计真的是很巧妙。

### **5. 配置 tomcat 运行环境**

项目搭建已经完毕，接下来需要做的就是配置项目的运行环境了，这里我们采用 tomcat 来充当应用服务器。

**5.1 去官网下载** **tomcat 8.0** ：

**5.2 配置 tomcat 服务器：**

点击 Edit Configurations

![20241229154732_tHo8ryx3.webp](https://cdn.dong4j.site/source/image/20241229154732_tHo8ryx3.webp)

点击 **+** , 并选择 Tomcat Server 中 local 选项

![20241229154732_ojYcFsU5.webp](https://cdn.dong4j.site/source/image/20241229154732_ojYcFsU5.webp)

添加启动任务名称，默认为 unnamed

![20241229154732_ig9DUzOL.webp](https://cdn.dong4j.site/source/image/20241229154732_ig9DUzOL.webp)

配置 Application Server

![20241229154732_fIKJvfBo.webp](https://cdn.dong4j.site/source/image/20241229154732_fIKJvfBo.webp)

装载开发版 (exploded) 应用 war 包, 此步骤有两种方式：

第一种方式：选择 Deploy at the server startup 下方的 **+** ，入下图所示：

![20241229154732_lD9SgjpR.webp](https://cdn.dong4j.site/source/image/20241229154732_lD9SgjpR.webp)

接下来在 Select Artifacts Deploy 弹出框中 选择 exploded 属性的 war 包

![20241229154732_BJd5P2dY.webp](https://cdn.dong4j.site/source/image/20241229154732_BJd5P2dY.webp)

接下来选择 apply－> ok ，最终的结果是：

![20241229154732_PcOBGRdB.webp](https://cdn.dong4j.site/source/image/20241229154732_PcOBGRdB.webp)

![20241229154732_hYLbPDmx.webp](https://cdn.dong4j.site/source/image/20241229154732_hYLbPDmx.webp)

最终点击启动按钮启动应用

![20241229154732_c5xOPjVC.webp](https://cdn.dong4j.site/source/image/20241229154732_c5xOPjVC.webp)

最终的启动效果如下所示

![20241229154732_YWeoAGWC.webp](https://cdn.dong4j.site/source/image/20241229154732_YWeoAGWC.webp)

### **6.webapp 文件夹下分层详解**

webapp 下有 res 文件夹，用于存储静态文件，WEB-INF 文件夹下有 view 文件夹表示

关于项目中应用到的 JNI 技术，会在后面讲解，主要侧重点是在代码层面解决 JNI link library 的问题。
