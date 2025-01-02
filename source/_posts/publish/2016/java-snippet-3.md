---
title: Java 基础：一些常用代码片段三
keywords:
  - Java
  - ClassLocationUtils
  - 定时任务
  - StringBuffer
  - List
  - 反射
  - 排序
  - 遍历Map
  - 日期处理
  - Math类
  - 单例模式
categories:
  - 新时代码农
tags:
  - Java
  - ClassLocationUtils
  - 定时任务
  - StringBuffer
  - List
  - 反射
  - 排序
  - 遍历Map
  - 日期处理
  - Math类
  - 单例模式
abbrlink: 5981a792
date: 2016-10-27 00:00:00
ai:
  - 本文介绍了Java中动态获取加载的JAR包位置的工具方法`ClassLocationUtils.where(cls)`。此外，还探讨了三种实现定时任务的方法：使用普通Thread、java.util.Timer和java.util.concurrent.ScheduledExecutorService。文章还涉及了去除字符串拼接时的最后一个多余逗号、将List对象转换为带分隔符的字符串、利用反射机制根据完整类名获取类对象、多条件排序ArrayList以及遍历Map对象的几种方法。此外，还介绍了使用`SimpleDateFormat`进行日期和字符串转换的方法，Math类的常用方法，单例模式的实现方式及其注意事项。
description: 本文介绍了Java中动态获取加载的JAR包位置的工具方法`ClassLocationUtils.where(cls)`。此外，还探讨了三种实现定时任务的方法：使用普通Thread、java.util.Timer和java.util.concurrent.ScheduledExecutorService。文章还涉及了去除字符串拼接时的最后一个多余逗号、将List对象转换为带分隔符的字符串、利用反射机制根据完整类名获取类对象、多条件排序ArrayList以及遍历Map对象的几种方法。此外，还介绍了使用`SimpleDateFormat`进行日期和字符串转换的方法，Math类的常用方法，单例模式的实现方式及其注意事项。
---

## 动态获取加载的 Jar 包

有时我们需要在运行时确定一个特定类所对应的 JAR 包或目录的位置。为此我们提供了`ClassLocationUtils.where(cls)`这个静态工具方法来帮助识别指定类的来源文件。

```java
import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.security.CodeSource;
import java.security.ProtectionDomain;

public class ClassLocationUtils {

    public static String where(final Class<?> cls) {
        if (cls == null)throw new IllegalArgumentException("null input: cls");
        URL result = null;
        final String clsAsResource = cls.getName().replace('.', '/').concat(".class");
        final ProtectionDomain pd = cls.getProtectionDomain();
        if (pd != null) {
            final CodeSource cs = pd.getCodeSource();
            if (cs != null) result = cs.getLocation();
            if ("file".equals(result.getProtocol())) {
                try {
                    if (result.toExternalForm().endsWith(".jar") ||
                            result.toExternalForm().endsWith(".zip"))
                        result = new URL("jar:".concat(result.toExternalForm())
                                .concat("!/").concat(clsAsResource));
                    else if (new File(result.getFile()).isDirectory())
                        result = new URL(result, clsAsResource);
                } catch (MalformedURLException ignore) { }
            }
        }
        if (result == null) {
            final ClassLoader clsLoader = cls.getClassLoader();
            result = clsLoader != null ?
                    clsLoader.getResource(clsAsResource) :
                    ClassLoader.getSystemResource(clsAsResource);
        }
        return result.toString();
    }
}
```

### 方法解释

- **获取类的资源表示**：首先，将提供的类名转换成资源路径的形式（例如，`com/example/MyClass.class`）。
- **获取代码源位置**：通过调用`ProtectionDomain.getCodeSource()`方法可以找到该类所在 JAR 或目录的位置。
- **处理文件 URL**：如果 URL 协议是“file”，则进一步检查它是否指向一个 ZIP/JAR 文件，如果是，则构建一个新的 URL 来表示内部的资源路径；如果不是 ZIP/JAR，并且是一个目录，则直接使用`URL.openConnection()`方法尝试获取到相应的类文件。

### 使用场景

在进行调试或分析时，此工具可以非常有用。例如，在 IDE 中设置断点后输入 `ClassLocationUtils.where(xxx.class)` 可以快速得到当前被加载的 JAR 包路径。

## 实现定时任务的三种方法

Java 提供了多种实现定时执行任务的方式，这里介绍了其中最常见的三种方式：

### 方法一：使用普通 Thread

这种方式是通过创建一个线程并让其在无限循环中执行指定的任务，并且在每次运行之间设置一定的延时。虽然简单易行，但它缺乏对任务启动和停止的控制。

```java
public class Task1 {
    public static void main(String[] args) {
        final long timeInterval = 1000; // 每秒执行一次
        new Thread(() -> {
            while (true) {
                System.out.println("Hello !!");
                try {
                    Thread.sleep(timeInterval);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}
```

### 方法二：使用`java.util.Timer`

这种方法提供了对任务启动和取消的控制能力，并允许指定延迟执行的时间间隔。缺点是仅支持单线程操作。

```java
import java.util.Timer;
import java.util.TimerTask;

public class Task2 {
    public static void main(String[] args) {
        Timer timer = new Timer();
        TimerTask task = () -> System.out.println("Hello !!!");

        // 第二个参数为延迟时间，第三个为每次执行任务的时间间隔
        timer.scheduleAtFixedRate(task, 0, 1000);
    }
}
```

### 方法三：使用`java.util.concurrent.ScheduledExecutorService`

这是 Java SE5 引入的一个高级定时任务处理类。它提供了更灵活的任务调度方式，支持多线程执行，并且能方便地设置首次执行的延迟时间。

```java
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class Task3 {
    public static void main(String[] args) {
        ScheduledExecutorService service = Executors.newSingleThreadScheduledExecutor();

        // 第二个参数为首次执行的延时时间，第三个为每次执行任务的时间间隔
        service.scheduleAtFixedRate(() -> System.out.println("Hello !!"), 10, 1, TimeUnit.SECONDS);
    }
}
```

## 拼接字符串时去除最后一个多余的逗号

当我们在 Java 中进行字符串拼接操作时，可能会遇到需要移除最后一个多余逗号的情况。下面的例子展示了如何使用 `StringBuffer` 类来实现这一功能：

```java
String str[] = { "hello", "beijing", "world", "shenzhen" };
StringBuffer buf = new StringBuffer();

for (int i = 0; i < str.length; i++) {
    buf.append(str[i]).append(",");
}

if (buf.length() > 0) {
    //方法一  : substring
    System.out.println(buf.substring(0, buf.length()-1));
    //方法二 ：replace
    System.out.println(buf.replace(buf.length() - 1, buf.length(), ""));
    //方法三： deleteCharAt
    System.out.println(buf.deleteCharAt(buf.length()-1));
}
```

上述代码中，我们通过 `substring`、`replace` 和 `deleteCharAt` 方法实现了对最后一个逗号的移除。

## 将 List 对象转换为带分隔符的字符串

有时我们需要将一个 `List` 类型的对象转换成包含特定分隔符的字符串。这里提供了一些实现此功能的方法：

```java
// 方法一：
public String listToString(List list, char separator) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i <list.size(); i++) {
        sb.append(list.get(i)).append(separator);
    }
    return list.isEmpty()?"":sb.toString().substring(0, sb.toString().length() - 1);
}

// 方法二：
public String listToString2(List list, char separator) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i <list.size(); i++) {
        if (i == list.size() - 1) {
            sb.append(list.get(i));
        } else {
            sb.append(list.get(i)).append(separator);
        }
    }
    return sb.toString();
}

// 方法三：
public String listToString3(List list, char separator) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i <list.size(); i++) {
        sb.append(list.get(i));
        if (i < list.size() - 1) {
            sb.append(separator);
        }
    }
    return sb.toString();
}

// 方法四：
public class Separator {
    private String next = "";
    private String separator;

    public Separator(String separator) {
        this.separator = separator;
    }

    public String get() {
        String result = next;
        next = separator;
        return result;
    }
}

public String listToString4(List<String> list, Separator separator) {
    StringBuilder sb = new StringBuilder();
    for (String s : list) {
        if (s != null && !"".equals(s)) {
            sb.append(separator.get()).append(s);
        }
    }
    return sb.toString();
}

// 方法五：
public String listToString5(List list, char separator) {
    return org.apache.commons.lang.StringUtils.join(list.toArray(),separator);
}
```

这些方法各具特点，可以根据具体需求选择最合适的实现。

## 利用反射机制根据完整类名获取类对象

Java 的反射机制允许我们动态地创建、访问和操作类及其成员。以下是一个通过反射加载并使用配置文件中指定的类实例的例子：

```java
public class Test {
    public static void main(String[] args) throws Exception {
        Properties properties = new Properties();
properties.load(Test.class.getClassLoader().getResourceAsStream("com/lsd/beanfactory/ApplicationContext.properties"));//根据配置文件的路径加载对象
        String key = properties.getProperty("vehicle");//根据key获取value
        Class c = Class.forName(key);
        System.out.println(key);
        Object object = c.newInstance();
        Vehicle vehicle = (Vehicle) object;
        vehicle.run();
    }
}
```

这段代码首先从 `Properties` 对象中读取配置文件中的类名，然后使用反射机制加载指定的类，并实例化对象最后调用该对象的方法。这在框架设计和依赖注入场景下非常有用。

## 使用多条件排序 ArrayList

当需要根据多个属性进行复杂的排序时，Java 提供了灵活的机制来实现这一点。下面的例子展示了如何使用自定义比较器对包含员工信息的 `ArrayList` 进行排序：

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class TestComparator {
    public static void main(String[] args) {

        ArrayList<Person> persons = new ArrayList<>();
        persons.add(new Person(10, 1000, 4));
        persons.add(new Person(1, 1020, 5));
        persons.add(new Person(1, 1020, 4));
        persons.add(new Person(13, 1100, 2));
        persons.add(new Person(1, 1020, 5));

        // 打印排序前的列表
        for (Person person : persons) {
            System.out.println(person);
        }
        System.out.println();

        // 使用自定义比较器进行多条件排序（级别、薪资和年份）
        Collections.sort(persons, new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                if (o1.level == o2.level) {
                    if (o1.salary == o2.salary) {
                        return Integer.compare(o2.years, o1.years);
                    } else {
                        return Integer.compare(o2.salary, o1.salary);
                    }
                } else {
                    return Integer.compare(o2.level, o1.level);
                }
            }
        });

        // 打印排序后的列表
        for (Person person : persons) {
            System.out.println(person);
        }
    }

    static class Person {
        int level;  // 级别
        int salary; // 薪资
        int years;  // 入职年数

        public Person(int level, int salary, int years) {
            this.level = level;
            this.salary = salary;
            this.years = years;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "level=" + level +
                    ", salary=" + salary +
                    ", years=" + years +
                    '}';
        }
    }
}
```

上述代码展示了如何根据多个属性进行排序。我们首先定义了一个 `Comparator`，并在其中实现了多条件的比较逻辑：先按照级别降序排列；如果级别相同，则按薪资降序排列；最后，在级别和薪资都相同时按入职年数升序排列。

## 遍历 Map 的几种方法

在 Java 中遍历 `Map` 对象有多种方式，以下是常用的四种方法：

### 使用 for 循环迭代

```java
Map<String, String> map = new HashMap<>();
map.put("username", "qq");
map.put("password", "123");  // 注意此处拼写修正
map.put("userID", "1");
map.put("email", "qq@qq.com");

for (Map.Entry<String, String> entry : map.entrySet()) {
    System.out.println(entry.getKey() + "-->" + entry.getValue());
}
```

### 使用 Iterator 进行迭代

```java
Set<Map.Entry<String, String>> set = map.entrySet();
Iterator<Map.Entry<String, String>> iterator = set.iterator();

while (iterator.hasNext()) {
    Map.Entry<String, String> entry = iterator.next();
    System.out.println(entry.getKey() + "==" + entry.getValue());
}
```

### 使用 keySet 进行迭代

```java
Iterator<String> it = map.keySet().iterator();

while(it.hasNext()){
    String key = it.next();
    String value = map.get(key);
    System.out.println(key+"--"+value);
}
```

### 使用 entrySet 进行迭代

```java
Iterator<Map.Entry<String, String>> it = map.entrySet().iterator();
System.out.println(map.entrySet().size());

while(it.hasNext()){
    Map.Entry<String, String> entry = it.next();
    String key = entry.getKey();
    String value = entry.getValue();
    System.out.println(key+"===="+value);
}
```

每种方法都有其适用的场景，根据实际需求选择合适的遍历方式可以提高代码效率和可读性。例如，在需要频繁访问 `entry` 对象时，直接使用 `for-each` 循环是最简单且高效的；如果对性能有较高要求，则可以通过提前获取 `Iterator` 对象来减少创建实例的开销。

## 使用 `SimpleDateFormat` 进行日期和字符串转换

在处理日期时，Java 提供了强大的 API 来进行格式化操作。下面的例子展示了如何将 `Date` 对象转化为指定格式的字符串：

### 字符串转日期

```java
public static Date stringToDate(String dateStr) throws ParseException {
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    return sdf.parse(dateStr);
}
```

给定一个日期时间字符串（例如 "2002-10-8 15:30:22"），可以使用 `SimpleDateFormat` 的 `parse` 方法将其解析为 `Date` 对象：

```java
try {
    Date date = sdf.parse("2002-10-8 15:30:22");
} catch (ParseException e) {
    // 处理异常情况
}
```

### 日期转字符串

```java
public static String dateToString(Date time){
    SimpleDateFormat formatter;
    formatter = new SimpleDateFormat ("yyyy-MM-dd HH:mm:ss");
    return formatter.format(time);
}
```

要将当前时间格式化为字符串，可以使用 `SimpleDateFormat` 的 `format` 方法：

```java
String datestr = sdf.format(new Date());
// 输出类似：2002-10-08 14:55:38
```

## Math 类常用方法

Java 提供了丰富的数学计算工具类，即 `Math`。以下是一个简单的示例：

```java
class MathTest {
    public static void main(String[] args) {
        System.out.println("ceil    向上取整 " + Math.ceil(11.2));
        System.out.println("floor   向下取整 " + Math.floor(11.8));
        System.out.println("rint    四舍五入取浮点 " + Math.rint(-11.1));
        System.out.println("round   四舍五入取整 " + Math.round(-11.1));
    }
}
```

输出结果如下：

- `ceil` 方法将数值向上取整，即向正无穷方向取最近的整数；
- `floor` 方法将数值向下取整，即向负无穷方向取最近的整数；
- `rint` 返回最接近参数的整数值的双精度浮点数；
- `round` 将参数四舍五入到最邻近的整数。

## 单例模式实现

单例模式是一种常用的软件设计模式，确保一个类只有一个实例，并提供全局访问点。以下是几种常见的实现方式：

### 懒汉式（线程不安全）

```java
public class Singleton {
    private static Singleton instance;
    private Singleton() {}

    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

这种方式在多线程环境中可以正常工作，但效率较低。99%的情况下不需要同步。

### 饿汉式

```java
public class Singleton {
    private static final Singleton INSTANCE = new Singleton();

    private Singleton() {}

    public static Singleton getInstance() {
        return INSTANCE;
    }
}
```

此方式利用类加载机制避免了多线程问题，但在加载时会立即创建实例。

### 静态内部类实现

```java
public class Singleton {
    private static class SingletonHolder {
        private static final Singleton INSTANCE = new Singleton();
    }

    private Singleton() {}

    public static final Singleton getInstance() {
        return SingletonHolder.INSTANCE;
    }
}
```

这种方式使用了 `classloader` 机制确保线程安全，并且在需要时才创建实例。

### 枚举实现

```java
public enum Singleton {
    INSTANCE;

    public void whateverMethod() {}
}
```

枚举单例模式是高效且线程安全的，但可能会让人感觉生疏，不常用。

### 双重检查锁实现（JDK 1.5+）

```java
public class Singleton {
    private volatile static Singleton singleton;
    private Singleton() {}

    public static Singleton getSingleton() {
        if (singleton == null) {
            synchronized (Singleton.class) {
                if (singleton == null) {
                    singleton = new Singleton();
                }
            }
        }
        return singleton;
    }
}
```

这种方式结合了延迟加载和线程安全的优点，但在某些情况下可能因 `volatile` 而影响性能。

## 注意事项

1. **类装载器**：如果单例由不同的类装载器装入，则有可能创建多个实例。例如，在一些 Servlet 容器中对每个 Servlet 使用完全不同的类装载器。
2. **序列化与反序列化**：
   - 如果实现了 `Serializable` 接口，可以添加一个 `readResolve()` 方法来确保单例模式在反序列化后仍只有一个实例。

### 修复示例

```java
private static Class<?> getClass(String classname) throws ClassNotFoundException {
    ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
    if (classLoader == null)
        classLoader = Singleton.class.getClassLoader();
    return classLoader.loadClass(classname);
}
```
