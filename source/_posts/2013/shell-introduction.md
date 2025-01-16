---
title: Shell脚本编写全攻略：从零开始
keywords:
  - Shell编程
  - 变量
  - 运算符
  - 字符串处理
  - 数组
  - 循环
  - 函数
  - 输出重定向
categories:
  - 新时代码农
tags:
  - Shell编程
  - 变量
  - 运算符
  - 字符串处理
  - 数组
  - 循环
  - 函数
  - 输出重定向
date: 2013-02-12 00:00:00
ai:
  - 本博客内容详细介绍了Shell编程的基础知识，包括定义变量、只读变量、删除变量、特殊变量、shell替换、运算符、字符串处理、数组操作、echo命令和printf命令的使用，以及if-else语句、case语句、for循环、while循环、until循环、break和continue语句、shell函数的定义和使用，最后还介绍了shell输出重定向和包含其他sh文件的方法。
description: 本博客内容详细介绍了Shell编程的基础知识，包括定义变量、只读变量、删除变量、特殊变量、shell替换、运算符、字符串处理、数组操作、echo命令和printf命令的使用，以及if-else语句、case语句、for循环、while循环、until循环、break和continue语句、shell函数的定义和使用，最后还介绍了shell输出重定向和包含其他sh文件的方法。
---

## 定义变量

```shell
#!/bin/bash
# 定义 变量名和等号之间不能有空格
your_name="dong4j"
# 使用
echo ${your_name}

# 循环输出
for skill in Ada Coffe Action Java
do
    echo "I am good at ${skill} Script"
done
```

## 只读变量

readonly 变量名

## 删除变量

unset 变量名

## 特殊变量

```
$0
当前脚本的文件名
$n
传递给脚本或函数的参数。n 是一个数字,表示第几个参数。例如,第一个参数是$1,第二个参数是$2。
$#
传递给脚本或函数的参数个数。
$*
传递给脚本或函数的所有参数。
$@
传递给脚本或函数的所有参数。被双引号(" ")包含时,与 $* 稍有不同,下面将会讲到。
$?
上个命令的退出状态,或函数的返回值。
$$
当前 Shell 进程 ID。对于 Shell 脚本,就是这些脚本所在的进程 ID。
```

## shell 替换

### 命令替换

```
#!/bin/bash
DATE=`date` echo "Date is $DATE"
USERS=`who | wc -l` echo "Logged in user are $USERS"
UP=`date ; uptime` echo "Uptime is $UP"
```

### 变量替换

```
#!/bin/bash

# 如果变量为空或被删除(unset),则返回 word,不改变 var的值
echo ${var:-"Variable is not set"}
echo "1 - Value of var is ${var}"

# 如果变量为空或被删除(unset),则返回 word,改变 var的值为 word
echo ${var:="Variable is not set"}
echo "2 - Value of var is ${var}"

unset var
# 如果变量 var 被定义,那么返回 word,但不改变 var 的值。
echo ${var:+"This is default value"}
echo "3 - Value of var is ${var}"

var="Prefix"
echo ${var:+"This is default value"}
echo "4 - Value of var is ${var}"

# 如果变量 var 为空或已被删除(unset),那么将消息 message 送到标 准错误输出,可以用来检测变 量 var 是否可以被正常赋值。若此替换出现在 Shell 脚本中,那么脚本将停止运行。
echo ${var:?"Print this message"}
echo "5 - Value of var is ${var}"
```

## shell 运算符

### 算数运算符

```bash
#!/bin/bash
a=10 b=20
val=`expr $a + $b`
echo "a + b : $val"
val=`expr $a - $b`
echo "a - b : $val"
val=`expr $a * $b`
echo "a * b : $val"
val=`expr $b / $a`
echo "b / a : $val"
val=`expr $b % $a`
echo "b % a : $val"

# 条件表达式放在[]中,且前后必须留空格
if [ $a == $b ]
then
    echo "a is equal to b"
fi
if [ $a != $b ]
then
    echo "a is not equal to b"
fi
```

### 关系运算符

```
#!/bin/bash
a=10 b=20
if [ $a -eq $b ]
then
    echo "$a -eq $b : a is equal to b"
else
    echo "$a -eq $b: a is not equal to b"
fi
```

`-eq`: 检测两个数是否相等,相等返回 true。

```shell
[ $a -eq $b ]
```

返回 true。

`-ne`: 检测两个数是否相等,不相等返回 true。

```shell
[ $a -ne $b ]
```

返回 true。

`-gt`: 检测左边的数是否大于右边的,如果是,则返回 true。

```shell
[ $a -gt $b ]
```

返回 false。

`-lt`: 检测左边的数是否小于右边的,如果是,则返回 true。

```shell
[ $a -lt $b ]
```

返回 true。

`-ge`: 检测左边的数是否大等于右边的,如果是,则返回 true。

```shell
[ $a -ge $b ]
```

返回 false。

`-le`: 检测左边的数是否小于等于右边的,如果是,则返回 true。

```shell
[ $a -le $b ]
```

返回 true。

### 布尔运算符

! : 非  
-o : 或 有一个为 true 则返回 true  
-a : 与 两个表达式都为 true 才返回 true

### 字符串运算符

`=` : 检测两个字符串是否相等，相等返回 true。 `[ $a = $b ]` 返回 false。  
`!=` : 检测两个字符串是否相等，不相等返回 true。`[ $a != $b ]` 返回 true。  
`-z` : 字符串长度为 0 时返回 true `[ -z ${str}]  `
`-n` : 长度不为零时返回 true  
`str` 检测字符串是否为空, 不为空返回 true `[ ${str} ]`

### 文件测试运算符

-b : 是否为块设备文件  
-c : 是否为字符设备文件  
-d : 是否为目录  
-f : 是否为普通文件 (不是目录也不是设备文件)  
-g : 是否设置了 SGID 位  
-k : 是否设置了沾着位 (Sticky Bit)  
-p : 是否是具名管道  
-u : 是否设置了 SUID 位  
-r : 是否可读  
-w : 是否可写  
-x : 是否可执行  
-s : 文件大小是否为空 不为空返回 true  
-e : 文件 (包括目录) 是否存在,存在返回 true

## shell 字符串处理

### 单引号

`str='this is a string'`

单引号字符串的限制: 单引号里的任何字符都会原样输出,单引号字符串中的变量是无效的; 单引号字串中不能 出现单引号 (对单引号使用转义符后也不行)。

### 双引号

```shell
your_name='qinjx'
str="Hello, I know your are \"${your_name}\"! \n"
```

双引号的优点: 双引号里可以有变量 双引号里可以出现转义字符

### 获取字符串长度

```shell
string="abcd"
# 输出4
echo ${#string}
```

### 提取子字符串

```shell
string="alibaba is a great company"
# 输出 liba 有点像 python 的切片
echo ${string:1:4}
```

### 查询子字符串

```shell
string="alibaba is a great company"
echo `expr index "${string}" is`
```

## 数组

### 定义

使用空格分割元素  
`array_name=(value1 value2….)`  
或者

```shell
array_name=(
value0
value1
value2
...
)
```

或者单独设置

```shell
array_name[0]=value0
array_name[1]=value1
array_name[2]=value2
```

### 读取数组数据

1. 获取指定元素  
   `${array_name[index]}`
2. 获取全部元素  
   `${array_name[*]}` 或者 `${array_name[@]}`

### 获取数组长度

```shell
length=${#array_name[*]}
# 或者
length=${#array_name[@]}
# 获取指定元素的长度
lengthn=${#array_name[index]}
```

## echo 命令

`echo "\"It is a test\"" --> "It is a test"`

显示结果重定向至文件

`echo "It is a test" > myfile`

原样输出字符串 使用单引号

`echo '@name\" '`

显示命令执行结果

`echo `date``

## printf 命令 格式化输出语句

```shell
# format-string 为双引号
$ printf "%d %s\n" 1 "abc" 1 abc
# 单引号与双引号效果一样
$ printf '%d %s\n' 1 "abc" 1 abc
# 没有引号也可以输出
$ printf %s abcdef abcdef
# 格式只指定了一个参数,但多出的参数仍然会按照该格式输出,format-string 被重用
$ printf %s abc def abcdef $ printf "%s\n" abc def
abc def $ printf "%s %s %s\n" a b c d e f g h i j abc def ghi j
# 如果没有 arguments,那么 %s 用 NULL 代替,%d 用0代替
$ printf "%s and %d \n" and 0
# 如果以 %d 的格式来显示字符串,那么会有警告,提示无效的数字,此时默认置为0
$ printf "The first program always prints'%s,%d\n'" Hello Shell -bash: printf: Shell: invalid number The first program always prints 'Hello,0' $
```

## if else 语句

### if .. eles

```shell
if [ expression ]
then
    do something
if
```

### if .. else .. fi

```shell
if [ expression ]
then
Statement(s) to be executed if expression is true else
Statement(s) to be executed if expression is not true fi
```

### if .. elif .. fi

```shell
if [ expression 1 ]
then
    Statement(s) to be executed if expression 1 is true
elif [ expression 2 ]
then
    Statement(s) to be executed if expression 2 is true
elif [ expression 3 ]
then
    Statement(s) to be executed if expression 3 is true
else
    Statement(s) to be executed if no expression is true
fi
```

## shell case esac (switch case)

```shell
case 值 in
模式1)
 command1
 command2
 command3
 ;;
模式2)
 command1
 command2
 command3
 ;;
*)
 command1
 command2
 command3
 ;;
esac
```

tomcat 命令

```shell
#!/bin/bash
# $0 代表 sh 文件名
# $1 第一个参数 如果为 start 则
case $1 in
start)
sh /Library/Tomcat/bin/startup.sh
;;
stop)
sh /Library/Tomcat/bin/shutdown.sh
;;
restart)
sh /Library/Tomcat/bin/shutdown.sh
sh /Library/Tomcat/bin/startup.sh
;;
*)
echo “Usage: start|stop|restart”
;;
esac
exit 0
```

## shell for

```shell
for 变量 in 列表
do
    command1
    command2
    ...
done
```

列表可以是一组值 (数字 字符串等) 组成的序列,四通空格分隔

## shell while

```shell
while command
do
    Statement(s) to be executed if command is true
done
```

```shell
COUNTER=0
while [ $COUNTER -lt 5 ]
do
    COUNTER='expr $COUNTER+1'
    echo $COUNTER
done
```

```shell
# 将从键盘读到的值给 FILM
while read FILM
do
    echo "Yeah! great film the $FILM"
done
```

## shell until 循环

与 while 相反

```shell
until command
do
    Statement(s) to be executed until command is true
done
```

## shell break 和 continue

```shell
#!/bin/bash

while :
do
    echo -n "Input a number between 1 to 5: "
    read aNum
    case $aNum
        in 1|2|3|4|5)
            echo "Your number is $aNum!"
        ;;
        *) echo "You do not select a number between 1 to 5, game is over!"
            break
        ;;
    esac
done

# 跳出第二层循环 从内往外数
for var1 in 1 2 3
do
    for var2 in 0 5
    do
        if [ $var1 -eq 2 -a $var2 -eq 0 ]
        then
            break 2
        else
            echo "$var1 $var2"
        fi
    done
done
```

continue 与其他语言一样

## shell 中的函数

先定义 后使用

```shell
(function) function_name () {
    list of commands
    # 如果不加 return 语句,默认将最后一条命令的结果作为返回值
    [ return value ]
}
```

```shell
#!/bin/bash

funWithReturn(){
    echo "The function is to get the sum of two numbers..."
    echo -n "Input first number: "
    read aNum
    echo -n "Input another number: "
    read anotherNum
    echo "The two numbers are $aNum and $anotherNum !"
    return $(($aNum+$anotherNum))

}

funWithReturn
# Capture value returnd by last command

ret=$1
echo "The sum of two numbers is $ret !"
```

删除函数

`unset.f function_name`

如果你希望直接从终端调用函数,可以将函数定义在主目录下的 .profile 文件,这样每次登录后,在命令提示符 后面输入函数名字就可以立即调用。

## shell 函数参数

在 Shell 中,调用函数时可以向其传递参数。在函数体内部,通过 $n 的形式来获取参数的值,例如,$1 表示第 一个参数,$2 表示第二个参数…

```shell
#!/bin/bash

funWithParam(){
    echo "The value of the first parameter is $1 !"
    echo "The value of the second parameter is $2 !"
    echo "The value of the tenth parameter is $10 !"
    echo "The value of the tenth parameter is ${10} !"
    echo "The value of the eleventh parameter is ${11} !"
    echo "The amount of the parameters is $# !" # 参数个数
    echo "The string of the parameters is $* !" # 传递给函数的所有参数

}

funWithParam 2 2 3 4 5 6 7 8 9 34 73

```

注意,$10 不能获取第十个参数,获取第十个参数需要 ${10}。当 n>=10 时,需要使用 ${n} 来获取参数。

```
$#  传递给函数的参数个数。
$_  显示所有传递给函数的参数。
$@  与 $_ 相同,但是略有区别,请查看 Shell 特殊变量。
$?  函数的返回值。
```

## shell 输出重定向 /dev/null

Unix 命令默认从标准输入设备 (stdin) 获取输入,将结果输出到标准输出设备 (stdout) 显示。一般情况下,标准输 入设备就是键盘,标准输出设备就是终端,即显示器。

`>` filename  
重定向到文件

`>>` filename  
追加内容到文件

`<` filename  
从文件获取输入

command > file

将输出重定向到 file。

command < file

将输入重定向到 file。

command >> file

将输出以追加的方式重定向到 file。

n > file

将文件描述符为 n 的文件重定向到 file。

n >> file

将文件描述符为 n 的文件以追加的方式重定向到 file。

n >& m

将输出文件 m 和 n 合并。

n <& m

将输入文件 m 和 n 合并。

<< tag

将开始标记 tag 和结束标记 tag 之间的内容作为输入。

## shell here document

```shell
command << delimiter
    document
delimiter
```

```shell
#!/bin/sh

filename=test.txt
vi $filename <<EndOfCommands
i
This file was created automatically
from a shell script
^[
ZZ
EndOfCommands
```

$ command > /dev/null  
/dev/null 是一个特殊的文件,写入到它的内容都会被丢弃; 如果尝试从该文件读取内容,那么什么也读不到。但 是 /dev/null 文件非常有用,将命令的输出重定向到它,会起到”禁止输出“的效果。

## shell 包含其他 sh 文件

像其他语言一样,Shell 也可以包含外部脚本,将外部脚本的内容合并到当前脚本。

```shell
# sub.sh
my_name = "dong4j"

# main.sh
. sub.sh
echo $my_name
```

注意: 被包含脚本不需要有执行权限。
