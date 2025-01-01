---
title: Java编程基础：类型转换和操作技巧详解
keywords:
  - Java
categories:
  - Java
tags:
  - Java编程
  - 条件运算符
  - 字符转换
  - 加法操作符
  - 变量交换
abbrlink: eee067eb
date: 2012-05-30 00:00:00
ai:
  - 本文主要讲述了Java编程中的几种基本数据类型转换和操作。首先，通过实例详细解释了条件表达式的类型转换过程以及在不同场景下的输出结果，并强调了在执行打印语句时对类型适配的操作。接着，介绍了加法运算符和连字符在不同类型之间的行为差异，特别提到了int类型的自动提升机制以兼容较小的数据类型如char或byte。最后，文章探讨了一种不使用临时变量来交换两个整数的技巧，并指出了一种常见的替代方法可能引发的数值溢出问题，提供了对数据范围限制的理解。
description: 本文主要讲述了Java编程中的几种基本数据类型转换和操作。首先，通过实例详细解释了条件表达式的类型转换过程以及在不同场景下的输出结果，并强调了在执行打印语句时对类型适配的操作。接着，介绍了加法运算符和连字符在不同类型之间的行为差异，特别提到了int类型的自动提升机制以兼容较小的数据类型如char或byte。最后，文章探讨了一种不使用临时变量来交换两个整数的技巧，并指出了一种常见的替代方法可能引发的数值溢出问题，提供了对数据范围限制的理解。
---

1. 看代码说结果:

```java
public static void main(String[] args){
    char x = ‘b’;
    int i = 0;
1.  System.out.println(true?x:0); //这个0是short类型
2.  System.out.println(true?x:1111111110);
3.  System.out.println(false?i:x);
}
```

**要类型转换**  
**直接写出的 0 是 short 类型**

> b  
> 98  
> 98

解释:  
条件运算符的 3 个核心要点

- 如果第二个和第三个操作数具有相同的类型, 那么他就是条件表达式的类型.
- 如果一个操作数的类型是 byte,shotr 或 char, 而另一个操作数类型是 int 的常量表达式, 条件表达式的值是可以用类型 byte,short 或 char 表示的,
- 否则, 将操作数类型运用二进制数字提升 (向上转型), 二表达式的类型就是第二个和第三个操作数提升后的类型

1. `System.out.println(true?x:0);`  
   对于语句 1 中的条件表达式, 第二个操作数是 char 类型, 第三个操作数是一个整型常量, 符合核心要点的第二点.  
   其实这里的常量 0, 实质是一个 short 类型的常量, 和 char 类型一样都占 2 个字节, 所以不会发生转型.  
   当执行 print 语句的时候, 将调用 PrintStream.print(char) 这个被重载的方法, 输出 b
2. `System.out.println(true?x:1111111110);`  
   这条语句同样适用于核心要点的第二点, 将调用 PrintStream.print(long) 方法, 输出 98
3. `System.out.println(false?i:x)`  
   因为 x 是 int 类型的, 所以必定放生向上转型, char 自动转型为 int i 的值变为 98, 调用 PrintStream.print(int) 方法, 输出 98.

## “+” 运算符和 “+=” 运算符

```java
char a = 'A';
1. a = a + 1;//报错
2. a += 1;
```

1.`a = a + 1;//报错`  
这条语句为什么会报错?  
在 Java 编程思想中有这样一句话

> 加号的唯一作用就是将较小数据类型的操作数提升为 **int**

这句话我们可以的得知, 只要是比 int 小的基本数据类型, 用加号与一个整数常量连接的时候, 会被自动转型为 int, 这也是为什么 `a = a + 1` 会报 _int 类型不能转换成 char 类型 _ 的原因了

2.`a += 1;`  
为什么这句有没有报错?  
因为 += 运算符存在隐式强转, 这条语句等价于:  
`a = (char)((int)a + 1 )`

## 交换值的问题

有 a,b 个 int 类型的变量, 要求不通过临时变量交换 2 个变量的值

```java
public class Change{
    public static void main(String[] args){
        int a = 7;
        int b = 5;
        a = a ^ b;
        b = b ^ a;
        a = a ^ b;
        System.out.println(a + "  " + b);
    }
}
```

这种方法是最正确也是最高效的

另一种方法

```java
a = a + b ;
b = a - b ;
a = a - b ;
```

这种方法看似可以, 但是却不正确, 因为没有考虑到数据溢出问题  
题上并没有说 a 和 b 的值有多大,  
a 和 b 都是 int 类型, 最大存储范围为 `2147483647` 到 `-2147483648`

```java
class Test {
    public static void main(String[] args) {
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);
    }
}
```

问题出在 `a = a + b;`  
如果当 `a+b` 的值大于了 `2147483647` 就会发生数据溢出, 从而导致后面的语句得不到正确的值.
