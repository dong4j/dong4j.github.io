---
title: Java 常用代码片段一
keywords:
  - Java
categories:
  - Java
tags:
  - Java
  - 数学运算
  - BigDecimal
  - 精确浮点数
  - double与BigDecimal转换
  - 四舍五入
abbrlink: 205d1f36
date: 2016-10-22 00:00:00
ai:
  - 本文详细介绍了Java编程中关于BigDecimal类的理解与应用，重点探讨了其在处理浮点数运算时的精度问题以及如何使用它进行精确算术操作。文章提供了精确加减乘除方法的实现，并讨论了四舍五入机制和精度控制的重要性。
description: 本文详细介绍了Java编程中关于BigDecimal类的理解与应用，重点探讨了其在处理浮点数运算时的精度问题以及如何使用它进行精确算术操作。文章提供了精确加减乘除方法的实现，并讨论了四舍五入机制和精度控制的重要性。
---

本文将详细介绍几种常见的 Java 编程技术及其相关知识点，并提供一些最佳实践和注意事项。这些内容包括面向切面编程（AOP）、使用 Jackson 进行泛型反序列化、单次执行逻辑的实现方法，以及防止主线程退出等。

## 面向切面编程 (Aspect-Oriented Programming, AOP)

### 代码片段展示

```java
try {
    try {
        doBefore(); // 对应@Before注解的方法切面逻辑
        method.invoke();
    } finally {
        doAfter(); //对应@After注解的方法切面逻辑
    }
    doAfterReturning(); //对应@AfterReturning注解的方法切面逻辑
} catch (Exception e) {
    doAfterThrowing(); // 对应@AfterThrowing注解的方法切面逻辑
}
```

### 解释与注意事项

AOP 是一种编程范式，用于将横切关注点（如日志、事务处理等）从核心业务逻辑中分离出来。上述代码展示了如何通过 try-catch-finally 结构来模拟 AOP 中的通知执行顺序。

- **最佳实践**：

  - 确保`doBefore()`方法在主要业务逻辑开始之前被调用。
  - `doAfterReturning()`应在业务逻辑成功返回时被触发，表示正常结束。
  - `catch`块内的`doAfterThrowing()`用于捕获并处理任何异常。

- **注意事项**：
  - 考虑到代码可维护性与扩展性，在实际应用中应使用 Spring AOP 框架或其他成熟的 AOP 工具库来实现这些逻辑，而不是手动复制粘贴上述结构。

## 使用 Jackson 进行泛型反序列化

### 代码片段展示

```java
CollectionType javaType = mapper.getTypeFactory().constructCollectionType(List.class, MyDto.class);
List<MyDTO> asList = mapper.readValue(jsonArray, javaType);
```

### 解释与注意事项

当需要将 JSON 字符串解析为带有泛型类型的列表时，Jackson 库提供了一种简便的方法。

- **最佳实践**：
  - 使用`constructCollectionType()`方法来指定具体的集合类型及元素类型。
  - 尽可能保持序列化和反序列化的数据结构一致，以避免出现不必要的错误或不兼容问题。

## 单次执行逻辑的实现

### 代码片段展示

```java
AtomicBoolean WARNED_TOO_MANY_INSTANCES = new AtomicBoolean();

if(WARNED_TOO_MANY_INSTANCES.compareAndSet(false, true)){
    xxxx //具体操作逻辑
}
```

### 解释与注意事项

此段代码使用了`AtomicBoolean`类来确保某段特定的执行逻辑在整个程序生命周期中仅被执行一次。

- **最佳实践**：
  - 使用原子性数据类型如`AtomicBoolean`可以有效避免多线程环境下的竞态条件问题。

## 分割字符串为迭代器

### 代码片段展示

```java
Splitter.on(",").trimResults().omitEmptyStrings().split(str)
```

- **最佳实践**：
  - 使用 Guava 库的`Splitter`类可以更灵活地处理复杂的文本分割任务，支持多种配置选项（如忽略空字符串、修剪结果等）。

## Slf4j 占位符格式化

### 代码片段展示

```java
FormattingTuple ft = MessageFormatter.arrayFormat(appendLogPattern, appendLogArguments);
```

- **最佳实践**：
  - 使用`MessageFormatter`类可以避免硬编码字符串中的占位符，从而提高日志信息的可读性和易管理性。

## 防止 Java 主线程退出

### 实现代码展示

```java
public class StartMain {

    private static final ReentrantLock LOCK = new ReentrantLock();
    private static final Condition STOP = LOCK.newCondition();

    public static void main(String[] args) {
        AbstractApplicationContext applicationContext = new ClassPathXmlApplicationContext("applicationContext.xml");
        applicationContext.start();
        logger.info("service start success !~");
        addHook(applicationContext);
        try {
            LOCK.lock();
            STOP.await();
        } catch (InterruptedException e) {
            logger.warn(" service   stopped, interrupted by other thread!", e);
        } finally {
            LOCK.unlock();
        }
    }

    private static void addHook(AbstractApplicationContext applicationContext) {
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try {
                applicationContext.stop();
            } catch (Exception e) { logger.error("StartMain stop exception ", e); }

            logger.info("jvm exit, all service stopped.");
            LOCK.lock();
            STOP.signal();
        }, "StartMain-shutdown-hook"));
    }

}
```

- **最佳实践**：
  - 在应用程序的入口点注册一个`shutdown hook`，确保在 JVM 退出前能够正常关闭服务。

## BeanDefinitionRegistryPostProcessor 的应用

### 示例代码展示

```java
@Component
public class RegistryDemo implements BeanDefinitionRegistryPostProcessor {
    @Override
    public void postProcessBeanDefinitionRegistry(BeanDefinitionRegistry beanDefinitionRegistry) throws BeansException {
        GenericBeanDefinition definition = new GenericBeanDefinition();
        definition.setBeanClass(Demo.class); //设置类
        definition.setScope("singleton"); //设置scope
        definition.setLazyInit(false); //设置是否懒加载
        definition.setAutowireCandidate(true); //设置是否可以被其他对象自动注入
        beanDefinitionRegistry.registerBeanDefinition("demo", definition);
    }
}
```

- **最佳实践**：
  - 使用`BeanDefinitionRegistryPostProcessor`可以在 Spring 容器启动之前对 bean 的定义进行自定义修改。

## instanceof, isInstance, isAssignableFrom 的区别

### 解释与实例分析

```java
String s = new String("javaisland");

// true，自身实例或子类实例 instanceof 自身类
System.out.println(s instanceof String);

// 使用Class类的isInstance(Object obj)方法进行测试。
// 正确的测试应为：自身类.class.isInstance(自身实例或子类实例)
String s = new String("javaisland");
System.out.println(String.class.isInstance(s)); // true

// Class 类的 isAssignableFrom (Class cls) 方法
System.out.println(ArrayList.class.isAssignableFrom(Object.class));  // false
System.out.println(Object.class.isAssignableFrom(ArrayList.class));  // true
```

- **最佳实践**：
  - 在编程中，根据具体的使用场景选择合适的方法来检测类型关系。对于对象实例的直接判断，`instanceof`运算符通常是最简单直接的选择。

## Dubbo 百分数与 Double 互转

### 百分数转 Double

```java
// import java.text.NumberFormat;
// import java.text.ParseException;

try {
    // 接口返回的是Number对象，但是实际是Double类型
    Double num = (Double) NumberFormat.getInstance().parse("67.89%");  // 转换的结果是67.89

    // 使用 getPercentInstance() 方法来正确解析百分比字符串为Double类型的值，结果会转换成真正的百分比值，即0.6789
    Double num2 = (Double) NumberFormat.getPercentInstance().parse("67.89%");  // 转换的结果是0.6789

    System.out.println(num);
} catch (ParseException e) {
    e.printStackTrace();
}
```

### Double 转百分数

```java
// import java.text.NumberFormat;
try {
    NumberFormat percentInstance = NumberFormat.getPercentInstance(); // 创建一个格式化为百分比的NumberFormatter对象
    percentInstance.setMaximumFractionDigits(2);  // 设置最多保留两位小数

    String formattedValue = percentInstance.format(0.81247);  // 将Double类型转换为包含两位小数的字符串，例如"81.25%"

    System.out.println(formattedValue);
} catch (Exception e) {
    // 这里不需要捕获ParseException，因为format方法不会抛出该异常
}
```

## Lombok 注解详解

Lombok 是一个强大的 Java 库，用于减少样板代码。

- `@val`: 类似于 final 的变量声明。
- `@var`: 与 JDK10 中的`var`关键字类似。
- `@Data`: 自动为类生成`get`/`set`方法，并且实现`equals`、`hashCode`和`toString`等方法。
- `@Setter`, `@Getter`: 分别用于自动生成所有或特定字段的 setter/getter 方法。
- `@NotNull`: 指定参数不能为 null，否则抛出异常。
- `@Synchronized`: 对于指定的方法添加同步控制。
- `@Builder`: 使用 builder 模式来创建对象实例。
- `@NoArgsConstructor`, `@AllArgsConstructor`: 分别提供无参构造器和全参构造器。
- `@Accessors(chain = true)`: 使得 setter 方法返回当前对象本身，用于链式调用。
- `@RequiredArgsConstructor`: 为类生成一个带有所有 final 字段或标记为`@NonNull`的构造函数。
- `@UtilityClass`, `@ExtensionMethod`, `@FieldDefaults`: 提供工具类、扩展父类和设置属性的访问级别等特性。
- `@Cleanup`: 确保在使用完流资源后自动关闭它们。

### 注意事项

当使用 Lombok 的 `Builder` 注解时，如果想要为某个字段指定默认值，并且希望这个默认值不会被清除，则需要额外添加 `@lombok.Builder.Default` 注解到该属性上。这允许你定义一个初始值，即使在未提供特定构造参数的情况下也能保持其有效性。

## 使用 Lombok @Builder 导致默认值无效

```java
// 示例代码展示如何正确使用 @Builder 和 @lombok.Builder.Default 来确保默认值不被清除。
public class User {
    private String name;
    private int age;

    // 使用 Lombok 的 Builder 注解来创建用户对象
    @Builder
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // 为 'age' 字段添加默认值，同时使用 @lombok.Builder.Default 确保其不会在构建时被清除。
    @Builder.Default
    private int defaultAge = 20; // 设置一个默认年龄

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
}
```

## Optional 类的使用

`Optional`类提供了处理可能为空的对象的方式，避免了空指针异常。

```java
public class Java8Tester {
   public static void main(String args[]){

      Java8Tester java8Tester = new Java8Tester();

      // 传入的两个参数值分别是 null 和一个整数实例化后的对象
      Integer value1 = null;
      Integer value2 = new Integer(10);

      // Optional.ofNullable - 允许传递为 null 参数，用于创建Optional实例。
       Optional<Integer> a = Optional.ofNullable(value1);

      // Optional.of - 如果传递的参数是null, 抛出异常 NullPointerException
      Optional<Integer> b = Optional.of(value2);

      System.out.println(java8Tester.sum(a,b));
   }

   public Integer sum(Optional<Integer> a, Optional<Integer> b){
        boolean valueExistsA = a.isPresent(); // 判断值是否存在
        boolean valueExistsB = b.isPresent();

        System.out.println(" 第一个参数值存在: " + valueExistsA);
        System.out.println(" 第二个参数值存在: " + valueExistsB);

        Integer valA = a.orElse(new Integer(0)); // 如果值存在，返回它；否则使用默认值。

       Integer valB = b.get();  // 获取值, 值需要存在
      return valA + valB;
   }
}
```

## Spring 读取 Classpath 下的文件

### 方法一：利用 `this.getClass().getResource()` 或 `this.getClass().getResourceAsStream()`

这两种方式适用于从当前类资源路径中获取指定文件或流对象。

```java
// 获取文件或流，注意"/"开头代表根目录下的位置
String path = this.getClass().getResource("/"+fileName).getPath();

InputStream inputStream = this.getClass().getResourceAsStream(failName); // 注意变量名拼写错误，应该是 fileName
```

### 方法二：通过 `org.springframework.util.ResourceUtils.getFile()`

此方法返回一个`File`对象，方便文件操作。

```java
// 获取资源路径下的文件
File file = org.springframework.util.ResourceUtils.getFile("classpath:test.txt");
```

### 方法三：使用 `ClassPathResource` 类

这个类提供了更强大的功能去访问 classpath 中的资源，并且能够直接获取到文件或输入流。

```java
import org.springframework.core.io.ClassPathResource;

// 获取资源路径下的文件
ClassPathResource classPathResource = new ClassPathResource("test.txt");
File file = classPathResource.getFile();
InputStream inputStream = classPathResource.getInputStream();
```

### 特别注意：读取 Jar 包中的文件

如果你的文件被存放在 jar 包中，可以通过类加载器来获取资源。

```java
// 通过当前线程的上下文类装载器获取资源
InputStream io = Thread.currentThread().getContextClassLoader().getResourceAsStream("test.txt");

// 或者使用当前类的类加载器
InputStream io = getClass().getClassLoader().getResourceAsStream("test.txt");
```

## BigDecimal 的基本操作与运算

`BigDecimal` 是 Java 中用于精确浮点数计算的重要工具，特别适合于金融或科学计算等领域。它提供了丰富的构造方法和操作方法。

### 常见的构造器

- `BigDecimal(int)`：创建一个具有指定整数值的对象。
- `BigDecimal(double)`：使用 double 类型参数初始化对象。（注意，double 转换为 BigDecimal 时会丢失精度）
- `BigDecimal(long)`：创建一个具有指定长整数值的对象。
- `BigDecimal(String)`：基于字符串表示的值来构造。

### 常见的方法

- `add(BigDecimal)`: 合并两个 BigDecimal 对象的值，返回一个新的对象。
- `subtract(BigDecimal)`: 从第一个参数中减去第二个参数的值，得到的结果存储在新的对象中。
- `multiply(BigDecimal)`: 将两个参数相乘后的结果放在一个新对象里返回。
- `divide(BigDecimal)`: 返回除法运算后的新 BigDecimal 对象。需要特别注意的是，这个方法会抛出 ArithmeticException 异常，除非调用者指定了适当的舍入模式。
- `toString()`: 把 BigDecimal 转换为 String 类型的表示形式。
- `doubleValue()`, `floatValue()`, `longValue()`, `intValue()`：分别将值转换成 double, float, long 和 int 型数据。

### 精确浮点数运算工具类

下面是一个实现精确算术操作，包括加法、减法、乘法以及除法（可指定精度）的示例。

```java
import java.math.BigDecimal;

/**
 * 提供精确的浮点数运算, 包括加减乘除及四舍五入等。
 */
public class ArithUtil {
    // 默认的除法运算结果保留10位小数
    private static final int DEF_DIV_SCALE = 10;

    private ArithUtil() {}

    /**
     * 加法运算
     *
     * @param v1 被加数
     * @param v2 加数
     * @return 和值
     */
    public static double add(double v1, double v2) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.add(b2).doubleValue();
    }

    /**
     * 减法运算
     *
     * @param v1 被减数
     * @param v2 减数
     * @return 差值
     */
    public static double sub(double v1, double v2) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.subtract(b2).doubleValue();
    }

    /**
     * 乘法运算
     *
     * @param v1 被乘数
     * @param v2 乘数
     * @return 积
     */
    public static double mul(double v1, double v2) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.multiply(b2).doubleValue();
    }

    /**
     * 除法运算，返回商，保留默认的小数位
     *
     * @param v1 被除数
     * @param v2 除数
     * @return 商值（四舍五入）
     */
    public static double div(double v1, double v2) {
        return div(v1, v2, DEF_DIV_SCALE);
    }

    /**
     * 除法运算，返回商，根据指定的小数位数进行四舍五入
     *
     * @param v1 被除数
     * @param v2 除数
     * @param scale 精度（保留几位小数）
     * @return 商值（四舍五入）
     */
    public static double div(double v1, double v2, int scale) {
        if (scale < 0)
            throw new IllegalArgumentException("The scale must be a positive integer or zero");
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));

        return b1.divide(b2, scale, BigDecimal.ROUND_HALF_UP).doubleValue();
    }

    /**
     * 四舍五入，保留指定的小数位
     *
     * @param v 需要四舍五入的数字
     * @param scale 小数点后保留几位
     * @return 修约后的结果
     */
    public static double round(double v, int scale) {
        if (scale < 0)
            throw new IllegalArgumentException("The scale must be a positive integer or zero");

        BigDecimal b = new BigDecimal(Double.toString(v));
        return b.setScale(scale, BigDecimal.ROUND_HALF_UP).doubleValue();
    }
}
```

### 注意事项

- `BigDecimal` 的构造函数不接受 `float` 或 `double` 类型，因为这些类型通常无法准确表示十进制数。
- 对于除法运算，务必指定合适的舍入模式（如 ROUND_HALF_UP）来避免出现异常或获得意外结果。
