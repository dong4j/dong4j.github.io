---
title: 从零开始：深入理解Hibernate框架的奥秘
keywords:
  - Hibernate
categories:
  - Hibernate
tags:
  - Spring
  - Hibernate
  - Web开发
  - 数据库连接池
  - 映射文件
  - SQL查询
abbrlink: f0fe1ae8
date: 2013-04-14 00:00:00
ai:
  - 该文档描述了如何在Spring框架中使用Hibernate实现基于对象的关系映射。通过配置文件和数据源连接池（如DBCP）初始化了SessionFactory，并在bean定义中提供了自定义方法来处理数据库查询事务。关键点包括设置方言、启用HQL解析器、决定SQL打印、开启外联优化、控制结果集格式化、调整查询缓存策略以及配置连接池参数以提高性能和资源管理。
description: 该文档描述了如何在Spring框架中使用Hibernate实现基于对象的关系映射。通过配置文件和数据源连接池（如DBCP）初始化了SessionFactory，并在bean定义中提供了自定义方法来处理数据库查询事务。关键点包括设置方言、启用HQL解析器、决定SQL打印、开启外联优化、控制结果集格式化、调整查询缓存策略以及配置连接池参数以提高性能和资源管理。
---

Hibernate 框架主要是实现数据库与实体类间的映射，使的操作实体类相当与操作 hibernate 框架。  
 只要实体类写好配置文件配好，就能实现和数据库的映射，其中实体类对应表，类的属性对应数据库的表字段。 这样就不用管数据库的相关操作了。

## 什么是 Hibernate

如今,大多数是关系型数据库,而 Java 是面向对象的编程语言,使用面向对象的语言结合关系型数据库相当麻烦,所以有了 Hibernate  
Hibernate 将对象模型和基于 sql 的关系模型映射起来,使得开发者可以采用面向对象的方式开发程序.  
Hibernate 是关系型数据库和面向对象的程序设计语言之间的桥梁,它允许开发者使用面向对象的语言操作关系型数据库  
以前是应用程序直接访问底层数据库,而采用 ORM 框架之后,应用程序以面向对象的方式操作持久化对象,而 ORM 框架则将这些面向对象的操作转换为底层的 SQL 操作.

## Hibernate 和 JDBC

1. jdbc 的优点和缺点

   - 缺点
     - 查询代码特别繁琐
     - 重复性代码特别多，频繁的 try,catch
     - 数据的缓存
     - sql 的移植性不好
   - 优点
     - 速度比较快
     - 把控性比较好

2. ormapping 框架：数据库的操作框架
   - 优点
     - 比较简单
     - 数据缓存：一级缓存 二级缓存 查询缓存
     - 移植性比较好
   - 缺点
     - 因为 sql 语句是 hibernate 内部生成的，所以程序员干预不了，不可控
     - 如果数据库特别大，不适合用 hibernate

### .hbm.xml(映射文件)

类与表的对应关系  
 类上的属性的名称和表中的字段的名称对应关系  
 类上的属性的类型和表中的字段的类型对应关系  
 把一对多和多对多的关系转化成面向对象的关系

### Hibernate.cfg.xml(配置文件)

hibernate 的配置文件：  
 作用是用来连接数据库的

## hibernate 的组成部分

1. 持久化类

- 实现对应的序列化接口
- 必须有默认的构造函数
- 持久化类的属性不能使用关键字

2. hibernate 的流程
   - Configuraction
     - 加载了配置文件
   - SessionFactory
     - 配置文件的信息、映射文件的信息、持久化类的信息
   - Session  
      1、crud 的操作都是由 session 完成的  
      2、事务是由 session 开启的  
      3、两个不同的 session 只能用各自的事务  
      4、session 决定了对象的状态  
      5、创建完一个 session，相当于打开了一个数据库的链接
   - Transaction  
      1、事务默认不是自动提交的  
      2、必须由 session 开启  
      3、必须和当前的 session 绑定 (两个 session 不可能共用一个事务)
3. 对象的状态的转化
4. hibernate 的原理：  
    根据客户端的代码，参照映射文件，生成 sql 语句，利用 jdbc 技术进行数据库的操作

## Hibernate 核心开发接口

1. Configuration configure() configure(String 配置文件路径)

   - 读取配置文件
   - 通过配置文件产生数据库连接
   - 产生 SessionFactory

2. SessionFactory 维护数据库连接池

   - sessionFactory.opeSession()
     - 得到一个新的 session
   - sessionFactory.getCurrentSession()
     - 如果当前环境 (线程) 中有 session,则直接使用,否则打开一个新的 session
     - 不需要写 session.close()
     - 当 session.commit() 之后,session 自动关闭
     - 界定事务边界
     - current-session_context_class(JTA thread )
       - thread 使用 connection 本身数据库中
       - JTA(Java Transaction API) 需要 application service 支持
         - 跨服务器事务管理
         - 分布式事务 (跨数据库事务,跨服务器事务)

3. 对象的三种状态

   - 瞬时 (Transient)
     - new 出来时,内存中有,缓存没有,数据库没有 (id)
   - 持久化 (persistent)
     - save() saveOrUpdate()
     - 缓存有,数据库有 (id)
   - 托管 (Detached)
     - evict()
     - close()
     - clear()
     - 缓存没有 (已经被销毁了),数据库有 (id)

- 区别:
  - 有没有 id transient
  - id 是否在数据库中 persistens
  - 是否在内存中 (Session 缓存)

4. Session 管理一个数据库的任务单元,执行 CRUD 操作  
   Session 缓存  
   session 对象中有一个 map  
   key 是 id,value 是持久化对象的引用.  
    get 和 load 的区别 - 不存在对应记录时 get 返回 null - load 报异常 - load 返回代理对象,等到真正要使用对象的内容时才发出 sql 语句 - get 直接从数据库加载,不会延迟 - 都会先到缓存中查询,如果没有才进数据库查

5. 代理模式  
   javassist -->直接生成二进制码  
   动态改变类的结构，或者动态生成类。

为什么那个 id 必须是 serializable 接口了

hibernate 不知道我们标识符的类型是什么,所以用一个接口类型作为一个参数,只要实现了 serializable 的数据类型都可以作为参数传进入,然后下午我问的是为什么我的类没有实现 serializable 接口,也能传 id 进去,这跟类没关系,只要参数是 serializable 的实现就可以了,正好穿的参数是 int,它自动包装为 Integer 了,然后 Integer 实现了 serializable 接口

update 方法

- 用来更新 detached 对象,,更新完成转为 persistent 状态
- 更新 transient 对象会报错
- 更新自己设定的 id 的 transient 对象可以 (前提是数据库有对应的数据记录)
- 更新部分更改的字段

  解决更新一个字段,hibernate 其他字段也会更新的问题

O/R Mapping -->对象关系映射  
将程序中的 java 对象和使用的关系型数据库中的表对应  
使用元数据 (描述数据格式的数据) 描述对象和数据库间的映射

好处:

1. 移植性好
2. 简单
3. 使用缓存技术

为什么集合类型的属性只能定义为接口类型  
Hibernate 底层没有使用 JCF 框架中的实现类,而是使用 Apache 自己的集合实现类

必须提供一个标示属性和数据表的主键对应  
因为 Hibernate 是通过用标识符和表中的主键对应,从而判定是表中的哪条记录

get 和 load 方法区别

1. 当查询一个不存在的对象时,get 方法返回 null,load 不返回 null,而是直接抛出 ObjectNotFound 的异常
2. get 方法不支持延迟加载;load 支持

## Hibernate 实体关系映射

1. one-to-one
   - 唯一外键关联
   - 主键关联
2. one-to-maney
   - 单项关联
   - 双向关联
3. maney-to-maney
4. 继承

映射文件中 class 有几个元素依赖于属性的个数  
谁 to 谁  
前面是当前对象.后面是关联对象

cascade 级联操作  
对当前对象的操作也会发生在关联对象上

get 方法的性能优化  
对于引用对象,hibernate 默认是延迟加载

## 1-N 单向关联

用户 用户地址 (家庭,公司)  
1 端有 N 端的集合对象  
通过 1 端找 N 端  
外键在 N 端

在 Hibernate 中，各表的映射文件….hbm.xml 可以通过工具生成，例如在使用 MyEclipse 开发时，它提供了自动生成映射文件的工具。本节简单的讲述一下这些配置文件的配置。

配置文件的基本结构如下：

```xml
<?xml version="1.0" encoding='UTF-8'?>
<!DOCTYPE hibernate-mapping PUBLIC
"-//Hibernate/Hibernate Mapping DTD 3.0//EN"
"http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd" >
<hibernate-mapping package="包名">
    <class name="类名" table="表名">
        <id name="主键在java类中的字段名" column="对应表中字段" type="类型 ">
            <generator class="主键生成策略"/>
        </id>
        <property name="实体bean属性名" type="属性类型" column="对应字段名"></property>
         ……
    </class>
</hibernate-mapping>
```

1.主键（id）  
 Hibernate 的主键生成策略有如下几种：  
1)assigned  
 主键由外部程序负责生成，在 save() 之前必须指定一个。Hibernate 不负责维护主键生成。与 Hibernate 和底层数据库都无关，可以跨数据库。在存储对象前，必须要使用主键的 setter 方法给主键赋值，至于这个值怎么生成，完全由自己决定，这种方法应该尽量避免。

```xml
<id name="id" column="id">
    <generator class="assigned" />
</id>
```

“id”是自定义的策略名，人为起的名字，后面均用“ud”表示。  
特点：可以跨数据库，人为控制主键生成，应尽量避免。

2. hilo  
   hilo（高低位方式 high low）是 hibernate 中最常用的一种生成方式，需要一张额外的表保存 hi 的值。保存 hi 值的表至少有一条记录（只与第一条记录有关），否则会出现错误。可以跨数据库。

```xml
<id name="id" column="id">
    <generator class="hilo">
        <param name="table">hibernate_hilo</param> 指定保存hi值的表名
        <param name="column">next_hi</param> 指定保存hi值的列名
        <param name="max_lo">100</param> 指定低位的最大值
    </generator>
</id>
```

也可以省略 table 和 column 配置，其默认的表为 hibernate_unique_key，列为 next_hi  
hilo 生成器生成主键的过程（以 hibernate_unique_key 表，next_hi 列为例）：

1. 获得 hi 值：读取并记录数据库的 hibernate_unique_key 表中 next_hi 字段的值，数据库中此字段值加 1 保存。
2. 获得 lo 值：从 0 到 max_lo 循环取值，差值为 1，当值为 max_lo 值时，重新获取 hi 值，然后 lo 值继续从 0 到 max_lo 循环。
3. 根据公式 hi _ (max_lo + 1) + lo 计算生成主键值。  
   注意：当 hi 值是 0 的时候，那么第一个值不是 0_(max_lo+1)+0=0，而是 lo 跳过 0 从 1 开始，直接是 1、2、3……

那 max_lo 配置多大合适呢？  
这要根据具体情况而定，如果系统一般不重启，而且需要用此表建立大量的主键，可以吧 max_lo 配置大一点，这样可以减少读取数据表的次数，提高效率；反之，如果服务器经常重启，可以吧 max_lo 配置小一点，可以避免每次重启主键之间的间隔太大，造成主键值主键不连贯。  
特点：跨数据库，hilo 算法生成的标志只能在一个数据库中保证唯一。

3. seqhilo  
   与 hilo 类似，通过 hi/lo 算法实现的主键生成机制，只是将 hilo 中的数据表换成了序列 sequence，需要数据库中先创建 sequence，适用于支持 sequence 的数据库，如 Oracle。

```xml
<id name="id" column="id">
    <generator class="seqhilo">
        <param name="sequence">hibernate_seq</param>
        <param name="max_lo">100</param>
    </generator>
</id>
```

特点：与 hilo 类似，只能在支持序列的数据库中使用。

4. increment  
   由 Hibernate 从数据库中取出主键的最大值（每个 session 只取 1 次），以该值为基础，每次增量为 1，在内存中生成主键，不依赖于底层的数据库，因此可以跨数据库。

```xml
<id name="id" column="id">
    <generator class="increment" />
</id>
```

Hibernate 调用 org.hibernate.id.IncrementGenerator 类里面的 generate() 方法，使用 select max(idColumnName) from tableName 语句获取主键最大值。该方法被声明成了 synchronized，所以在一个独立的 Java 虚拟机内部是没有问题的，然而，在多个 JVM 同时并发访问数据库 select max 时就可能取出相同的值，再 insert 就会发生 Dumplicate entry 的错误。所以只能有一个 Hibernate 应用进程访问数据库，否则就可能产生主键冲突，所以不适合多进程并发更新数据库，适合单一进程访问数据库，不能用于群集环境。  
官方文档：只有在没有其他进程往同一张表中插入数据时才能使用，在集群下不要使用。  
特点：跨数据库，不适合多进程并发更新数据库，适合单一进程访问数据库，不能用于群集环境。

5. identity  
   identity 由底层数据库生成标识符。identity 是由数据库自己生成的，但这个主键必须设置为自增长，使用 identity 的前提条件是底层数据库支持自动增长字段类型，如 DB2、SQL Server、MySQL、Sybase 和 HypersonicSQL 等，Oracle 这类没有自增字段的则不支持。

```xml
<id name="id" column="id">
    <generator class="identity" />
</id>
```

例：如果使用 MySQL 数据库，则主键字段必须设置成 auto_increment。  
id int(11) primary key auto_increment  
特点：只能用在支持自动增长的字段数据库中使用，如 MySQL。

6. sequence  
   采用数据库提供的 sequence 机制生成主键，需要数据库支持 sequence。如 oralce、DB、SAP DB、PostgerSQL、McKoi 中的 sequence。MySQL 这种不支持 sequence 的数据库则不行（可以使用 identity）。

```xml
<generator class="sequence">
    <param name="sequence">hibernate_id</param>
</generator>
```

<param name="sequence">hibernate_id</param> 指定sequence的名称
Hibernate生成主键时，查找sequence并赋给主键值，主键值由数据库生成，Hibernate不负责维护，使用时必须先创建一个sequence，如果不指定sequence名称，则使用Hibernate默认的sequence，名称为hibernate_sequence，前提要在数据库中创建该sequence。
特点：只能在支持序列的数据库中使用，如Oracle。

7. native  
   native 由 hibernate 根据使用的数据库自行判断采用 identity、hilo、sequence 其中一种作为主键生成方式，灵活性很强。如果能支持 identity 则使用 identity，如果支持 sequence 则使用 sequence。  
   例如 MySQL 使用 identity，Oracle 使用 sequence  
   注意：如果 Hibernate 自动选择 sequence 或者 hilo，则所有的表的主键都会从 Hibernate 默认的 sequence 或 hilo 表中取。并且，有的数据库对于默认情况主键生成测试的支持，效率并不是很高。  
   使用 sequence 或 hilo 时，可以加入参数，指定 sequence 名称或 hi 值表名称等，如

<param name="sequence">hibernate_id</param>
特点：根据数据库自动选择，项目中如果用到多个数据库时，可以使用这种方式，使用时需要设置表的自增字段或建立序列，建立表等。

8. uuid  
   UUID：Universally Unique Identifier，是指在一台机器上生成的数字，它保证对在同一时空中的所有机器都是唯一的。按照开放软件基金会 (OSF) 制定的标准计算，用到了以太网卡地址、纳秒级时间、芯片 ID 码和许多可能的数字，标准的 UUID 格式为：  
   xxxxxxxx-xxxx-xxxx-xxxxxx-xxxxxxxxxx (8-4-4-4-12)  
   其中每个 x 是 0-9 或 a-f 范围内的一个十六进制的数字。  
   Hibernate 在保存对象时，生成一个 UUID 字符串作为主键，保证了唯一性，但其并无任何业务逻辑意义，只能作为主键，唯一缺点长度较大，32 位（Hibernate 将 UUID 中间的“-”删除了）的字符串，占用存储空间大，但是有两个很重要的优点，Hibernate 在维护主键时，不用去数据库查询，从而提高效率，而且它是跨数据库的，以后切换数据库极其方便。  
   特点：uuid 长度大，占用空间大，跨数据库，不用访问数据库就生成主键值，所以效率高且能保证唯一性，移植非常方便，推荐使用。

9. guid  
   GUID：Globally Unique Identifier 全球唯一标识符，也称作 UUID，是一个 128 位长的数字，用 16 进制表示。算法的核心思想是结合机器的网卡、当地时间、一个随即数来生成 GUID。从理论上讲，如果一台机器每秒产生 10000000 个 GUID，则可以保证（概率意义上）3240 年不重复。  
   Hibernate 在维护主键时，先查询数据库，获得一个 uuid 字符串，该字符串就是主键值，该值唯一，缺点长度较大，支持数据库有限，优点同 uuid，跨数据库，但是仍然需要访问数据库。  
   注意：长度因数据库不同而不同  
   MySQL 中使用 select uuid() 语句获得的为 36 位（包含标准格式的“-”）  
   Oracle 中，使用 select rawtohex(sys_guid()) from dual 语句获得的为 32 位（不包含“-”）  
   特点：需要数据库支持查询 uuid，生成时需要查询数据库，效率没有 uuid 高，推荐使用 uuid。

10. foreign  
    使用另外一个相关联的对象的主键作为该对象主键。主要用于一对一关系中。

```xml
<id name="id" column="id">
    <generator class="foreign">
        <param name="property">user</param>
    </generator>
</id>
<one-to-one name="user" class="domain.User" constrained="true" />
```

该例使用 domain.User 的主键作为本类映射的主键。  
特点：很少使用，大多用在一对一关系中。。

2.普通属性（property）  
 开发人员可以打开网址：<http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd>  
来查看 hibernate3.0 的 dtd 信息，可看到 property 的定义如下：

<!ELEMENT property (meta*,(column|formula)*,type?)>

                    <!ATTLIST property name CDATA #REQUIRED>
                    <!ATTLIST property node CDATA #IMPLIED>
                    <!ATTLIST property access CDATA #IMPLIED>
                    <!ATTLIST property type CDATA #IMPLIED>
                    <!ATTLIST property column CDATA #IMPLIED>
                    <!ATTLIST property length CDATA #IMPLIED>
                    <!ATTLIST property precision CDATA #IMPLIED>
                    <!ATTLIST property scale CDATA #IMPLIED>
                    <!ATTLIST property not-null (true|false) #IMPLIED>
                    <!ATTLIST property unique (true|false) "false">
                    <!ATTLIST property unique-key CDATA #IMPLIED>
                    <!ATTLIST property index CDATA #IMPLIED>                                                                                  <!-- include the columns spanned by this property in an index -->
                    <!ATTLIST property update (true|false) #IMPLIED>
                    <!ATTLIST property insert (true|false) #IMPLIED>
                    <!ATTLIST property optimistic-lock (true|false) "true">          <!-- only supported for properties of a class (not component) -->
                    <!ATTLIST property formula CDATA #IMPLIED>
                    <!ATTLIST property lazy (true|false) "false">
    <!ATTLIST property generated (never|insert|always) "never">
       它的各属性中比较常用的有：name（对应的java类的属性名称）、column（对应的表中的字段）、tyope（属性的类型，eg.java.lang.String）、not-null（设置该属性是否为空，为true时表示非空，默认为false）和length(字段的长度限制)。

Eg1. <property name="accessname" column="accessName" type="java.lang.String" not-null="true" />  
Eg2. <property name="state" column="state" type="java.lang.Byte" not-null="true" />  
Eg3. <property name="description" column="description" type="java.lang.String" />

3.一对多关系（`<many-to-one…/>和<set…></set>`）  
 一对多关系一般是用在一个表与另一个表存在外键关联的时候，例如用户表的组织 id 与组织表存在外键关联，则“一”方为组织表，“多”方为用户表，因为一个组织可以包含多个用户，而一个用户只能隶属于一个组织。  
对于存在一对多关系和多对一关系的双方，需要在…hbm.xml 中进行相应配置，这时在“一”方（例如：组织）需要在映射文件中添加<set…></set>元素，因为它包含多个“多”方的对象，一般的格式如下：

```xml
<set name="java映射类中对应的属性" inverse="true" lazy="true">
<key column="表中对应字段"/>
<one-to-many class="多方的类"/>
</set>
```

“多”方（例如：用户）隶属于一个“一”方对象，一般的格式如下：  
<many-to-one name="java映射类中对应的属性" column="表中对应字段" class="类名" not-null="true" />

4.一对一关系（`<one-to-one…/>`）  
一对一关系相对一对多关系来说比较少见，但也在某些情况下要用到，例如有一个用户的基本信息表（USER）和一个用户的密码表（PASSWD）就存在一对一的关系。下面来看一下一对一关系在 Hibernate 的配置。  
其中主表（eg. 用户的基本信息表）的配置如下：

```xml
<one-to-one name="主表对象中子表对象的属性名" class="子表对象的类名" cascade="save-update"/>
```

子表（eg. 用户的密码表）的配置如下：

```xml
<one-to-one name="子表对象中主表对象的属性名" class="主表对象的类名" constrained="true" />
```

5.多对多关系（<many-to-many…/>）  
在数据库设计时，一般将多对多关系转换为两个一对多（或多对一）关系，例如在基于角色的权限系统中，用户和角色存在的关系就是典型的多对多关系，即一个用户可以具有多个角色，而一个角色又可以为多个用户所有，一般在设计时，都会加一个用户与角色的关联表，该表与用户表以及角色表都存在外键关联。  
在本小节中讲述的是没有分解的多对多关系在 Hibernate 中如何配置。设置格式如下：

```xml
<set name="java对象的属性名" table="表名" cascade="all" outer-join="false">
<key column="表的对应字段"/>
<many-to-many class="另一个表的对象类" column="另一个表的字段"/>
</set>
```

6.完整实例  
在本小节中举一些.hbm.xml 映射文件的例子，让开发人员对其有一个感性的认识。接下来讲述一个用户表（tbl_user）、用户与角色关联表（tbl_user_role）、角色表（tbl_role）以及组织表（tbl_organization）的例子。

（1）tbl_user

```xml
<?xml version="1.0" encoding='UTF-8'?>
<!DOCTYPE hibernate-mapping PUBLIC
 "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
"http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd" >
<hibernate-mapping package="com.amigo.dao.pojo">
    <class name="User" table="tbl_user">
        <id name="loginname" column="loginName" type="java.lang.String">
            <generator class="assigned"/>
        </id>
        <property name="name" column="name" type="java.lang.String" not-null="true" />
        <property name="password" column="password" type="java.lang.String" not-null="true" />
        <property name="mobile" column="mobile" type="java.lang.String" />
        <property name="telephone" column="telephone" type="java.lang.String" />
        <property name="email" column="email" type="java.lang.String" />
        <property name="createtime" column="createTime" type="java.util.Date" not-null="true" />
        <property name="lastlogintime" column="lastLoginTime" type="java.util.Date" />
        <property name="logintimes" column="loginTimes" type="java.lang.Long" not-null="true" />
        <property name="state" column="state" type="java.lang.Byte" not-null="true" />
        <property name="description" column="description" type="java.lang.String" />
        <many-to-one name="organization" column="orgId" class="Organization" not-null="true" />
        <set name="userRoleSet" inverse="true" cascade="all-delete-orphan" lazy="true">
            <key column="loginName"/>
            <one-to-many class="UserRole"/>
        </set>
</hibernate-mapping>
```

（2）tbl_organization

```xml
<?xml version="1.0" encoding='UTF-8'?>
<!DOCTYPE hibernate-mapping PUBLIC
"-//Hibernate/Hibernate Mapping DTD 3.0//EN"
"http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd" >
<hibernate-mapping package="com.amigo.dao.pojo">
    <class name="Organization" table="tbl_organization">
        <id name="orgid" column="orgId" type="java.lang.Long">
            <generator class="native"/>
        </id>
        <property name="parentorgid" column="parentOrgId" type="java.lang.Long" not-null="true" />
        <property name="orgname" column="orgName" type="java.lang.String" not-null="true" />
        <property name="orgfullname" column="orgFullName" type="java.lang.String" />
        <property name="orglevel" column="orgLevel" type="java.lang.Integer" not-null="true" />
        <property name="state" column="state" type="java.lang.Byte" not-null="true" />
        <property name="description" column="description" type="java.lang.String" />
        <property name="creator" column="creator" type="java.lang.String" />
        <property name="createtime" column="createTime" type="java.util.Date" />
        <set name="userSet" inverse="true" lazy="true">
            <key column="orgId"/>
            <one-to-many class="User"/>
        </set>
    </class>
</hibernate-mapping>
```

（3）tbl_user_role

```xml
<?xml version="1.0" encoding='UTF-8'?>
<!DOCTYPE hibernate-mapping PUBLIC
"-//Hibernate/Hibernate Mapping DTD 3.0//EN"
"http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd" >
<hibernate-mapping package="com.cotel.netvote.dao.model">
    <class name="UserRole" table="tbl_user_role">
        <id name="urid" column="urId" type="java.lang.Integer">
            <generator class="native"/>
        </id>
        <many-to-one name="role" column="roleId" class="Role" not-null="true" />
        <many-to-one name="user" column="loginName" class="User" not-null="true" />
    </class>
</hibernate-mapping>
```

（4）`tbl_role`

```xml
<?xml version="1.0" encoding='UTF-8'?>
<!DOCTYPE hibernate-mapping PUBLIC
"-//Hibernate/Hibernate Mapping DTD 3.0//EN"
 "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd" >
<hibernate-mapping package="com.cotel.netvote.dao.model">
    <class name="Role" table="tbl_role">
        <id name="roleid" column="roleId" type="java.lang.Integer">
            <generator class="native"/>
        </id>
        <property name="rolename" column="roleName" type="java.lang.String" not-null="true" />
        <property name="createdate" column="createDate" type="java.util.Date" not-null="true" />
        <property name="description" column="description" type="java.lang.String" />
        <set name="userRoleSet" inverse="true" lazy="true" cascade="all">
            <key column="roleId"/>
            <one-to-many class="UserRole"/>
        </set>
    </class>
</hibernate-mapping>
```

```xml
<!--标准的XML文件的起始行，version='1.0'表明XML的版本，encoding='gb2312'表明XML文件的编码方式-->
                <?xml version='1.0' encoding='gb2312'?>
<!--表明解析本XML文件的DTD文档位置，DTD是Document Type Definition 的缩写,即文档类型的定义,XML解析器使用DTD文档来检查XML文件的合法性。hibernate.sourceforge.net/hibernate-configuration-3.0dtd可以在Hibernate3.1.3软件包中的src\org\hibernate目录中找到此文件-->
<!DOCTYPE hibernate-configuration PUBLIC
          "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
          "http://hibernate.sourceforge.net/hibernate-configuration-3.0.dtd">
    <!--声明Hibernate配置文件的开始-->
    <hibernate-configuration>
    <!--表明以下的配置是针对session-factory配置的，SessionFactory是Hibernate中的一个类，这个类主要负责保存HIbernate的配置信息，以及对Session的操作-->
      <session-factory>
      <!--配置数据库的驱动程序，Hibernate在连接数据库时，需要用到数据库的驱动程序-->
          <property name="hibernate.connection.driver_class">com.mysql.jdbc.Driver </property>
      <!--设置数据库的连接url:jdbc:mysql://localhost/hibernate,其中localhost表示mysql服务器名称，此处为本机，    hibernate是数据库名-->
            <property name="hibernate.connection.url">jdbc:mysql://localhost/hibernate </hibernate>
    <!--连接数据库是用户名-->
          <property name="hibernate.connection.username">root </property>
          <!--连接数据库是密码-->
          <property name="hibernate.connection.password">123456 </property>
          <!--数据库连接池的大小-->
          <property name="hibernate.connection.pool.size">20 </property>
        <!--是否在后台显示Hibernate用到的SQL语句，开发时设置为true，便于差错，程序运行时可以在Eclipse的控制台显示Hibernate的执行Sql语句。项目部署后可以设置为false，提高运行效率-->
        <property name="hibernate.show_sql">true </property>
        <!--jdbc.fetch_size是指Hibernate每次从数据库中取出并放到JDBC的Statement中的记录条数。Fetch Size设的越大，读数据库的次数越少，速度越快，Fetch Size越小，读数据库的次数越多，速度越慢-->
        <property name="jdbc.fetch_size">50 </property>
        <!--jdbc.batch_size是指Hibernate批量插入,删除和更新时每次操作的记录数。Batch Size越大，批量操作的向数据库发送Sql的次数越少，速度就越快，同样耗用内存就越大-->
        <property name="jdbc.batch_size">23 </property>
        <!--jdbc.use_scrollable_resultset是否允许Hibernate用JDBC的可滚动的结果集。对分页的结果集。对分页时的设置非常有帮助-->
        <property name="jdbc.use_scrollable_resultset">false </property>
        <!--connection.useUnicode连接数据库时是否使用Unicode编码-->
        <property name="Connection.useUnicode">true </property>
        <!--connection.characterEncoding连接数据库时数据的传输字符集编码方式，最好设置为gbk，用gb2312有的字符不全-->
    <property name="connection.characterEncoding">gbk </property>

        <!--hibernate.dialect 只是Hibernate使用的数据库方言,就是要用Hibernate连接那种类型的数据库服务器。-->
          <property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect </property>
        <!--指定映射文件为“hibernate/ch1/UserInfo.hbm.xml”-->
          <mapping resource="org/mxg/UserInfo.hbm.xml">
  </session-factory>
  </hibernate-configuration>



  <bean id="dataSource"
  class="org.apache.commons.dbcp.BasicDataSource"
  destroy-method="close">
//连接驱动
  <property name="driverClassName" value="${jdbc.driverClassName}" />
//连接url,
<property name="url" value="${jdbc.url}" />
//连接用户名
  <property name="username" value="${jdbc.username}" />
//连接密码
  <property name="password" value="${jdbc.password}" />
</bean>

<bean id="hbSessionFactory"
  class="org.springframework.orm.hibernate3.annotation.AnnotationSessionFactoryBean">
  <property name="dataSource" ref="dataSource" />
  <property name="configLocation">
//hibernate配置文件位置
  <value>WEB-INF/hibernate.cfg.xml </value>
  </property>
  <property name="configurationClass"
  value="org.hibernate.cfg.AnnotationConfiguration" />
  <property name="hibernateProperties">
  <props>
  //针对oracle数据库的方言,特定的关系数据库生成优化的SQL
    <prop key="hibernate.dialect">
    org.hibernate.dialect.OracleDialect
    </prop>
  //选择HQL解析器的实现
    <prop key="hibernate.query.factory_class">
    org.hibernate.hql.ast.ASTQueryTranslatorFactory
    </prop>
    //是否在控制台打印sql语句
    <prop key="hibernate.show_sql">true </prop>
    //在Hibernate系统参数中hibernate.use_outer_join被打开的情况下,该参数用来允许使用outer join来载入此集合的数据。
    <prop key="hibernate.use_outer_join">true </prop>
  //默认打开，启用cglib反射优化。cglib是用来在Hibernate中动态生成PO字节码的，打开优化可以加快字节码构造的速度
  <prop key="hibernate.cglib.use_reflection_optimizer">true </prop>
  //输出格式化后的sql,更方便查看
  <prop key="hibernate.format_sql">true </prop>
  //“useUnicode”和“characterEncoding”决定了它是否在客户端和服务器端传输过程中进行Encode，以及如何进行Encode
  <prop key="hibernate.connection.useUnicode">true </prop>
  //允许查询缓存, 个别查询仍然需要被设置为可缓存的.
  <prop key="hibernate.cache.use_query_cache">false </prop>
  <prop key="hibernate.default_batch_fetch_size">16 </prop>
    //连接池的最大活动个数
    <prop key="hibernate.dbcp.maxActive">100 </prop>
  //当连接池中的连接已经被耗尽的时候，DBCP将怎样处理(0 = 失败,1 = 等待,2  =  增长)
    <prop key="hibernate.dbcp.whenExhaustedAction">1 </prop>
    //最大等待时间
    <prop key="hibernate.dbcp.maxWait">1200 </prop>
    //没有人用连接的时候，最大闲置的连接个数
    <prop key="hibernate.dbcp.maxIdle">10 </prop>
    ##以下是对prepared statement的处理，同上。
    <prop key="hibernate.dbcp.ps.maxActive">100 </prop>
    <prop key="hibernate.dbcp.ps.whenExhaustedAction">1 </prop>
    <prop key="hibernate.dbcp.ps.maxWait">1200 </prop>
    <prop key="hibernate.dbcp.ps.maxIdle">10 </prop>
  </props>
  </property>
</bean>
```
