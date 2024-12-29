---
title: 数学运算类和包装类
keywords:
  - Java
categories:
  - Java
tags:
  - Java
abbrlink: 5d1ffcf3
date: 2012-05-25 00:00:00
---

### Math 类

Math 类中所有的属性和方法都是静态的, 也就是说全露都可以可用 Math. 属性和 Math. 方法名调用属性和方法.

- 属性
- `static double E`: 比任何值都接近 e 的 double 值
- `static double PI`: 比任何值都接近 pi 的 double 值
- 几个常用的方法
  - `ceil(double a)` : 返回大于等于这个参数的整数
    - Math.ceil(-12.1) 返回 - 12 ; Math.ceil(12.8) 返回 13;
  - `floor(double a)`: 返回小于等于参数的整数;
    - Math.floor(-12.1) 返回 - 13;Math.floor(12.9) 返回 12;
  - `rint(double a)`: 返回接近参数并等于某一整数的 double 值
    - Math.floor(-12.1) 返回 - 12;Math.floor(12.9) 返回 13;
  - `random()`: 返回 `[0,1)` 之间的 double 值;

### 随机数

获得随机数的 3 种方法

1. 通过 `System.currentTimeMillis()` 获取当前时间毫秒数的 long 型数字作为随机数
2. 使用 `Math.random()`
3. 通过 `Random` 类产生一个随机数
   - `Random r = new Random()`
     - 默认使用当前时间 `System.currentTimeMillis()` 作为生成器的种子, 每次产生的随机数都不同
   - `Random r1 = new Random(10)`
     - 使用固定的种子, 每次生成的随机数都相同

### 包装类

为了贯彻执行 **一切皆是对象** 的指导方针, 对于不是对象的 8 种基本类型, 我们也要想办法给他们找对象, 所以包装类这个媒婆就出现了.

| 基本数据类型 |    包装类 |
| :----------- | --------: |
| boolean      |   Boolean |
| byte         |      Byte |
| char         | Character |
| short        |     Short |
| int          |   Integer |
| long         |      Long |
| float        |     Float |
| double       |    Double |

值得注意的是:

- 所有包装类都是 final 类型, 不能创建子类;
- 包装类是不可变的, 一旦创建了一个包装类对象, 那么它包含的基本类型数据就不能改变

#### 基本数据类型, 包装类和 String 类之间的转换

**基本 转 包装**

1. 自动装箱;  
   `Integer in = 10;`
2. 调用包装类的带参构造方法;  
   `Integer in = new Integer(10);`
3. 调用包装内的静态方法 valueOf(int i)  
   `int a = Integer.valueOf(10);`

**包装 转 基本**

1. 自动拆包;  
   `Integer in = 10;`  
   `int a = in;`
2. 调用包装类对象的 xxxValue() 方法;  
   `Integer in = 10;`  
   `int a = in.intValue();`

**基本类型 转 String**

```java
int a = 10;
String str = "" ;
```

1. 用 “+”;  
   `str = str + a;`
2. 用包装类的工具类转换成对象, 然后用对应包装类的 toString(变量) 转;  
   `new Integer(a).toString();`  
   或者  
   `Integer.toString(a);`

**String 转 基本类型**

```java
String s = "12345";
int a = Integer.parseInt(s);
```

**String 转 包装类**

1. 调用包装类的带参构造

```java
String str = "200";
Integer in  = new Integer(str);
```

2. 调用包装类的 valueOf() 方法  
   `Integer in = Integer.valueOf(str);`

**包装类 转 String**

```java
Integer in = new Integer(10);
String s = "";
```

`s = in.toString();`
