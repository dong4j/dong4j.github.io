---
title: MyBatis 一对多、一对一查询详解与配置示例
keywords:
  - MyBatis
  - 数据库操作
  - 一对一关联
  - 一对多关联
  - 继承关联
categories:
  - 新时代码农
tags:
  - MyBatis
  - 数据库操作
  - 一对一关联
  - 一对多关联
  - 继承关联
abbrlink: 2a833323
date: 2013-04-17 00:00:00
ai:
  - 本文介绍了使用MyBatis进行数据库操作的方法，包括一对一关联、一对多关联和继承关联。通过配置XML文件，可以实现数据库的查询、更新、删除等操作。文章中详细说明了如何使用association和collection标签来实现不同类型的关联关系。此外，还介绍了一种新的关联方式：使用discriminator标签实现继承关联。最后，本文提供了一个具体的例子，展示如何在MyBatis中使用这些功能。
description: 本文介绍了使用MyBatis进行数据库操作的方法，包括一对一关联、一对多关联和继承关联。通过配置XML文件，可以实现数据库的查询、更新、删除等操作。文章中详细说明了如何使用association和collection标签来实现不同类型的关联关系。此外，还介绍了一种新的关联方式：使用discriminator标签实现继承关联。最后，本文提供了一个具体的例子，展示如何在MyBatis中使用这些功能。
---

## 一对一关联

1.要求  
假设一间房子只有一把锁,要求通过锁找到房子  
2.创建表和数据

```sql
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_lock
-- ----------------------------
DROP TABLE IF EXISTS `t_lock`;
CREATE TABLE `t_lock` (
  `lock_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_type` varchar(255) DEFAULT NULL,
  `fk_home_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`lock_id`),
  KEY `fk_home_id` (`fk_home_id`),
  CONSTRAINT `t_lock_ibfk_1` FOREIGN KEY (`fk_home_id`) REFERENCES `t_home` (`home_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_lock
-- ----------------------------
INSERT INTO `t_lock` VALUES ('1', '防盗锁', '2');
INSERT INTO `t_lock` VALUES ('2', '铁锁', '1');
INSERT INTO `t_lock` VALUES ('3', '铜锁', '3');
-- ----------------------------
-- Table structure for t_home
-- ----------------------------
DROP TABLE IF EXISTS `t_home`;
CREATE TABLE `t_home` (
  `home_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`home_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_home
-- ----------------------------
INSERT INTO `t_home` VALUES ('1', '1号家庭');
INSERT INTO `t_home` VALUES ('2', '2号家庭');
INSERT INTO `t_home` VALUES ('3', '3号家庭');
```

3.定义实体类

- HomeBean.java

```java
package com.code.bean;
public class HomeBean {
    private int id;
    private String address;
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }
    public void setAddress(String address) {
        this.address = address;
    }
    @Override
    public String toString() {
        return "HomeBean [id=" + id + ", address=" + address + "]";
    }
}
```

- LockBean.java

```java
package com.code.bean;

import java.util.ArrayList;
import java.util.List;
public class LockBean {
    private int id;
    private String type;
    /**
    * lock表中有一个fk_home_id字段,
    * 所以在lock中定义一个myHome属性,
    * 用来维护2个表之间一对一关系
    * 通过这个属性就可以知道这把锁死哪家的
    */
    private HomeBean myHome;
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }
    public HomeBean getMyHome() {
        return myHome;
    }
    public void setMyHome(HomeBean myHome) {
        this.myHome = myHome;
    }
    @Override
    public String toString() {
        return "LockBean [id=" + id + ", type=" + type + ", myHome=" + myHome
                + ", keyLst=" + keyLst + "]";
    }
}
```

4.定义 sql 映射文件 lockMapper.xml

```xml

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >

<mapper namespace="com.code.mapper.LockMapper">

    <!--
        根据lockid查询home信息
        ##1. 连表查询
        select * from t_lock l,t_home h where l.fk_home_id=h.home_id and l.lock_id=1;
        ##2. 执行两次查询
        select fk_home_id from t_lock where lock_id=1;
        select * from t_home where home_id=(上一次的结果);
    -->

    <!--
        方式一:嵌套查询:使用嵌套结果映射来处理重复的联合结果的子集
                封装联表查询的数据(去除重复的数据)
    -->
    <resultMap id="lockMapWithHome1" type="LockBean">
        <id property="id" column="lock_id" javaType="int"/>
        <result property="type" column="f_type" javaType="string"/>
        <association  property="myHome"  javaType="HomeBean" >
            <id property="id" column="home_id"/>
            <result property="address" column="f_address"/>
        </association>
    </resultMap>

    <select id="getHomeByLock" resultMap="lockMapWithHome1">
        select * from t_lock l,t_home h where l.fk_home_id=h.home_id and l.lock_id=#{id};
    </select>

    <!--  方式二：嵌套查询：通过执行另外一个SQL映射语句来返回预期的复杂类型
        select fk_home_id from t_lock where lock_id=1;
        select * from t_home where home_id=(上一次的结果);
    -->
    <resultMap id="lockMapWithHome2" type="LockBean">
        <id property="id" column="lock_id" javaType="int"/>
        <result property="type" column="f_type" javaType="string"/>
        <association  property="myHome" column="fk_home_id" javaType="HomeBean" select="getHomeByLock"/>
    </resultMap>

    <select id="getHomeByLock" resultMap="com.code.mapper.HomeMapper.homeMap">
        select * from t_home where home_id = #{0}
    </select>
</mapper>
```

db.propertiespe 文件

```
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/mybatis?useUnicode=true&characterEncoding=UTF-8
jdbc.username=code
jdbc.password=8998
```

mybatis-config.xml 配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org/DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd" >

<configuration>
    <!--使用数据库连接配置文件-->
    <properties resource="datasource.properties"/>

    <!--自动扫描包,用类名做别名-->
    <typeAliases>
        <package name="com.code.bean1"/>
    </typeAliases>
    <!-- 给Bean对象起别名 -->
    <!-- 一个个指定别名-->
    <!--<typeAliases>-->
        <!--<typeAlias type="com.lovo.bean.UserBean" alias="UserBean"/>-->
    <!--</typeAliases>-->

    <!--配置JDBC环境-->
    <environments default="development">
        <environment id="development">
            <!-- type="JDBC" 代表直接使用JDBC的提交回滚来做事务 -->
            <!-- type="MANAGED" 代表使用外部容器（Spring）操作事务 -->
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="${jdbc.driver}"/>
                <property name="url" value="${jdbc.url}"/>
                <property name="username" value="${jdbc.username}"/>
                <property name="password" value="${jdbc.password}"/>
            </dataSource>
        </environment>
    </environments>

    <!--告知映射文件-->
    <mappers>
        <package name="com/code/mapper"/>
    </mappers>
    <!-- 告知Mapper文件的存在 -->
    <!--
        一各个告知映射文件
        <mappers>
            <mapper resource="com/lovo/mapper/UserMapper.xml"/>
        </mappers>
    -->
</configuration>
```

DBUtil.java 跟以前的一样

5.MyBatis 一对一关联查询总结  
MyBatis 中使用 association 标签来解决一对一的关联查询，association 标签可用的属性如下：

    * property:对象属性的名称
    * javaType:对象属性的类型
    * column:所对应的外键字段名称
    * select:使用另一个查询封装的结果

## 一对一双向关联关系

只需要在 home 中页设置一个 lockBean 的属性即可  
通过 homeid 找到 lock 跟通过 lockid 找 home 的配置相同

## 一对多关联关系

一个 lock 可以有多把钥匙  
也有 2 中配置方式  
只需要将 association 换成 collection

```xml
<resultMap  id="lockMapWithKey" type="LockBean">
  		<id property="id" column="lock_id" javaType="int"/>
  		<result property="type" column="f_type" javaType="java.lang.String"/>
  		<collection property="keyLst" ofType="KeyBean" column="lock_id" select="getAllKeyByLock">
  		</collection>
  	</resultMap>
```

7.MyBatis 一对多关联查询总结  
MyBatis 中使用 collection 标签来解决一对多的关联查询，ofType 属性指定集合中元素的对象类型。

## 继承关联关系

使用 discriminator

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.code.mapper.PetMapper">

   <resultMap type="com.code.bean.PetBean" id="petMap">
		<id property="id" column="pet_id" javaType="int" />
		<result property="name" column="f_name" javaType="java.lang.String" />
		<discriminator javaType="java.lang.String" column="f_type">
		 <case value="dog" resultType="com.code.bean.DogBean">
		  <result property="boneNumber" column="f_boneNumber" javaType="int"/>
		 </case>
		<case value="cat" resultType="com.code.bean.CatBean">
		 <result property="fishNumber" column="f_fishNumber" javaType="int"/>
		 <result property="mouseNumber" column="f_mouseNumber" javaType="int"/>
		</case>

		<case value="duck" resultType="com.code.bean.DuckBean">
		 <result property="fishNumber" column="f_fishNumber" javaType="int"/>
		</case>
		</discriminator>
	</resultMap>


	<select id="getPetById" parameterType="int" resultMap="petMap">
	  select * from t_pet where pet_id=#{petId}
	</select>

	<select id="getAllPet" resultMap="petMap">
	 select * from t_pet
	</select>
</mapper>

```
