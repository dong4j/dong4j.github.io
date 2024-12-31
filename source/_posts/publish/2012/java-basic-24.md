---
title: 了解 MySQL
keywords:
  - Java
categories:
  - Java
tags:
  - MySQL
  - 数据库管理
  - SQL命令
  - 数据操作
  - 备份恢复
abbrlink: 329422b3
date: 2012-06-02 00:00:00
ai:
  - 本段提供了MySQL数据库管理系统中关于表创建、修改和数据操作的基本命令解释与示例。包括如何创建表、插入记录、更新、删除以及对字段属性、表名、数据引擎等进行调整。此外，还涵盖了表结构查询、备份和恢复数据库的方法，以及导出整个数据库的流程。
description: 本段提供了MySQL数据库管理系统中关于表创建、修改和数据操作的基本命令解释与示例。包括如何创建表、插入记录、更新、删除以及对字段属性、表名、数据引擎等进行调整。此外，还涵盖了表结构查询、备份和恢复数据库的方法，以及导出整个数据库的流程。
---

![20241229154732_BzwGJwS3.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_BzwGJwS3.webp)

- 表头 (header): 每一列的名称;
- 列 (row): 具有相同数据类型的数据的集合;
- 行 (col): 每一行用来描述某个人 / 物的具体信息;
- 值 (value): 行的具体信息, 每个值必须与该列的数据类型相同;
- 键 (key): 表中用来识别某个特定的人或物的方法, 键的值在当前列中具有唯一性

### SQL 语句的分类

- DQL 查询语句 select
- DML 操作语句 insert update delete
- DDL 定义语句 create alter drop truncate
- DCL 控制语句 grant revoke
- 实务控制语句 commit rollback savepoint

### MySQL 服务的启动、停止与卸载

在 Windows 命令提示符下运行:  
启动: net start MySQL  
停止: net stop MySQL  
卸载: sc delete MySQL

### MySQL 的登录

#### MySQL 参数

| 参数                 |               描述 |
| :------------------- | -----------------: |
| -D, –fatabase = name |     打开指定数据库 |
| –delimiter = name    |         指定分隔符 |
| -h, –host = name     |         服务器名字 |
| -p, –password[=name] |               密码 |
| -P, –port=#          |             端口号 |
| –prompt=name         |         设置提示符 |
| -u, –user=name       |             用户名 |
| -V, –version         | 输出版本信息并退出 |

![20241229154732_mIOdOceD.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_mIOdOceD.webp)

如果登录本地服务器, 则可以不写端口号和 IP 地址

#### cmd 登录 mysql

> mysql -h 主机名 -u 用户名 -p (回车)

##### 登录时选择使用哪个数据库

> mysql -D 选择的数据库名 -h 主机名 -u 用户名 -p

- h : 该命令用于指定客户端所要登录的 MySQL 主机名, 登录当前机器该参数可以省略;
- u : 所要登录的用户名;
- p : 告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项

#### 修改 MySQL 提示符

- 连接客户端时通过参数指定

> mysql -uroot - p –prompt 提示符

![20241229154732_11dDPovH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_11dDPovH.webp)

`--prompt` 后面跟的 `\h` 参数表示服务器名字

- 连上客户端后通过 `prompt` 命令

> mysql > prompt 提示符

![20241229154732_DKXsoFjh.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_DKXsoFjh.webp)

提示符从原来的 `loaclhost` 变成了 `mysql>`

- 或者 `\R`

> mysql > `\R` 提示符

![20241229154732_uzTrtuvG.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_uzTrtuvG.webp)

参看 mysql 的命令知道:

> prompt (`\R`) Change your mysql prompt.

可以使用 `\R` 代替 `prompt`

我们也可以使用提示符参数来增加提示符信息

##### Mysql 提示符

| 参数 |       描述 |
| :--- | ---------: |
| `\D` | 完整的日期 |
| `\d` | 当前数据库 |
| `\h` | 服务器名称 |
| `\u` |   当前用户 |

![20241229154732_ZnBVWt71.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_ZnBVWt71.webp)

使用 `\d` 参数时, 必须使用 `use 数据库名` 切换到指定数据库  
不然会显示为 null

![20241229154732_yJ1tKd1l.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_yJ1tKd1l.webp)

### 退出 MySQL

- mysql > exit
- mysql > quit
- mysql > `\q`

### MySQL 常用命令

- 显示当前服务器版本
  - `SELECT VERSION();`
- 显示当前日期
  - `SELECT NOW();`
- 显示当前用户
  - `SELECT USER();`
- 添加管理员账户
  - `grant all on *.* to user@localhost identified by "password";`  
     ![20241229154732_nIq4S1eJ.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_nIq4S1eJ.webp)

#### 修改密码

> mysqladmin -u root -p password 新密码

执行后提示输入旧密码完成密码修改, 当旧密码为空时直接按回车键确认即可.

### MySQL 语句的规范

- 关键字与函数名称全部大写
- 数据库名称, 表名称, 字段名称小写
- SQL 语句必须以分号结尾

MySQL 也可以全程使用小写  
(为了方便查看, 本文中全部使用小写命令)

### MySQL 数据库的操作

#### 显示所有存在的数据库

> show databases;

#### 创建数据库

> create{database| schema}  
> [if not exists] db_name –如果不存在 `db_name` 这个数据库就创建 db_name 数据库  
> [defalut] character set [=] charset_name; –设置编码格式

![20241229154732_NJFvISw9.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_NJFvISw9.webp)

- **在登录的时候创建**

> mysqladmin -u root -p create demo_db

#### 删除数据库

> drop {database | schema} [if exists] db_name;

#### 使用数据库

> use 数据库名称;

显示当前选择的数据库

> select database();

## 数据类型和操作数据表

### 数据类型

数据类型指的是列, 存储过程参数, 表达式和局部变量的数据特征,  
他决定了数据的存储格式, 代表了不同的信心类型

### 整型

| 数据类型  | 字节 |
| :-------- | ---: |
| tinyint   |    1 |
| smallint  |    2 |
| mediumint |    3 |
| int       |    4 |
| bigint    |    8 |

### 浮点型

| 数据类型      | 描述                                        |
| :------------ | :------------------------------------------ |
| float[(m,d)]  | m 是数字中位数, d 是小数位数                |
| double[(m,d)] | 如果省略 m 和 d, 根据硬件允许的限制来保存值 |

### 日期类型

| 列类型    | 存储需求 | 描述                                                                     |
| :-------- | :------: | :----------------------------------------------------------------------- |
| year      |    1     | 默认存储 4 位数字                                                        |
| time      |    3     | -8385959 到 8385959                                                      |
| date      |    3     | 1000 年 1 月 1 日到 9999 年 12 月 31 日之间的日期                        |
| datetime  |    8     | 1000 年 1 月 1 日 0 点 0 分 0 秒到 9999 年 12 月 31 日 59 点 59 分 59 秒 |
| timestamp |    4     | 时间戳: 1970.1.1 到 2037 年 12.31                                        |

### 字符型

| 列类型                    | 描述                                                               |
| :------------------------ | :----------------------------------------------------------------- |
| char(m)                   | (定长) m 个字节, 0<=m<=255                                         |
| varchar(m)                | (变长) L+1 个字节, L<=m 且 0<=m<=65535                             |
| tinytext                  | L+1 个字节, L<2 的 8 次方                                          |
| text                      | L+2 个字节, L<2 的 16 次方                                         |
| mediumtext                | L+3 个字节, L<2 的 24 次方                                         |
| longtext                  | L+4 个字节, L<2 的 32 次方                                         |
| enum(‘value1’,’value2’,…) | 1 或 2 个字节, 取决于枚举值的个数 (最多 65535 个值)                |
| set(‘value1’,’value2’,…)  | (集合) 1,2,3,4 或 8 个字节, 取决于 set 成员的数目 (最多 64 个成员) |

#### 创建数据表

```
create table [if not exists] table_name(
    cloumn_name1 data_type,
    cloumn_name2 data_type,
    ...
);
```

最后一条语句不需要加 `,`;

```
create table tb1(
    username varchar(20),
    age tinyint unsigned, --无符号
    salary float(8,2) unsigned
);
```

以创建 students 表为例, 表中将存放 学号 (id)、姓名 (name)、性别 (sex)、年龄 (age)、联系电话 (tel) 这些内容:

```
create table students
（
    id int unsigned not null auto_increment primary key,
    name char(8) not null,
    sex char(4) not null,
    age tinyint unsigned not null,
    tel char(13) null default '-'
);
```

(提示: 1. 如果连接远程主机请加上 -h 指令; 2. createtable.sql 文件若不在当前工作目录下需指定文件的完整路径。)

语句解说:

- create table tablename(columns) 为创建数据库表的命令, 列的名称以及该列的数据类型将在括号内完成;

括号内声明了 5 列内容, id、name、sex、age、tel 为每列的名称, 后面跟的是数据类型描述, 列与列的描述之间用逗号 (,) 隔开;

以 “id int unsigned not null auto_increment primary key” 行进行介绍:

- “id” 为列的名称;
- “int” 指定该列的类型为 int(取值范围为 -8388608 到 8388607), 在后面我们又用 - “unsigned” 加以修饰, 表示该类型为无符号型, 此时该列的取值范围为 0 到 16777215;
- “not null” 说明该列的值不能为空, 必须要填, 如果不指定该属性, 默认可为空;
- “auto_increment” 需在整数列中使用, 其作用是在插入数据时若该列为 NULL, MySQL 将自动产生一个比现存值更大的唯一标识符值。在每张表中仅能有一个这样的值且所在列必须为索引列。
- “primary key” 表示该列是表的主键, 本列的值必须唯一, MySQL 将自动索引该列。  
   下面的 char(8) 表示存储的字符长度为 8, tinyint 的取值范围为 -127 到 128, default 属性指定当该列值为空时的默认值。

#### 参看数据表列表

> show tables [from db_name] [like ‘pattern’ | where expr];

如果直接写 `show tables` 会显示当前所选择的数据库中的所有数据表  
如果加上了 `from`, 会显示特定数据库中的表  
但是当前所在数据库的位置没有改变

#### 参看数据表结构

> show columns from tb_name;  
> 或者  
> describe (desc) tb_name;

#### 插入记录

> insert [into] tb_name [(col_name1,col_name2,…)] values(val1,val2,..);

```
insert into students values
    (1,'张三','男',25,'123467890'),
    (2,'李四','男',22,'0987654321'),
    (3,'王五','男',20,'0984324321'),
    (4,'赵六','男',29,'0944654321');
```

当只需要插入部分数据, 或者不按照顺序插入

> insert into students (name,sex,age) values(‘田七’,’男’,30);

#### 更新记录

> update students set age = 50 where name = ‘张三’;

#### 删除记录

> delete from students where id > 1; –删除 ID 大于 1 的所有记录
>
> delete from students where id = 10 limit 1 –限制删除掉 1 条 id=10 的记录
>
> delete from students; –删除全表记录
>
> drop table tablename1, tablename2, ….; –删除多个表

#### 更改表名

> alter table t1 rename t2;

#### 修改字段属性

> alter table tablename modify int(10) unsigned auto_increment primary key not null;

#### 修改默认值

> alter table tablename alter id default 0;

#### 给字段添加主键

> alter table tablename add primary key(id);

#### 删除主键

> alter table tablename drop primary key;

或者

> drop primary key on tablename;

#### 修改表数据引擎

> alter table tablename ENGINE = MyISAM(InnoDB);

#### 增加新字段 (列)

> alter table tablename add column single char(1);

或者

> alter table tablename add field int unsigned not null;

#### 数据的备份和恢复

##### 备份

> mysqldump -u root -p demo_db students > `C:\Users\CodeA\Desktop\abc.sql`

##### 恢复

进入 mysql

> create database school;  
> use school;  
> source school.sql;

##### 导出数据库

mysqldump –databases db1 db2 >db1.db2.sql;
