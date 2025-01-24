---
title: 掌握Java数组：入门到进阶指南
keywords:
  - Java
  - 数组
  - 内存管理
  - 初始化
  - 动态分配
  - 越界
  - 排序
  - 查找
  - 二分法
categories:
  - 新时代码农
tags:
  - Java
  - 数组
  - 内存管理
  - 初始化
  - 动态分配
  - 越界
  - 排序
  - 查找
  - 二分法
abbrlink: 340249a9
date: 2012-05-15 00:00:00
ai:
  - 本文详细介绍了Java数组的基本概念、用法和操作。文章首先解释了数组的定义，包括它们在内存中的存储方式以及如何通过下标访问元素。接着讨论了数组下标的起始问题及其原因。然后，文章深入探讨了Java中数组的声明、初始化和动态分配空间的方法。此外，还介绍了数组的基本操作，如读取和修改元素值，并强调了数组越界的错误处理机制。最后，文章展示了如何使用数组来实现排序和查找算法，同时给出了一个二分法查找的示例代码。
description: 本文详细介绍了Java数组的基本概念、用法和操作。文章首先解释了数组的定义，包括它们在内存中的存储方式以及如何通过下标访问元素。接着讨论了数组下标的起始问题及其原因。然后，文章深入探讨了Java中数组的声明、初始化和动态分配空间的方法。此外，还介绍了数组的基本操作，如读取和修改元素值，并强调了数组越界的错误处理机制。最后，文章展示了如何使用数组来实现排序和查找算法，同时给出了一个二分法查找的示例代码。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

1.  数组是一个连续的内存空间, 存储了多个相同数据类型的数据, 是对这些数据的统一管理; 里面的元素可以是任何类型, 包括基本类型和引用类型;
2.  数组中的元素的变量是引用类型, 数组也可以看成是对象，数组中的每个元素相当于该对象的成员变量;
3.  数组变量存放的是连续空间第一个元素的地址;
4.  为什么数组下标要从 0 开始
    - 数组是一段连续的空间，要求 a[i] 就是求它的地址，然后找到它。如果从 0 开始，则 a[i] 的地址 = 首地址 + i _ 每个数据所占的长度；如果从 1 开始, 则 a[i] 的地址 = 首地址 + (i-1)_ 每个数据所占的长度
5.  数组中变量的类型 , 就是声明数组时定义的类型.
6.  java 中声明数组是不能指定长度; 数组创建后, 长度不可变化.
7.  java 中数组不能越界, 否则编译器会报数组越界错误.(ArrayIndexOutOfBoundsException)
8.  数组存储在 Java 堆的连续内存空间，所以如果你创建一个大的索引，你可以有足够的堆空间直到抛出 OutofmemoryError，因为请求的内存大小在连续的内存空间不可用。
9.  数组创建后, 每个元素都会自动初始化

| 类型   | byet | short | int | long | float | double |  char   | booble | 引用类型 |
| :----- | ---: | :---: | :-: | :--: | :---: | :----: | :-----: | :----: | -------- |
| 默认值 |    0 |   0   |  0  |  0   | 0.0f  |  0.0d  | `u0000` | false  | null     |

#### 一维数组

1.  定义  
    `type[] arrayName`; 或者 `type arrayName[];`  
    例如: `int[] intArray;` `double doubleArray[];`
2.  初始化
    - 静态初始化  
      `int[] intArray = {1,2,3,4};`  
      `String stringArray[] = {"hello","world"};`  
      `char[] charArray = new char[]{'a','b','c'};`
    - 动态初始化
      - 简单类型的数组  
        `int[] intArray;`  
        `intArray = new int[5];`
      - 复合类型的数组

```java
String[] stringArray = new String[3];
stringArray[0]= new String("How");
stringArray[1]= new String("are");
stringArray[2]= new String("you");
```

3. 数组元素的引用  
   数组元素的引用方式为：  
   　　　　　 arrayName[index]

index 为数组下标，它可以为整型常数或表达式，下标从 0 开始。每个数组都有一个属性 length 指明它的长度，例如：intArray.length 指明数组 intArray 的长度

**代码举例**  
**1. 数组对象的创建**  
数组名 = new 数组元素类型 [数组元素个数]  
例如:

```java
public class TestArray{
        public static void main(String args[]){
            int[] arr;
            arr = new int[5];
            for(int i=0;i<5;i++){
                arr[i] = i;
                System.out.println(arr[i]);
            }
        }
    }
```

**元素为引用类型的数据（注意：元素为引用数据类型的数组中的每一个元素都需要实例化）**

```java
public class TestArray{
    public static void main(String args[]){
        Student[] student;
        student = new student[3];
        for(int i=0; i<3; i++){
            student[i] = new Student("李四",89,9527);
            System.out.println("姓名:"
            +student[i].name
            +"  分数:"+student[i].score
            +"  学号:"+student[i].ID);
       }
   }
}
class Student{
    int name,score,ID;
    public Student(String name,
                            int score,
                            int ID){
        this.name = name;
        this.score = score;
        this.ID = ID;
    }
}
```

**2. 数组初始化：**

1. 动态初始化：  
   数组定义与为数组元素分配空间和赋值的操作分开进行，  
   例如：

```java
public class TestArray{
        public static void main(String args[]){
            int[] arr = new int[3];
            arr[0] = 1 ;
            arr[1] = 2 ;
            arr[2] = 3 ;

            Student[] student = new Student[3];
            student[0] = new Student("张三",87,0528);
            student[1] = new Student("李四",76,0529);
            student[2] = new Student("赵六",91,0530);
        }
    }

    class Student{
        int name,score,ID;
        public Student(String name,int score,int ID){
            this.name = name;
            this.score = score;
            this.ID = ID;
        }
    }
```

1.  静态初始化  
    在定义数组的同时就为数组元素分配空间并赋值，  
    例如：

```java
public class TestArray{
    public static void main(String args[]){
        int[] arr = {1,2,3}


        Student[] student = {new Student("张三",87,0528),
                            new Student("李四",76,0529),
                            new Student("赵六",91,0530)};
    }
}
class Student{
    int name,score,ID;
    public Student(String name,int score,int ID){
        this.name = name;
        this.score = score;
        this.ID = ID;
    }
}
```

**注意:**

- int[] a ; 等价于 int a[]; –> 定义一个 int 类型数组的引用 a;
- int[] a = new int[5]; –> 定义一个 int 类型引用并且分配空间, 但是元素没有初始化, 系统根据数组类型自动初始化
- int[] a = {1,2,2,3,4}; 等价于 int[] a = new int[]{1,2,2,3,4}–> 定义并初始化;
- 每个数组都有一个静态的属性, length, 它是这个数组的长度; 它是一个成员属性, 没有加 (), 同 String 求字符串长度的 length() 方法有区别

**字符串数组**

```java
String[] s = {"ss","bb","cc","rr"};
for(int i = 0 ; i < s.length ; i++){
    System.out.println(s[i]);
}
```

**字符串**

```java
String s = "aabbccdd";
    int length = s.length();
```

**主方法中的字符串数组**  
`public static void main(String[] args){}`  
我们每个类中的主函数也有一个数组，名叫 args.  
那么这个数组时干嘛用的呢？  
这个数组就好比，我们在命令行中注入 ipconfig -all 中的 all. 我们可以在输入  
`java 类名 23,12,aa,bbb` 这个跟几个参数。然后可以在代码中输出来看到

```java
class ClassName {
    public static void main(String[] args) {
        for(int i = 0 ; i < args.length;i ++){
            System.out.println(args[i]);
        }
    }
}
```

运行的时候 用命名 `java ClassName 1,2,3,4,5`, 就会在控制台输出 `1,2,3,4,5`  
这句命令的意思是: args[0] = “1,2,3,4,5”; args.length 的值为 1  
如果我们输入 `java ClassName 1 2 3 4 5`;  
这句命令的意思是: args[0] = “1”;  
args[1] = “2”;  
……  
args.length 的值为 5.

举一个 args[] 参数和基础类型包装类一起使用的例子，用来计算 +-x/：

```java
public class ClassName{
    public static void main(String args[]){
        if(args.length<3){//必须要输入3个字符,中间字符是运算符
        //其他2个字符是要运算的值
            System.out.println("error~~~");
            System.exit(0);
        }
        //把字符串转换为double类型
        double  b1 = Double.parseDouble(args[0]);
        double  b2 = Double.parseDouble(args[2]);
        double  b = 0;
        if(args[1].equals("+")){
            b = b1 + b2;
        }else if(args[1].equals("-")){
            b = b1-b2;
        }else if(args[1].equals("x")){
            b = b1*b2;
        }else if(args[1].equals("/")){
            b = b1/b2;
        }else{
            System.out.println("error operation!!!");
        }
        System.out.println(b);
    }
}
```

下面举一个用 ars 输入 10 个数，并且用选择排序，从小到大排序的示例：

```java
public class TestSortInt{
    public static void main(String args[]){
        int[] a = new int[args.length];
        for(int i=0; i<args.length; i++){
            a[i] = Integer.parseInt(args[i]);
        }
        int k,temp;
        for(int i=0; i<a.length; i++){
            k = i;
            for(int j=i+1; j<a.length; j++){
                if(a[k]>a[j]){
                    k=j;//k存储的是最小值的下标
                 }
            }
            if(k!=i){
                temp = a[i];
                a[i] = a[k];
                a[k] = temp;
            }
        }
        for(int i=0; i<a.length; i++){
            System.out.print(a[i] + " ");
        }
    }
}
```

下面我们用数组里面装一个日期类型做排序的示例，用了冒泡排序。

```java
public class TestDateSort{
    public static void main(String args[]){
        Date[] date = new Date[5];
        date[0] = new Date(2006,5,4);
        date[1] = new Date(2006,7,4);
        date[2] = new Date(2008,5,4);
        date[3] = new Date(2004,5,9);
        date[4] = new Date(2006,5,4);

        bubbleSort(date);

        for(int i=0; i < date.length; i++){
            System.out.println(date[i]);
        }
    }
    public static Date[] bubbleSort(Date[] a){
        int len = a.length;
        for(int i=len; i>=1; i--){
            for(int j=0; j<i-1; j++){
                if(a[j].compare(a[j+1])>0){
                    Date temp = a[j+1];
                    a[j+1] = a[j];
                    a[j] = temp;
                }
            }
        }
        return a;
    }
}
class Date{
    private int year,month,day;
    public Date(int year,int month,int day){
        this.year = year;
        this.month = month;
        this.day = day;
    }
    public int compare(Date date){
        return year>date.year?1
               :year<date.year?-1
               :month>date.month?1
               :month<date.month?-1
               :day>date.day?1
               :day<date.day?-1
               :0;
    }
    public String toString(){
        return "year,month,day ---- " +year+" - "+month+" - "+day;
    }
}
```

下面我们用数组做一个数三退一的游戏，就是说，好多人围城一圈，数 1,2,3 三个数，数到 3 的人退出，剩余的人继续重新从 1 开始数数，知道剩下最后一个人，我们用数组求最后一个人是谁？

```java
public class Count3Quit{
    public static void main(String args[]){
        boolean[] arr = new boolean[500];
        for(int i=0; i<arr.length; i++){
            arr[i] = true;
        }

        int leftCount = arr.length;
        int count = 0;
        int index = 0;
        while(leftCount > 1){
            if(arr[index] == true){
                count++;
                if(count == 3){
                    count = 0;
                    arr[index] = false;
                    leftCount --;
                }
            }
            index ++;
            if(index == arr.length){
                index=0;
            }
        }

        for(int i=0; i<arr.length; i++){
            if(arr[i]==true){
                System.out.println(i);
            }
        }
    }
}
```

有了数组之后，我们可以设计各种各样的排序算法。然后在排好序的时候，我们又可以设计各种各样的查找算法，接下来，我们用数组实现一个简单的二分法查找算法

```java
public class TestSearch{
    public static void main(String args[]){
        int[] a = {12,23,41,53,24,57,32,52,98,43,19,73};
        int postion = binarySearch(a,57);
        System.out.println(postion);
    }
    public static int binarySearch(int[] a, int searchNum){

        if(a.length==0)return -1;

        int startFlag = 0;
        int endFlag = a.length-1;
        int m = (startFlag+endFlag)/2;
        while(startFlag<=endFlag){
            if(a[m] == searchNum){
                return m;
            }else if(a[m]<searchNum){
                startFlag = m+1;
            }else if(a[m]>searchNum){
                startFlag = m+1;
            }
            m = (startFlag+endFlag)/2;
        }
        return -1;
    }
}
```

#### 多维数组

1．二维数组的定义

```　　
type arrayName[][]；
type [][]arrayName;
```

2．二维数组的初始化

- 静态初始化

`int intArray[][]={{1,2},{2,3},{3,4,5}};`

Java 语言中，由于把二维数组看作是数组的数组，数组空间不是连续分配的，所以不要求二维数组每一维的大小相同。

    - 动态初始化

- 直接为每一维分配空间，格式如下：

```java
arrayName = new type[arrayLength1][arrayLength2];
int a[][] = new int[2][3]；
```

      - 从最高维开始，分别为每一维分配空间：

```java
arrayName = new type[arrayLength1][ ];
arrayName[0] = new type[arrayLength20];
arrayName[1] = new type[arrayLength21];
…
arrayName[arrayLength1-1] = new type[arrayLength2n];
```

1. 例：  
   　　二维简单数据类型数组的动态初始化如下:

```java
int a[][] = new int[2][ ]；
a[0] = new int[3];
a[1] = new int[5];
```

对二维复合数据类型的数组，必须首先为最高维分配引用空间，然后再顺次为低维分配空间。  
　　而且，必须为每个数组元素单独分配空间。

例如：

```java
String s[][] = new String[2][ ];
s[0]= new String[2];// 为最高维分配引用空间
s[1]= new String[2]; // 为最高维分配引用空间
s[0][0]= new String(“Good”);// 为每个数组元素单独分配空间
s[0][1]= new String(“Luck”);// 为每个数组元素单独分配空间
s[1][0]= new String(“to”);// 为每个数组元素单独分配空间
s[1][1]= new String(“You”);// 为每个数组元素单独分配空间
```

3．二维数组元素的引用

对二维数组中的每个元素，引用方式为：arrayName[index1][index2]  
　　例如： num[1][0];  
　　两个矩阵交换:

```java
class twoArrayTest {
    public static void main(String[] args) {
        int arry[][] = {{1,2,3},{4,5,6},{7,8,9}};
        for(int i = 0 ; i <= 2 ; i++){
            for(int j = 0 ; j <= 2 ; j++){
                System.out.print(arry[i][j]+" ");
            }
            System.out.println();
        }
        for(int i = 0 ; i <= 2 ; i++){
            for(int j =  i; j <= 2 ; j++){
                int temp = arry[i][j];
                arry[i][j] = arry[j][i];
                arry[j][i] = temp;
            }
        }
        System.out.println("转换后");
        for(int i = 0 ; i <= 2 ; i++){
            for(int j = 0 ; j <= 2 ; j++){
                System.out.print(arry[i][j]+" ");
            }
            System.out.println();
        }
    }
}
```

### 2. 位运算

#### 按位与 & (AND)

**都为 1 才为 1, 否则为 0**

```java
public class Demo1 {
    public static void main(String[] args) {
        int a = 4 ;// 00000000 00000000 00000000 00000100
        int b = 7 ;// 00000000 00000000 00000000 00000111
        int c = a & b ; //                       00000100
        System.out.println(c);
    }
}
```

应用:

1. 迅速清零  
   `int a = 4 ;`  
   `a = a & 0; //结果为0`
2. 保留指定位数据  
   `int a = 409; // 00000000 00000000 00000001 10011001`  
   `int b = 255; // 00000000 00000000 00000000 11111111`  
   // 取 a 的低 8 位  
   `a = a & b ; // 00000000 00000000 00000000 10011001`

3. 判断奇偶性  
   int a = 整数 ;  
   `int b = a & 1;`  
   如果 b = 1, 则 a 是奇数;  
   如果 b = 0, 则 a 是偶数;  
   解释: 把一个整数用二进制表示, 如果最低位是 1 的话, 则这个整数肯定是奇数;  
   这个整数跟 1 按位与的时候, 即最低位跟二进制 001 按位与, 如果结果为 1, 则这个整  
   数对应二进制位的最低位必定也为 1, 所以这个整数必定是奇数.

#### 按位或 | (OR)

**有一个为 1, 结果就为 1; 全为 0, 结果才为 0**

```java
public class Demo2 {
        public static void main(String[] args) {
            int a = 9 ;// 00000000 00000000 00000000 00001001
            int b = 5 ;// 00000000 00000000 00000000 00000101
            int c = a | b ; //                       00001101
            System.out.println(c);
    }
}
```

应用:

1. 设定数据的指定位置  
   将 Demo2 中 a 的低 8 位全部设置为 1  
   `a = a | 0xFF;`//0xFF–>255–>10000000

#### 按位异或 ^ (XOR)

**当对应位互斥的时候, 结果才为 1, 否则为 0**

```java
public class Demo3 {
        public static void main(String[] args) {
            int a = 10;// 00000000 00000000 00000000 00001010
            int b = 7 ;// 00000000 00000000 00000000 00000111
            int c = a ^ b ; //                       00001101
            System.out.println(c);
    }
}
```

- 性质:

  1.  交换律
  2.  结合律
  3.  对于任何数 x，都有 x^x=0，x^0=x
  4.  自反性 A XOR B XOR B = A xor 0 = A

- 应用:

  1.  定位反转  
      `a = a ^ x;` //(x 是一个跟 a 对应的二进制有相同位数的全为一的二进制数)
  2.  数值交换  
      `a = a ^ b;`  
      `b = b ^ a;`  
      `a = a ^ b;`

- 练习:  
  1-1000 放在含有 1001 个元素的数组中，只有唯一的一个元素值重复，其它均只出现一次。每个数组元素只能访问一次，设计一个算法，将它找出来；不用辅助存储空  
  间，能否设计一个算法实现？

  - 算法一:  
    把所有数加起来再减去 1+2+..+1000 的和, 剩下的就是那个数  
    缺点是如果数据足够大, 会超过数据存储范围

    ```java
    public static int methode (int[] a) {
        int arraySum = 0 ;
        int sum = 0;
        for(int i = 0 ; i < a.length ; i ++){
            arraySum += a[i];
        }
        for(int j = 1 ; j <= 1000 ; j ++){
            sum += j;
        }
        return arraySum - sum;
    }
    ```

  - 算法二:  
    将所有的数全部异或，得到的结果与 1^2^3^…^1000 的结果进行异或，得到的结果就是重复数  
    证明: 由 ^ 操作符的 4 个性质, 假设多出的那个数为 n,  
    则 1^2^…^n^n^…^1000 = (1^2^..^1000)^n^n= a (这个结果里面没有 n)  
    然后把这个结果同从 1 异或到 1000 的结果异或,  
    假设 b = 1^2^3^…^1000(有 n)–> b = a ^ n  
    则 a ^ b = a ^ (a ^ n) 就等于 n (对于任何数 x，都有 x^x=0，x^0=x)

```java
public static int method(int[] a) {
        int resultA = 0;
        int resultB = 0;
        for(int i = 0 ; i < a.length ; i++){
            resultA ^= a[i];
        }
        for(int j = 1 ; j <= 1000 ; j++){
            resultB ^= j;
        }
        return resultA ^ resultB;
    }
```

#### 取反 ~

~(00001011)

#### 左移 <<右移>>

左移 n 位, 就是乘以 2 的 n 次方  
右移 n 位, 就是除以 2 的 n 次方

```java
public class Demo4 {
        public static void main(String[] args) {
            int a = 10;// 00000000 00000000 00000000 00001010
            int c = a << 4 ; //                      11010000
            System.out.println(c);
    }
}
```
