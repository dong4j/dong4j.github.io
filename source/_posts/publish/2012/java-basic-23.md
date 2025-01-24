---
title: 轻松掌握Java Properties文件操作，从入门到实践
keywords:
  - Java
  - Properties
  - 持久化
  - 文件读写
categories:
  - 新时代码农
tags:
  - Java
  - Properties
  - 持久化
  - 文件读写
abbrlink: c89e3217
date: 2012-06-01 00:00:00
ai:
  - Properties 类在Java中用于持久化保存属性集，支持从流读取和写入文件。通过 load() 方法可以从输入流加载属性列表，使用 getProperty()
    和 getProperty(String, String) 查询属性，setProperty(String, String) 设置或更新属性值，store(OutputStream,
    String) 将属性集合存储到输出流中。Properties 类可以用于多种场景，如配置文件的读取和写入、用户设置保存等。
description: Properties 类在Java中用于持久化保存属性集，支持从流读取和写入文件。通过 load() 方法可以从输入流加载属性列表，使用
  getProperty() 和 getProperty(String, String) 查询属性，setProperty(String, String) 设置或更新属性值，store(OutputStream,
  String) 将属性集合存储到输出流中。Properties 类可以用于多种场景，如配置文件的读取和写入、用户设置保存等。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

`public class Propertiesextends Hashtable<Object,Object>`  
Properties 类表示了一个持久的属性集。Properties 可保存在流中或从流中加载。属性列表中每个键及其对应值都是一个字符串。  
新建一个文件  
内容为  
键 1 = 值 1  
键 2 = 值 2  
…

使用此类可以对文件数据进行持久化保存

### 方法的使用

- `load(InputStream inStream);` 从输入流中读取属性列表（键和元素对）。

```
Properties pro = new Properties();
pro.load(new FileInputStream(相对路径或绝对路径));//此方法将抛出FileNotFoundException
```

- `getPropertiy(String key)` 使用指定的键在此属性列表中搜索属性, 返回 String
- `getProperty(String key, String defaultValue)` 用指定的键在属性列表中搜索属性。返回 String
- `setProperty(String key, String value)` 如果存在了这个键, 则更改对应的值, 如果不存在, 则添加这个属性, 这个方法是调用 Hashtable 的 put 的结果
- `public void store(OutputStream out, String comments) throws IOException` 写入文件中

```java
props.store(new FileOutputStream(相对路径或绝对路径), 说明);
```

### Properties 综合使用

```java
import java.io.*;
import java.util.*;
public class PropertiesTest {
    static Properties props = new Properties();
    public static void main(String[] args) {
        //读文件
        Read();
        System.out.println(props.getProperty("Teacher"));
        //添加数据
        //使用setProperties()方法,如果文件中没有相同的键,则添加,如果有相同的,就覆盖
        props.setProperty("Teacher","胡老大");
        props.setProperty("Student","Code");
        System.out.println(props.getProperty("Student"));
        Save();
        //删除全部数据
        //直接在没有加载文件的情况下使用store()方法存入空数据到文件中
        Read();
        //存入Sudtent对象
        for(int i = 0 ; i < 3; i++){
            Scanner scan = new Scanner(System.in);
            System.out.println("请输入学生名字：");
            String name = scan.next();
            System.out.println("请输入学生年龄：");
            int age = scan.nextInt();
            System.out.println("请输入学生成绩");
            int score = scan.nextInt();
            Student stu = new Student(name,age,score);
            props.setProperty(stu.getName(), stu.getName() + "&" + stu.getAge() + "&" + stu.getScore());
        }
        Save();
        //删除指定的键  直接调用Map类的remove方法
        props.remove("Student");
        Save();
        //构造学生对象
        //把值取出来分解,然后赋值给学生
        //调用继承Map的values()方法,取得所有的值
        Collection<String> cl = props.values();
        for(String str : cl){
            System.out.println(str);
            //拆分字符串
        }
    }
    public static void Read(){
        try {
            props.load(new FileInputStream("data.properties"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    //存文件
    public static void Save(){
        try {
            props.store(new FileOutputStream("data.properties"), null);
        } catch (FileNotFoundException e) {
        // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
        // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```
