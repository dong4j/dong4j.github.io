---
title: 奇数性
keywords:
  - Java
categories:
  - Java
tags:
  - Java
abbrlink: 2363f1e9
date: 2012-05-19 00:00:00
---

下面的方法意图确定它那唯一的参数是否是一个奇数. 这个方法能够正确运转吗?

```java
import javax.swing.JOptionPane;
public class Test1 {
    public static void main(String[] args) {
        String s = JOptionPane.showInputDialog("请输入一个整数");
        int a = Integer.parseInt(s);
        System.out.println(a);
        if (isOdd(a))
            System.out.println("奇数");
        else {
            System.out.println("偶数");
        }
    }

    public static boolean isOdd(int i) {
        return i % 2 == 1;
    }
}
```

结果:

1. 当输入正整数时, 可以正确判断奇偶性;
2. 当输入负整数时, 结构都为 false;

解释:  
% 这个运算符的结果, 是根据前一个数值的正负性来判断, 如果是负数, 结果就是负数; 所以当输入的值是负数时, 结果都是负数, 返回的结果是 false;

改进:

1. 只要 `i % 2` 的结果不为零, i 就是一个奇数;

```java
public static boolean isOdd(int i) {
        return i % 2 != 0;
}
```

2. 用按位于 (&) 运算符 `i & 1` 结果如果为 `1`, 则 `i` 为奇数, 结果为 `0`, 则 `i` 为偶数

```java
public static boolean isOdd(int i) {
        return i & 1 == 1;
}
```

**% 操作符详解:**  
如果有:  
a: int 类型  
b: 非 0 的 int 类型  
则有恒等式:`(a / b)*b + (a % b) == a;` 成立

- 如果 `a` 为正整数,`b` 为正整数; 等式成立;
- 如果 `a` 为正整数,`b` 为负整数; 为了保证等式成立,`a % b` 的结果必须为正数;
- 如果 `a` 为负整数,`b` 为正整数; 为了保证等式成立,`a % b` 的结果必须为负数;
- 如果 `a` 为负整数,`b` 为负整数; 为了保证等式成立,`a % b` 的结果必须为负数;

由此可以得出, % 运算符得出的结果都是根据 `%` 前面的数值的正负性给定结果的正负性.
