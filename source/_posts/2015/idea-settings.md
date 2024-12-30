---
title: IDEA 设置
keywords:
  - IDEA
categories:
  - IDEA
tags:
  - IntelliJ IDEA
  - 集成开发环境
  - 颜色设置
  - 自定义代码折叠
  - 快捷键
abbrlink: eb599575
date: 2015-11-22 00:00:00
ai:
  - 本文介绍如何在IntelliJ IDEA中自定义编辑器颜色设置、代码折叠和快捷键，包括编辑器背景色、行号栏颜色以及控制台背景色调整。此外，还提供了用于调试、代码生成、文档查看等的常用及自定义快捷键。同时，介绍了如何配置VM选项以优化IDE性能，并指导如何设置全局HTTP代理。
description: 本文介绍如何在IntelliJ IDEA中自定义编辑器颜色设置、代码折叠和快捷键，包括编辑器背景色、行号栏颜色以及控制台背景色调整。此外，还提供了用于调试、代码生成、文档查看等的常用及自定义快捷键。同时，介绍了如何配置VM选项以优化IDE性能，并指导如何设置全局HTTP代理。
---

IntelliJ IDEA 是一款功能强大的集成开发环境（IDE），它提供了丰富的快捷键来提高编程效率。下面是一些常用的编辑器背景色、行号栏颜色以及控制台背景色的设置方法，同时涵盖了自定义代码折叠和一些 IDEA 常用及自定义快捷键。

## 设置编辑器颜色

1. **编辑器背景色**：
   - 前往 `Preference` -> `Editor` -> `Color & Fonts` -> `Editor` -> `General` -> `Text` -> `Default text`
2. **行号栏的颜色**：

   - 前往 `Preference` -> `Editor` -> `Color & Fonts` -> `General` -> `Editor` -> `Gutter background`

3. **控制台背景色设置**：
   - 在 `Setting` 中找到 `Editor`，然后选择 `color Scheme` -> `console Colors`。右侧的 Console 部分可以调整背景颜色。
4. 其他编辑器颜色设置：
   - 调整光标当前行颜色：前往 `Editor` -> `Colors & Fonts` -> `General` -> `Editor` -> `Caret row`
   - 修改行背景色：前往 `Editor` -> `Colors & Fonts` -> `General` -> `Gutter` -> `Background`

## 自定义代码折叠

在需要自定义代码折叠的情况下，可以使用以下语法：

```java
//region 描述
Your code goes here...
//endregion
```

## IntelliJ IDEA 常用快捷键

- **插入**：`control+enter`
- **排错**：`option+enter`
- **下方插入一行**：`shift+enter`
- **上方插入一行**：`command + enter`
- **创建测试用例**：`shift + command -- > 创建测试用例`
- **运行代码**： `shift + control + r`
- **快速折叠/展开代码段**：使用 `option + command + (+/-)`
- **关闭/打开当前折叠**：`command + >`
- **返回上一跳转位置**：`command + [`
- **跳到下一个位置**：`command + ]`

此外，还有：

- 生成代码模板：`shift+command+j`
- 查看文档：使用 `F1`
- 搜索关键字：使用 `shift+command+f`

### Debugging 快捷键

- 开始调试：`control+d`
- 调试时查看选中值：`alt+f8`
- 单步执行到下一个断点：`f8`
- 强制进入代码：`alt+shift+f7`
- 运行 Java 类（非 debug）: `ctrl+shift+f10`

### 翻译快捷键

- 选中文本翻译：使用 `option + 数字键`
- 全句翻译并替换：`option+r`

## 自定义 IntelliJ IDEA VM Options

在启动 IntelliJ IDEA 时可以自定义 VM 选项，以优化性能：

```properties
-Xverify:none # 关闭Java字节码验证, 加快类装入速度
-server # 启用服务器模式
-XX:+UseG1GC # 使用 G1 垃圾回收器
-Dfile.encoding=UTF-8 # 设置文件编码为UTF-8
-XX:MaxMetaspaceSize=512m # 设置元空间最大大小
-javaagent:JetbrainsCrack-3.1-release-enc.jar # 启用 Jetbrains 装饰工具
```

### 使用 HTTP 代理

若需要设置全局的 HTTP 代理，请在 `idea.exe.vmoptions` 及 `idea64.exe.vmoptions` 文件中添加如下内容：

```properties
-DproxySet=true
-Dhttp.proxyHost=127.0.0.1 # 这里是你的 HTTP 代理服务器地址
-Dhttp.proxyPort=1080 # 这里是你代理的端口号
```
