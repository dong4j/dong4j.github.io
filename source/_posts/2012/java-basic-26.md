---
title: 从零到一学习SQL：内连接与外连接实战
keywords:
  - Java
categories:
  - Java
tags:
  - 数据库
  - SQL
  - 连接查询
  - 内连接
  - 自然连接
  - 外连接（左、右）
  - 全连接
  - 子查询
abbrlink: f9bb212c
date: 2012-06-04 00:00:00
ai:
  - 数据库连接查询与子查询概述
description: 数据库连接查询与子查询概述
---

#### 聚合函数

- count 返回结果集中行的数目
- sum 返回结果集中所有值得总和
- avg 返回结果集中所有值得平均值
- max 返回结果集中所有值中最大值
- min 返回结果集中所有值中最小值

##### count

> select count([* | all | distinct] expr) from 表名;

- - : 计算所有选择的行, 包括 null
- all : 计算指定列所有的非空行, 默认选项
- distinct : 计算指定列所有唯一非空值

#### sum

> select sum([all | distinct] expr) as 别名 from 表名;

#### avg

> select avg(mark) as ‘平均成绩’ from sutdent  
> where studentID = 10;  
> 输出表 student 中 studentID 为 10 的所有 mark 的平均值

#### 最大值和最小值

```sql
select max(mark) as '最高成绩', min(mark) as '最低成绩'
from student
where examID = 6;
```

#### 常用数据库函数

[mysql 常用函数](http://www.cnblogs.com/cocos/archive/2011/05/06/2039469.html)

### 数据分组

将表按条件分组, 然后在组中查找需要的值

```sql
select 列A, 聚合函数(聚合函数规范)
from 表名
where 过滤条件
group by 列A;
```

当需要分组查询时需要使用 GROUP BY 子句，例如查询每个部门的工资和，这说明要使用部分来分组。

- 查询每个部门的部门编号和每个部门的工资和：

```sql
SELECT deptno, SUM(sal)
FROM emp
GROUP BY deptno;
```

- 查询每个部门的部门编号以及每个部门的人数：

```sql
SELECT deptno,COUNT(*)
FROM emp
GROUP BY deptno;
```

- 查询每个部门的部门编号以及每个部门工资大于 1500 的人数：

```sql
SELECT deptno,COUNT(*)
FROM emp
WHERE sal>1500
GROUP BY deptno;
```

#### HAVING 子句

- 查询工资总和大于 9000 的部门编号以及工资和

```sql
SELECT deptno, SUM(sal)
FROM emp
GROUP BY deptno
HAVING SUM(sal) > 9000;
```

##### 子句顺序问题

如果 where 在 group by 前面, 并不是从分组中查询  
如果 where 在 group by 后面, 则是从分组中查询需要的结果

select  
from  
where 条件中不能有聚合函数  
group by  
[where]  
having 条件中都是聚合函数, 就在选出的分组中再次筛选  
order by 如果需要, 最后进行排序

注意，WHERE 是对分组前记录的条件，如果某行记录没有满足 WHERE 子句的条件，那么这行记录不会参加分组；而 HAVING 是对分组后数据的约束。

#### 分页查询

LIMIT 用来限定查询结果的起始行，以及总行数。

- 查询 5 行记录，起始行从 0 开始

> `SELECT * FROM emp LIMIT 0, 5;`

注意，起始行从 0 开始，即第一行开始！

- 查询 10 行记录，起始行从 3 开始

> `SELECT * FROM emp LIMIT 3, 10;`

如果一页记录为 10 条，希望查看第 3 页记录应该怎么查呢？

- 第一页记录起始行为 0，一共查询 10 行；
- 第二页记录起始行为 10，一共查询 10 行；
- 第三页记录起始行为 20，一共查询 10 行；

查询页的下标 = `(要查询的页数 - 1) * 每页记录的行数`

### 单表查询

```sql
select 列名1[, 列名2,...]
from 数据源
[where condition];
```

- 数据源可以是表也可以是视图;
- 列名 和 where 关键字选出的行确定选择的查询结果
- 没有 where 关键字则选出所有的行
- 如果不指定选择的列, 使用 `*` 代表所有的列

#### 字符串的连接

```sql
select concat(teacher_name,'xxx')
from teacher_table;
```

在 mysql 中, 字符串和 null 连接会返回 null,  
对于其他一些数据库, 如果让字符串和 null 连接, 会把 null 当成空字符串处理

#### 去除重复行

```sql
select distinct student_name ,java_teacher
from student_table;
```

#### where 关键字

| 运算符                          | 含义                                      |
| :------------------------------ | :---------------------------------------- |
| `expr1 between expr2 and expr3` | 要求 `expr2 <= expr1 <= expr3`            |
| `expr1 in (expr2, expr3, ..)`   | 要求 `expr1` 等于括号内任意表达式的值     |
| `like`                          | 字符串匹配，`like` 后面的字符串支持通配符 |
| `is null`                       | 要求指定值等于 `null`                     |
| `=`                             | 是否相等                                  |
| `<>`                            | 不相等                                    |
| `:=`                            | 赋值                                      |

##### like 模糊匹配

SQL 支持 2 个通配符

- 下划线 `_` : 代表一个任意的字符
- 百分号 %: 代表任意多个字符

当查询中需要使用到下划线或百分号时, 可以使用 `\` 转义,  
也可使用 `escape` 关键字

```sql
select * from student_table
where student_name like '_%' escape '\';
```

##### 条件组合查询

SQL 提供了 `and` 和 `or` 来组合 2 个条件, 并提供 `not` 来对逻辑表达式求否.

```sql
select * from student_table
where stduent_name like '__' and student_id > 3;
```

##### 比较运算符和逻辑运算符的优先级

| 运算符           | 优先级 (小的优先) |
| :--------------- | :---------------: |
| 所有的比较运算符 |         1         |
| not (非)         |         2         |
| and (且)         |         3         |
| or (或者)        |         4         |

括号的优先级最高, 所以可以使用括号来改变逻辑运算符优先级

```sql
select * from student_table
where (student_id > 3 or student_name > '张') and java_teacher > 1;
```

##### 查询结果排序

查询结果默认按插入顺序排序, 如果需要查询结果按某列值得大小进行排序,  
则可以使用 `order by`

```sql
order by 列名1 [desc] ,列名2,列名3,...;
```

上面语法进行排序时可以采用列名, 列序号和列别名.

进行排序时默认进行升序排序, 如果想按降序排列, 可以写上 `desc` 关键字  
与之对应的是 `asc` 关键字

下面的语句选出 student_table 中所有的记录, 然后按 java_teacher 列的升序排列

```sql
select * from student_table
order by java_teacher;
```

如果需要按多行排序, 则每行的 asc 和 desc 必须单独指定,  
如果指定了多个排序列, 则第一个排序列是又要排序列, 只要当第一列中存在多个相同的值时, 第二列才会起作用

```sql
select * from student_table
order by java_teacher desc , student_name;
```

当 java_teacher 列的值相同时, 按照 student_name 列的升序排列.

### 多表查询

- 合并结果集
- 连接查询
  - 内连接
  - 外链接
    - 左外连接
    - 右外连接
    - 外全连接 (mysql 不支持, 使用左外, 右外结合)
  - 自然连接
- 子查询

#### 合并结果集

1. 作用: 合并结果集就是把两个 select 语句的查询结果合并到一起
2. 两种方式:

   - union: 去除重复记录

> select _ from t1 union select _ from t2;

- union all : 不去除重读记录

> select _ from t1 union all select _ from t2;

![20241229154732_Qcswql68.webp](20241229154732_Qcswql68.webp)

![20241229154732_hLYA8bVL.webp](20241229154732_hLYA8bVL.webp)

被合并的 2 个结果必须列数, 类型一致

#### 连接查询

连接查询就是求出多个表的乘积, 例如 t1 和 t2 连接, 那个查询出的结果就是 `t1*t2`

![20241229154732_iX48n3Ju.webp](20241229154732_iX48n3Ju.webp)

就这是笛卡尔积

所以查询出来的结果有重复的, 所以需要去除无用信息  
![20241229154732_K19FdTdE.webp](20241229154732_K19FdTdE.webp)

> `select * from emp,dept where emp.deptno = dept.depton;`

![20241229154732_FCkyRd8h.webp](20241229154732_FCkyRd8h.webp)

##### 内连接

标准格式:

```sql
select * from empe
inner join dept
on empe.deptno = dept.deptno;
```

###### 自然连接

```sql
select * from 表1
natural join 表2
```

系统自动找到两张连接的表中名称和类型完全一致的列

##### 外连接

###### 左外连接

先查询出左表, 然后查询右表, 右表中满足条件的显示出来, 不满足的显示为 null

```sql
SELECT * FROM emp e
LEFT OUTER JOIN dept d
ON e.deptno=d.deptno;
```

###### 右外连接

同左外连接的效果相反, 先把右表中所有的记录查出来, 然后左表满足条件的显示, 不满足的显示为 null

```sql
SELECT * FROM emp e
RIGHT OUTER JOIN dept d
ON e.deptno=d.deptno;
```

###### 外全连接

在 mysql 中实现外全连接

```sql
SELECT * FROM emp e
LEFT OUTER JOIN dept d
ON e.deptno=d.deptno;
union
SELECT * FROM emp e
RIGHT OUTER JOIN dept d
ON e.deptno=d.deptno;
```

连接不限与两张表，连接查询也可以是三张、四张，甚至 N 张表的连接查询。通常连接查询不可能需要整个笛卡尔积，而只是需要其中一部分，那么这时就需要使用条件来去除不需要的记录。这个条件大多数情况下都是使用主外键关系去除。  
两张表的连接查询一定有一个主外键关系，三张表的连接查询就一定有两个主外键关系，所以在大家不是很熟悉连接查询时，首先要学会去除无用笛卡尔积，那么就是用主外键关系作为条件来处理。如果两张表的查询，那么至少有一个主外键条件，三张表连接至少有两个主外键条件。

##### 子查询

子查询就是嵌套查询，即 SELECT 中包含 SELECT，如果一条语句中存在两个，或两个以上 SELECT，那么就是子查询语句了

1. 子查询出现的位置：

   - where 后，作为条件的一部分；
   - from 后，作为被查询的一条表;

2. 当子查询出现在 where 后作为条件时，还可以使用如下关键字：

   - any
   - all

3. 子查询结果集的形式

   - 单行单列（用于条件）:

> `select * from 表 1 where 列 1 [=,>,<,>=,<=,!=] (select 列 from 表 where 条件)`

- 单行多列（用于条件）:

> `select * from 表 where (列 1, 列 2) in (select 列 1, 列 2 from 表 where 条件)`

- 多行单列（用于条件）:

> `select * from 表 where 列 1 [in ,all ,any] (select 列 from 表 where 条件)`

- 多行多列（用于表）:

> select _ from 表 1,(select _ from …) where 条件
