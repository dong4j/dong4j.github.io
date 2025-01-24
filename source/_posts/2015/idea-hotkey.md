---
title: 从入门到精通：IDEA 的所有快捷键汇总
keywords:
  - IntelliJ IDEA
  - 快捷键
  - 文件编辑
  - 代码重构
  - 调试
  - 文档查看
  - 翻译
categories:
  - 新时代码农
tags:
  - IntelliJ IDEA
  - 快捷键
  - 文件编辑
  - 代码重构
  - 调试
  - 文档查看
  - 翻译
abbrlink: 72a223e0
date: 2015-11-12 00:00:00
ai:
  - IntelliJ IDEA 提供了一系列快捷键来提高文件编辑、代码重构与调试的效率。这些快捷键包括文件和编辑相关操作，如插入行、创建测试用例、运行/调试任务等；代码重构与调试相关操作，如生成方法返回类型、提炼新方法、跳转到断点等；以及文档查看和翻译功能。通过使用这些快捷键，用户可以更高效地进行软件开发工作。
description: IntelliJ IDEA 提供了一系列快捷键来提高文件编辑、代码重构与调试的效率。这些快捷键包括文件和编辑相关操作，如插入行、创建测试用例、运行/调试任务等；代码重构与调试相关操作，如生成方法返回类型、提炼新方法、跳转到断点等；以及文档查看和翻译功能。通过使用这些快捷键，用户可以更高效地进行软件开发工作。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## 文件和编辑相关

- **control+enter** - 插入(与 alt+insert 相同)
- **option+enter** - 排错(与 alt+enter 相同)
- **shift+enter** - 在当前行下面插入新行
- **command + enter** - 在光标前一行插入新行
- **shift + command** - 创建测试用例
- **shift + control + r** - 运行配置的运行/调试任务
- **option + commmand + (+/-)** - 快速折叠代码段或打开折叠的部分 (Ctrl+Shift+/)
- **command + > 或 <** - 关闭或展开当前文件夹内的所有折叠部分（仅针对文件夹）
- **command + [ 或 ]** - 跳转到上次编辑的位置
- **shift + command + F** - 在项目中查找关键字
- **option + command + l** - 代码格式化 (Ctrl+Alt+L)
- **shift+command+j** - 插入代码模板（Live Templates）
- **command + j** - Acejump: 快速定位到行首、变量或方法等
- **shift + command + A** - 在全局范围内查找操作或设置选项
- **Class... 或 File...** - 跳转到某个类或文件 (Ctrl+Shift+N)
- **File structure** - 可跳转至代码内部的特定部分，如函数、变量等 (Ctrl+F12)
- **Declaration** - 快速定位到所选符号或类型的定义处（Ctrl+B）
- **Back/Front** - 返回/前进至上一次跳转的位置
- **Search everywhere** - 跳转至任意位置
- **command + y** - 展示当前光标所在函数或类的全部内容 (Alt+F7)
- **shift+f12** - 关闭所有非编辑区域，回到编辑器界面（Ctrl+Shift+F12）
- **cmd + e 或 cmd + shift + e** - 跳转到最近使用的文件或最近编辑过的文件
- **opt + f12** - 打开命令行窗口 (Alt+F12)

## 代码重构与调试相关

- **alt+command+v** - 快速生成方法返回类型 (Ctrl+Alt+V)
- **alt+command+m** - 将选中的代码段提炼成新方法(Refactor -> Extract Method) (Ctrl+Alt+M)
- **shift+f8** - 跳转到下一个断点
- **f8** - 单步执行调试程序
- **control+d** - 开始或停止调试会话（Debug）
- **alt+f8** - 在运行时查看表达式的值 (Eval Expression)
- **f7** - 进入代码内部的函数 (Step Into)
- **alt+shift+f7** - 强制进入函数（Force Step into）
- **ctrl+shift+f9** - 重新启动当前会话(默认为最后一个运行过的会话) (Run)
- **ctrl+shift+f10** - 在 IDEA 中直接运行或调试 Java 程序
- **command+f2** - 停止正在执行的代码（停止任务）
- **control + h 或 control + opt + h** - 显示方法层级图 (Ctrl+H)
- **opt + cmd + U** - 生成类、接口或枚举的 UML 图 (Alt+Insert -> Diagrams -> Class Diagram for File)

## 方法和使用相关

- **opt+f7 或 opt+alt+f7** - 查找当前函数或变量被使用的所有地方（Find Usages）(Ctrl+F7)
- **ctrl+u** - 跳转到父类或接口的定义处 (Alt+Up/Down Arrows)

## 书签与任务

- **f3** - 新建不带标签的书签
- **opt+f3** - 新建带标签的书签
- **cmd + f3** - 打开书签浏览器窗口 (Ctrl+F11)
- **opt+shift+n** - 在当前文件中新建任务或标记位置（对于 CVS 用户）(Alt+Insert -> Task)

## 文档查看相关

- **f1** - 查看文档帮助 (Quick Documentation Lookup) (Alt+Q)
- **shift+command+d** - 在 Dash 中快速查找对应类或方法的文档

## 翻译功能快捷键

IntelliJ IDEA 还支持多种语言的翻译。

- **alt+1, 2 或 3** - 执行选中文本翻译，分别选择最小范围、最大范围和单词级别 (Alt+Shift+Insert)
- **alt+r** - 将翻译后的文本自动替换掉源代码
- **alt+t** - 翻译一些界面元素内的文字（如提示气泡等）
- **alt+0** - 打开反应窗口，显示已翻泽的内容
