---
title: MyBatis 入门必备：如何配置和运行第一个程序
keywords:
  - MyBatis
  - 持久层框架
  - iBATIS
  - Java
  - JDBC
  - XML配置
  - 注解配置
categories:
  - 新时代码农
tags:
  - MyBatis
  - 持久层框架
  - iBATIS
  - Java
  - JDBC
  - XML配置
  - 注解配置
abbrlink: 535f8b87
date: 2013-04-15 00:00:00
ai:
  - MyBatis是一个基于Java的持久层框架，由iBATIS演变而来。它支持普通SQL查询、存储过程和高级映射，并自动处理大部分JDBC代码。MyBatis使用XML或注解配置，将接口和Java对象映射到数据库记录。快速入门指南包括创建项目、添加库依赖、设置数据库环境、定义实体类、建立SQL映射文件、注册映射文件以及编写测试代码。
description: MyBatis是一个基于Java的持久层框架，由iBATIS演变而来。它支持普通SQL查询、存储过程和高级映射，并自动处理大部分JDBC代码。MyBatis使用XML或注解配置，将接口和Java对象映射到数据库记录。快速入门指南包括创建项目、添加库依赖、设置数据库环境、定义实体类、建立SQL映射文件、注册映射文件以及编写测试代码。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

MyBatis 本是 apache 的一个开源项目 iBatis, 2010 年这个项目由 apache software foundation 迁移到了 google code，并且改名为 MyBatis 。2013 年 11 月迁移到 Github。

iBATIS 一词来源于“internet”和“abatis”的组合，是一个基于 Java 的持久层框架。iBATIS 提供的持久层框架包括 SQL Maps 和 Data Access Objects（DAO）

MyBatis 是一个支持普通 SQL 查询，存储过程和高级映射的优秀持久层框架。MyBatis 消除了几乎所有的 JDBC 代码和参数的手工设置以及对结果集的检索封装。MyBatis 可以使用简单的 XML 或注解用于配置和原始映射，将接口和 Java 的 POJO（Plain Old Java Objects，普通的 Java 对象）映射成数据库中的记录。

## Mybatis 快速入门

### 准备开发环境

1. 创建测试项目,普通的 Java 项目或者 JavaWeb 项目均可
2. 添加相应的 jar 包

   - Mybatis 核心包 mybatis-3.30.jar
   - 数据库驱动 mysql-connector-5.1.19-bin.jar

3. 创建数据库和表

```sql
create table `t_user` (
  `user_id` int(11) not null auto_increment,
  `f_name` varchar(255) default null,
  `f_age` int(11) default null,
  primary key (`user_id`)
) engine=InnoDB default charset=utf-8
insert into  t_user(f_name,f_age) values('CODE',26);
insert into  t_user(f_name,f_age) values('array',26);
```

### 使用 Mybatis 查询表中数据

1. 添加 Mybatis 配置文件 mybatis-config.xml

```sql
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- Continue going here -->
    <!--给Bean起别名,就不用每次都要写一长串的全类名了-->
    <typeAliases>
        <typeAlias type="com.code.bean.UserBean" alias="UserBean"/>
    </typeAliases>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/mybatis"/>
                <property name="username" value="code"/>
                <property name="password" value="8998"/>
            </dataSource>
        </environment>
    </environments>

</configuration>
```

2. 建立实体 Bean

```java
package com.code.bean;
public class UserBean {
    private int id;
    private String name;
    private int age;
    public UserBean() {
    }
    public UserBean(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public UserBean(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    @Override
    public String toString() {
        return "UserBean{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

3. 建立操作数据表的 sql 映射文件 userMapper.xml

- 创建一个包 com.code.mapper,用来放映射文件和 xxxMapper.java
- UserMapper.java

```java
package com.code.mapper;
import com.code.bean.UserBean;
import org.apache.ibatis.annotations.Param;
public interface UserMapper {
	   //@Param为参数设置别名,在select语句的就用写 #{0} 了,而是 #{userID}
	   UserBean getUserById(@Param("userID")int userID);
}
```

- userMapper.xml 配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<!--
    为这个mapper指定一个唯一的namespace，
    这样就能够保证namespace的值是唯一的
-->
<mapper namespace="com.code.mapper.UserMapper">
    <!--
        这里是当数据表字段名和实体类属性名不一致时将他们一一对应
    -->
    <resultMap id="userBean" type="UserBean">
        <id property="id" column="user_id" javaType="int"/>
        <result property="name" column="f_name" javaType="string"/>
        <result property="age" column="f_age" javaType="int"/>
    </resultMap>
    <!--
         根据id查询得到一个user对象
     -->
    <!--
         在select标签中编写查询的SQL语句， 设置select标签的id属性为getUser，id属性值必须是唯一的，不能够重复.
         这里的id是UserMapper接口中的方法名
         使用parameterType属性指明查询时使用的参数类型，resultType属性指明查询返回的结果集类型
         resultType="com.code.bean.UserBean"就表示将查询结果封装成一个UserBean类的对象返回
         如果实体类属性和数据表字段名字不相同,则通过resultMap指定
    -->
    <select id="getUserById" resultMap="userBean" parameterType="int">
        select * from t_user where user_id = #{userID}
    </select>
</mapper>
```

4. 在配置文件中注册映射文件

- 在 mybaits-config.xml 文件中添加

```xml
<mappers>
        <!--
            注册userMapper.xml文件，
            userMapper.xml位于com.code.mapper这个包下，
            所以resource写成com/code/mapper/userMapper.xml
        -->
	<mapper resource="com/code/mapper/userMapper.xml"/>
</mappers>
```

5. 新建一个 DBUtil.java 工具类,位于 com.code.util 包下

```java
package com.code.util;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;

public class DBUtil {
    private static SqlSessionFactory sqlSessionFactory;

    //初始化
    static {
        InputStream in = null;
        try {
            //加载配置文件
            in = Resources.getResourceAsStream("mybatis-config.xml");
            //得到sqlSessionFactory工厂
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(in);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (in != null) {
                    in.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static SqlSession getSession() {
        //返回能执行映射文件中sql的sqlSession
        return sqlSessionFactory.openSession();
    }
}

```

6. 编写测试代码,执行 select 操作

```java
package com.code.test;

import com.code.bean.UserBean;
import com.code.mapper.UserMapper;
import com.code.util.DBUtil;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class Test1 {
    @Test
    public void testGetUserById(){
        SqlSession sqlSession = DBUtil.getSession();
        UserMapper userMapper =  sqlSession.getMapper(UserMapper.class);
        UserBean userBean = userMapper.getUserById(1);
        System.out.println(userBean);
    }
}
```
