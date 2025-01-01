---
title: 探索 Java 8 Stream API：从排序到过滤的全面指南
keywords:
  - Java
categories:
  - 新时代码农
tags:
  - Java
  - Stream API
  - List Processing
  - Mapping Operations
  - Sorting Techniques
  - Data Aggregation
  - Guava Libraries
  - HashMap Methods
  - Performance Considerations
abbrlink: 845cfa4f
date: 2016-10-15 00:00:00
ai:
  - 本文详细介绍了Java 8 Stream API在List到Map转换、排序、过滤和聚合操作中的应用。其中包括使用Stream API进行对象映射、列表过滤、数据聚合以及分组操作的方法。同时讨论了如何利用Lambda表达式和Stream的高级特性，如反向排序、多条件排序等，并提供了多个示例代码。此外，文章还简要介绍了HashMap的compute、computeIfAbsent和computeIfPresent方法在实现动态映射时的应用场景。
description: 本文详细介绍了Java 8 Stream API在List到Map转换、排序、过滤和聚合操作中的应用。其中包括使用Stream API进行对象映射、列表过滤、数据聚合以及分组操作的方法。同时讨论了如何利用Lambda表达式和Stream的高级特性，如反向排序、多条件排序等，并提供了多个示例代码。此外，文章还简要介绍了HashMap的compute、computeIfAbsent和computeIfPresent方法在实现动态映射时的应用场景。
---

Java 8 引进了强大的 Stream API，使得集合操作更加简洁优雅。本文将详细介绍如何使用 Java 8 的 Stream API 进行 List 转 Map、List 排序、列表过滤及 Map 中的条件操作。

## 使用 Java 8 Lambda 将 list 转为 map

### 常用方式

要将一个 List 转换为 Map，我们可以利用 `Collectors.toMap()` 方法。例如：

```java
public Map<Long, String> getIdNameMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, Account::getUsername));
}
```

### 收集成实体本身 map

有时候我们可能希望将列表中的对象直接映射到 Map 中作为值，可以这样做：

```java
public Map<Long, Account> getIdAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, account -> account));
}
```

`account -> account` 是一个返回本身的 lambda 表达式。使用 `Function.identity()` 会使得代码更简洁：

```java
public Map<Long, Account> getIdAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getId, Function.identity()));
}
```

### 处理重复 key 的情况

当需要根据可能有重复值（如 name）的字段来创建 map 时，可能会遇到 `java.lang.IllegalStateException: Duplicate key` 异常。为了处理这种情况，可以给 `toMap()` 方法传入一个合并函数：

```java
public Map<String, Account> getNameAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getUsername, Function.identity(), (key1, key2) -> key2));
}
```

这里只是简单的使用后者覆盖前者。`toMap()` 还允许我们指定一个具体的 `Map` 实现类来收集数据：

```java
public Map<String, Account> getNameAccountMap(List<Account> accounts) {
    return accounts.stream().collect(Collectors.toMap(Account::getUsername, Function.identity(), (key1, key2) -> key2, LinkedHashMap::new));
}
```

## JDK 8 对 List 和 Map 的排序

### Java 8 更新前的 List 排序操作

在使用 Java 8 之前，我们通常需要创建一个匿名内部类来实现排序：

```java
Collections.sort(humans, new Comparator<Human>() {
    @Override
    public int compare(Human h1, Human h2) {
        return h1.getName().compareTo(h2.getName());
    }
});
```

### 使用 Lambda 表达式的 List 排序

Java 8 中，我们可以直接使用 lambda 表达式来定义比较器：

```java
humans.sort((Human h1, Human h2) -> h1.getName().compareTo(h2.getName()));
```

还可以进一步简化为：

```java
humans.sort((h1, h2) -> h1.getName().compareTo(h2.getName()));
```

或者使用静态方法引用：

```java
humans.sort(Human::compareByNameThenAge);
```

以及比较器提供的辅助方法：

```java
Collections.sort(humans, Comparator.comparing(Human::getName));
```

### 反序排序

Java 8 提供了 `Comparator.reversed()` 方法来实现反向排序：

```java
humans.sort(comparator.reversed());
```

### 使用多个条件进行排序

可以使用链式操作来进行多级排序：

```java
humans.sort(Comparator.comparing(Human::getName).thenComparing(Human::getAge));
```

## 利用 Stream API 进行 List 的过滤和 map 操作

### 列表的过滤处理

使用 `stream().filter()` 可以方便地对列表进行过滤：

```java
List<String> list2 = list1.stream().filter(s -> s != "1").collect(Collectors.toList());
```

输出结果是 `[2, 3]`。

### List 转换为另一个 List

可以利用 `stream().map()` 来转换列表中的每个元素，然后收集到新的列表中：

```java
List<String> list2 = list1.stream().map(string -> "stream ().map () 处理之后：" + string).collect(Collectors.toList());
```

### 数据聚合

以下是一些利用 Stream 对列表中的用户对象 `User` 进行各种数据聚合的方法：

- **求和**：`list.stream().mapToDouble(User::getHeight).sum()` 此方法返回用户集合中所有用户的身高总和。
- **最大值**：`list.stream().mapToDouble(User::getHeight).max()` 获取用户对象中的最高身高的用户，返回的是 Optional 类型。
- **最小值**：`list.stream().mapToDouble(User::getHeight).min()` 返回用户集合中最矮的用户，也是返回 Optional 类型。
- **平均值**：`list.stream().mapToDouble(User::getHeight).average()` 计算所有用户的身高平均值，并以 `Optional<Average>` 形式返回。

### 列表拆分与合并

在 Java8 中，我们可以使用 Stream 的方法来完成字符串的拆分以及列表的合并。例如：

- **分割**：`Stream.of(string.split(","))` 将原始字符串按逗号分割，并将结果转换为 List。
- **拼接**：`asList.stream().collect(Collectors.joining())` 可以把一个集合里的元素使用指定的符号连接起来，形成一个新的字符串。

### 提取字段转换成列表

有几种方法可以用于提取 `appPermissionVoList` 列表中的用户 ID：

1. 使用 Stream 的方式：
   ```java
   List<String> userIds = appPermissionVoList.stream()
           .map(appPermissionVo -> appPermissionVo.getUserId())
           .collect(Collectors.toList());
   ```
2. 使用 Guava 库的 `Lists.transform()` 方法:
   ```java
   List<String> usrIds = Lists.transform(appPermissionVoList,appPerm->appPerm.getUserId());
   ```

### 分组

分组操作是一种常见的需求。例如：

```java
Map<String, List<User>> groupBySex = userList.stream()
        .collect(Collectors.groupingBy(User::getSex));
```

此代码将根据用户性别进行列表的分组处理。

## HashMap 的 `compute`, `computeIfAbsent` 及 `computeIfPresent`

这三者都是用来对映射中的元素进行修改。它们的区别在于：

- `computeIfPresent(K key, BiFunction<? super K, ? super V, ? extends V> remappingFunction)` 仅当指定的键存在时才执行操作。
- `computeIfAbsent(K key, Function<? super K, ? extends V> mappingFunction)` 当给定的键不存在于该映射中，则计算其对应的值，并将其放入该映射中，然后返回该值；否则直接返回当前值。
- `compute(K key, BiFunction<? super K, ? super V, ? extends V> remappingFunction)` 不管是新插入还是已存在的键都可以操作。

```java
Object key2 = map.computeIfAbsent("key", k -> new Object());
```

## 注意事项与最佳实践

1. **性能考虑**：尽管 Stream API 提供了极大的便利性，但过度使用可能会导致性能问题。因此，需要权衡代码的可读性和效率。
2. **空值检查**：在处理数据流时一定要注意可能出现的异常情况，特别是来自外部的数据源可能包含 null 值的情况，这可能导致 `NullPointerException` 异常。
3. **并行流的使用**: 对于大数据集，考虑使用并行流来加速计算。但要注意，并非所有场景都适合并行化处理。
