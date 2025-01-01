---
title: Java数据类型转换：实战案例解析
keywords:
  - Java
categories:
  - Java
tags:
  - mathematics
  - programming
  - algorithms
  - user_input
  - number_operations
abbrlink: 3daa4bf4
date: 2012-05-13 00:00:00
ai:
  - 这是一个包含多个编程任务和数学问题的教学材料，主要集中在Java语言上。这些任务涉及基本的控制结构、函数、数据类型、输入输出操作和条件判断。此外，还提供了解决回文数的问题，并以JSON格式存储结果。
description: 这是一个包含多个编程任务和数学问题的教学材料，主要集中在Java语言上。这些任务涉及基本的控制结构、函数、数据类型、输入输出操作和条件判断。此外，还提供了解决回文数的问题，并以JSON格式存储结果。
---

double > float > long > int > short > byte  
A. 小类型转大类型是自动转换 (向上转型);  
B. 大类型转小类型会发生精度丢失, 也有可能发生数据溢出, 所以编译器要求我们必须强制转换, 否则会有编译错误.

```
int i = 1 , j ;                     //正确:对于 j 这里只是定义,没有初始化.
float f1  = 0.1 ;                   //错误:在java中,有小数的数值默认为double类型,所以结果为double类型，看B解释
float f2 = 123;                     //正确: 结果为int类型,自动转换成float类型,A解释
double d1 = 2e20,d2 = 123;          //正确:A解释
byte b1 = 1,b2 = 2 ,b3 = 129;       //错误: b1,b2没有错,A解释;b3超过范围.
j = j + 10;                         //错误:只有定义 没有初始化
i= i / 10;                          //正确:
i = i * 0.1;                        //错误:i先自动转型为double,所以结果为double类型,看B解释.
char c1 = 'a',c2 = 125;             //正确:
byte b = b1 - b2;                   //错误:结果为in类型
char c = c1 + c2 -1;                //错误:结果为int类型,看B解释
float f3 = f1 + f2 ;                //正确:在f1和f2为float为前提条件下
float f4 = f1 + f2*0.1;             //错误:先是f2转换成double,然后f1转换为double,所以结果为double类型,看B解释
double d = d1*i + j;                //错误:j未初始化.
float f = (float)(d1*5 + d2);       //正确:结果为double,但是强制转换成了float,看B解释.
```

## **if 判断语句**

1.  if - else

```java
if(判断条件) {
    执行语句;
}else {
    执行语句;
}
```

1.  if - else if

```java
if(判断条件){
    执行语句;
}else if(判断条件) {
    执行语句;
}
...
else if(判断条件) {
    执行语句;
}
```

3.

```java
if(判断条件){
    执行语句;
}else if(判断条件) {
    执行语句;
}
...
else if(判断条件) {
    执行语句;
}else {
    执行语句;
}
```

### **练习:**

要求:

- 输入成绩, 给出等级;
- A:100-90;
- B:89-80
- C:79-70
- D:69-60
- 不及格: 小于 59
- 输入 quit 退出程序;

```java
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

### **作业一**

```java
/*
* 输入两个数,然后弹出选择框:1.加,2.减,3.乘,4.除.然后根据选择操作符,计算结果
*  两个数可以是正负数,可以是小数
*/
import javax.swing.JOptionPane;
class Operation {
    public static void Result (double number1, double number2 ,String operate) {
        switch (operate){
            case "1":{
                JOptionPane.showMessageDialog(null,number1+" + "+number2+" = "+(number1+number2));
                break;
            }
            case "2":{
                JOptionPane.showMessageDialog(null,number1+" - "+number2+" = "+(number1-number2));
                break;
            }
            case "3":{
                JOptionPane.showMessageDialog(null,number1+" * "+number2+" = "+(number1*number2));
                break;
            }
            case "4":{
                if(number2 != 0){
                    JOptionPane.showMessageDialog(null,number1+" / "+number2+" = "+(number1/number2));
                }else
                    JOptionPane.showMessageDialog(null,"被除数不能为0");
                break;
            }

        }
    }
}
class OperationTest {
    public static void main(String[] args) {
        while(true){
            try{//try catch 语句是为了判断输入是否符合要求,如果不是一个数字,则转到catch语句
                String s1 = JOptionPane.showInputDialog(null,"请输入第一个数");
                String s2 = JOptionPane.showInputDialog(null,"请输入第二个数");
                String s = JOptionPane.showInputDialog(null,"请选择算法:1.加法,2.减法,3.乘法,4.除法;\"quit\"退出");
                if (s.equals("quit"))
                    return ;
                //System.out.println(s);
                double firstNumber = Double.parseDouble(s1);
                double secondNumber = Double.parseDouble(s2);
                Operation.Result(firstNumber,secondNumber,s);
            }catch(Exception e){
                JOptionPane.showMessageDialog(null,"输入有误,请重新输入");
            }
        }
    }
}
```

### **作业二**

```java
// 键盘输入一个五位数,判断这个数是否为回文(1.它的是数字;2.是正整数;3.5位数;4.是否为回文数)
import javax.swing.JOptionPane;
class PalindromicNumber {
    public static void main(String[] args) {
        String s ;
        int num ;
        JOptionPane.showMessageDialog(null,"输入 quit 退出,回车继续");
        //判断这个数是否符合要求 先判断它是不是一个数字
        while(true){
            s =  JOptionPane.showInputDialog(null,"请输入一个5位整数");
            try {
            //判断它是不是一个5位数,2种方法:1.9 <= num/10000 >= 1; 2.toCharArray.length == 5
            num = Integer.parseInt(s); //这个是为了try catch语句判断是不是一个数字
            if(num < 0 ){
                JOptionPane.showMessageDialog(null,"请输入正整数");
                continue ;
            }
            //System.out.println(num);
            //用第二中方法判断它是不是一个5位数
            char[] charArray = s.toCharArray();
            System.out.println(charArray.length);
            if(5 == charArray.length){
                //判断是不是回文数
                //for(int i = 0 ; i < charArray.length ; i++)
                //  System.out.println( charArray[i] );//打印输入数组
                boolean on_off = false ;
                for(int j = 0 ; j < charArray.length/2 ;j++) {
                    if(charArray[j] == charArray[charArray.length -1 - j])
                        on_off = true ;
                }
                if (on_off)
                    JOptionPane.showMessageDialog(null,"是回文数");
                else
                    JOptionPane.showMessageDialog(null,"不是回文数");
            }else
                JOptionPane.showMessageDialog(null,"请输入一个5位的整数");
            }catch (Exception e){
                if(s.equals("quit"))
                    return ;
                JOptionPane.showMessageDialog(null,"请正确输入一个5位整数");
            }
        }
    }
}
```

### **回文数练习**

不用数组的方法打印 1-100000 之间所有的回文数

```java
class PalindromicNumber2 {
    public static void main(String[] args) {
       int k = 0,num;
       for(int i = 0 ; i <= 1000000 ; i++){
            num = i ;
            while (num != 0){
                //将num的数反转存储到k中
                k = k*10 + num%10;
                num = num/10;
                //System.out.println("k= "+k+"\n"+"i = "+i+"\n");
            }
            if(k == i){
                System.out.println(i);
            }
            k = 0;
       }
    }
}
```
