---
title: HashSet、TreeSet、HashMap：Java集合类的核心
keywords:
  - Java
categories:
  - Java
tags:
  - Java
  - 集合框架
  - Map
  - Set
  - List
  - HashSet
  - TreeSet
  - HashMap
  - Properties
abbrlink: 220ed6be
date: 2012-05-31 00:00:00
ai:
  - 本文详述了Java中的核心集合类：Set、Map与相关接口的理解和使用。主要分为三部分：Set接口及HashSet和TreeSet实现、Map接口及其HashMap应用，以及Properties类用于操作属性文件。文章深入讨论了每个类的特性和方法，如添加元素、获取元素、删除元素、判断是否存在键或值等，还介绍了如何遍历集合内容，并以HashSet为例展示了属性文件的操作方式。
description: 本文详述了Java中的核心集合类：Set、Map与相关接口的理解和使用。主要分为三部分：Set接口及HashSet和TreeSet实现、Map接口及其HashMap应用，以及Properties类用于操作属性文件。文章深入讨论了每个类的特性和方法，如添加元素、获取元素、删除元素、判断是否存在键或值等，还介绍了如何遍历集合内容，并以HashSet为例展示了属性文件的操作方式。
---

Java Conllection Frame

![20241229154732_HsNl759p.webp](20241229154732_HsNl759p.webp)

在集合框架中，分为两种 API：

1. 装载数据的集合类

- HashSet 类
- ArrayList 类
- LinkedList 类
- HashMap 类
- ….

2. 操作集合的工具类

- Arrays 类
- Collections 类

### Iterator 接口

java.util  
`public interface Iterator`  
Iterator 模式是用于遍历集合类的标准访问方法。  
它可以把访问逻辑从不同类型的集合类中抽象出来，从而避免向客户端暴露集合的内部结构

```java
public interface Iterator{
    boolean hasNext();//如果仍有元素可以迭代，则返回 true
    Object next();//返回迭代的下一个元素。 NoSuchElementException - 没有元素可以迭代。
    void remove();//从迭代器指向的 collection 中移除迭代器返回的最后一个元素（可选操作）。
}
```

### Iterable 接口

java.lang  
`public interface Iterable`  
实现这个接口允许对象成为 “foreach” 语句的目标。

Iterable 只有一个方法  
`iterator()` 返回一个迭代器  
实现类包括今天所学的 ArrayList,HashSet,LinkedList 等类  
然而并没有被 HashMap 类实现.

### 泛型

泛型（Generic type 或者 generics）是对 Java 语言的类型系统的一种扩展，以支持创建可以按类型进行参数化的类。可以把类型参数看作是使用参数化类型时指定的类型的一个占位符，就像方法的形式参数是运行时传递的值的占位符一样。

可以在集合框架（Collection framework）中看到泛型的动机。例如，Map 类允许您向一个 Map 添加任意类的对象，即使最常见的情况是在给定映射（map）中保存某个特定类型（比如 String）的对象。

因为 Map.get() 被定义为返回 Object，所以一般必须将 Map.get() 的结果强制类型转换为期望的类型，如下面的代码所示：

```
HashMap m = new HashMap();
m.put("key", "blarg");
String s = (String) m.get("key");
```

要让程序通过编译，必须将 get() 的结果强制类型转换为 String，并且希望结果真的是一个 String。但是有可能某人已经在该映射中保存了不是 String 的东西，这样的话，上面的代码将会抛出 ClassCastException。

```
HashMap<String,String> m = new HashMap<String,String>();
m.put("key", "blarg");
String s =  m.get("key");
```

理想情况下，可能会得出这样一个观点，即 m 是一个 Map，它将 String 键映射到 String 值。这可以**消除代码中的强制类型转换**，**同时获得一个附加的类型检查层**，该检查层可以防止有人将错误类型的键或值保存在集合中。这就是泛型所做的工作。

### Collection 接口

`public interface Collection extends Iterable{}`

> Collection 层次结构 中的根接口。Collection 表示一组对象，这些对象也称为 collection 的元素。一些 collection 允许有重复的元素，而另一些则不允许。一些 collection 是有序的，而另一些则是无序的。JDK 不提供此接口的任何直接 实现：它提供更具体的子接口（如 Set 和 List）实现。此接口通常用来传递 collection，并在需要最大普遍性的地方操作这些 collection。

Collection 接口定义了 Collection 对象公有的一些基本方法, 这些方法分为:

- 基本操作
  - int size()
  - isEmpty()
  - boolean contains(Object obj) 判断集合中是否包含指定元素
  - boolean add(Object obj) 向集合中添加元素
  - boolea remove(Object obj) 删除某元素
  - Iterator iterator() 返回一个遍历器, 用来访问集合中的各个元素
- 批量操作
  - containsAll(Collection c) 判断集合中是否包含指定集合
  - ….
- 数组操作
  - Object[] toArray() 返回一个包含集合所有元素的 array 数组.

#### List 接口

一列数据，数据内容可以重复，以元素安插的次序来放置元素，不会重新排列。

- 特点
  - 其中的元素是有顺序的
  - 允许重复元素
  - 支持 null 元素
  - 可以通过索引访问元素
- List 接口的实现类具有共同的方法：
  - add() —— 向集合中添加元素（增）
  - remove() – 将元素从集合中移除（删）
  - get() —— 从集合中获取元素（查）
  - set() —— 修改集合中的元素（改）
  - size() —— 查看集合长度

##### ArrayList

特点:

- 数组实现
- 可以添加相同的元素
- 使用最广泛，集合元素增加或删除操作不频繁时使用。最适合查询。

```java
ArrayList<Student> lst = new ArrayList<Student>();
        lst.add(new Student("zhang3",25,80));
        lst.add(new Student("li4",21,90));
        Student stu = lst.get(1);
        lst.size();
        for(Student stuTmp : lst){
            System.out.println(stuTmp.getName()+
                        stuTmp.getAge()+
                        stuTmp.getScore());
        }
```

##### LinkedList

特点:

- 双向链表实现
- 方法和 ArrayList 一样
- 当需要在集合的中间位置，频繁增加或删除元素时使用。

```java
//使用遍历器遍历各个元素
Iterator it = al.iterator();
while(it.hasNext()){
    Object objtmp = it.next();
    System.out.println(objtmp);
}
```

##### Vector

与 ArrayList 类似，但 Vector 是线程安全的，所以性能要低于 ArrayList

#### Set 接口

一列数据，**数据内容不能重复**，使用自己内部的一个排列机制放置元素。

- 特点:
  - 不能包含重复元素 , 当加入一个元素到容器中时, 要比较元素的内容是否存在重复, 所以加入容器中的对象必须重写 equals() 方法;
  - 元素可能有序, 也可能无序
  - 因为元素可能无序, 所以不能用索引访问 Set 中的元素
- Set 接口的实现类具有共同的方法：
  - add() —— 向集合中添加元素（增）
  - remove(Object o) – 将元素从集合中移除（删）
  - size() —— 查看集合长度

##### HashSet

特点:

- 速度快，不排序。
- 当遍历 HashSet 时, 其中的元素是没有顺序的
- HashSet 中不允许出现重复的元素 (重复的元素是指由相同的 hashCode, 并且 equals() 比较是, 返回 true 的两个对象)
- 允许包含 null 的元素

```java
import java.util.HashSet;
import java.util.Iterator;
public class TestSet {
    public static void main(String[] args) {
        HashSet<Student> set = new HashSet<Student>();
        set.add(new Student("zhang3",25,80));
        set.add(new Student("li4",21,90));
        set.add(new Student("wang5",27,70));
        Student stu = new Student("zhao6",22,65);
        set.add(stu);
        set.add(stu);//Set集合不能放入重复元素
        System.out.println(set.size());
        //要取出元素只能有遍历的方式，而且不支持普通for循环(因为没有下标)
        //迭代器
        Iterator<Student> it = set.iterator();
        while(it.hasNext()){
            Student stutmp = it.next();
            System.out.println(stutmp.getName());
        }
        for(Student stutmp : set){
            System.out.println(stutmp.getName());
        }
        //没有修改方法
        //删除--只能按对象移除，没有按位置移除
        set.remove(stu);
    }
}
```

##### TreeSet

速度慢，排序。

### Map 接口

一列数据对，使用自己内部的一个排列机制放置元素  
Map 接口用于维护 键 / 值对 (key/value pairs)。  
每个条目包括单独的两部分 :

- key
- Value

特点:

- 在 Map 中不允许出现重复的键, 但是可以有重复的值
- key 和 value 可以是任何类的实例

共同的方法:

- put() 将键值对存入集合
- get() 根据键取出元素的值
- keySet() 将 Map 中的所有键取出形成一个 Set
- values() 将 Map 中的所有值取出形成一个 Collection
- remove() 根据键移除值
- containsKey 判断 HashMap 中是否存在这个键
- containsValue 判断 HashMap 中是否存在这个值

#### HashMap

- 速度快，不排序。

```java
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class TestMain {
    public static void main(String[] args) {
        HashMap<String, Student> map = new HashMap<String, Student>();

        //放元素
        map.put("001", new Student("zhang3",25,80));
        map.put("002", new Student("li4",21,90));
        map.put("003", new Student("wang5",27,70));
        System.out.println(map.size());
        Student stu = new Student("zhao6",22,65);
        map.put("004", stu);
        map.put("005", stu);
        System.out.println(map.size());
        //向重复的键放入新的值,相当于在做修改动作.
        map.put("005", new Student("chen7",18,62));

        //取元素是根据键去取值
        Student stu1 = map.get("003");
        System.out.println(stu1.getName());

        //删除元素也给根据键去删除
        map.remove("002");
        System.out.println(map.size());

        //遍历
        Set<String> ks = map.keySet();//得到所有的键
        for(String key : ks){
            System.out.println(map.get(key).getName());
        }

        Collection<Student> cl = map.values();//得到所有的值
        for(Student stutmp : cl){
            System.out.println(stutmp.getName());
        }

        //获取某个键是否存在于Map对象当中
        System.out.println(map.containsKey("007"));
        //获取某个值是否存在于Map对象当中
        System.out.println(map.containsValue(stu));
    }
}
```

#### Properties 方便操作属性文件)

![20241229154732_BjJ8f4hM.webp](20241229154732_BjJ8f4hM.webp)
