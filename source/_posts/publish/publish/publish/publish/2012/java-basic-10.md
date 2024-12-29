---
title: 长整型
keywords:
  - Java
categories:
  - Java
tags:
  - Java
abbrlink: b0abc087
date: 2012-05-20 00:00:00
---

话说有这样一个小例子:  
MICROS_PER_DAY 表示一天的微秒数  
MILLIS_PER_DAY 表示一天的毫秒数  
然后下面例子的结果是多少呢?

```java
public class Test3 {
    public static void main(String[] args) {
        final long MICROS_PER_DAY = 24 * 60 * 60 * 1000 * 1000;
        final long MILLIS_PER_DAY = 24 * 60 * 60 * 1000;
        System.out.println(MICROS_PER_DAY / MILLIS_PER_DAY);
    }
}
```

So easy  
数据类型为 `long` , 很容易保存这两个乘积不产生溢出.  
因此, 结果肯定是 `1000`!

but…..  
结果是:  
![20241229154732_wTbwOPoH.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_wTbwOPoH.webp)

**解释:**  
为什么答案与我们想象不一样呢?  
因为数据溢出了…  
你在逗我? 但我没学过 java?  
long 能表示 -2 的 63 次方到 2 的 63 次方 - 1 的整数.  
数都数不过来, 怎么会溢出?  
哈哈, 小心陷阱啊, 虽然我们定义的是 `long` 类型,  
准确的说最终的结果应该是 `long` 类型的.

我们看看表达式右边,  
`24 * 60 * 60 * 1000 * 1000`  
这个表达式是以 `int` 类型作为运算的,  
`int` 跟 `int` 类型相乘, 结果还是 `int` 类型,  
最终结果超过 int 所能保存的范围, 所以数据溢出了,  
然后才被 `long` 所保存;

**改进**  
`24 * 60 * 60 * 1000 * 1000`–>`24L * 60 * 60 * 1000 * 1000`  
在表达式随便哪个数值后面加上一个 `l` 或者 `L` 就搞定了,  
其结果会自动转换为 `long` 而不是 `int` 了, 然后再保存到 `long` 类型变量中.  
就是这么简单, 就是这么任性.
