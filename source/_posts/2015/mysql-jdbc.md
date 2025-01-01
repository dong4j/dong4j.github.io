---
title: 轻松掌握Java数据库操作：JDBC入门
keywords:
  - MySQL
categories:
  - MySQL
tags:
  - Java
  - JDBC
  - MySQL
  - 数据库操作
  - 数据库编程
abbrlink: 5a428776
date: 2015-06-25 00:00:00
ai:
  - 本文介绍了在Java中使用JDBC进行基本数据库操作的详细指南。包括连接MySQL服务器、执行SQL语句、预处理数据等，并通过示例代码演示了如何插入、更新和删除数据。此外，还涉及了环境准备中的数据库配置属性文件以及实用工具类的实现，以封装创建和释放数据库连接的相关逻辑。
description: 本文介绍了在Java中使用JDBC进行基本数据库操作的详细指南。包括连接MySQL服务器、执行SQL语句、预处理数据等，并通过示例代码演示了如何插入、更新和删除数据。此外，还涉及了环境准备中的数据库配置属性文件以及实用工具类的实现，以封装创建和释放数据库连接的相关逻辑。
---

在 Java 中，我们可以使用 JDBC（Java Database Connectivity）来连接、查询和操作关系型数据库。以下是一个详细的指南，展示如何进行基本的数据库操作，包括连接到 MySQL 服务器、执行 SQL 语句以及预处理数据。

## 数据库操作的基本步骤：

### 1. 导入必要的包

```java
import java.sql.*;
```

### 2. 定义一个主类来初始化和测试数据库操作

#### 基本的数据库连接与查询：

首先，我们定义一些基本的变量用于存储数据库的信息。

```java
public class DataBasePractice {

    public static void main(String[] args) {
        Connection con = null;

        // MySQL驱动程序名
        String driver = "com.mysql.jdbc.Driver";
        // 数据库URL
        String url = "jdbc:mysql://localhost:3306/mydata";
        // 用户名和密码
        String user = "root";
        String password = "root";

        try {
            Class.forName(driver);

            con = DriverManager.getConnection(url, user, password);
            if (!con.isClosed()) System.out.println("Succeeded connecting to the Database!");

            Statement statement = con.createStatement();

            // SQL查询语句
            ResultSet rs = statement.executeQuery("select * from student");

            String name, id;
            while(rs.next()){
                name = rs.getString("stuname").trim();
                id = rs.getString("stuid").trim();

                // 字符集转换（如果需要的话）
                name = new String(name.getBytes("ISO-8859-1"), "gb2312");

                System.out.println(id + "\t" + name);
            }
        } catch (ClassNotFoundException e) {
            System.out.println("Sorry, can't find the Driver!");
            e.printStackTrace();
        } catch (SQLException e) {
            // 数据库连接失败异常处理
            e.printStackTrace();
        } finally{
            try{
                if(con != null)
                    con.close();
            }catch(SQLException se){
                se.printStackTrace();
            }

            System.out.println("数据库数据成功获取！！");
        }

    }
}
```

### 3. 使用`PreparedStatement`进行预处理操作

#### 插入、更新和删除数据：

```java
// 假设在主类中已经有了一个Connection con对象。
try {
    // 插入新记录到student表
    PreparedStatement psql = con.prepareStatement("insert into student values(?,?)");
    psql.setInt(1, 8);
    psql.setString(2, "xiaogang");
    psql.executeUpdate();

    // 更新数据
    psql = con.prepareStatement("update student set stuname = ? where stuid = ?");
    psql.setString(1,"xiaowang");
    psql.setInt(2, 10);
    psql.executeUpdate();

    // 删除记录
    psql = con.prepareStatement("delete from student where stuid = ?");
    psql.setInt(1, 5);
    psql.executeUpdate();

    System.out.println("执行增加、修改、删除后的数据");
    res = psql.executeQuery();
    while(res.next()){
        name = res.getString("stuname").trim();
        id = res.getString("stuid").trim();

        // 字符集转换（如果需要的话）
        name = new String(name.getBytes("ISO-8859-1"), "gb2312");

        System.out.println(id + "\t" + name);
    }
} catch (SQLException e) {
    e.printStackTrace();
}
```

## 环境准备

### 数据库配置属性文件`db.properties`

该配置文件中包含必要的数据库连接参数，如驱动名称、URL 地址等。

```properties
# Oracle 连接信息
driver=oracle.jdbc.driver.OracleDriver
url=jdbc:oracle:thin:@localhost:1521:vill
username=vill
password=villvill

# MySQL 连接信息（注释状态）
# driver=com.mysql.cj.jdbc.Driver # 使用最新MySQL驱动版本
# url=jdbc:mysql://localhost:3306/vill?useSSL=false&serverTimezone=UTC
# username=root
# password=root
```

### 实用工具类`DBUtil.java`

该类提供了一个静态的数据库连接获取方法，并在程序结束时关闭所有数据库相关资源（如连接、语句等）。

```java
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

/**
 * 数据库操作工具类，封装了创建和释放数据库连接的逻辑。
 */
public class DBUtil {

    // 静态变量用于保存从配置文件读取到的数据
    private static String driver, url, user, pwd;

    // 使用静态块初始化这些变量
    static {
        try {
            Properties properties = new Properties();
            properties.load(DBUtil.class.getClassLoader().getResourceAsStream("vill/util/db.properties")); // 加载资源路径下的属性文件
            driver = properties.getProperty("driver");
            url = properties.getProperty("url");
            user = properties.getProperty("username"); // 读取配置的用户名和密码信息
            pwd = properties.getProperty("password");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 获取与数据库建立的连接。
     *
     * @return 数据库连接对象，如果发生异常，则返回null。
     */
    public static Connection getConnection() throws Exception{
        Class.forName(driver); // 动态加载驱动
        return DriverManager.getConnection(url, user, pwd);
    }

    /**
     * 关闭所有与数据库相关的资源：包括结果集、语句和连接等。
     *
     * @param conn 数据库连接对象
     * @param stm  SQL执行语句对象
     * @param rs   查询结果集对象
     */
    public static void closeConnection(Connection conn, Statement stm, ResultSet rs) {
        try {
            if (conn != null)
                conn.close();
            if (stm != null)
                stm.close();
            if (rs != null)
                rs.close();
        } catch (Exception e) {
            // 捕获异常，防止资源释放过程中出现错误中断程序运行
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        try {
            System.out.println(new DBUtil().getConnection().getClass().getName());
        } catch (Exception e) {
            e.printStackTrace();  // 输出异常信息以便调试
        }
    }
}
```

### 实现解析

1. **配置文件读取**
   - 利用`Properties`类从资源路径中加载并解析`.properties`格式的属性文件，从而得到数据库连接所需的驱动和 URL 等参数。
2. **数据库连接获取方法**
   - `getConnection()`：首先通过反射机制动态地注册数据库驱动（如 Oracle 或 MySQL），然后使用这些配置信息建立与数据库的实际连接。
3. **资源管理**
   - 为了防止内存泄漏，`closeConnection()`提供了关闭数据库操作过程中可能打开的多种类型对象的功能。这包括但不限于`ResultSet`, `Statement`以及最后是`Connection`本身。
4. **异常处理**
   - 在`getConnection()`和`closeConnection()`方法中均存在捕获并打印错误信息的机制。这样可以确保即使在资源释放失败的情况下，程序也能继续执行，并且开发者能明确看到问题发生的位置。

### 注意事项

- 确保你的项目包含了所使用的 JDBC 驱动库（例如 Oracle 或 MySQL 的 JDBC jar 文件）。
- 配置文件`db.properties`应放置于项目的类路径中，以便通过`ClassLoader.getResourceAsStream()`正确加载。
- 建议使用 try-with-resources 语句来简化资源管理和异常处理逻辑。
