---
title: Java 基础：一些常用的代码片段四
keywords:
  - Java
  - Comparator
  - Comparable
  - 外部排序
  - 内部排序
  - 事务管理
  - JDBC
categories:
  - 新时代码农
tags:
  - Java
  - Comparator
  - Comparable
  - 外部排序
  - 内部排序
  - 事务管理
  - JDBC
abbrlink: 1553cb8c
date: 2016-10-28 00:00:00
ai:
  - 本文讨论了Java中排序和事务管理的两种重要技术：外部排序（使用Comparator）和内部排序（实现Comparable接口），以及JDBC中的事务管理。外部排序提供灵活的排序方式，而内部排序保持了类的一致性。事务管理确保数据库操作要么全部完成要么全部不执行，对于保持数据一致性至关重要。
description: 本文讨论了Java中排序和事务管理的两种重要技术：外部排序（使用Comparator）和内部排序（实现Comparable接口），以及JDBC中的事务管理。外部排序提供灵活的排序方式，而内部排序保持了类的一致性。事务管理确保数据库操作要么全部完成要么全部不执行，对于保持数据一致性至关重要。
---

## 外部排序：通过 Comparator 实现个性化排序

### 使用 Comparator 的基本步骤

1. **定义一个实现了 `Comparator<T>` 接口的类**，其中需要实现 `compare` 方法。
2. **使用 Collections.sort(List<T> list, Comparator<T> c)** 对列表进行排序。

### 示例代码：

#### Person 类

```java
public class Person {
    private int age;
    private String name;

    public Person(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "age=" + age +
                ", name='" + name + '\'' +
                '}';
    }
}
```

#### PersonComparator 类（实现了 Comparator 接口）

```java
import java.util.Comparator;

public class PersonComparator implements Comparator<Person> {
    @Override
    public int compare(Person o1, Person o2) {
        return Integer.compare(o1.getAge(), o2.getAge());
    }
}
```

#### TestComparator 类（测试排序逻辑）

```java
import java.util.*;

public class TestComparator {

    public static String outCollection(Collection<?> coll) {
        StringBuffer sb = new StringBuffer();
        for (Object obj : coll) {
            sb.append(obj + "\n");
        }
        System.out.println(sb.toString());
        return sb.toString();
    }

    public static void main(String[] args) {
        test1();
    }

    public static void test1() {
        System.out.println("----------test1()---------");
        System.out.println("升序排序测试:");
        List<Person> listPerson = new ArrayList<>();
        Person person1 = new Person(34, "lavasoft");
        Person person2 = new Person(12, "lavasoft");
        Person person3 = new Person(23, "leizhimin");
        Person person4 = new Person(13, "sdg");

        listPerson.add(person1);
        listPerson.add(person2);
        listPerson.add(person3);
        listPerson.add(person4);

        Comparator<Person> ascComparator = new PersonComparator();

        System.out.println("原集合为:");
        outCollection(listPerson);

        System.out.println("排序后集合为:");
        Collections.sort(listPerson, ascComparator);
        outCollection(listPerson);
    }
}
```

### 输出结果

```
----------test1()---------
升序排序测试:
原集合为:
Person{age=34, name='lavasoft'}
Person{age=12, name='lavasoft'}
Person{age=23, name='leizhimin'}
Person{age=13, name='sdg'}

排序后集合为:
Person{age=12, name='lavasoft'}
Person{age=13, name='sdg'}
Person{age=23, name='leizhimin'}
Person{age=34, name='lavasoft'}
```

## 内部排序：通过实现 Comparable 接口

### 使用 Comparable 的基本步骤

1. **在需要排序的类中实现 `Comparable<T>` 接口**，并重写 `compareTo` 方法。
2. **使用 Collections.sort(List<T> list)** 对列表进行默认升序或调用 `Collections.reverseOrder()` 进行降序。

### 示例代码：

#### Cat 类

```java
public class Cat implements Comparable<Cat> {
    private int age;
    private String name;

    public Cat(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Cat{" +
                "age=" + age +
                ", name='" + name + '\'' +
                '}';
    }

    @Override
    public int compareTo(Cat o) {
        return Integer.compare(this.getAge(), o.getAge());
    }
}
```

#### TestComparable 类（测试排序逻辑）

```java
import java.util.*;

public class TestComparable {

    public static String outCollection(Collection<?> coll) {
        StringBuffer sb = new StringBuffer();
        for (Object obj : coll) {
            sb.append(obj + "\n");
        }
        System.out.println(sb.toString());
        return sb.toString();
    }

    public static void main(String[] args) {
        test();
    }

    public static void test() {
        System.out.println("----------test()---------");
        System.out.println("升序排序测试:");
        List<Cat> listCat = new ArrayList<>();
        Cat cat1 = new Cat(34, "hehe");
        Cat cat2 = new Cat(12, "haha");
        Cat cat3 = new Cat(23, "leizhimin");
        Cat cat4 = new Cat(13, "lavasoft");

        listCat.add(cat1);
        listCat.add(cat2);
        listCat.add(cat3);
        listCat.add(cat4);

        System.out.println("原集合为:");
        outCollection(listCat);

        System.out.println("调用Collections.sort(List<T> list)排序：");
        Collections.sort(listCat);
        outCollection(listCat);

        System.out.println("逆序排列元素:");
        Collections.sort(listCat, Collections.reverseOrder());
        outCollection(listCat);
    }
}
```

### 输出结果

```
----------test()---------
升序排序测试:
原集合为:
Cat{age=34, name='hehe'}
Cat{age=12, name='haha'}
Cat{age=23, name='leizhimin'}
Cat{age=13, name='lavasoft'}

调用Collections.sort(List<T> list)排序：
Cat{age=12, name='haha'}
Cat{age=13, name='lavasoft'}
Cat{age=23, name='leizhimin'}
Cat{age=34, name='hehe'}

逆序排列元素:
Cat{age=34, name='hehe'}
Cat{age=23, name='leizhimin'}
Cat{age=13, name='lavasoft'}
Cat{age=12, name='haha'}
```

## 总结

通过上述示例，我们可以看到使用 `Comparator` 和实现 `Comparable` 接口分别实现了外部排序和内部排序。两种方法各有优势：

- **外部排序（使用 Comparator）**：

  - 高度灵活，可以为一个类定义多种不同的比较方式。
  - 对于不希望修改原始类的代码结构的情况特别有用。

- **内部排序（实现 Comparable 接口）**：
  - 简洁且直接在对象内部定义排序逻辑，保持了单个类的一致性。
  - 对于需要频繁排序的对象特别合适，并且可以通过 `Collections.reverseOrder()` 快速反转排序顺序。

## 使用迭代器删除集合元素

### 场景描述

当你需要遍历一个集合并根据某些条件移除其中的元素时，直接在循环体内进行删除操作会导致 `ConcurrentModificationException`。这是因为直接修改集合（如调用 `List.remove()`）会破坏迭代器的状态。

为了避免这种情况，我们可以使用 Java 的 `Iterator` 接口来安全地执行删除操作。

### 示例代码

假设我们有一个订单列表，并希望根据店铺 ID 移除不属于特定店铺的商品项。

```java
for (OrderDto orderDto : list) {
    Iterator<ProductItemDto> productItemDtoIterator = orderDto.getProductItems().iterator();
    while (productItemDtoIterator.hasNext()) {
        ProductItemDto productItemDto = productItemDtoIterator.next();
        if (!productItemDto.getShopId().equals(shopId)) {
            // 通过调用迭代器的 remove 方法来安全地移除元素
            productItemDtoIterator.remove();
        }
    }
}
```

这里，我们使用了 `Iterator` 的 `remove()` 方法而不是直接删除集合中的元素。此方法确保了操作的安全性，并且避免了并发修改异常。

### 注意事项

- **不要在循环中调用其他可能改变列表的方法**。
- 当需要同时进行增删改查等复杂操作时，建议使用迭代器来遍历和修改数据结构。

## JDBC 中的事务管理

### 事务基础概念

数据库事务是一组数据库操作指令集，这些操作要么全部完成（成功），要么全部都不执行（失败）。JDBC 提供了对 SQL 语句执行的控制能力，并且可以进行显式地提交或回滚当前事务。

### 示例代码

以下是一个简单的示例，展示了如何使用 JDBC 管理数据库中的事务：

```java
Connection con = null;
Statement st = null;
ResultSet rs = null;
PreparedStatement ps = null;

public void startTransaction() {
    try {
        // 获取连接对象
        con = DBCManager.getConnect();

        // 设置事务的提交方式为非自动提交，确保需要的所有操作都成功后才进行提交。
        con.setAutoCommit(false);

        // 准备并执行 SQL 语句
        String sql1 = "delete from me where id = 7";
        ps = con.prepareStatement(sql1);
        ps.executeUpdate();

        String sql2 = "update me set name='chengong', age=34 where id=4";
        ps = con.prepareStatement(sql2);
        ps.executeUpdate();

        // 如果事务成功执行，则提交事务。
        con.commit();
    } catch (SQLException e) {
        try {
            // 出现异常时，回滚当前的数据库操作。
            if(con != null)
                con.rollback();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }

        // 打印错误信息
        e.printStackTrace();
    } finally {
        // 释放资源
        DBCManager.release(rs, ps, con);
    }
}
```

### 输出结果与解释

如果上述操作在执行过程中没有任何异常，则整个事务会被提交到数据库。如果有任何 SQL 操作失败，那么 `commit` 调用将不会发生，并且之前的更改将会被回滚。

## 总结

通过使用 Java 的迭代器接口来安全地修改集合中的元素是处理并发访问时的一个关键技巧；而在执行多个操作以确保数据的一致性时，事务管理则是 JDBC 编程中的重要组成部分。这两种技术都提供了强大的工具来帮助我们编写更加健壮的应用程序代码。
