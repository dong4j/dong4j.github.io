---
title: MyBatis CRUD操作指南
keywords:
  - Mybatis
categories:
  - Mybatis
tags:
  - MyBatis
  - 数据库连接
  - 事务管理
  - 类型别名
  - SQL映射
  - 字段属性映射
  - 数据库配置
  - 性能优化
abbrlink: 68dfa52e
date: 2013-04-16 00:00:00
ai:
  - 文章详细阐述了MyBatis框架中对数据库操作的相关接口和方法。通过使用注解（@Select、@Insert、@Delete、@Update）来执行SQL查询和更新语句，并将配置信息写入db.properties文件，简化了连接与配置过程。此外，介绍了通过typeAliases和<package>标签为实体类定义别名的机制，便于在映射文件中引用。文章还特别强调了解决字段名与属性名不一致问题的方法，包括在SQL语句中设置别名和使用<resultMap>元素进行显式映射。整个过程确保了代码的简洁性和易维护性，为MyBatis框架的应用提供了实用指南。
description: 文章详细阐述了MyBatis框架中对数据库操作的相关接口和方法。通过使用注解（@Select、@Insert、@Delete、@Update）来执行SQL查询和更新语句，并将配置信息写入db.properties文件，简化了连接与配置过程。此外，介绍了通过typeAliases和<package>标签为实体类定义别名的机制，便于在映射文件中引用。文章还特别强调了解决字段名与属性名不一致问题的方法，包括在SQL语句中设置别名和使用<resultMap>元素进行显式映射。整个过程确保了代码的简洁性和易维护性，为MyBatis框架的应用提供了实用指南。
---

上一节中对 Mybatis 的基本操作有了初步的了解,  
这一节中将使用 Mybatis 对数据表进行简单的 CRUD 操作.  
使用的测试环境和上一篇博客一样.

## 使用 Mybatis 对表执行 CRUD 操作 -- 基于 XML 实现

1.定义 UserMapper.java

```java
package com.code.mapper;
import com.code.bean.UserBean;
import org.apache.ibatis.annotations.Param;
import java.util.List;

public interface UserMapper {
    //根据ID查找用户
    UserBean getUserById(@Param("userID")int userID);
    //添加用户
    int addUser(@Param("userBean")UserBean userBean);
    //删除用户
    int deleteUser(@Param("userID")int userID);
    //修改用户
    int updateUser(@Param("userBean")UserBean userBean);
    //查询全部用户
    List<UserBean> getAllUsers();
    //查询全部用户,模糊查询
    List<UserBean> getAllUsersLikeName(@Param("name")String name);
}
```

2.定义 sql 映射文件  
userMapper.xml 文件内容如下:

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

    <!--按id查找用户-->
    <select id="getUserById" resultMap="userBean" parameterType="int">
        select * from t_user where user_id = #{userID}
    </select>

    <!--添加用户-->
    <!--
        当为参数设置别名时(userBean),使用 别名.属性名 来取值;
        如果传入的参数是一个Bean对象或者Map对象,可以不用设置别名,
        自动根据属性名取值
    -->
    <insert id="addUser" parameterType="UserBean" keyProperty="userBean.id" useGeneratedKeys="true">
        insert into t_user values(null,#{userBean.name},#{userBean.age})
    </insert>
    <!--删除用户-->
    <delete id="deleteUser">
        delete from t_user where user_id = #{userID}
    </delete>
    <!--修改用户-->
    <update id="updateUser">
        update t_user set f_name = #{userBean.name},f_age = #{userBean.age} where user_id=#{userBean.id}
    </update>
    <!--查询所有用户-->
    <select id="getAllUsers" resultMap="userBean">
        select * from t_user
    </select>
    <select id="getAllUsersLikeName" resultMap="userBean">
        select * from t_user where f_name like '%${name}%'
    </select>
</mapper>
```

3.测试类

```java
package com.code.test;

import com.code.bean.UserBean;
import com.code.mapper.UserMapper;
import com.code.util.DBUtil;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;
import java.util.List;

public class Test2 {
    @Test
    public void addUserTest() {
        SqlSession sqlSession = DBUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        UserBean   newUser    = new UserBean("张三", 26);
        System.out.println(userMapper.addUser(newUser));
        //手动提交事物
        sqlSession.commit();
        System.out.println(newUser.getId());
        //关闭session
        sqlSession.close();
    }

    @Test
    public void delUserTest() {
        SqlSession sqlSession = DBUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        System.out.println(userMapper.deleteUser(2));
        sqlSession.commit();
        sqlSession.close();
    }

    @Test
    public void updateUserTest() {
        SqlSession sqlSession = DBUtil.getSession();
        UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
        UserBean   updateUser = new UserBean(1, "李四", 25);
        System.out.println(userMapper.updateUser(updateUser));
        ;
        sqlSession.commit();
        sqlSession.close();
    }

    @Test
    public void getAllUsersTest() {
        SqlSession     sqlSession = DBUtil.getSession();
        UserMapper     userMapper = sqlSession.getMapper(UserMapper.class);
        List<UserBean> allUsers   = userMapper.getAllUsers();
        System.out.println(allUsers);
    }

    @Test
    public void getAllUsersLikeNameTest() {
        SqlSession     sqlSession = DBUtil.getSession();
        UserMapper     userMapper = sqlSession.getMapper(UserMapper.class);
        List<UserBean> allUsers   = userMapper.getAllUsersLikeName("c");
        System.out.println(allUsers);
    }
}

```

## 使用 Mybatis 对表执行 CRUD 操作 -- 基于 Annotation 实现

1.UserMapper.java

```java
package com.code.mapper;
/**
 * @author Code.Ai (Email: Code.Ai@outlook.com)
 * @link http://blog.csdn.net/codeai
 * @date 2015/11/19
 * @version 0.1
 * @describe 用于操作数据库的接口
 */

import com.code.bean.UserBean;
import org.apache.ibatis.annotations.*;

import java.util.List;

/**
 * 需要说明的是，我们不需要针对UserMapperI接口去编写具体的实现类代码，
 * 这个具体的实现类由MyBatis帮我们动态构建出来，我们只需要直接拿来使用即可。
 */

public interface UserMapper {
    //根据ID查找用户
    @Select("select * from t_user where user_id = #{userID}")
    UserBean getUserById(@Param("userID") int userID);
    //添加用户
    @Insert("insert into t_user values(null,#{userBean.name},#{userBean.age})")
    int addUser(@Param("userBean") UserBean userBean);
    //删除用户
    @Delete(" delete from t_user where user_id = #{userID}")
    int deleteUser(@Param("userID") int userID);
    //修改用户
    @Update(" update t_user set f_name = #{userBean.name},f_age = #{userBean.age} where user_id=#{userBean.id}")
    int updateUser(@Param("userBean") UserBean userBean);
    //查询全部用户
    @Select("select * from t_user")
    List<UserBean> getAllUsers();
    //查询全部用户,模糊查询
    @Select("select * from t_user where f_name like '%${name}%'")
    List<UserBean> getAllUsersLikeName(@Param("name") String name);
}
```

## 将数据库连接配置信息写入到 properties 文件中

1.db.properties

```
driver=com.mysql.jdbc.Driver
url=jdbc:mysql://localhost:3306/mybatis
name=code
password=8998
```

2.在 mybatis 中引入 db.properties 文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- Continue going here -->
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="${driver}"/>
                <property name="url" value="${url}"/>
                <property name="username" value="${name}"/>
                <property name="password" value="${password}"/>
            </dataSource>
        </environment>
    </environments>
</configuration>
```

## 为实体类定义别名,简化 sql 映射文件的引用

之前已经配置过  
1.在 mybatis-config.xml 文件中配置如下

```xml
<typeAliases>
    <typeAlias type="com.code.bean.UserBean" alias="UserBean"/>
</typeAliases>
```

2.第二种方式:

```xml
<!-- 配置实体类的别名，配置实体类别名的目的是为了在引用实体类时可以使用实体类的别名来代替实体类，达到简写的目的 -->
    <typeAliases>
        <!-- 为com.code.bean包下的所有实体类配置别名，MyBatis默认的设置别名的方式就是去除类所在的包后的简单的类名比如com.code.bean.UserBean这个实体类的别名就会被设置成UserBean
         -->
        <package name="com.code.bean"/>
    </typeAliases>
```

## 解决字段名和实体类属性名不相同造成查询不到结果

解决办法一:  
通过在查询的 sql 语句中定义字段名的别名，让字段名的别名和实体类的属性名一致，这样就可以表的字段名和实体类的属性名一一对应上了，这种方式是通过在 sql 语句中定义别名来解决字段名和属性名的映射关系的。

```sql
select user_id id,f_name name, f_age age from t_user where user_id=#{userID}
```

解决办法二:  
通过<resultMap>来映射字段名和实体类属性名的一一对应关系。这种方式是使用 MyBatis 提供的解决方式来解决字段名和属性名的映射关系的。

```xml
<resultMap id="userBean" type="UserBean">
        <id property="id" column="user_id" javaType="int"/>
        <result property="name" column="f_name" javaType="string"/>
        <result property="age" column="f_age" javaType="int"/>
    </resultMap>
```
