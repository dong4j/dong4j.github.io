---
title: Java并发编程的利器：volatile的关键技巧和应用
keywords:
  - Java
  - Concurrency
  - Memory Model
  - Volatile
categories:
  - 新时代码农
tags:
  - Java
  - Concurrency
  - Memory Model
  - Volatile
abbrlink: da43da6e
date: 2014-08-12 00:00:00
ai:
  - 本文探讨了volatile关键字在Java并发编程中的作用和意义，主要涵盖了两个方面：可见性和指令重排。volatile关键字确保了变量的可见性，即当一个线程修改了一个共享变量时，其他线程能够立即得知这个修改。它还禁止了指令重排，从而保证了程序执行的有序性。然而，volatile关键字不能保证操作的原子性，这可能导致并发问题。文章通过具体的例子和代码分析，深入解释了这些概念。
description: 本文探讨了volatile关键字在Java并发编程中的作用和意义，主要涵盖了两个方面：可见性和指令重排。volatile关键字确保了变量的可见性，即当一个线程修改了一个共享变量时，其他线程能够立即得知这个修改。它还禁止了指令重排，从而保证了程序执行的有序性。然而，volatile关键字不能保证操作的原子性，这可能导致并发问题。文章通过具体的例子和代码分析，深入解释了这些概念。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

**volatile 关键字的 2 层含义:**

> 用 volatile 修饰的变量，线程在每次使用变量的时候，都会读取变量修改后的最新的值.  
> 作为指令关键字，确保本条指令不会因编译器的优化而省略，且要求每次直接读值.

## 可见性

可见性是指 当一个线程修改了一个共享变量,其他线程能够立刻得知这个修改.  
这里有必要了解一下 Java 的内存模型

![20241229154732_UNw0TFwI.webp](./volatile-comprehend/20241229154732_UNw0TFwI.webp)

被 volatile 修饰的变量,当线程需要使用这个变量时,回去主内存中读取,然后加载到自己的工作线程中,  
工作线程中的变量只是主存变量的一个拷贝,当使用完这个变量后,会刷新会主存中.

![20241229154732_Lg19Egdh.webp](./volatile-comprehend/20241229154732_Lg19Egdh.webp)

当数据中主内存复制到工作内存存储时,必须出现两个动作:

1. 由主内存执行的 read 操作
2. 有工作内存执行相应的 load 操作

当数据从工作内存拷贝到主内存时,也会有两个操作:

1. 用工作内存执行的 store 操作
2. 用主内存执行相应的 write 操作

volatile 的特殊规则就是 read、load、use 必须连续出现。assign、store、write 动作必须连续出现。所以使用 volatile 变量能够保证必须先从主内存刷新最新的值，每次修改后必须立即同步回主内存当中。

所以 colatile 的可见性很适合用来控制并发:

```java
public class VolatileDemo {
	private static volatile boolean flag;
	public static void shutdown(){
		flag=true;
	}
	public static void main(String[] args) throws InterruptedException{
		VolatileDemo m = new VolatileDemo();
		for(int i=0;i<20;i++){
			new Thread(new Runnable() {
				public void run() {
					while(!flag){
						  System.out.println("aaa");
					}
				}
			}).start();
		}
		Thread.sleep(2000);
		shutdown();
	}
}
```

当调用 shutdown() 时,能保证所有线程立刻停止.

## volatile 的禁止指令重排序

指令重排是 编译器和 cup 在不影响执行结果的情况下,进行的一种优化策略.

> 在 Java 中普遍的变量仅仅会保证在该方法的执行过程中所有依赖的赋值结果的地方都能获取到正确的结果，而不能保证变量赋值操作的顺序与程序代码中的执行顺序一致。因为在一个线程的方法执行过程中无法感知到这点，这也就是 Java 内存模型中描述的所谓“线程内表现为串行的语义”。

### 有序性

计算机在执行代码时,不一定按照程序的顺序来执行.

```java
class OrderExample {
	int a = 0;
	boolean flag = false;
	public void writer() {
		a = 1;
		flag = true;
	}
	public void reader() {
		if (flag) {
			int i = a +1;
		}
	}
}
```

比如上述代码，两个方法分别被两个线程调用。  
按照常理，写线程应该先执行 a=1，再执行 flag=true。  
当读线程进行读的时候，i=2；  
但是因为 a=1 和 flag=true，并没有逻辑上的关联。  
所以有可能执行的顺序颠倒，有可能先执行 flag=true，再执行 a=1。  
这时当 flag=true 时，切换到读线程，此时 a=1 还没有执行，那么读线程将 i=1。

**指令重排可以使流水线更加顺畅**

当然指令重排的原则是不能破坏串行程序的语义，例如 a=1,b=a+1，这种指令就不会重排了，因为重排的串行结果和原先的不同。

在 Java 里面，可以通过 volatile 关键字来保证一定的“有序性”。另外可以通过 synchronized 和 Lock 来保证有序性，很显然，synchronized 和 Lock 保证每个时刻是有一个线程执行同步代码，相当于是让线程顺序执行同步代码，自然就保证了有序性。

### Happen-Before

Java 内存模型具备一些先天的“有序性”，即不需要通过任何手段就能够得到保证的有序性，这个通常也称为 happen-before 原则。如果两个操作的执行次序无法从 happen-before 原则推导出来，那么它们就不能保证它们的有序性，虚拟机可以随意地对它们进行重排序。

- 程序顺序原则：一个线程内保证语义的串行性 (写在前面的先发生,用来保证单线程结果的正确性)
- volatile 规则：volatile 变量的写，先发生于读，这保证了 volatile 变量的可见性
- 锁规则：解锁（unlock）必然发生在随后的加锁（lock）前
- 传递性：A 先于 B，B 先于 C，那么 A 必然先于 C
- 线程的 start() 方法先于它的每一个动作
- 线程的所有操作先于线程的终结（Thread.join()）
- 线程的中断（interrupt()）先于被中断线程的代码
- 对象的构造函数执行结束先于 finalize() 方法

**为什么 Happen-Before 原则不被指令重排影响?**  
例如你让一个 volatile 的 integer 自增（i++），其实要分成 3 步：1）读取 volatile 变量值到 local； 2）增加变量的值；3）把 local 的值写回，让其它的线程可见。这 3 步的 jvm 指令为：

```
mov
0xc(%r10),%r8d
 ; Load
inc
 %r8d           ; Increment
mov
 %r8d,0xc(%r10)
 ; Store
lock
 addl $0x0,(%rsp)
 ; StoreLoad Barrier
```

StoreLoad Barrier 就是内存屏障

> 内存屏障（memory barrier）是一个 CPU 指令。基本上，它是这样一条指令：
>
> 1.  确保一些特定操作执行的顺序；
> 2.  影响一些数据的可见性 (可能是某些指令执行后的结果)。  
>     编译器和 CPU 可以在保证输出结果一样的情况下对指令重排序，使性能得到优化。  
>     插入一个内存屏障，相当于告诉 CPU 和编译器先于这个命令的必须先执行，后于这个命令的必须后执行。  
>     内存屏障另一个作用是强制更新一次不同 CPU 的缓存。  
>     例如，一个写屏障会把这个屏障前写入的数据刷新到缓存，这样任何试图读取该数据的线程将得到最新值，而不用考虑到底是被哪个 cpu 核心或者哪颗 CPU 执行的。

**内存屏障和 volatile 的关系**  
上面的虚拟机指令里面有提到，如果你的字段是 volatile，Java 内存模型将在写操作后插入一个**写屏障指令**，在读操作前插入一个**读屏障指令**。  
这意味着如果你对一个 volatile 字段进行写操作，你必须知道：

1. 一旦你完成写入，任何访问这个字段的线程将会得到最新的值。
2. 在你写入前，会保证所有之前发生的事已经发生，并且任何更新过的数据值也是可见的，因为内存屏障会把之前的写入值都刷新到缓存。

明白了内存屏障这个 CPU 指令，回到前面的 JVM 指令：从 load 到 use 到 assign 到 store 到内存屏障，一共 4 步，其中最后一步 jvm 让这个最新的变量的值在所有线程可见，也就是最后一步让所有的 CPU 内核都获得了最新的值，但中间的几步（从 Load 到 Store）是不安全的，中间如果其他的 CPU 修改了值将会丢失。

### volatile 禁止指令重排的两层含义

1. 当程序执行到 volatile 变量的读操作或者写操作时,在其前面的操作肯定已经全部进行,且结果对后面的操作可见; 且后面的操作还没有进行;
2. 在进行指令优化时,不能将对 volatile 变量的访问语句放在气候执行,也不能把 volatile 变量后面的语句放在其前面执行.

```java
//x、y为非volatile变量
//flag为volatile变量
x = 2;          //语句1
y = 0;          //语句2
flag = true;  //语句3
x = 4;          //语句4
y = -1;         //语句5
```

由于 flag 变量为 volatile 变量，那么在进行指令重排序的过程的时候，不会将语句 3 放到语句 1、语句 2 前面，也不会讲语句 3 放到语句 4、语句 5 后面。但是要注意语句 1 和语句 2 的顺序、语句 4 和语句 5 的顺序是不作任何保证的。

并且 volatile 关键字能保证，执行到语句 3 时，语句 1 和语句 2 必定是执行完毕了的，且语句 1 和语句 2 的执行结果对语句 3、语句 4、语句 5 是可见的

## vloatile 的并发问题

volatile 能保证可见性和禁止指令重排,但是却不能保证原子性,  
其实通过上面的分析也能得出这个结论.

比如 i++ 操作:

1. 读取 volatile 变量值到当前线程的工作内存中
2. 进行 i+1 计算
3. 将工作内存中的值写会到主内存,让其他线程可见

现在有 2 个线程同时对 volatile 变量进行操作,  
当第一个变量从主内存中读取了变量,但是还未进行 i+1 操作,  
此时第二个线程也从主存中读取了这个变量,但是和线程一读取的值一样,因为线程一还未将计算过的值刷新到主内存中,此时 2 个线程都对变量进行 +1 操作,然后刷新到主内存,此时,主内存中的值只是做了一次 +1 操作,而不是 2 次.

**某个线程将一个共享值优化到了内存中，而另一个线程将这个共享值优化到了缓存中，当修改内存中值的时候，缓存中的值是不知道这个修改的。**
