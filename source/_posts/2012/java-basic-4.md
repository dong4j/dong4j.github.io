---
title: Java 虚拟机
keywords:
  - Java
categories:
  - Java
tags:
  - 编程基础
  - 数据结构
  - C语言
  - 数组操作
  - 条件判断
  - 循环控制
  - 函数调用
  - 字符串处理
  - 排序算法
  - 高级功能实现
abbrlink: c69e2769
date: 2012-05-14 00:00:00
ai:
  - 本教程涵盖了从基础到高级Java编程的各种主题。它包括了对数组、排序算法（如冒泡排序和快速排序）、基本数据类型处理、字符串操作、异常处理、泛型以及面向对象编程等概念的详细讲解。还特别强调了数据结构的理解，比如数组和链表的应用。通过实际示例和代码片段，教程深入浅出地介绍了这些关键概念，并提供了解决问题的方法和技巧。
description: 本教程涵盖了从基础到高级Java编程的各种主题。它包括了对数组、排序算法（如冒泡排序和快速排序）、基本数据类型处理、字符串操作、异常处理、泛型以及面向对象编程等概念的详细讲解。还特别强调了数据结构的理解，比如数组和链表的应用。通过实际示例和代码片段，教程深入浅出地介绍了这些关键概念，并提供了解决问题的方法和技巧。
---

- 在一条计算机上由软件或硬件模拟的计算机或硬件模拟的计算机. JVM 读取并处理经编译后的平台无关的字节码 class 文件
- java 编译器针对 java 虚拟机产生的 class 文件, 因此是独立于平台的
- java 解释器负责将 java 虚拟机的代码在特定的平台上运行

### **类的定义**

```java
public class HelloWorld {
    public static void mian(String[] args) {
        System.out.println("HelloWorld");
    }
}
```

`[public] class 类名称 {}`  
对于类的定义有两种形式:

1. public class 定义: 内名称必须和文件名称一致, 在一个 java 文件里只能有一个 public 修饰的类
2. class 定义: 类名称可以和文件名不一致, 但是生成的是 class 定义的名称, 在一个 java 程序之中可以同时存在多个 class 的定义, 编译之后会分为不同 class 文件.

### **主方法**

主方法表示的是一个程序的起点, 要放在一个类中, 主方法定义格式如下:  
`public static void main(String[] args){}`

### **系统输出**

可以直接在屏幕上显示输出信息  
输出不加换行: `System.out.print(输出内容);`  
输出加换行 :`System.out.println(输出内容);`

### **classPath 配置**

如果要要想执行某一个 java 程序, 那么一定要进入到程序所在的路径下才可以.  
如果要想执行这个文件夹中的所有 class 文件, 则需要进入到此目录项执行, 那么如果现在希望在不同的目录下执行呢? 会提示用户找不到这个类., 这时候就需要配置 classpath

`SET CLASSPATH=*.class文件所在路径`

比如: classpath 配置到 `d:\testjava` 目录之中  
`SET CLASSPATH=D:\testjava`

**结论**: 当使用 java 命令执行一个类的时候, 会首先通过 classpath 找到指定的路径,  
而后在此路径下加载所需要的 class 文件  
但是, 如果这样到处指定 classpath 太乱也太麻烦, 所以最好的做法还是从当前路径下加载 class 文件, 那么这个额时候往往将 classpath 设置为 “.”

- **面试题**: 请解释 classpath 和 path 的区别
  - path: 是操作系统的环境属性, 指的是可以执行命令的程序路径
  - classpath: 是所有 class 文件的执行路径, java 命令执行的时候将利用此路径加载所需要的 class 文件

### 标识符和关键字

- **标识符**: 由字母, 数字,`_`,$ 组成, 其中不能以数字开头, 而且不能是 java 的保留字
- **定义变量 (标识符) 或方法时**: 第一个单词的首字母小写, 之后每个单词的首字母大写. –> String studentName ;
- **定义类的时候**: 第一个单词的首字母大写, 之后每个单词的首字母大写 –> class TestDemo {}
- **关键字**  
  常用的几种类型:
- int:
  - 取得最大值:`Integer.MAX_VALUE;`
  - 取得最小值:`Integer.MIN_VALUE;`
  - 最大值 + 1 = 最小值 最小值 - 1 = 最大值 (数据溢出)
- double
- byte
  - 在为 byte 赋值的时候, 如果给出的数值范围在 byte 范围内, 则自动将 int 类型变为 byte 类型, 这种操作只是在直接赋值的情况下

```java
class Test {
        public static void main(String[] args) {
            byte = 20 ;//20是int类型
            System.out.println(b);
        }
    }
```

- boolean : true 和 false
  - 布尔型主要表示一种逻辑判断, 布尔是一个人命, 他发明了逻辑运算 (AND,NOT,OR)
- long
- char
  - 在各个语言中, char 和 int 可以相互转换, 在 c 语言中转换的编码是 ASCII 码, 范围:
    - 大写字母范围: 65-90
    - 小写字母范围: 97-122
  - java 在定义字符的时候所使用的不是 ASCII 编码, 而是 UNICODE 编码, 这是一种使用十六进制定义的编码, 可以表示任何文字, 其中包含了中文

掌握类型之间的转换:

- 自动转型 (从小到大):byte–>short–>int–>long–>float–>double
- 强制转型 (从大到小):double–>float–>long–>int–>short–>byte

**初见 String**  
String 本事不属于 java 基本数据类型, 因为它属于一个类 (应用型数据), 但是这个类型使用起来可以像基本类型一样方便, 而且使用也很多

- 字符串的定义 :
- `String str = "aabbccdd";`
- 字符串数组:
- `String[] str = {"aa","bb","cc"};`
- 字符串连接:
- `String str = "Hello"; str = str + " World";`

**s += 1.0 和 s = s + 1.0 的区别**

- s += 1.0 隐含了强制转换,, 如果 s 是 int 类型, 则这句不会报错, 自动把结果强制转换为 int 类型的
- 而 s = s + 1.0 则没有强制转换, 如果 s 同样是 int 类型的变量, 则结果是 double 类型, 大类型转换为小类型会发生精度丢失, 如果我们没有显示强制转换, 编译器就会报错

### 程序逻辑

- 顺序结构
  - 所有代码按修后顺序执行
- 选择结构
  - (多) 条件判断: if , if…else, if..else if …else ;
  - (多) 数值判断: switch ….case ;
- 循环结构
  - for 循环, 知道循环次数的时候用, 用可以不用知道, 直接满足条件的时候用 break 跳出循环
  - while 循环 , 知道条件不满足的时候跳出循环
  - do…while 循环, 先循环一次, 然后判断循环条件是否满足
  - foreach 循环: 一种 for 循环的简单写法, 一般用来循环遍历数组.

```java
//输出一个乘法表
class MultiplicationTable {
    public static void main(String[] args) {
        for(int i = 1 ; i <= 9 ; i ++){
            for(int j = 1 ; j <= i ; j ++){
                System.out.print(j+"*"+i+"="+j*i+" ");
            }
            System.out.println(" ");
        }
    }
}
```

打印一个三角

```java
int i,j,k;
        for(i = 1 ; i <= 7; i++){
            //打印前面的空格
            for(j = 1;j < 7 - i+1;j++)
                System.out.print(" ");
            for(k = 1 ;k <= i*2 -1 ;k++)
                System.out.print("*");
            //循环完一次,换行
            System.out.println();
        }
```

### 练习

1.  输入成绩, 判断等级

```java
//输入成绩,给出等级
import javax.swing.JOptionPane;
import java.util.regex.Matcher; //正则表达式的类
class Demo {
    public static void main(String[] args) {
        while(true){
            String s = JOptionPane.showInputDialog(null,"请输入成绩");
            //如果输入的是数字,则判断成绩;
            if(s.matches("^[0-9]{1,3}$")){
                int num = Integer.parseInt(s);
                //System.out.println(num);
                if(num >= 90 )
                    JOptionPane.showMessageDialog(null,"等级:A");
                else if(num >= 80)
                    JOptionPane.showMessageDialog(null,"等级:B");
                else if(num >= 70)
                    JOptionPane.showMessageDialog(null,"等级:C");
                else if(num >= 60)
                    JOptionPane.showMessageDialog(null,"等级:D");
                else if(num <= 59 )
                    JOptionPane.showMessageDialog(null,"不及格");
            }
            //输入quit时退出程序
            else if(s.equals("quit")){
                return ;
            }
            else
                JOptionPane.showMessageDialog(null,"输入错误,请重新输入");
        }
    }
}
```

1.  判断一个数是不是水仙花数

```java
//判断一个数是不是水仙花数
import javax.swing.JOptionPane;

class Demo4 {
    public static void main(String[] args) {
        while(true){
            String s = JOptionPane.showInputDialog(null,"请输入三位数");
            int  num  = Integer.parseInt(s);
            //百位 num / 100 = 153 / 100 = 1
            //个位  num % 10 = 3
            //十位 (num /10)%10 = 5
            int a = num / 100 ;
            int b = num % 10 ;
            int c = (num / 10 )% 10 ;
            if(a*a*a + b*b*b + c*c*c == num){
                JOptionPane.showMessageDialog(null,"是水仙花书数");
                return;
            }
            else
                JOptionPane.showMessageDialog(null,"不是水仙花数");
        }
    }
}
```

1.  求 100-999 之间的水仙花数

```java

//求100-999之间的水仙花数

class Demo5 {
    public static void main(String[] args) {
        int a ;
        int b ;
        int c ;

        for(int i = 100 ; i <=999 ; i++){
            a = i / 100 ;
            b = i % 10 ;
            c = (i / 10 )% 10;
            if(a*a*a + b*b*b +c*c*c == i)
                System.out.println(i);
        }
    }
}
```

1. 运算

```java
import javax.swing.JOptionPane;
public class Test2 {
    public static void main(String[] args) {
        String s1 = JOptionPane.showInputDialog(null,"请输入第一个数字");
        String aa = JOptionPane.showInputDialog(null,"请输入运算符号");
        String s2 = JOptionPane.showInputDialog(null,"请输入第二个数字");

        int x = Integer.parseInt(s1);
        int y = Integer.parseInt(s2);
        switch (aa) {
            case "+": {
                JOptionPane.showMessageDialog(null,x+"+"+y+"="+(x+y));
                break;
            }
            case "-" :{
                JOptionPane.showMessageDialog(null,x+"-"+y+"="+(x-y));
                break;
            }
            case "*" :{
                JOptionPane.showMessageDialog(null,x+"*"+y+"="+(x*y));
                break;
            }
            case "/" :{
                JOptionPane.showMessageDialog(null,x+"/"+y+"="+(x/y));
                break;
            }

        }


    }
}
```

1.  JOptionPane 类

```java
import javax.swing.JOptionPane;
class JOptionPaneTest {
    public static void main(String[] args) {
        //显示一个错误对话框，该对话框显示的 message 为 'alert'：
        JOptionPane.showMessageDialog(null,
                                    "alert",
                                    "alert",
                                    JOptionPane.ERROR_MESSAGE);

        //显示一个内部信息对话框，其 message 为 'information'：
        JOptionPane.showInternalMessageDialog(frame,
                                            "information",
                                            "information",
                                            JOptionPane.INFORMATION_MESSAGE);

        //显示一个信息面板，其 options 为 "yes/no"，message 为 'choose one'：
        JOptionPane.showConfirmDialog(null,
                                    "choose one",
                                    "choose one",
                                    JOptionPane.YES_NO_OPTION);

        //显示一个内部信息对话框，其 options 为 "yes/no/cancel"，message 为 'please choose one'，并具有 title 信息：
        JOptionPane.showInternalConfirmDialog(frame,
                                            "please choose one",
                                            "information",
                                            JOptionPane.YES_NO_CANCEL_OPTION,
                                            JOptionPane.INFORMATION_MESSAGE);

        //显示一个警告对话框，其 options 为 OK、CANCEL，title 为 'Warning'，message 为 'Click OK to continue'：
        Object[] options = { "OK", "CANCEL" };
        JOptionPane.showOptionDialog(null,
                                    "Click OK to continue",
                                    "Warning",
                                    JOptionPane.DEFAULT_OPTION,
                                    JOptionPane.WARNING_MESSAGE,
                                    null,
                                    options, options[0]);

        //显示一个要求用户键入 String 的对话框：
        String inputValue = JOptionPane.showInputDialog("Please input a value");

        //显示一个要求用户选择 String 的对话框：
        Object[] possibleValues = { "First", "Second", "Third" };
        Object selectedValue = JOptionPane.showInputDialog(null,
                                                            "Choose one",
                                                            "Input",
                                                            JOptionPane.INFORMATION_MESSAGE,
                                                            null,
                                                            possibleValues,
                                                            possibleValues[0]);
    }
}
```

1.  2

```java
import javax.swing.JOptionPane;
class xunhuanTest {
    public static void main(String[] args) {
        /*int i = 0 ;
        int j = 0;
        while(i < 10){
            while(j < 10){
                System.out.print("*");
                j++;
            }
            j = 0;
            i++;
            System.out.println("");
        }*/

        /*int count = 0;
        String s ;
        int num = 0;
        int sum = 0;
        while (count < 5){
            count++;
            s= JOptionPane.showInputDialog(null,"请输入第"+count+"个人的成绩");
            num = Integer.parseInt(s);
            sum +=  num;
        }
        JOptionPane.showMessageDialog(null,"平局成绩为:"+sum / 5.0);*/

        /*int sum = 0;
        int i = 1;
        while(i < 101){
            sum = sum + i ;
            i++;
        }
        System.out.println(sum);*/

       /* int i = 1 ;
        int sum = 0;
        while (i < 100){
            sum = sum + i;
            System.out.println(i);
            i += 2 ;

        }
        System.out.println(i);
        System.out.println(sum);*/

        //3的倍数和带3的数都要敲桌子其他的报数

        /*int i = 0;
        while (i < 50) {
            i++;
            if(i % 3 == 0 ||  i/10 == 3 ||  i%10 == 3 )
                System.out.println("敲桌子");
            else
                System.out.println(i);
        }*/


        /*//输入5个数,给出最大值
        int count = 1;
        String str = "";
        int[] intArray = new int[5];
        int i = 0 ;
        int num ;
        while(count <=5 ){
            String s = JOptionPane.showInputDialog(null,"请输入第"+count+"个数");
            count++;
            //str = str + s;
            num = Integer.parseInt(s);
            intArray[i] = num;
            i++;
        }
        int mix = intArray[0] ;
        for(int j = 0 ; j < intArray.length - 1; j++){
            if(mix < intArray[j+1]){
                mix = intArray[j+1];
            }
        }
        System.out.println(mix);*/
    }
}
```

1.  异或

```java
class Demo2 {
    public static void main(String[] args) {
        int a = 5;
        int b = 8;
        //异或性质 :1.交换律;2.结合律;3.x^x = 0 , x^0 = x;4.自反性
        a = a^b;
        b = b^a;
        a = a^b;
        System.out.println("a = "+a+" b = "+b);
    }
}
```

1.  输出 3-100 之间的素数

```java

//输出3-100之间的素数
class Test4 {
    public static void main(String[] args) {
        for(int i = 3 ; i <= 100 ; i++){
            boolean on_off = true ;
            for(int j = 2 ; j < i ; j++){
                if(i % j == 0){
                    on_off = false ;
                    //结束内层循环
                    break ;
                }
            }
            if(on_off){
                System.out.println(i);

            }
        }
    }
}
```

1.  求 2 个数的最大公约数

```java
import javax.swing.JOptionPane;
class Test3 {
    public static void main(String[] args) {
        int a = Integer.parseInt(JOptionPane.showInputDialog("第一个数"));
        int b = Integer.parseInt(JOptionPane.showInputDialog("第二个数"));
        //求2个数的最大公约数
        int a1 = 0 ;
        for(int i = 1; i <= a && i <= b; i++){
            //找出能被a整除和b整除的数
            if(a % i == 0 && b % i == 0){
                //找出最大的公约数
                    a1 = i ;
            }
        }
        System.out.println(a1);
    }
}
```

1.  数组的定义及初始化

```java
//数组的定义 赋值
import javax.swing.JOptionPane ;
class Test1 {
    public static void main(String[] args) {
        int[] a = new int[10];
        for(int i = 0 ; i <= 9 ; i++)
            a[i] = i+1;
        for(int j = 0 ; j <= 9 ; j++)
            System.out.println(a[j]);

        int[] a1 = new int[4];
        for(int i = 0 ; i < a1.length ;  i++){
            a1[i] = Integer.parseInt(JOptionPane.showInputDialog("请输入第"+(i+1)+"个数"));
        }
        for(int i = 0 ;i < a1.length; i++){
            System.out.println(a1[i]);
        }
    }
}
```

1.  字符串数组的定义及赋值

```java
import javax.swing.JOptionPane;
class Test2 {
    public static void main(String[] args) {
        String[] name = new String[3];
        //String name ;
        for(int i = 0 ; i < name.length; i++){
            name[i] = JOptionPane.showInputDialog("请输入姓名");
        }
        for(int i = 0 ; i < name.length ; i++)
            System.out.println(name[i]);
    }
}
```

1.  求数组中最大值

```java

class Test3 {
    public static void main(String[] args) {
        int[] a = {4,58,34,50,21,42};
        //找出数组中最大的数
        int count = 0;
        int max = a[0];
        for(int i = 1 ; i < a.length - 1 ; i ++){
            if(max < a[i]){
                max = a[i];
                count = i;
            }
        }
        System.out.println("最大的数是: "+ max+"最大数的下标:"+count);


    }
}
```

1.  查找字符串数组中的特定值

```java
import javax.swing.JOptionPane;
class Test4 {
    public static void main(String[] args) {
        String[] str = {"张三","李四","王六加二","赵六","田七"};
        String s = JOptionPane.showInputDialog("找谁?");
        int count = -1 ;
        //boolean on_off = true;
        for(int i = 0 ; i < str.length ; i ++){
            //on_off = false;
            if(s.equals(str[i])){
                count  = i;
                JOptionPane.showMessageDialog(null,"找到了"+"位置在:"+(count+1));
                //on_off = true ;
                break ;
            }
        }
        if(count == -1)
            JOptionPane.showMessageDialog(null,"未找到");
    }
}
```

1.  5.

```java
import javax.swing.JOptionPane;
class Test5 {
    public static void main(String[] args) {
        String[] nameArray = new String[4];
        int[] moneyArray = new int[4];
        for(int i = 0 ; i < nameArray.length ; i ++){
            nameArray[i] = JOptionPane.showInputDialog("请输入第"+(i+1)+"个人的名字");
            moneyArray[i] = Integer.parseInt(JOptionPane.showInputDialog("请输入第"+(i+1)+"个人的工资"));
        }
        int max = -1 ;
        int bb =  -1 ;
        for(int k = 0 ; k < moneyArray.length ; k ++){
            if(max < moneyArray[k]){
                max = moneyArray[k];
                bb = k ;
            }
        }
        String s = "姓名:           工资\n";

        for(int j = 0 ; j < nameArray.length; j++){
            /*System.out.print(nameArray[j]+" ");
            System.out.print(moneyArray[j]);
            System.out.println();*/
            s +=nameArray[j] + "          "+moneyArray[j]+"\n";
        }
        JOptionPane.showMessageDialog(null,s);
        JOptionPane.showMessageDialog(null,"工资最高:"+ max +"人:"+nameArray[bb]);
    }
}
```

1.  6.

```java

//查找工资
import javax.swing.JOptionPane;
class Test6 {
    public static void main(String[] args) {
        String[] nameArray = {"阿一","阿二","阿三","阿四","阿五","阿六"};
        int[] moneyArray = {3500,8500,6412,8964,5105,6982};
        //要求:输入姓名,输出他的工资
        String s = JOptionPane.showInputDialog("请输入要查找的姓名:");
        int index = -1 ;
        for(int i = 0 ; i < nameArray.length ; i ++) {
            if(s.equals(nameArray[i])){
                index = i;
                break ;
            }
        }

        if(index == -1 )
            JOptionPane.showMessageDialog(null,"无此人,  滚粗");
        else
            JOptionPane.showMessageDialog(null,"姓名:"+nameArray[index] + " 工资:"+moneyArray[index]);
    }
}
```

1.  删除数组中某个元素

```java

//删除数组中的某个元素
import javax.swing.JOptionPane;
class Test7 {
    public static void main(String[] args) {
        int[] a = {3,5,7,9,12};
        int length = a.length;
        for(int i = 0 ; i < a.length ; i ++)
            System.out.println(a[i]);
        int deletNum = Integer.parseInt(JOptionPane.showInputDialog("请输入一个数"));
        for(int j = 0 ; j < length ; j ++){
            //找出那个数,删除
            if(deletNum == a[j]) {
                //用后一个数覆盖前面的数
                for(int k = j ; k < length -1; k ++){
                    a[k] = a[k+1];
                }
            }
        }
        for(int i = 0 ; i < a.length-1 ; i ++)
            System.out.println(a[i]);
    }
}
```

1.  排序

```java

class Test9 {
    public static void main(String[] args) {
        int[] a = {3,8,2,1,6};

        for(int i = 0 ; i < a.length ; i ++){
            for(int j = i + 1 ; j < a.length ; j ++){
                //第一轮,找出最小的数,放到0号位
                if(a[i] > a[j]) {
                    a[i] = a[i] ^ a[j];
                    a[j] = a[j] ^ a[i];
                    a[i] = a[i] ^ a[j];
                }
            }
        }
        for(int k = 0 ; k < a.length; k++)
            System.out.println(a[k]);
    }
}
```

```java

import javax.swing.JOptionPane;
class Demo {
    public static void main(String[] args) {
        //初始化数组
        String[] nameArray = new String[4];
        int[] moneyArray = new int[4];
        for(int i = 0 ; i < nameArray.length ; i ++){
            nameArray[i] = JOptionPane.showInputDialog("请输入第"+(i+1)+"个人的名字");
            moneyArray[i] = Integer.parseInt(JOptionPane.showInputDialog("请输入第"+(i+1)+"个人的工资"));
        }

        String s = "姓名:             工资:"+"\n";
        for(int j = 0 ; j < nameArray.length ; j++){
            System.out.println(nameArray[j]+"     "+moneyArray[j]);
            s += nameArray[j]+"                 "+moneyArray[j]+"\n";
        }
        JOptionPane.showMessageDialog(null,"排序前:\n"+s);

        //排序 按照工资排名名字，并且用弹出框弹出来.
        //因为存储名字的数组和工资的数组长度一样,只要将工资数组排序,顺带将名字也排序了,然后打印输出
        //moneyArray数组-->由大到小排序
        //第一次循环,把第一个元素同后面的元素一一对比,将第一大的数排到第一位
        String temp = null;
        for(int i = 0 ; i < moneyArray.length ; i ++) {
            for(int j = i + 1 ; j < moneyArray.length ; j++) {
                //交换数值,把大数放第一位
                if(moneyArray[i] < moneyArray[j]) {
                    //这是排的工资
                    moneyArray[i] = moneyArray[i] ^ moneyArray[j];
                    moneyArray[j] = moneyArray[j] ^ moneyArray[i];
                    moneyArray[i] = moneyArray[i] ^ moneyArray[j];

                    //排名字
                    temp = nameArray[i] ;
                    nameArray[i] = nameArray[j];
                    nameArray[j] = temp ;
                }
            }
        }
        String str = "姓名:             工资:"+"\n";
        for(int j = 0 ; j < moneyArray.length ; j++)
            str += nameArray[j]+"                 "+moneyArray[j]+"\n";
        JOptionPane.showMessageDialog(null,"排序后:\n"+str);
    }
}
```
