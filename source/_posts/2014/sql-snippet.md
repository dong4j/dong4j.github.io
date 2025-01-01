---
title: SQL 基础：常用的 SQ操作
keywords:
  - SQL
categories:
  - 新时代码农
tags:
  - SQL
  - JOIN操作
  - CASE WHEN
  - 条件处理
  - 重复记录删除
  - 模式设置
  - XML冲突
  - 模糊查询
  - mycli
  - MyBatis
  - 动态SQL
abbrlink: ac8eb277
date: 2014-08-19 00:00:00
ai:
  - 本文介绍了SQL中连接操作、使用CASE WHEN处理条件逻辑、删除具有重复shop_id记录的方法、设置和查看SQL模式、避免XML中的<=>错误、模糊查询应用、mycli工具查询数据库以及MyBatis动态SQL的最佳实践。文章还详细阐述了如何在MyBatis中处理单个参数、多个参数、数组参数以及List参数的情况。
description: 本文介绍了SQL中连接操作、使用CASE WHEN处理条件逻辑、删除具有重复shop_id记录的方法、设置和查看SQL模式、避免XML中的<=>错误、模糊查询应用、mycli工具查询数据库以及MyBatis动态SQL的最佳实践。文章还详细阐述了如何在MyBatis中处理单个参数、多个参数、数组参数以及List参数的情况。
---

## 1. SQL 连接操作简介

在数据库查询中，`JOIN` 操作是一种非常强大的工具。它允许我们将来自不同表的数据结合起来。下面是几种常见的 `JOIN` 类型及其用途：

- **INNER JOIN**（内连接）：返回两个表中匹配的行。
- **LEFT JOIN**（左连接）：返回左表所有记录，右表无匹配时返回 NULL。
- **RIGHT JOIN**（右连接）：返回右表所有记录，左表无匹配时返回 NULL。

## 2. 使用 CASE WHEN 在 SQL 中处理条件逻辑

在 SQL 查询中，`CASE WHEN` 是一种强大的工具，它允许你在查询结果中根据特定条件添加不同的值。以下是一个示例：

```sql
SELECT *,
       CASE
           WHEN (A - B) = 0 THEN 'T'
           WHEN (A - B) < 0 THEN 'WRONG'
           ELSE CASE WHEN (A IS NULL OR B IS NULL) THEN 'F' ELSE 'T' END
       END
FROM 临时表;
```

此查询返回了原始列以及一个新列，该列基于条件 `A - B` 的值。

## 3. 删除具有重复 `shop_id` 记录的行

在某些情况下，你可能需要删除具有重复 `shop_id` 的记录。以下是一个使用子查询来查找具有多个相同 `shop_id` 的记录并删除它们的示例：

```sql
DELETE FROM ec_shop_bg_image
WHERE shop_id NOT IN (
    SELECT MAX(shop_id)
    FROM ec_shop_bg_image
    GROUP BY shop_id
    HAVING COUNT(shop_id) > 1
);
```

这段代码通过首先找到每个 `shop_id` 的最大值，然后从原表中删除除了这些最大值之外的所有记录。

## 4. 设置和查看 SQL 模式

在 MySQL 中，你可以使用 `SET sql_mode` 来设置数据库的运行模式。一个常用的模式是 `ONLY_FULL_GROUP_BY`，它要求在 `GROUP BY` 后面显式列出所有选定的列。下面是如何查看和设置这个模式的示例：

```sql
-- 查看 SQL 模式
SELECT version(), @@sql_mode;

-- 设置 SQL 模式
SET sql_mode = 'STRICT_TRANS_TABLES';
```

## 5. 在 XML 中避免 `<=>` 错误

当处理包含 SQL 语句的 XML 数据时，应使用 `<![CDATA[ ... ]]>` 来避免与 XML 标签冲突的情况。

```xml
<![CDATA[
SELECT * FROM user WHERE name = #{name};
]]>
```

## 6. 模糊查询的使用

在 SQL 中执行模糊查询时，你可以使用 `LIKE` 和 `%` 通配符来查找匹配特定模式的数据。以下是一个示例：

```sql
LIKE CONCAT('%', #{name} ,'%');
```

这个表达式会找到所有以指定名称开头的行。

## 7. 使用 mycli 工具查询数据库

`mycli` 是一个交互式命令行工具，用于连接 MySQL 数据库并执行查询。以下是如何使用 `mycli` 的示例：

```bash
mycli -h localhost -u root 数据库名
```

然后，你可以输入 SQL 查询来获取数据。

## 8. MyBatis 动态 SQL 中的 #{ } 和 ${ } 区别

在使用 MyBatis 进行动态 SQL 编写时，理解 `#{ }` 和 `${ }` 的区别非常重要。以下是它们的主要区别：

- **`#{ }`**: 解析为一个 JDBC 预编译语句（prepared statement）的参数标记符。它提供了预处理和参数替换的功能，以防止 SQL 注入。

  ```sql
  select * from user where name = #{name};
  ```

  解析为：

  ```sql
  select * from user where name = ?;
  ```

- **`${ }`**: 仅仅为一个字符串替换。在动态 SQL 解析阶段将会进行变量替换。

  ```sql
  select * from user where name = ${name};
  ```

  解析为：

  ```sql
  select * from user where name = 'ruhua';
  ```

## 9. 使用 MyBatis 动态 SQL 的最佳实践

在编写 MyBatis 动态 SQL 时，遵循以下最佳实践：

- **优先使用 `#{ }`**: 当你正在处理参数时。
- **仅当需要字符串替换时使用 `${ }`**: 例如表名或列名。

- **避免在表名作为变量时使用 `#{ }`**: 因为这会带上单引号，导致语法错误。

通过遵循这些最佳实践，你可以创建安全、高效且易于维护的动态 SQL。

## MyBatis：单个参数和多个参数的例子

在 MyBatis 中，你可以定义接口方法来执行数据库操作，并通过 XML 映射文件将这些方法映射到实际的 SQL 语句。以下是如何处理单个和多个参数的例子。

### 单个参数

假设我们有一个接口方法 `getAgeById`，它根据用户 ID 查询用户的年龄：

```java
// 接口方法
int getAgeById(Integer id);
```

对应的 XML 映射文件中的 SQL 语句如下：

```xml
<select id="getAgeById" resultType="Integer">
    select age from user where user_id = #{id}
</select>
```

### 多个参数

当需要传递多个参数时，可以使用 `@Param` 注解来指定每个参数的名称。例如，`login` 方法：

```java
// 接口方法
User login(@Param("username") String username, @Param("password") String password);
```

对应的 XML 映射文件：

```xml
<select id="login" resultMap="BaseResultMap">
    select *
    from user
    where username = #{username} and password = #{password}
</select>
```

## MyBatis 动态 SQL 处理数组参数和 List 参数

在处理数组或 List 类型的参数时，MyBatis 提供了 `foreach` 元素来构建 SQL 查询。下面是如何使用 `foreach` 来处理这两种类型的例子。

### 数组参数

如果我们有一个接口方法 `selectByIds` 接受一个整型数组作为 ID：

```java
// 接口方法
ArrayList<User> selectByIds(Integer[] ids);
```

对应的 XML 映射文件中的 SQL 语句：

```xml
<select id="selectByIds" resultMap="BaseResultMap">
    select *
    from user
    where id in
    <foreach item="item" index="index" collection="array" open="(" separator="," close=")">
        #{item}
    </foreach>
</select>
```

### List 参数

如果 `ids` 是一个 List 类型：

```java
// 接口方法
ArrayList<User> selectByIds(List<Integer> ids);
```

对应的 XML 映射文件中的 SQL 语句：

```xml
<select id="selectByIds" resultMap="BaseResultMap">
    Select
    <include refid="Base_Column_List" />
    from jria where ID in
    <foreach item="item" index="index" collection="list" open="(" separator="," close=")">
          #{item}
      </foreach>
  </select>
```
