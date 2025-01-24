---
title: 打造个性化编程环境：Sublime Text插件深度体验
keywords:
  - Sublime Text
  - Java 编辑器
  - 前端开发
  - 代码编辑器
  - 插件安装
categories:
  - 新时代码农
tags:
  - Sublime Text
  - Java 编辑器
  - 前端开发
  - 代码编辑器
  - 插件安装
abbrlink: b5d8b5d5
date: 2012-05-03 00:00:00
ai:
  - Sublime Text 是一款适合前端开发的代码编辑器，界面美观且插件丰富。本文详细介绍了如何安装和使用 Sublime Text 进行 Java 开发环境的搭建，包括使用
    Package Control 安装插件，解决中文乱码问题，以及提供一系列快捷键操作指南。
description: Sublime Text 是一款适合前端开发的代码编辑器，界面美观且插件丰富。本文详细介绍了如何安装和使用 Sublime Text 进行
  Java 开发环境的搭建，包括使用 Package Control 安装插件，解决中文乱码问题，以及提供一系列快捷键操作指南。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

Sublime Text 是一款款平台代码编辑器, 很适合前端开发使用.  
它的插件足够丰富, 我只是拿来当 java 编辑器使用, 因为我觉得它的界面很好看.  
但是它对中文支持不够好 (是不是跨平台的编辑器对中文支持都不好?).  
下面我就对我使用 Sublime 期间遇到的问题和解决问题做一个备忘录.

### 编辑器的选择

我是一个初学编程的人, 对编辑器的选择不是很多, 就用过 Eclipse 和 Sublime.  
Eclipse 对于初学者的我来说, 显得过于庞大, 平时就联系一些小例子, 还用不上这么高大上的编辑器.  
为什么选择 Sublime?  
我觉得它性感, 界面好看, 插件丰富, 教程也多, 所以选择了它. 虽然 Sublime 不是免费的, 但是在伟大的天朝, 一切皆有可能.

### 插件

#### Package Control

Package Control 是 Sublime 必装的插件之一, 它就像一个管家, 下载, 管理其它插件

- **使用 Ctrl+` 打开 Sublime Text 控制台**
- **复制下面代码到控制台**

```
import urllib.request,os,hashlib;
    h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0';
    pf = 'Package Control.sublime-package';
    ipp = sublime.installed_packages_path();
    urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) );
    by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read();
    dh = hashlib.sha256(by).hexdigest();
    print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

- **等待 Package Control 安装完成, 然后使用`Ctrl+Shift+P`打开命令面板, 输入 intsall, 回车，然后选择或者输入要安装的插件**

#### 一些常用的插件

1.  ConvertToUTF8：解决中文乱码问题
2.  Alignment：主要用于代码对齐
3.  Autoprefixer：自动添加兼容前缀
4.  BracketHighlighter：能为 ST 提供括号，引号这类高亮功能.
5.  AutoFileName：自动补全文件名
6.  Terminal：唤起终端控制台
7.  SublimeLinter：代码提示高亮
8.  CodeFormatter：代码格式化
9.  Colorcoder：高亮所有变量
10. ColorPicker：调色盘 ：
11. SideBarEnhancements：实用的右键菜单增强插件
12. Sublime​Code​Intel：是一个代码提示、补全插件
13. Git 插件集成了 git 的常用功能
14. Emmet：前身是大名鼎鼎的 Zen coding，如果你从事 Web 前端开发的话，对该插件一定不会陌生。它使用仿 CSS 选择器的语法来生成代码，大大提高了 HTML/CSS 代码编写的速度.
15. FileHeader：当打开一个空文件时, 判断文件后缀自动添加语法模板.
16. GoSublime：是一个 sublime 的 go 语言插件提供自动补全和其他 IDE 特性。
17. SublimeLinter：一个支持 lint 语法的插件，ctrl+alt+l 呼出（与 qq 的锁定冲突，自己去改热键吧）可以高亮 linter 认为有错误的代码行
18. IMESupport：输入中文时, 让输入框跟随
19. markdownPreview：sublime 中的 MoarkDwn 编辑器

### Sublime 下搭建 Java 开发环境

- 安装目录下 Packages–>Java.sublime-package 文件改后缀名 zip 解压找到 Java.sublime-build 用记事本打开复制以下代码

```
{
    "cmd": "runJava.bat \"$file\"",
    "file_regex": "^(...*?):([0-9]*):?([0-9]*)",
    "selector": "source.java",
     "encoding":"GBK"
}
```

- 在 JDK 安装目录下的 bin 目录下新建一个 **runJava.bat**
- 复制一下代码

```
@ECHO OFF
ECHO Compiling   %~nx1
IF EXIST %~n1.class (
DEL %~n1.class
)
 javac -encoding UTF-8  %~nx1
::如果正确 打开cmd输出
IF EXIST %~n1.class (
ECHO ---------Out----------
start cmd /k java %~n1
)
```

- 注意名字要跟 Java.sublime-build 里面的一样

### 快捷键

#### 选择类

Ctrl+D 选中光标所占的文本，继续操作则会选中下一个相同的文本。  
Alt+F3 选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑。举个栗子：快速选中并更改所有相同的变量名、函数名等。  
Ctrl+L 选中整行，继续操作则继续选择下一行，效果和 Shift+↓ 效果一样。  
Ctrl+Shift+L 先选中多行，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行。  
Ctrl+Shift+M 选择括号内的内容（继续选择父括号）。举个栗子：快速选中删除函数中的代码，重写函数体代码或重写括号内里的内容。  
Ctrl+M 光标移动至括号内结束或开始的位置。  
Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。  
Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。  
Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。
Ctrl+Shift+] 选中代码，按下快捷键，展开代码。  
Ctrl+K+0 展开所有折叠代码。  
Ctrl+← 向左单位性地移动光标，快速移动光标。  
Ctrl+→ 向右单位性地移动光标，快速移动光标。  
shift+↑ 向上选中多行。  
shift+↓ 向下选中多行。  
Shift+← 向左选中文本。  
Shift+→ 向右选中文本。  
Ctrl+Shift+← 向左单位性地选中文本。  
Ctrl+Shift+→ 向右单位性地选中文本。  
Ctrl+Shift+↑ 将光标所在行和上一行代码互换（将光标所在行插入到上一行之前）。  
Ctrl+Shift+↓ 将光标所在行和下一行代码互换（将光标所在行插入到下一行之后）。  
Ctrl+Alt+↑ 向上添加多行光标，可同时编辑多行。  
Ctrl+Alt+↓ 向下添加多行光标，可同时编辑多行。

#### 编辑类

Ctrl+J 合并选中的多行代码为一行。举个栗子：将多行格式的 CSS 属性合并为一行。  
Ctrl+Shift+D 复制光标所在整行，插入到下一行。  
Tab 向右缩进。  
Shift+Tab 向左缩进。  
Ctrl+K+K 从光标处开始删除代码至行尾。  
Ctrl+Shift+K 删除整行。  
Ctrl+/ 注释单行。  
Ctrl+Shift+/ 注释多行。  
Ctrl+K+U 转换大写。  
Ctrl+K+L 转换小写。  
Ctrl+Z 撤销。  
Ctrl+Y 恢复撤销。  
Ctrl+U 软撤销，感觉和 Gtrl+Z 一样。  
Ctrl+F2 设置书签  
Ctrl+T 左右字母互换。  
F6 单词检测拼写

#### 搜索类

Ctrl+F 打开底部搜索框，查找关键字。  
Ctrl+shift+F 在文件夹内查找，与普通编辑器不同的地方是 sublime 允许添加多个文件夹进行查找，略高端，未研究。  
Ctrl+P 打开搜索框。举个栗子：1、输入当前项目中的文件名，快速搜索文件，2、输入 @和关键字，查找文件中函数名，3、输入：和数字，跳转到文件中该行代码，4、输入 #和关键字，查找变量名。  
Ctrl+G 打开搜索框，自动带：，输入数字跳转到该行代码。举个栗子：在页面代码比较长的文件中快速定位。  
Ctrl+R 打开搜索框，自动带 @，输入关键字，查找文件中的函数名。举个栗子：在函数较多的页面快速查找某个函数。  
Ctrl+： 打开搜索框，自动带 #，输入关键字，查找文件中的变量名、属性名等。  
Ctrl+Shift+P 打开命令框。场景栗子：打开命名框，输入关键字，调用 sublime text 或插件的功能，例如使用 package 安装插件。  
Esc 退出光标多行选择，退出搜索框，命令框等。

#### 显示类

Ctrl+Tab 按文件浏览过的顺序，切换当前窗口的标签页。  
Ctrl+PageDown 向左切换当前窗口的标签页。  
Ctrl+PageUp 向右切换当前窗口的标签页。  
Alt+Shift+1 窗口分屏，恢复默认 1 屏（非小键盘的数字）  
Alt+Shift+2 左右分屏 - 2 列  
Alt+Shift+3 左右分屏 - 3 列  
Alt+Shift+4 左右分屏 - 4 列  
Alt+Shift+5 等分 4 屏  
Alt+Shift+8 垂直分屏 - 2 屏  
Alt+Shift+9 垂直分屏 - 3 屏  
Ctrl+K+B 开启 / 关闭侧边栏。  
F11 全屏模式  
Shift+F11 免打扰模式
