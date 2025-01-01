---
title: IDEA 处理 i18n 的方式
keywords:
  - i18n
  - IDEA
categories:
  - 新时代码农
tags:
  - Java
  - 本地化
  - 国际化
  - Message Bundle
description: 从 IDEA 处理 i18n 的方式中学习如何设计微服务错误码
abbrlink: c1e0543
date: 2023-11-07 00:00:00
ai:
  - 实现了基于Java的本地化（国际化）功能，通过自定义类和配置文件来处理文本资源和消息。包括了使用占位符、处理不存在键及动态提供消息的功能，并测试验证其正确性。
---

## 缘起

最近一段时间在开发 IDEA 插件, UI 界面需要使用到国际化配置, 于是就看了看 IDEA 是怎么实现的, 发现很简单, 正好能用到框架开发上.

打算为每个 `atom-kernel` 模块配置一个国际化配置, 同时将错误信息配置化. 因为是框架底层的组件, 如果使用 Spring Boot 的 i18n 实现就太重了, 因此需要一种超轻量级的实现方式.

## IDEA 中如何实现 i18n

IDEA 使用 `ResourceBundle` 这个类实现了 i18n, 源码如下:

```java
/**
 * 特定作用域捆绑包的基类（例如“vcs”捆绑包、“aop”捆绑包等）。
 * 使用模式：
 * 创建一个扩展该类并为当前类构造函数提供目标bundle路径的类；
 * 可选地在子类中创建静态facade方法-创建单个共享实例并委托给它的getMessage（String，Object…）
 *
 * @author Denis Zhdanov
 */
public abstract class AbstractBundle {
  private static final Logger LOG = Logger.getInstance("#com.intellij.AbstractBundle");
  private Reference<ResourceBundle> myBundle;
  @NonNls private final String myPathToBundle;

  protected AbstractBundle(@NonNls @NotNull String pathToBundle) {
    myPathToBundle = pathToBundle;
  }

  @NotNull
  public String getMessage(@NotNull String key, @NotNull Object... params) {
    // CommonBundle.message() 主要用于参数替换与空值处理, 快捷键标识等
    return CommonBundle.message(getBundle(), key, params);
  }

  private ResourceBundle getBundle() {
    ResourceBundle bundle = com.intellij.reference.SoftReference.dereference(myBundle);
    if (bundle == null) {
      bundle = getResourceBundle(myPathToBundle, getClass().getClassLoader());
      myBundle = new SoftReference<>(bundle);
    }
    return bundle;
  }

  private static final Map<ClassLoader, Map<String, ResourceBundle>> ourCache =
    ConcurrentFactoryMap.createWeakMap(k -> ContainerUtil.createConcurrentSoftValueMap());

  /**
   * 使用 ResourceBundle.Control 来实现 i18n
   */
  public static ResourceBundle getResourceBundle(@NotNull String pathToBundle, @NotNull ClassLoader loader) {
    Map<String, ResourceBundle> map = ourCache.get(loader);
    ResourceBundle result = map.get(pathToBundle);
    if (result == null) {
      try {
        ResourceBundle.Control control = ResourceBundle.Control.getControl(ResourceBundle.Control.FORMAT_PROPERTIES);
        result = ResourceBundle.getBundle(pathToBundle, Locale.getDefault(), loader, control);
      }
      catch (MissingResourceException e) {
        LOG.info("Cannot load resource bundle from *.properties file, falling back to slow class loading: " + pathToBundle);
        ResourceBundle.clearCache(loader);
        result = ResourceBundle.getBundle(pathToBundle, Locale.getDefault(), loader);
      }
      map.put(pathToBundle, result);
    }
    return result;
  }
}
```

**实现自己的 Bundle 类:**

```java
public class IdeBundle extends AbstractBundle {
  public static String message(@NotNull @PropertyKey(resourceBundle = BUNDLE) String key, @NotNull Object... params) {
    return INSTANCE.getMessage(key, params);
  }

  public static final String BUNDLE = "messages.IdeBundle";
  private static final IdeBundle INSTANCE = new IdeBundle();

  private IdeBundle() {
    super(BUNDLE);
  }
}
```

**添加配置文件:**

还需要在 classpath 中添加一个 messages 目录, 然后添加 `IdeBundle.properties` 配置文件, 或者可以直接使用 IDEA 新增资源包, 需要注意的是, `messages.IdeBundle` 表示在 `messages` 目录下的 `IdeBundle.properties` 文件, 一定不能错:

```properties
error.malformed.url=Malformed url: {0}
browsers.explorer=Internet Explorer
```

**使用方式:**

```java
# 有占位符的
IdeBundle.message("error.malformed.url", "xxx")
# 无占位符
IdeBundle.message("browsers.explorer")
```

从上面可以看出, 直接 JDK 自带的 `ResourceBundle` 类实现了国际化和占位符替换的功能, 刚好符合我的要求, 因此打算使用这种方式来实现一下.

## 实现逻辑

我需要的功能:

1. 国际化;
2. 占位符替换;

IDEA 的 `AbstractBundle` 有很多我不需要的功能, 做了一些简单的修改后完全符合我的要求:

```java
@Slf4j
public abstract class AbstractBundle {
    private static final Map<ClassLoader, Map<String, ResourceBundle>> CACHE =
            ConcurrentFactoryMap.createWeakMap(k -> new ConcurrentSoftValueHashMap<>());
    @NonNls
    private final String myPathToBundle;
    private Reference<ResourceBundle> myBundle;

    @Contract(pure = true)
    protected AbstractBundle(@NonNls @NotNull String pathToBundle) {
        this.myPathToBundle = pathToBundle;
    }

    /**
     * 获取延迟加载的字符串
     *
     * @param key    键
     * @param params 参数
     * @return Supplier字符串
     */
    @NotNull
    public Supplier<String> getLazyMessage(@NotNull String key, Object... params) {
        return () -> this.getMessage(key, params);
    }

    /**
     * 获取字符串
     *
     * @param key    键
     * @param params 参数
     * @return 字符串
     */
    @NotNull
    public String getMessage(@NotNull String key, Object... params) {
        return message(this.getResourceBundle(), key, params);
    }

    /**
     * 获取本地化字符串
     *
     * @param bundle 资源包
     * @param key    键
     * @param params 参数
     * @return 字符串
     */
    @Nls
    @NotNull
    public static String message(@NotNull ResourceBundle bundle, @NotNull String key, Object... params) {
        return messageOrDefault(bundle, key, null, params);
    }

    /**
     * 获取资源包
     *
     * @return 资源包
     */
    public ResourceBundle getResourceBundle() {
        ResourceBundle bundle = SoftReference.dereference(this.myBundle);
        if (bundle == null) {
            bundle = this.getResourceBundle(this.myPathToBundle, this.getClass().getClassLoader());
            this.myBundle = new SoftReference<>(bundle);
        }
        return bundle;
    }

    /**
     * 获取资源包
     *
     * @param pathToBundle 资源包路径
     * @param loader       类加载器
     * @return 资源包
     */
    @NotNull
    public ResourceBundle getResourceBundle(@NotNull String pathToBundle, @NotNull ClassLoader loader) {
        Map<String, ResourceBundle> map = CACHE.get(loader);
        ResourceBundle result = map.get(pathToBundle);
        if (result == null) {
            try {
                ResourceBundle.Control control = ResourceBundle.Control.getControl(ResourceBundle.Control.FORMAT_PROPERTIES);
                result = this.findBundle(pathToBundle, loader, control);
            } catch (MissingResourceException e) {
                log.info("无法从 *.properties 文件中加载资源包，降级为慢的类加载： " + pathToBundle);
                ResourceBundle.clearCache(loader);
                result = ResourceBundle.getBundle(pathToBundle, Locale.getDefault(), loader);
            }
            map.put(pathToBundle, result);
        }
        return result;
    }

    /**
     * 查找资源包
     *
     * @param pathToBundle 资源包路径
     * @param loader       类加载器
     * @param control      控制
     * @return 资源包
     */
    protected ResourceBundle findBundle(@NotNull String pathToBundle, @NotNull ClassLoader loader,
                                        @NotNull ResourceBundle.Control control) {
        return ResourceBundle.getBundle(pathToBundle, Locale.getDefault(), loader, control);
    }

    /**
     * 获取本地化字符串或默认值
     *
     * @param bundle       资源包
     * @param key          键
     * @param defaultValue 默认值
     * @param params       参数
     * @return 字符串
     */
    public static String messageOrDefault(@Nullable ResourceBundle bundle,
                                          @NotNull String key,
                                          @Nullable String defaultValue,
                                          @NotNull Object... params) {
        if (bundle != null) {
            String value;
            try {
                value = bundle.getString(key);
            } catch (MissingResourceException e) {
                value = useDefaultValue(bundle, key, defaultValue);
            }
            return postprocessValue(bundle, value, params);
        }

        return defaultValue;
    }

    /**
     * 使用默认值
     *
     * @param bundle       资源包
     * @param key          键
     * @param defaultValue 默认值
     * @return 字符串
     */
    @NotNull
    static String useDefaultValue(ResourceBundle bundle, @NotNull String key, @Nullable String defaultValue) {
        if (defaultValue != null) {
            return defaultValue;
        }

        log.error("在资源包中 {} 未找到键: [{}]", bundle.getBaseBundleName(), key);
        return StringPool.NULL_STRING;
    }

    /**
     * 后处理值
     *
     * @param bundle 资源包
     * @param value  值
     * @param params 参数
     * @return 后处理后的值
     */
    static String postprocessValue(@NotNull ResourceBundle bundle, @NotNull String value, @NotNull Object @NotNull [] params) {
        if (params.length > 0 && value.indexOf('{') >= 0) {
            if (value.contains("{0")) {
                Locale locale = bundle.getLocale();
                try {
                    MessageFormat format = locale != null ? new MessageFormat(value, locale) : new MessageFormat(value);
                    OrdinalFormat.apply(format);
                    value = format.format(params);
                } catch (IllegalArgumentException e) {
                    value = "!format 错误: `" + value + "`!";
                }
            } else {
                value = StrFormatter.format(value, params);
            }
        }

        return value;
    }
}
```

创建绑定类:

```java
public final class CoreBundle extends DynamicBundle {
    @NonNls
    private static final String BUNDLE = "i18n.CoreBundle";
    private static final CoreBundle INSTANCE = new CoreBundle();

    @Contract(pure = true)
    private CoreBundle() {
        super(BUNDLE);
    }

    @NotNull
    public static String message(@NotNull String key, Object... params) {
        return INSTANCE.getMessage(key, params);
    }

    public static @NotNull Supplier<String> messagePointer(@NotNull String key, Object... params) {
        return INSTANCE.getLazyMessage(key, params);
    }
}

```

上面的代码基本上是固定的写法, 只需要修改 `BUNDLE` 即可, 然后创建国际化配置文件:

![20241229154732_JF2bLLEZ.webp](20241229154732_JF2bLLEZ.webp)

**测试一下:**

```java
@Slf4j
class CoreBundleTest {
    @Test
    void test_1() {
      	// 有占位符但是没有参数, 占位符原样输出
        log.info("{}", CoreBundle.message("code.param.verify.error"));
      	// 不存在的 key
        log.info("{}", CoreBundle.message("aaa"));
      	// 正常输出
        log.info("{}", CoreBundle.messagePointer("code.param.verify.error", "aaaaa").get());
    }
}
```

输出:

```
[main] INFO io.github.atom.kernel.core.CoreBundleTest - 参数校验失败: [{}]
[main] ERROR io.github.atom.kernel.core.bundle.AbstractBundle - 在资源包 [i18n.CoreBundle] 未找到键: [aaa]
[main] INFO io.github.atom.kernel.core.CoreBundleTest - N/A
[main] INFO io.github.atom.kernel.core.CoreBundleTest - 参数校验失败: [aaaaa]
```
