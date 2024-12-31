---
title: 字符串常量到底存放在哪
keywords:
  - Java
categories:
  - Java
tags:
  - Java
  - 内存模型
  - 永久代
  - 堆内存
  - 字符串常量池
  - intern()方法
  - final修饰符
  - StringBuilder
description: ' '
abbrlink: 4453ea00
date: 2015-11-12 00:00:00
ai:
  - 本文详细解释了Java内存模型中关于字符串字面量、永久代与堆内存的不同概念以及它们之间的关系。文章阐述了JDK 1.6和JDK 1.7在处理字符串实例intern()方法时的不同行为，以及字符串常量池（Interned
    String位置）从永久代迁移到堆内存的过程。此外，还讨论了final修饰的char数组是否共享同一份数据的问题，并提供了相关链接以供进一步研究。最后，推荐了几篇深入探讨Java内存模型和字符串处理的文章。
---

字符串常量归常量池管理，那比如 String str = "abc"; "abc" 这个对象是放在内存中的哪个位置，是字符串常量池中还是堆？

”这句代码的 abc 当然在常量池中，只有 new String("abc") 这个对象才在堆中创建“，他们大概是这么回答。

“abc”这个东西，是放在常量池中，这个答案是错误的。

**字符串“abc" 的本体、实例，应该是存在于 Java 堆中。**

可能还真的有部分同学对这个知识点不熟悉，今天和大家聊聊字符串这个问题 ~

初学 Java 时，学到字符串这一部分，有一段代码

```java
String str1 = "hello";
String str2 = new String("hello");
复制代码
```

> 书上的解释是：执行第一行的时候，已经把 "hello" 字符串放到了常量池中，执行第二行代码时，会将常量池中已经存在的 "hello" 复制一份到堆内存中，创建一个的新的 String 对象。虽然值一样，但他们是不同的对象。

当时看完这个解释，我产生了很多疑惑。因为在此之前已经知道字符串的底层是 char 数组实现的。我很疑惑：

- 他 copy 一份过去，是 copy 了 char 数组呢？
- 还是 copy 整个 String 对象？
- "hello" 这个对象实例真的存放在常量池中吗？

当时在网上搜了一些文章和答案，各有说辞，大部分回答都是 "str" 这个对象在常量池中，但也有认为字符串常量实例（或叫对象）是在堆中创建，只是将其引用放到字符串常量池中，交给常量池管理。

## JAVA 内存区域 — 运行时数据区

理清这个问题前，需要梳理一下前置知识。

从一个经典的示意图讲起，以 hotspot 虚拟机为例，此内存模型需建立在 JDK1.7 之前的版本来讨论，JDK1.7 之后有所改变，但是原理还是一样的。

![20241229154732_uaxPxuHQ.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_uaxPxuHQ.webp)

Java 虚拟机管理的内存是运行时数据区那一部分，简单概括一下其中各个区域的区别：

- **虚拟机栈**：线程私有，生命周期与线程相同，即每条线程都一个独立的栈（VM Stack）。每个方法执行时都会创建一个栈帧，也就是说，当有一条线程执行了多个方法时，就会有一个栈，栈中有多个栈帧。
- **本地方法栈**：线程私有
- **程序计数器**：线程私有
- **堆 Heap**：线程共享，是 Java 虚拟机所管理的内存中最大的一块，在虚拟机启动时创建。此内存区域的唯一目的就是存放对象实例，几乎所有的对象实例都在这里分配内存。**在 Java 虚拟机规范中的描述是：所有的对象实例以及数组都要在堆上分配。 ** *（原文：The heap is the runtime data area from which memory for all class instances and arrays is allocated）* 但有特殊情况，随着 JIT 编译器的发展，逃逸分析和标量替换技术的逐渐成熟，对象也可以在**栈上**分配。另外，虽说堆是线程共享，但其中也可以划分出多个线程私有的分配缓冲区 _（Thread Local Allocation Buffer，TLAB）_。
- **方法区**：线程共享，它用于存储已被虚拟机加载的类信息、常量、静态变量、即时编译器编译后的代码等数据。

## JAVA 的三种常量池

此外，Java 有三种常量池，即**字符串常量池（又叫全局字符串池）、class 文件常量池、运行时常量池**。  
![20241229154732_i9lS5QCd.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_i9lS5QCd.webp)

**1. 字符串常量池（也叫全局字符串池、string pool、string literal pool）**

字符串常量池在每个 VM 中只有一份，他在内存中的位置如图，红色箭头所指向的区域 Interned Strings

**2. 运行时常量池（runtime constant pool）**

当程序运行到某个类时，class 文件中的信息就会被解析到内存的方法区里的运行时常量池中。看图可清晰感知到每一个类被加载进来都会产生一个**运行时常量池**，由此可知，每个类都有一个运行时常量池。它在内存中的位置如图，蓝色箭头所指向的区域，方法区中的 Class Date 中的运行时常量池（Run-Time Constant Pool）

![20241229154732_qETfdsVS.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229154732_qETfdsVS.webp)

**3. class 文件常量池（class constant pool）**

class 常量池是在编译后每个 class 文件都有的，class 文件中除了包含类的版本、字段、方法、接口等描述信息外，还有一项信息就是  **常量池**（constant pool table）_，用于存放编译器生成的各种字面量（Literal）和符号引用（Symbolic References）。_ 字面量就是我们所说的常量概念，如文本字符串、被声明为 final 的常量值等. 他在 class 文件中的位置如上图所示，Constant Pool 中。

## 个人理解

```java
public static void main(String[] args) {
	String str = "hello";
}
复制代码
```

回到一开始说到的这句代码，可以来总结一下它的执行过程了。

1. 首先，字面量 "hello" 在编译期，就会被记录在 class 文件的  **class 常量池**中。
2. 而当 class 文件被加载到内存中后，JVM 就会将 class 常量池中的**大部分内容存放到运行时常量池**中，但是**字符串 "hello" 的本体**（对象）和其他所有对象一样，是**会在堆中创建**，**再将引用放到字符串常量池**，也就是图一的 Interned Strings 的位置。（RednaxelaFX 的文章里，测试结果是在新生代的 Eden 区。但因为一直有一个引用驻留在字符串常量池，所以不会被 GC 清理掉）
3. 而到了 String str = "hello" 这步，JVM 会去字符串常量池中找，如果找到了，JVM 会在栈中的局部变量表里创建 str 变量，然后把字符串常量池中的（hello 对象的）**引用**复制给 str 变量。

在《深入理解 Java 虚拟机》这本书中也有字符串相关的解释，举其中几个例子：

**例子 1**

> （原文）运行时常量池（Runtime Constant Pool）是方法区的一部分。Class 文件中除了有类的版本、字段、方法、接口等描述信息外，还有一项信息是常量池（Constant Pool Table），用于存放编译期生成的各种字面量和符号引用，**这部分内容将在类加载后进入方法区的运行时常量池中存放。**

最后一句描述不太准确，编译期生成的各种字面量并不是全部进入方法区的运行时常量池中。**字符串字面量就不进入运行时常量池**，而是**在堆中创建了对象**，**再将引用驻留到字符串常量池中。**

**例子 2**

```java
//代码清单2-7&emsp;String.intern（）返回引用的测试

public class RuntimeConstantPoolOOM{

	public static void main（String[]args）{
		String str1=new StringBuilder（"计算机"）.append（"软件"）.toString（）；
		System.out.println（str1.intern（）==str1）；
		String str2=new StringBuilder（"ja"）.append（"va"）.toString（）；
		System.out.println（str2.intern（）==str2）；
	}
}
复制代码
```

> （原文）这段代码在 JDK 1.6 中运行，会得到两个 false，而在 JDK 1.7 中运行，会得到一个 true 和一个 false。产生差异的原因是：在 JDK 1.6 中，intern（）方法会把首次遇到的字符串实例复制到永久代中，返回的也是永久代中这个字符串实例的引用，而由 StringBuilder 创建的字符串实例在 Java 堆上，所以必然不是同一个引用，将返回 false。而 JDK 1.7（以及部分其他虚拟机，例如 JRockit）的 intern（）实现不会再复制实例，只是在常量池中记录首次出现的实例引用，因此 intern（）返回的引用和由 StringBuilder 创建的那个字符串实例是同一个。对 str2 比较返回 false 是因为 “java” 这个字符串在执行 StringBuilder.toString（）之前已经出现过，字符串常量池中已经有它的引用了，不符合“首次出现”的原则，而“计算机软件”这个字符串则是首次出现的，因此返回 true。

原文解释也不太准确，我觉得在 JDK 1.6 中，intern（）并不会把首次遇到的字符串实例复制到永久代中，而是会将实例再复制一份到堆（heap）中，然后将其引用放入字符串常量池中进行管理，所以此代码返回 false。而 JDK1.7 中的 intern（）不会再复制实例，直接将首次遇到的此字符串实例的引用，放入字符串常量池，于是返回 true。关于此观点，还没看到大神文章实锤，欢迎讨论。

最后再延伸一点，大家都知道，字符串的 value 是 final 修饰的 char 数组，那么以下这段代码：

```java
// private final char value[];
String str1 = "hello world";
String str2 = new String("hello world");
String str3 = new String("hello world");
复制代码
```

str1、str2、str3 三个变量所指向的都是不同的对象。（str1 != str2 != str3）

那么，这三个对象里的 char 数组是否是同一个数组？相信大家都有答案了。

---

此文所讨论的 Java 内存模型是建立在 JDK1.7 之前。JDK 7 开始 Hotspot 虚拟机把字符串常量池（Interned String 位置）从永久代（PermGen）挪到 Heap 堆，JDK 8 又彻底取消 PermGen，把诸如 class 之类的元数据都挪到 GC 堆之外管理。但不管怎样，基本原理还是不变的，字面量 ”hello“ 等依旧不是放在 Interned String 中。

---

**推荐文章：**

- [请别再拿 “String s = new String("xyz"); 创建了多少个 String 实例” 来面试了吧](https://link.juejin.im/?target=https%3A%2F%2Frednaxelafx.iteye.com%2Fblog%2F774673)
- [借 HSDB 来探索 HotSpot VM 的运行时数据](https://link.juejin.im/?target=https%3A%2F%2Frednaxelafx.iteye.com%2Fblog%2F1847971) *作者：RednaxelaFX，曾为《深入理解 Java 虚拟机》提推荐语*
- [java 用这样的方式生成字符串：String str = "Hello"，到底有没有在堆中创建对象？](https://link.juejin.im/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F29884421%2Fanswer%2F113785601) - 胖君的回答 - 知乎
