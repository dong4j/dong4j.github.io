---
title: Java 常用代码片段二
keywords:
  - Java
categories:
  - Java
tags:
  - Java
  - 日期时间处理
  - GC日志分析
  - 字符串处理
  - Properties管理
abbrlink: 1bdd319f
date: 2016-10-23 00:00:00
ai:
  - 文章包含了关于Java编程、数据结构与算法、数据库原理、操作系统、Web开发以及网络基础知识等多个领域的专业知识和实践。主要内容涵盖了JDK 8中的日期处理类、JVM参数优化、GC日志分析、字符串操作、Properties对象遍历等具体技术点，同时也提到了一些工具库如Apache
    Commons Lang的使用，并提供了代码示例以辅助理解。
description: 文章包含了关于Java编程、数据结构与算法、数据库原理、操作系统、Web开发以及网络基础知识等多个领域的专业知识和实践。主要内容涵盖了JDK
  8中的日期处理类、JVM参数优化、GC日志分析、字符串操作、Properties对象遍历等具体技术点，同时也提到了一些工具库如Apache Commons Lang的使用，并提供了代码示例以辅助理解。
---

在 Java 开发中，我们经常需要进行字符串的拼接和处理集合中的元素。此外，在某些特定场景下，如性能监控或代码调试时，也需要查看 GC 日志以及字节码信息。本文将详细介绍这些常用技术及其最佳实践。

## 字符串拼接方法

### 使用 `org.apache.commons.lang.StringUtils` 拼接

```java
import org.apache.commons.lang3.StringUtils;

String result = StringUtils.join(array, "-");
```

该方法使用指定的分隔符（如这里的'-'）将数组中的元素连接成一个字符串。

### 使用 Google Guava 的 `Joiner` 类

```java
import com.google.common.base.Joiner;
String result = Joiner.on('-').join(array);
```

Guava 库提供的`Joiner`类可以更加灵活地拼接字符串，支持多种分隔符和自定义转换函数。

## 获取集合中的第一个元素

### 使用 `Iterables.getOnlyElement` 方法

```java
import com.google.common.collect.Iterables;
Object first = Iterables.getOnlyElement(collection);
```

该方法用于确保集合中只有一个元素时获取该元素，如果多个或为空则会抛出异常。适用于确认集合内容的情况下。

### 获取第一个元素并允许指定默认值

```java
Object firstOrDefault = Iterables.getFirst(collection, defaultValue);
```

`Iterables.getFirst` 方法允许在集合为空时返回一个默认值，增加了代码的灵活性和健壮性。

### 直接从迭代器中获取第一个元素

```java
Object first = collection.iterator().next();
```

直接使用`iterator()`并调用`next()`是最基本的方法。适用于快速而简单的场景。

## 查看 GC 日志

为了调试应用程序中的内存问题，可以通过以下参数启动 Java 虚拟机（JVM）以查看详细的垃圾收集(GC)活动：

```bash
java -XX:+PrintGCDetails -jar yourApp.jar
```

此命令会输出每次 GC 事件的详细信息。

## 查看字节码

为了更好地理解类的工作原理或者用于反编译目的，可以使用`javap`工具查看类文件的内容。例如:

```bash
javap -c class_path
```

## 集合操作：并集、交集和差集等

### 示例代码展示集合的各种操作

```java
public static void main(String[] args) {
    List<String> list1 = new ArrayList<>();
    list1.add("A");
    list1.add("B");
    list1.add("C");

    List<String> list2 = new ArrayList<>();
    list2.add("C");
    list2.add("B");
    list2.add("D");

    // 并集
    List<String> unionList = new ArrayList<>(list1);
    unionList.addAll(list2);

    // 去重复并集
    Set<String> tempSet = new HashSet<>();
    tempSet.addAll(unionList);
    unionList.clear();
    unionList.addAll(tempSet);

    System.out.println("去重后的并集： " + unionList);

    // 交集
    List<String> intersectionList = new ArrayList<>(list1);
    intersectionList.retainAll(list2);
    System.out.println("交集: " + intersectionList);

    // 差集
    List<String> diffList = new ArrayList<>(list1);
    diffList.removeAll(list2);
    System.out.println("差集: " + diffList);
}
```

## 通过枚举属性获取枚举实例

### 枚举示例代码展示

```java
enum Gender {
    MALE(0),
    FEMALE(1);

    private int code;

    private static final Map<Integer, Gender> MAP = new HashMap<>();

    static {
        for (Gender item : Gender.values()) {
            MAP.put(item.code, item);
        }
    }

    public int getCode() {
        return code;
    }

    private Gender(int code) {
        this.code = code;
    }
}

public class EnumUtil {

    @SuppressWarnings("unchecked")
    public static <E extends Enum<?>> E getByCode(Class<E> enumClass, int code) {
        try {
            for (E e : enumClass.getEnumConstants()) {
                Field field = e.getClass().getField("code");
                Object value = field.get(e);
                if (value.equals(code)) {
                    return e;
                }
            }
        } catch (Exception ex) {
            throw new RuntimeException("根据code获取枚举实例异常" + enumClass.getName() + " code:" + code, ex);
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(EnumUtil.getByCode(Gender.class, 0));
    }
}
```

## 国际化处理

### 使用 .properties 文件实现国际化

在 Java 程序中，我们可以通过创建和使用`.properties`文件来支持多种语言的国际化的操作。这些文件通常包含键值对的形式存储文本信息，而当需要特定语言版本时，则加载相应的`.properties`文件。

#### `.properties`文件中文字符与 Unicode 字符之间的转换

- 使用`native2ascii.exe`工具可以将`.properties`文件中的中文字符转为 Unicode 格式。
  ```bash
  native2ascii resources.properties tmp.properties 或者
  native2ascii -encoding Unicode resources.properties tmp.properties
  ```
- 若需要再将其转化为中文，使用如下命令：
  ```bash
  native2ascii -reverse -encoding GB2312 resources.properties tmp.properties
  ```

## `switch` vs. `if-else`

### 性能比较

在 Java 中，`switch-case`结构常用于多分支选择。它与`if-else`语句在功能上有一定的重叠。然而，在实际应用时，两者在效率上存在区别：

1. **二叉树算法**：`switch`使用了 Binary Tree 算法而`if-else`顺序比较。
2. **跳转表生成**：对于多个分支的场景下（大于等于四个），`switch`会创建一个最大 case 常量+1 大小的 jump table，这比简单的线性查找效率更高。

## 反射与注解

### 获取方法上的注解

从 Java 7 开始，可以通过反射机制获取类上或方法上的注解信息。下面展示了在 JDK 版本为 7 和 8 时的不同代码实现：

```java
// JDK7方式:
RequestMapping methodDeclaredAnnotation = method.getAnnotation(RequestMapping.class);

// JDK8方式:
RequestMapping methodDeclaredAnnotation = method.getDeclaredAnnotation(RequestMapping.class);
```

## 阅读文件中的内容

使用 Java 标准库可以轻松从资源或文件中读取数据，例如：

```java
InputStream stream = this.getClass().getClassLoader().getResourceAsStream("test.md");
BufferedReader reader = new BufferedReader(new InputStreamReader(stream, "utf-8"));
List<String> list = reader.lines().collect(Collectors.toList());
String content = Joiner.on("\n").join(list);
```

## Java 枚举类的特性

### 为什么`Enum`不能被继承？

在 Java 中，当一个类使用`enum`关键字定义后，默认会继承`java.lang.Enum`。这意味着该枚举类型是不可再扩展的，并且会被编译器标记为 final 以防止任何子类型的创建。

## Timer 类高级用法

### 六种执行任务的方法

```java
import java.util.Calendar;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;
public class TimerUtil {
    public static void main(String[] args) throws Exception {
        System.out.println(new Date().getTime() + "-------开始定时任务--------");
        timer1();
        timer2();
        timer3();
        timer4();
        timer5();
        timer6();
    }
    // 第一种方法：指定任务task在指定时间time执行
    // schedule(TimerTask task, Date time)
    public static void timer1() {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, 0); // 控制时
        calendar.set(Calendar.MINUTE, 0);    // 控制分
        calendar.set(Calendar.SECOND, 0);    // 控制秒
        Date time = calendar.getTime();     // 得出执行任务的时间,此处为今天的00：00：00
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println(new Date().getTime() + "-------定时任务1--------");
            }
        }, time);
    }
    // 第二种方法：指定任务task在指定延迟delay后执行
    // schedule(TimerTask task, long delay)
    public static void timer2() {
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println(new Date().getTime() + "-------定时任务2--------");
            }
        }, 2000); // 指定延迟2000毫秒后执行
    }
    // 第三种方法：指定任务task在指定时间firstTime执行后，进行重复固定延迟频率period的执行
    // schedule(TimerTask task, Date firstTime, long period)
    public static void timer3() {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, 0); // 控制时
        calendar.set(Calendar.MINUTE, 0);    // 控制分
        calendar.set(Calendar.SECOND, 0);    // 控制秒
        Date time = calendar.getTime();     // 得出执行任务的时间,此处为今天的00：00：00
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println(new Date().getTime() + "-------定时任务3--------");
            }
        }, time, 1000 * 60 * 60 * 24);
    }
    // 第四种方法：指定任务task在指定延迟delay后，进行重复固定延迟频率period的执行
    // schedule(TimerTask task, long delay, long period)
    public static void timer4() {
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println(new Date().getTime() + "-------定时任务4--------");
            }
        }, 1000, 5000);
    }
    // 第五种方法：指定任务task在指定时间firstTime执行后，进行重复固定延迟频率period的执行
    // scheduleAtFixedRate(TimerTask task, Date firstTime, long period)
    public static void timer5() {
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, 0); // 控制时
        calendar.set(Calendar.MINUTE, 0);    // 控制分
        calendar.set(Calendar.SECOND, 0);    // 控制秒
        Date time = calendar.getTime();     // 得出执行任务的时间,此处为今天的00：00：00
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                System.out.println(new Date().getTime() + "-------定时任务5--------");
            }
        }, time, 1000 * 60 * 60 * 24);
    }
    // 第六种方法：指定任务task在指定延迟delay后，进行重复固定延迟频率period的执行
    // scheduleAtFixedRate(TimerTask task, long delay, long period)
    public static void timer6() {
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                System.out.println(new Date().getTime() + "-------定时任务6--------");
            }
        }, 1000, 2000);
    }
}
```

## Cron 表达式详解

Cron 表达式的格式由至少 6 个部分组成，每一部分使用空格分隔：

1. 秒 (0-59)
2. 分钟 (0-59)
3. 小时 (0-23)
4. 日期 (0-31)
5. 月份 (0-11 或 JAN-DEC)
6. 星期几 (0-7 或 SUN-SAT，其中 0 和 7 都表示周日)

### 常用实例

#### 每隔若干时间执行

- 每隔 5 秒：`*/5 * * * * ?`
- 每隔 1 分钟：`0 */1 * * * ?`

#### 定时任务

- 每天 23 点执行：`0 0 23 * * ?`
- 每日凌晨 1 点执行：`0 0 1 * * ?`
- 每月 1 号凌晨 1 点执行：`0 0 1 1 * ?`

#### 复杂任务调度

- 每天的 0 点、13 点、18 点和 21 点触发一次任务：`0 0 0,13,18,21 * * ?`
- 在每天上午 10:15 执行：`0 15 10 * * ?`

### Cron 表达式高级用法

- 每月最后一天晚上 11 点触发一次任务：`0 0 23 L * ?`
- 每年的某个特定星期几（如每周三）的某时执行：`0 0 12 ? * WED`

### 特殊字符的意义

- `*`: 所有可能值。
- `,`: 分隔列表中的多个值。
- `-`: 表示区间，如 `6-8/2` 表示在第 6、8 分钟时执行任务。
- `/`: 指定增量步长。

## 解决`java.lang.OutOfMemoryError: PermGen space`

### 常见的解决方案

```bash
-server -XX:PermSize=256M -XX:MaxPermSize=512m
```

这行命令可以通过调整永久代（Permanent Generation）的空间大小来解决内存溢出问题。

## 使用 CXF 生成客户端代码

Apache CXF 提供了 wsdl2java 工具用于从 WSDL 文件自动生成 Java 客户端代码。其基本使用方法如下：

```bash
/opt/apache-cxf-3.2.5/bin/wsdl2java -client -encoding utf-8 'http://172.16.4.207/iavpwebservice/CallOut.asmx?wsdl'
```

## JDK 8 中推荐使用的日期处理类

JDK 8 引入了新的日期和时间 API，包括`Instant`, `LocalDateTime`, 和 `DateTimeFormatter`等。这些新工具比旧的`Date`和`Calendar`更强大且易于使用。

### 示例代码

```java
// 得到小时
private int getHour(Date date) {
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    return calendar.get(Calendar.HOUR_OF_DAY);
}

// 得到分钟
private int getMinute(Date date) {
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    return calendar.get(Calendar.MINUTE);
}

// 设置小时
private Date setHour(int hour, Date date) {
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    calendar.set(Calendar.HOUR_OF_DAY, hour);
    return calendar.getTime();
}

// 设置分钟
private Date setMinute(int minute, Date date) {
    Calendar calendar = Calendar.getInstance();
    calendar.setTime(date);
    calendar.set(Calendar.MINUTE, minute);
    return calendar.getTime();
}
```

## 打印 GC 详情

为了能够获得详细的 GC 信息，包括每次垃圾回收的时间、持续时间和应用程序暂停时间等细节数据，可以在启动 JVM 时添加以下选项：

```bash
java -XX:+PrintGCTimeStamps
-XX:-PrintClassHistogram
-XX:+PrintHeapAtGC
-verbose:gc
-XX:+PrintGCDetails
-XX:+PrintGCTimeStamps
-XX:+PrintGCApplicationStoppedTime
-XX:+HeapDumpOnOutOfMemoryError
```

这些选项的作用分别是：

1. `-XX:+PrintGCTimeStamps` - 每次垃圾回收都记录时间戳；
2. `-XX:-PrintClassHistogram` - 打印类的直方图（通常在 Full GC 后打印）；
3. `-XX:+PrintHeapAtGC` - 在每次垃圾回收之前输出堆信息；
4. `-verbose:gc` - 输出简要的 GC 日志信息；
5. `-XX:+PrintGCDetails` - 打印详细的 GC 日志。

## 移除字符串中的所有空格

在处理文本数据时，经常需要去除不必要的空白字符。以下是几种有效的移除方法：

### 使用 Apache Commons Lang 库

最简单直接的方法是使用第三方库如 Apache Commons Lang 的`StringUtils.deleteWhitespace()`函数。

```java
import org.apache.commons.lang3.StringUtils;

public class StringProcessor {
    public static void main(String[] args) {
        System.out.println(StringUtils.deleteWhitespace(" a b c d "));
    }
}
```

### 手动实现去除所有空格

1. 使用正则表达式替换：

   ```java
   public class MainClass {
       public static void main(String[] args) {
           String str = " hell o ";
           System.out.println(str.replaceAll("\\s+", ""));
       }
   }
   ```

2. 遍历字符串中的每个字符，并使用`StringBuilder`构建新字符串：

   ```java
   public class MainClass {
       public static void main(String[] args) {
           String str = " a b c d ";
           StringBuilder sb = new StringBuilder();
           for (int i = 0; i < str.length(); i++) {
               if (!Character.isWhitespace(str.charAt(i))) {
                   sb.append(str.charAt(i));
               }
           }
           System.out.println(sb.toString());
       }
   }
   ```

3. 使用`replaceAll()`方法处理连续的空格：
   ```java
   public class MainClass {
       public static void main(String[] args) {
           String str = " hell o ";
           str = str.replaceAll(" +", "");
           System.out.println(str);
       }
   }
   ```

## 遍历 Properties 对象

`Properties`类提供了多种遍历其内部数据的方式，以下是一个简单的示例：

```java
public static void printProp(Properties properties) {
    System.out.println("---------（方式一）------------");
    for (String key : properties.stringPropertyNames()) {
        System.out.println(key + "=" + properties.getProperty(key));
    }

    System.out.println("---------（方式二）------------");
    Set<Object> keys = properties.keySet();
    for (Object key : keys) {
       System.out.println(key.toString() + "=" + properties.get(key));
    }

    System.out.println("---------（方式三）------------");
    Set<Map.Entry<Object, Object>> entrySet = properties.entrySet();
    for (Map.Entry<Object, Object> entry : entrySet) {
        System.out.println(entry.getKey() + "=" + entry.getValue());
    }

    System.out.println("---------（方式四）------------");
    Enumeration<?> e = properties.propertyNames();
    while (e.hasMoreElements()) {
       String key = (String) e.nextElement();
       String value = properties.getProperty(key);
        System.out.println(key + "=" + value);
   }
}
```
