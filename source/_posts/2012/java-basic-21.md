---
title: Java编程进阶之路：学习Collections和Arrays的强大功能
keywords:
  - Java
categories:
  - Java
tags:
  - Java
  - Collections
  - Arrays
  - Comparable
  - Comparator
abbrlink: d366874c
date: 2012-05-30 00:00:00
ai:
  - 本文介绍了Java中Collections和Arrays类的基本方法以及比较器的相关使用。主要包括元素排序（sort()）、查找最大或最小元素（max(),
    min()）、反向排序(reverse())、随机排列(shuffle())等操作，以及如何通过Comparable接口实现对象的自然排序，并展示了如何定义自定义比较规则通过Comparator进行非自然排序。通过例子演示了在List集合中使用Collections.sort方法进行排序，同时说明了Comparator接口的应用可以在更广泛的场景下进行复杂对象的比较和排序。
description: 本文介绍了Java中Collections和Arrays类的基本方法以及比较器的相关使用。主要包括元素排序（sort()）、查找最大或最小元素（max(),
  min()）、反向排序(reverse())、随机排列(shuffle())等操作，以及如何通过Comparable接口实现对象的自然排序，并展示了如何定义自定义比较规则通过Comparator进行非自然排序。通过例子演示了在List集合中使用Collections.sort方法进行排序，同时说明了Comparator接口的应用可以在更广泛的场景下进行复杂对象的比较和排序。
---

### Collections 类

此类方法众多, 只介绍几个常用方法

- sort() 对元素进行排序, 可以传入比较器
- max() 返回最大元素, 可以传入比较器
- min() 返回最小元素, 可以传比较器
- reverse() 反排序
- shuffle() 混排

### Arrays 类

此类包含用来操作数组（比如排序和搜索）的各种方法。  
方法更多, 还是看 API 吧

### 比较器

#### Comparable

内部比较器  
`public interface Comparable`  
此接口强行对实现它的每个类的对象进行整体排序。这种排序被称为类的自然排序，类的 compareTo 方法被称为它的自然比较方法。  
`int compareTo(T o)`  
一个类继承了 Comparable 接口后, 重写 compareTo() 方法, 就能按照我们自己的规则排序

例子:

```java
public class Student implements Comparable<Student>{
    private String name;
    private int age;
    private int score;
    public Student() {
    }
    public Student(String name, int age, int score) {
        super();
        this.name = name;
        this.age = age;
        this.score = score;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public int getScore() {
        return score;
    }
    public void setScore(int score) {
        this.score = score;
    }
    /**
     * 比较规则是按照年龄来排
     */
    @Override
    public int compareTo(Student stu) {
        // TODO Auto-generated method stub
        if(this.age > stu.getAge()){
            return 1;
        }else if(this.age < stu.getAge()){
            return -1;
        }else{
            return 0;
        }
    }
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "名字:" + this.name + "；年龄：" + this.age + ";成绩：" + this.score;
    }
}
```

当把 Student 对象存储在 List 集合中的时候,  
可以使用 Collections 工具类对这个 Student 集合进行排序.

- 如果调用 Collections 的 `sort(List<T> list)` 方法, 就会根据元素的自然顺序 对指定列表按升序进行排序
- 当调用 `sort(List<T> list, Comparator<? super T> c)` 方法时,  
   当我们传入一个比较器的时候, 就会根据我们自己定义的规则进行排序

```java
ArrayList<Student> arrayStudent = new ArrayList<Student>();
arrayStudent.add(new Student("张三",26,90));
arrayStudent.add(new Student("李四",20,76));
arrayStudent.add(new Student("王武",24,68));
Collections.sort(arrayStudent);
```

因为在 Student 类继承 Comparable 接口, 重写了此接口的 compareTo() 方法, 当对 arrayStudent 集合进行排序的时候, 会按照我们重写后的规则进行排序

#### Comparator

外部比较器  
接着上面的例子

重新定义一个实现了 Comparator 接口的类

```java
public class StudentComparator implements Comparator<Student>{
    @Override
    public int compare(Student stu1, Student stu2) {
        // TODO Auto-generated method stub
        if(stu1.getName().length() > stu2.getName().length()){
            return 1;
        }else if(stu1.getName().length() < stu2.getName().length()){
            return -1;
        }else{
            return 0;
        }
    }
}
```

然后调用  
`Collections.sort(arrayStudent,new StudentComparator());`  
将按照我们的规则进行排序.

在以前我们只能比较基本数据类型和字符串  
现在学习了比较器之后, 我们就可以比较 (排序) 对象了,  
只要继承了 Comparable 或者传入一个实现了 Comparator 接口的自己定义的比较规则的对象,  
就可以按照我们的想法对元素进行排序.
