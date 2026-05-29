#!/usr/bin/env python3
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.category import Category

# 4个分类的 id 映射
CAT = {
    "syntax": 1,
    "data-structure": 2,
    "algorithm": 3,
    "math": 4,
}

# 章节数据：每条 (title, slug, category_slug, difficulty, order, content)
CHAPTERS = [

    # ===== 难度1：基础知识与编程环境 =====
    (
        "计算机基础知识与编程环境",
        "computer-basics",
        "syntax", 1, 1,
        """# 计算机基础知识与编程环境

## 本章简介

本章介绍学习C++编程前必须掌握的计算机基础知识，包括计算机基本组成、进制概念、编译运行原理，以及常用开发环境搭建。

---

## 1. 计算机基本组成

一台计算机由以下硬件组成：

| 硬件 | 作用 |
|------|------|
| CPU（中央处理器） | 执行计算和指令，是计算机的大脑 |
| 内存（RAM） | 临时存储程序和数据，断电后数据丢失 |
| 硬盘 | 永久存储数据，断电后数据保留 |
| 输入设备 | 键盘、鼠标等，向计算机输入信息 |
| 输出设备 | 显示器、打印机等，输出计算结果 |

**冯·诺依曼体系**：计算机采用"存储程序"原理，程序和数据都存在内存中，CPU从内存读取指令执行。

---

## 2. 进制的概念

### 二进制、八进制、十六进制

计算机内部使用**二进制**（基数为2），每位只能是0或1。

常用进制对照表：

| 十进制 | 二进制 | 八进制 | 十六进制 |
|--------|--------|--------|----------|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 8 | 1000 | 10 | 8 |
| 10 | 1010 | 12 | A |
| 15 | 1111 | 17 | F |
| 16 | 10000 | 20 | 10 |

### 位、字节、字

- **位（bit）**：最小单位，0或1
- **字节（Byte）**：1 Byte = 8 bit，千字节用KB表示
- **字（Word）**：CPU一次处理的数据单位，32位/64位系统

```cpp
// C++中数据大小（64位系统）
// char: 1字节，int: 4字节，long long: 8字节
#include <iostream>
using namespace std;

int main() {
    cout << "char:  " << sizeof(char)  << " 字节" << endl;
    cout << "int:   " << sizeof(int)   << " 字节" << endl;
    cout << "long long: " << sizeof(long long) << " 字节" << endl;
    cout << "double: " << sizeof(double) << " 字节" << endl;
    return 0;
}
```

---

## 3. 程序编译运行原理

### 编译型语言 vs 解释型语言

C++是**编译型语言**，源代码需要经过编译器翻译成机器码才能执行：

```
源代码(.cpp) → 预处理器 → 编译器 → 汇编器 → 链接器 → 可执行文件
```

### Windows下用Dev-C++运行第一个程序

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

**操作步骤**：
1. 打开Dev-C++ → 新建源代码
2. 输入上述代码
3. 按 `F11` 编译运行
4. 看到黑色控制台输出 `Hello, World!` 表示成功

---

## 4. 常用IDE介绍

### Dev-C++（推荐初学者）

- 免费开源，界面简洁
- 体积小，一键编译运行
- 适合Windows

### Code::Blocks

- 跨平台（Windows/Linux/Mac）
- 支持多种编译器

### VS Code + g++

- 适合有一定基础的同学
- 需要手动配置编译器

### g++编译器命令

```bash
# 编译
g++ main.cpp -o main.exe

# 运行（Windows）
main.exe

# 运行（Linux/Mac）
./a.out   # 默认输出文件是a.out
```

---

## 5. 程序的基本结构

C++程序有固定的结构：

```cpp
// 1. 头文件包含
#include <iostream>   // 输入输出流库
using namespace std;  // 使用标准命名空间

// 2. 主函数（程序入口）
int main() {
    // 3. 函数体：写你要计算机做什么
    cout << "Hello!" << endl;
    
    // 4. 返回值
    return 0;  // 0表示程序正常结束
}
```

**注意**：
- C++严格区分大小写：`cout` ≠ `Cout`
- 每条语句以分号 `;` 结尾
- `main` 函数是程序的唯一入口

---

## 本章小结

1. 计算机由CPU、内存、硬盘等组成，采用冯·诺依曼体系
2. 计算机使用二进制，常见进制有二进制、八进制、十六进制
3. 1字节=8位，int通常占4字节
4. C++是编译型语言，需要编译器将源代码翻译成可执行文件
5. 程序基本结构：`头文件 → using namespace → main函数`
"""
    ),

    (
        "第一个C++程序",
        "first-cpp-program",
        "syntax", 1, 2,
        """# 第一个C++程序

## 本章简介

通过编写和运行第一个C++程序，熟悉开发环境，理解程序的基本结构和运行原理。

---

## 1. Hello World程序详解

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

### 代码逐行解释

| 行号 | 代码 | 含义 |
|------|------|------|
| 1 | `#include <iostream>` | 引入输入输出库，`iostream`包含`cin`和`cout` |
| 2 | `using namespace std;` | 使用标准命名空间，简写`cout`代替`std::cout` |
| 3 | `int main()` | 定义主函数，返回整数 |
| 4 | `cout << "Hello!" << endl;` | 输出字符串到屏幕 |
| 5 | `return 0;` | 返回0表示程序正常结束 |

---

## 2. cout输出详解

### 基本用法

```cpp
// 输出字符串
cout << "你好，世界！" << endl;

// 输出数字
cout << 2024 << endl;

// 输出变量
int age = 15;
cout << age << endl;

// 多个输出连写
cout << "年龄：" << age << "岁" << endl;
// 输出：年龄：15岁
```

### endl的作用

`endl`表示换行（end of line），相当于回车键。

```cpp
cout << "第一行" << endl;
cout << "第二行" << endl;
// 输出：
// 第一行
// 第二行
```

---

## 3. 注释的使用

注释是给人看的说明，编译器会忽略。

### 单行注释 `//`

```cpp
int main() {
    // 这是一条注释，编译器会忽略
    int a = 10;  // 这是行尾注释
    return 0;
}
```

### 多行注释 `/* ... */`

```cpp
int main() {
    /*
     * 这是一个多行注释
     * 可以写很多行说明
     * 不会被执行
     */
    return 0;
}
```

**建议**：写代码时多加注释，方便自己和他人理解！

---

## 4. 常见错误

### 忘记分号

```cpp
// ❌ 错误
cout << "Hello" << endl

// ✅ 正确
cout << "Hello" << endl;
```

### 大小写错误

```cpp
// ❌ 错误
Cout << "Hello";  // C是大写

// ✅ 正确
cout << "Hello";   // c是小写
```

### 中文括号或引号

```cpp
// ❌ 错误（使用了中文标点）
cout << "Hello"（ endl）；   // 中文括号

// ✅ 正确（使用英文标点）
cout << "Hello" << endl;
```

---

## 5. 动手练习

### 练习1：输出自我介绍

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "===== 我的信息 =====" << endl;
    cout << "姓名：张三" << endl;
    cout << "年级：初二" << endl;
    cout << "学校：数据谷中学" << endl;
    cout << "爱好：编程" << endl;
    return 0;
}
```

### 练习2：简单计算

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;
    cout << "a + b = " << a + b << endl;
    cout << "a * b = " << a * b << endl;
    return 0;
}
```

---

## 本章小结

1. `cout << 数据 << endl;` 用于向屏幕输出内容
2. `endl` 表示换行
3. 注释用 `//` 或 `/* */`，不参与编译
4. 常见错误：忘分号、大小写、中文标点
5. 编程习惯：多写注释，代码整洁
"""
    ),

    (
        "变量、数据类型与常量",
        "variables-and-data-types",
        "syntax", 2, 3,
        """# 变量、数据类型与常量

## 本章简介

介绍C++中变量的声明与使用、基本数据类型、以及常量的概念。这是C++程序设计的基石。

---

## 1. 变量

### 什么是变量

变量是内存中的一块存储空间，用来保存数据。就像一个带标签的盒子，盒子的名字就是变量名，里面放的是数据。

### 变量的声明与赋值

```cpp
#include <iostream>
using namespace std;

int main() {
    // 声明一个整数变量
    int age;

    // 给变量赋值
    age = 15;

    // 输出变量的值
    cout << "年龄是：" << age << endl;

    // 声明时直接赋值（初始化）
    int score = 100;

    cout << "分数是：" << score << endl;

    return 0;
}
```

### 变量命名规则

1. 由字母、数字、下划线组成
2. 不能以数字开头：`int 2name;` ❌
3. 不能使用关键字：`int int;` ❌
4. 区分大小写：`int A;` 和 `int a;` 是不同变量

**合法的变量名**：
```cpp
int age;        // ✅
int score1;     // ✅
int _temp;      // ✅
int myScore;    // ✅
int AgeOfUser;  // ✅
```

---

## 2. 基本数据类型

### 整型

| 类型 | 大小 | 范围 | 说明 |
|------|------|------|------|
| `int` | 4字节 | -2³¹~2³¹-1（约±21亿） | 最常用的整数类型 |
| `long long` | 8字节 | -2⁶³~2⁶³-1 | 大整数 |
| `short` | 2字节 | -32768~32767 | 短整数 |
| `unsigned int` | 4字节 | 0~2³²-1 | 无符号整数（正数） |

```cpp
int a = 100000;        // 正常范围
long long b = 1e12;    // 大整数用long long
unsigned int c = 300;  // 非负数用unsigned
```

### 浮点型（小数）

| 类型 | 大小 | 精度 |
|------|------|------|
| `float` | 4字节 | 单精度，约6-7位有效数字 |
| `double` | 8字节 | 双精度，约15位有效数字 |

```cpp
float pi1 = 3.14f;      // float常量加f后缀
double pi2 = 3.1415926; // double更精确

cout << 3.14 + 1.2 << endl;  // 输出：4.34
```

### 字符型

```cpp
char grade = 'A';   // 用单引号
char digit = '5';
cout << grade << endl;  // 输出：A
```

### 布尔型

```cpp
bool isStudent = true;   // 真
bool isPassed = false;   // 假

cout << isStudent << endl;  // 输出：1（true=1）
cout << isPassed << endl;   // 输出：0（false=0）
```

---

## 3. 常量

常量是值不能改变的量。

### const关键字

```cpp
const int WEEK_DAYS = 7;       // 每周7天，不能修改
const double PI = 3.14159;    // 圆周率
const char newline = '\\n';   // 换行符
```

### 宏定义常量

```cpp
#define MAX_SCORE 100    // 定义满分
#define PI 3.14159

cout << PI << endl;  // 输出：3.14159
```

**建议**：优先使用`const`，比`#define`更安全。

---

## 4. 类型转换

### 自动转换（隐式）

小类型 → 大类型 自动转换，不会丢失精度。

```cpp
int a = 10;
double b = a;   // int自动转double
cout << b << endl;  // 输出：10
```

### 强制转换（显式）

```cpp
double x = 3.99;
int y = (int)x;   // 强制转int，小数部分被截断
cout << y << endl;  // 输出：3
```

---

## 5. 常用运算符

### 算术运算符

```cpp
int a = 10, b = 3;

cout << a + b << endl;   // 加法：13
cout << a - b << endl;   // 减法：7
cout << a * b << endl;   // 乘法：30
cout << a / b << endl;   // 除法：3（整数除法）
cout << a % b << endl;   // 取余：1
```

### 复合赋值运算符

```cpp
int x = 10;
x += 5;   // 等价于 x = x + 5，结果15
x *= 2;   // 等价于 x = x * 2，结果30
```

---

## 本章小结

1. 变量：声明时指定类型，命名遵守规则
2. 整型用`int/long long`，浮点用`double`，字符用`char`，布尔用`bool`
3. 常量用`const`或`#define`定义
4. 类型转换有自动和强制两种
5. 常用算术运算符：`+ - * / %`
"""
    ),

    (
        "输入输出与分支结构",
        "input-output-and-conditionals",
        "syntax", 2, 4,
        """# 输入输出与分支结构

## 本章简介

学习使用`cin`从键盘读取数据，以及`if`和`switch`分支结构。这是程序实现逻辑判断的基础。

---

## 1. cin输入详解

### 基本用法

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "请输入你的年龄：" << endl;
    cin >> age;
    cout << "你的年龄是：" << age << endl;
    return 0;
}
```

**运行示例**：
```
请输入你的年龄：
15
你的年龄是：15
```

### 一次读取多个数据

```cpp
int a, b, c;
cin >> a >> b >> c;  // 依次输入三个整数
cout << "和=" << a + b + c << endl;
```

### 常见数据类型输入

```cpp
int age;
double score;
char grade;
string name;

cin >> age;        // 输入整数
cin >> score;       // 输入小数
cin >> grade;       // 输入字符
cin >> name;       // 输入字符串（不含空格）
```

---

## 2. if分支结构

### 基本if语句

```cpp
int score;
cout << "请输入成绩：";
cin >> score;

if (score >= 60) {
    cout << "及格！" << endl;
}
```

### if-else语句

```cpp
int score;
cin >> score;

if (score >= 60) {
    cout << "及格" << endl;
} else {
    cout << "不及格" << endl;
}
```

### if-else if-else多分支

```cpp
int score;
cin >> score;

if (score >= 90) {
    cout << "优秀" << endl;
} else if (score >= 80) {
    cout << "良好" << endl;
} else if (score >= 70) {
    cout << "中等" << endl;
} else if (score >= 60) {
    cout << "及格" << endl;
} else {
    cout << "不及格" << endl;
}
```

---

## 3. 关系运算符与逻辑运算符

### 关系运算符

| 运算符 | 含义 | 示例 |
|--------|------|------|
| `>` | 大于 | `a > b` |
| `<` | 小于 | `a < b` |
| `>=` | 大于等于 | `a >= b` |
| `<=` | 小于等于 | `a <= b` |
| `==` | 等于 | `a == b` |
| `!=` | 不等于 | `a != b` |

### 逻辑运算符

| 运算符 | 含义 | 说明 |
|--------|------|------|
| `&&` | 逻辑与 | 两个都真才为真 |
| `\|\|` | 逻辑或 | 至少一个为真即为真 |
| `!` | 逻辑非 | 真变假，假变真 |

```cpp
int age = 15;
int score = 85;

// 逻辑与：同时满足
if (age >= 13 && age <= 18 && score >= 80) {
    cout << "符合参赛条件" << endl;
}

// 逻辑或：满足任一即可
if (score == 100 || score == 0) {
    cout << "极端分数" << endl;
}

// 逻辑非
bool isPass = true;
if (!isPass) {
    cout << "需要补考" << endl;
}
```

---

## 4. switch分支结构

当需要对一个变量进行多个值的比较时，`switch`比`if-else`更清晰。

```cpp
int grade;
cout << "输入等级（A/B/C/D）：";
cin >> grade;

switch (grade) {
    case 'A':
        cout << "90~100分" << endl;
        break;
    case 'B':
        cout << "80~89分" << endl;
        break;
    case 'C':
        cout << "70~79分" << endl;
        break;
    case 'D':
        cout << "60~69分" << endl;
        break;
    default:
        cout << "成绩无效" << endl;
}
```

**注意**：
- `case`后是常量，不是范围
- `break`不能省略，否则会"穿透"执行下一个`case`
- `default`处理所有未匹配的情况

---

## 5. 条件运算符（三目运算符）

```cpp
// 语法：条件 ? 值1 : 值2
int a = 10, b = 20;
int max = (a > b) ? a : b;   // max = 20

// 等价于：
int max;
if (a > b) {
    max = a;
} else {
    max = b;
}
```

---

## 本章小结

1. `cin >> 变量;` 从键盘读取数据
2. `if-else`处理两个分支，`if-else if-else`处理多分支
3. 逻辑运算符：`&&`（与）、`||`（或）、`!`（非）
4. `switch`适合等值多分支，用`break`防止穿透
5. 三目运算符 `? :` 是简写版的if-else
"""
    ),

    (
        "循环结构",
        "loops",
        "syntax", 2, 5,
        """# 循环结构

## 本章简介

循环是程序设计中最重要的结构之一。本章介绍`for`、`while`、`do-while`三种循环，以及循环嵌套的应用。

---

## 1. for循环

### 基本语法

```cpp
for (初始化; 条件; 更新) {
    // 循环体
}
```

### 打印1到10

```cpp
for (int i = 1; i <= 10; i++) {
    cout << i << " ";
}
// 输出：1 2 3 4 5 6 7 8 9 10
```

### for循环执行顺序

```
1. 执行初始化（只执行一次）
2. 判断条件
3. 如果条件为真 → 执行循环体 → 执行更新 → 回到步骤2
4. 如果条件为假 → 循环结束
```

---

## 2. while循环

### 基本语法

```cpp
while (条件) {
    // 循环体
}
```

### 计算1+2+...+100

```cpp
int sum = 0;
int i = 1;
while (i <= 100) {
    sum += i;
    i++;
}
cout << "1+2+...+100 = " << sum << endl;
// 输出：5050
```

---

## 3. do-while循环

至少执行一次循环体，再判断条件。

```cpp
int n;
do {
    cout << "请输入1~100的数：";
    cin >> n;
} while (n < 1 || n > 100);

cout << "你输入了：" << n << endl;
```

---

## 4. 循环中的break和continue

### break：跳出整个循环

```cpp
for (int i = 1; i <= 100; i++) {
    if (i == 10) {
        cout << "遇到10，停止" << endl;
        break;  // 跳出循环
    }
    cout << i << " ";
}
// 输出：1 2 3 4 5 6 7 8 9 遇到10，停止
```

### continue：跳过本次循环

```cpp
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;  // 跳过偶数
    }
    cout << i << " ";
}
// 输出：1 3 5 7 9
```

---

## 5. 循环嵌套

### 打印九九乘法表

```cpp
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        cout << j << "×" << i << "=" << i*j << "\\t";
    }
    cout << endl;
}
```

---

## 本章小结

1. `for`适合已知循环次数的场景
2. `while`适合条件驱动型循环
3. `do-while`先执行再判断，保证至少执行一次
4. `break`跳出循环，`continue`跳过本次
5. 循环可以嵌套，常用于二维图案打印
"""
    ),

    (
        "一维数组与二维数组",
        "arrays",
        "syntax", 2, 6,
        """# 一维数组与二维数组

## 本章简介

数组是存储多个相同类型数据的集合。本章介绍一维数组和二维数组的声明、使用和方法。

---

## 1. 一维数组

### 声明与初始化

```cpp
// 声明
int a[10];           // 定义10个整数的数组，下标0~9

// 初始化
int b[5] = {1, 2, 3, 4, 5};        // 完全初始化
int c[5] = {1, 2};                  // 部分初始化，未填的为0
int d[] = {10, 20, 30};            // 自动确定大小（3个元素）
```

### 数组的使用

```cpp
int score[5] = {85, 92, 78, 96, 88};

// 遍历数组
for (int i = 0; i < 5; i++) {
    cout << "第" << i+1 << "个成绩：" << score[i] << endl;
}

// 修改元素
score[0] = 90;  // 修改第1个元素
```

### 数组长度计算

```cpp
int arr[] = {1, 2, 3, 4, 5};
int len = sizeof(arr) / sizeof(arr[0]);  // 5
```

---

## 2. 数组的基本操作

### 求最大值

```cpp
int a[] = {85, 92, 78, 96, 88};
int max = a[0];  // 假设第1个最大

for (int i = 1; i < 5; i++) {
    if (a[i] > max) {
        max = a[i];
    }
}
cout << "最大成绩：" << max << endl;  // 96
```

### 数组逆序

```cpp
int a[] = {1, 2, 3, 4, 5};
int len = 5;

// 逆序
for (int i = 0; i < len / 2; i++) {
    int temp = a[i];
    a[i] = a[len - 1 - i];
    a[len - 1 - i] = temp;
}

// 输出：5 4 3 2 1
```

### 冒泡排序

```cpp
int a[] = {64, 34, 25, 12, 22, 11, 90};
int n = 7;

for (int i = 0; i < n-1; i++) {
    for (int j = 0; j < n-1-i; j++) {
        if (a[j] > a[j+1]) {
            swap(a[j], a[j+1]);
        }
    }
}
```

---

## 3. 二维数组

### 声明与初始化

```cpp
// 声明3行4列的矩阵
int mat[3][4];

// 初始化
int a[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

// 按行初始化（省略内层花括号）
int b[2][3] = {1, 2, 3, 4, 5, 6};
```

### 二维数组遍历

```cpp
int a[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        cout << a[i][j] << " ";
    }
    cout << endl;
}
// 输出：
// 1 2 3
// 4 5 6
```

---

## 4. 矩阵转置

```cpp
int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
int b[3][2];

// 转置
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        b[j][i] = a[i][j];
    }
}

// 输出转置后的矩阵b（3行2列）
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++) {
        cout << b[i][j] << " ";
    }
    cout << endl;
}
```

---

## 本章小结

1. 数组下标从0开始，`a[n]`是第n+1个元素
2. `sizeof(arr)/sizeof(arr[0])`计算数组长度
3. 数组名是常量指针，不能赋值
4. 二维数组`a[m][n]`是m行n列
5. 冒泡排序是经典的数组排序算法
"""
    ),

    (
        "字符串处理",
        "strings",
        "syntax", 2, 7,
        """# 字符串处理

## 本章简介

介绍C++中两种字符串的处理方式：字符数组和`string`类。重点掌握`string`类的常用操作。

---

## 1. string类的基本用法

### 头文件与声明

```cpp
#include <string>   // string类头文件
using namespace std;

string s1 = "Hello";    // 直接赋值
string s2("World");    // 构造函数
string s3;             // 空字符串
```

### 字符串输入

```cpp
string name;
cout << "请输入你的名字：";
cin >> name;         // 遇到空格停止，不含空格
getline(cin, name);  // 读取整行，包含空格
```

---

## 2. string常用操作

```cpp
string s = "Hello, World!";

// 长度
cout << s.length() << endl;   // 13
cout << s.size() << endl;     // 13

// 拼接
string a = "Hello";
string b = "World";
string c = a + " " + b;  // "Hello World"

// 比较
if (a == b) cout << "相同";   // 不相等

// 访问字符
cout << s[0] << endl;   // 'H'
cout << s[7] << endl;   // 'W'

// 子串
cout << s.substr(0, 5) << endl;   // "Hello"
cout << s.substr(7, 5) << endl;   // "World"
```

---

## 3. 字符串的遍历与修改

```cpp
string s = "Hello";

// 遍历
for (int i = 0; i < s.length(); i++) {
    cout << s[i] << " ";
}
// H e l l o

// 修改
s[0] = 'h';       // 改成小写：hello
s += "!";         // 追加：hello!

// 插入
s.insert(5, ",");  // "hello,!"

// 删除
s.erase(5, 1);     // 删除逗号
```

---

## 4. 字符串查找与替换

```cpp
string s = "Hello, World! World!";

// find查找，返回位置（找不到返回-1）
int pos = s.find("World");
cout << pos << endl;  // 7

// rfind从右往左查
pos = s.rfind("World");
cout << pos << endl;  // 13

// replace替换
string s2 = "Hello";
s2.replace(0, 5, "Hi");  // 把"Hello"替换成"Hi"
cout << s2 << endl;  // "Hi"
```

---

## 5. 字符串与数字互转

```cpp
#include <string>
// 数字转字符串
int n = 123;
string s = to_string(n);    // "123"

// 字符串转数字
string t = "456";
int n2 = stoi(t);            // 456
double d = stod("3.14");    // 3.14
```

---

## 6. 字符判断函数

```cpp
#include <cctype>

char c = 'A';

// 判断函数（返回bool）
isalpha(c);  // 是否是字母
isdigit(c);  // 是否是数字
isupper(c);  // 是否是大写
islower(c);  // 是否是小写
isspace(c);  // 是否是空格

// 转换函数
char lower = tolower(c);  // 'a'
char upper = toupper(c);  // 'A'
```

---

## 本章小结

1. `string`类使用前需`#include <string>`
2. `length()/size()`获取长度，`+`拼接字符串
3. `substr(pos, len)`截取子串，`find()`查找
4. `to_string()`数字转字符串，`stoi()/stod()`字符串转数字
5. 字符判断用`cctype`库的函数
"""
    ),

    (
        "函数与参数传递",
        "functions",
        "syntax", 3, 8,
        """# 函数与参数传递

## 本章简介

函数是组织代码的基本单元。本章介绍函数的定义、调用、参数传递方式（值传递、引用传递、指针传递）。

---

## 1. 函数的定义与调用

### 基本结构

```cpp
// 函数声明（定义）
int add(int a, int b) {
    int sum = a + b;
    return sum;  // 返回结果
}

// 函数调用
int main() {
    int result = add(3, 5);
    cout << result << endl;  // 8
    return 0;
}
```

### 无参函数

```cpp
void printMenu() {
    cout << "===== 菜单 =====" << endl;
    cout << "1. 开始游戏" << endl;
    cout << "2. 退出" << endl;
}

int main() {
    printMenu();
    return 0;
}
```

---

## 2. 参数传递：值传递

默认方式，函数内部修改不影响实参。

```cpp
void change(int x) {
    x = 100;  // 只改变副本
}

int main() {
    int a = 10;
    change(a);
    cout << a << endl;  // 仍然是10
    return 0;
}
```

---

## 3. 参数传递：引用传递

使用`&`，函数内部修改会影响实参。

```cpp
void change(int &x) {
    x = 100;  // 改变原变量
}

int main() {
    int a = 10;
    change(a);
    cout << a << endl;  // 变成100
    return 0;
}
```

---

## 4. 参数传递：指针传递

使用指针，函数内部修改会影响实参。

```cpp
void change(int *p) {
    *p = 100;  // 通过指针修改原变量
}

int main() {
    int a = 10;
    change(&a);  // 传入地址
    cout << a << endl;  // 变成100
    return 0;
}
```

### 值传递 vs 引用传递 vs 指针传递

| 方式 | 语法 | 函数内修改影响实参 |
|------|------|------------------|
| 值传递 | `void f(int x)` | ❌ |
| 引用传递 | `void f(int &x)` | ✅ |
| 指针传递 | `void f(int *p)` | ✅（解引用后） |

---

## 5. 递归函数

函数调用自身叫递归。

### 阶乘

```cpp
int factorial(int n) {
    if (n <= 1) return 1;       // 递归终止条件
    return n * factorial(n-1);   // 递归调用
}

int main() {
    cout << factorial(5) << endl;  // 120
    return 0;
}
```

### 递归执行过程

```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

### 斐波那契数列

```cpp
int fib(int n) {
    if (n <= 2) return 1;
    return fib(n-1) + fib(n-2);
}
```

**注意**：递归要有终止条件，否则会无限递归导致栈溢出。

---

## 6. 函数重载

同名函数，不同参数（类型或个数不同）。

```cpp
int max(int a, int b) {
    return (a > b) ? a : b;
}

double max(double a, double b) {
    return (a > b) ? a : b;
}

int max(int a, int b, int c) {
    return max(max(a, b), c);
}
```

---

## 7. 内联函数

用`inline`建议编译器内联，减少函数调用开销。

```cpp
inline int add(int a, int b) {
    return a + b;
}
```

---

## 本章小结

1. 函数：`返回类型 函数名(参数) { 函数体; return值; }`
2. 值传递：副本，不影响原变量
3. 引用传递`&`：直接影响原变量，推荐使用
4. 指针传递：传入地址，解引用修改
5. 递归：函数调用自身，必须有终止条件
6. 函数重载：同名不同参，编译器自动选择
"""
    ),

    (
        "STL标准模板库",
        "stl-containers",
        "data-structure", 3, 9,
        """# STL标准模板库

## 本章简介

STL（Standard Template Library）是C++标准库的重要组成部分，提供了常用的数据结构和算法。本章介绍`vector`、`stack`、`queue`等容器。

---

## 1. vector向量容器

### 基本用法

```cpp
#include <vector>
using namespace std;

int main() {
    vector<int> v;              // 空向量
    vector<int> v2(5);           // 5个元素，默认0
    vector<int> v3(5, 10);       // 5个元素，每个都是10
    vector<int> v4 = {1, 2, 3}; // 初始化列表

    // 尾部添加
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);

    // 访问
    cout << v[0] << endl;           // 1
    cout << v.front() << endl;     // 1
    cout << v.back() << endl;      // 3

    // 大小
    cout << v.size() << endl;      // 3
    cout << v.empty() << endl;    // false

    return 0;
}
```

### vector遍历

```cpp
vector<int> v = {10, 20, 30, 40, 50};

// 方式1：下标
for (int i = 0; i < v.size(); i++) {
    cout << v[i] << " ";
}

// 方式2：迭代器
for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}

// 方式3：范围for（c++11）
for (int x : v) {
    cout << x << " ";
}
```

### 常用操作

```cpp
vector<int> v = {3, 1, 4, 1, 5, 9};

v.push_back(2);         // 尾部添加：{3,1,4,1,5,9,2}
v.pop_back();          // 删除尾部：{3,1,4,1,5,9}
v.insert(v.begin()+2, 7);  // 插入：{3,1,7,4,1,5,9}
v.erase(v.begin()+1);      // 删除：{3,4,1,5,9}
sort(v.begin(), v.end());  // 排序
reverse(v.begin(), v.end()); // 逆序
```

---

## 2. stack栈容器

**后进先出（LIFO）**

```cpp
#include <stack>
using namespace std;

int main() {
    stack<int> s;

    s.push(1);   // 入栈：{1}
    s.push(2);   // 入栈：{1,2}
    s.push(3);   // 入栈：{1,2,3}

    cout << s.top() << endl;   // 看栈顶：3
    s.pop();                    // 出栈：{1,2}
    cout << s.top() << endl;    // 2

    cout << s.size() << endl;   // 2
    cout << s.empty() << endl;  // false

    return 0;
}
```

### 栈的应用：括号匹配

```cpp
#include <stack>
#include <string>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) return false;
            char top = st.top();
            if ((c==')'&&top!='(') || (c==']'&&top!='[') || (c=='}'&&top!='{')) {
                return false;
            }
            st.pop();
        }
    }
    return st.empty();
}

int main() {
    cout << isValid("()[]{}") << endl;  // 1（真）
    cout << isValid("([)]") << endl;     // 0（假）
    return 0;
}
```

---

## 3. queue队列容器

**先进先出（FIFO）**

```cpp
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    q.push(1);   // 入队：{1}
    q.push(2);   // 入队：{1,2}
    q.push(3);   // 入队：{1,2,3}

    cout << q.front() << endl;   // 看队首：1
    cout << q.back() << endl;     // 看队尾：3
    q.pop();                      // 出队：{2,3}
    cout << q.front() << endl;    // 2

    return 0;
}
```

---

## 4. deque双端队列

两端都可以插入和删除。

```cpp
#include <deque>
using namespace std;

deque<int> dq;
dq.push_back(1);    // 尾部加：{1}
dq.push_front(2);    // 头部加：{2,1}
dq.push_back(3);     // 尾部加：{2,1,3}

cout << dq.front() << endl;  // 2
cout << dq.back() << endl;   // 3
```

---

## 5. 算法排序与查找

```cpp
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};

    // 排序
    sort(v.begin(), v.end());         // 升序
    sort(v.begin(), v.end(), greater<int>()); // 降序

    // 查找
    auto it = find(v.begin(), v.end(), 5);
    if (it != v.end()) {
        cout << "找到：" << *it << endl;
    }

    // 最大最小
    cout << *max_element(v.begin(), v.end()) << endl;  // 9
    cout << *min_element(v.begin(), v.end()) << endl;  // 1

    return 0;
}
```

---

## 本章小结

1. `vector`：动态数组，最常用的容器，支持随机访问
2. `stack`：后进先出，适合括号匹配、表达式求值
3. `queue`：先进先出，适合BFS广搜、任务调度
4. `deque`：双端队列，两端操作都高效
5. `algorithm`：提供`sort`、`find`、`max_element`等算法
"""
    ),

    (
        "深度优先搜索（DFS）",
        "dfs",
        "algorithm", 4, 10,
        """# 深度优先搜索（DFS）

## 本章简介

DFS（Depth-First Search）是图和树遍历的核心算法，通过深度优先的方式系统搜索解空间。本章介绍DFS的思想、实现及其在排列组合、走迷宫等问题中的应用。

---

## 1. DFS基本思想

### 核心思想

"一条路走到黑，不撞南墙不回头"——沿着一条路径一直搜索，遇到死胡同就回退到上一个节点，尝试其他路径。

### 与BFS的区别

| 特征 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈（递归调用栈） | 队列 |
| 搜索顺序 | 深入再回退 | 层层扩散 |
| 特点 | 占用内存少 | 能找到最短路径 |
| 适合问题 | 排列组合、连通块 | 最短路、层次遍历 |

---

## 2. 递归实现DFS

### 模板

```cpp
void dfs(int state) {
    // 1. 判断终止条件
    if (/* 到达目标状态 */) {
        // 记录答案
        return;
    }

    // 2. 剪枝：排除非法情况
    if (/* 不合法 */) return;

    // 3. 尝试每一种选择
    for (每一种可能的选择) {
        if (这种选择可行) {
            // 做选择
            choose();

            // 4. 递归下一层
            dfs(state + 1);

            // 5. 撤销选择（回溯）
            undo();
        }
    }
}
```

---

## 3. 全排列问题

### 例题：输出1~n的全排列

```cpp
#include <iostream>
using namespace std;

int n;
int used[11];       // 标记哪些数字用过
int path[11];        // 当前排列

void dfs(int step) {
    if (step > n) {  // 排列完成
        for (int i = 1; i <= n; i++) {
            cout << path[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (!used[i]) {       // 数字i还没用过
            used[i] = 1;      // 做选择
            path[step] = i;

            dfs(step + 1);     // 递归下一位

            used[i] = 0;      // 撤销选择
        }
    }
}

int main() {
    n = 3;
    dfs(1);
    return 0;
}
```

**输出**：
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

---

## 4. 组合问题

### 例题：从n个数中选k个数的组合

```cpp
#include <iostream>
using namespace std;

int n = 5, k = 3;
int used[11];
int path[11];

void dfs(int start, int depth) {
    if (depth == k) {  // 选够了k个数
        for (int i = 0; i < k; i++) {
            cout << path[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = start; i <= n; i++) {  // 从start开始避免重复
        path[depth] = i;
        dfs(i + 1, depth + 1);
    }
}

int main() {
    dfs(1, 0);
    return 0;
}
```

---

## 5. 迷宫问题

### 经典迷宫（0通路1墙）

```cpp
#include <iostream>
using namespace std;

int n = 5, m = 5;
int maze[5][5] = {
    {0, 0, 1, 0, 0},
    {0, 0, 0, 0, 0},
    {1, 0, 1, 0, 1},
    {0, 0, 0, 0, 0},
    {0, 1, 0, 0, 0}
};
int vis[5][5];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

bool dfs(int x, int y) {
    if (x == n-1 && y == m-1) {  // 到达终点
        return true;
    }

    vis[x][y] = 1;

    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
            maze[nx][ny] == 0 && !vis[nx][ny]) {
            if (dfs(nx, ny)) return true;
        }
    }

    return false;
}

int main() {
    if (dfs(0, 0)) {
        cout << "有路径" << endl;
    } else {
        cout << "无路径" << endl;
    }
    return 0;
}
```

---

## 6. DFS+剪枝

剪枝是提升DFS效率的关键。

### 例题：N皇后问题

```cpp
#include <iostream>
using namespace std;

int n = 8;
int queenPos[8];  // queenPos[i]=j 表示第i行皇后在第j列
int cnt = 0;

bool isValid(int row, int col) {
    for (int i = 0; i < row; i++) {
        int j = queenPos[i];
        if (j == col) return false;              // 同一列
        if (row - i == abs(col - j)) return false; // 同一对角线
    }
    return true;
}

void dfs(int row) {
    if (row == n) {
        cnt++;
        return;
    }

    for (int col = 0; col < n; col++) {
        if (isValid(row, col)) {
            queenPos[row] = col;
            dfs(row + 1);
            queenPos[row] = -1;
        }
    }
}

int main() {
    dfs(0);
    cout << cnt << endl;  // 8皇后有92种摆法
    return 0;
}
```

---

## 本章小结

1. DFS核心：递归+回溯，用栈实现
2. 模板：终止条件→剪枝→选择→递归→撤销
3. 全排列：标记+路径数组
4. 组合：从start开始避免重复
5. 迷宫：4方向扩展，注意边界
6. 剪枝：提前排除无效搜索，大幅提升效率
"""
    ),

    (
        "广度优先搜索（BFS）",
        "bfs",
        "algorithm", 4, 11,
        """# 广度优先搜索（BFS）

## 本章简介

BFS（Breath-First Search）采用层层扩展的方式搜索，能在无权图中找到从起点到终点的最短路径。本章介绍BFS的实现及其在最短路、层序遍历等问题中的应用。

---

## 1. BFS基本思想

### 核心思想

从起点开始，一层一层向外扩展，先访问离起点最近的节点，再访问远的节点。

### 实现方式

使用**队列**（FIFO）：队首出队，拓展所有邻居入队。

```
队列: [起点]
出队 → 入队邻居 → 队首出队 → 入队邻居 → ...
```

---

## 2. BFS模板

```cpp
#include <queue>
using namespace std;

void bfs(起点) {
    queue<状态> q;
    q.push(起点);
    vis[起点] = true;

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();

        if (/* 达到目标 */) {
            // 处理答案
        }

        for (每一种扩展方式) {
            auto next = cur扩展后的状态;
            if (next合法 && !vis[next]) {
                q.push(next);
                vis[next] = true;
            }
        }
    }
}
```

---

## 3. 图的BFS遍历

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // 邻接表
    vector<vector<int>> g = {
        {1, 2},      // 0号点连接1,2
        {0, 3, 4},   // 1号点连接0,3,4
        {0, 5},      // 2号点连接0,5
        {1},         // 3号点连接1
        {1, 6},      // 4号点连接1,6
        {2},         // 5号点连接2
        {4}          // 6号点连接4
    };

    queue<int> q;
    vector<bool> vis(7, false);

    q.push(0);  // 从0开始
    vis[0] = true;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        cout << cur << " ";  // 访问

        for (int nxt : g[cur]) {
            if (!vis[nxt]) {
                q.push(nxt);
                vis[nxt] = true;
            }
        }
    }
    // 输出：0 1 2 3 4 5 6
    return 0;
}
```

---

## 4. BFS求最短路

### 例题：迷宫最短路径

```cpp
#include <iostream>
#include <queue>
using namespace std;

struct Node {
    int x, y, dist;
};

int n = 5, m = 5;
int maze[5][5] = {
    {0, 0, 1, 0, 0},
    {0, 0, 0, 0, 0},
    {1, 0, 1, 0, 1},
    {0, 0, 0, 0, 0},
    {0, 1, 0, 0, 0}
};
bool vis[5][5];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int bfs() {
    queue<Node> q;
    q.push({0, 0, 0});
    vis[0][0] = true;

    while (!q.empty()) {
        Node cur = q.front();
        q.pop();

        if (cur.x == n-1 && cur.y == m-1) {
            return cur.dist;
        }

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
                maze[nx][ny] == 0 && !vis[nx][ny]) {
                q.push({nx, ny, cur.dist + 1});
                vis[nx][ny] = true;
            }
        }
    }
    return -1;  // 不可达
}

int main() {
    int ans = bfs();
    if (ans >= 0) cout << "最短路径：" << ans << endl;
    else cout << "不可达" << endl;
    return 0;
}
```

---

## 5. 拓扑排序（BFS实现）

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n = 6;  // 6个任务
    vector<vector<int>> g(n);
    vector<int> indeg(n, 0);  // 入度

    // 添加边：0→2, 0→3, 1→3, 1→4, 3→5, 4→5
    g[0] = {2, 3};
    g[1] = {3, 4};
    g[3] = {5};
    g[4] = {5};

    for (int i = 0; i < n; i++) {
        for (int j : g[i]) indeg[j]++;
    }

    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indeg[i] == 0) q.push(i);
    }

    vector<int> topo;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        topo.push_back(cur);

        for (int nxt : g[cur]) {
            if (--indeg[nxt] == 0) {
                q.push(nxt);
            }
        }
    }

    if (topo.size() == n) {
        cout << "拓扑序：";
        for (int x : topo) cout << x << " ";
    }
    return 0;
}
```

---

## 6. BFS与DFS对比

| 特征 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈（递归） | 队列 |
| 搜索顺序 | 深度优先 | 层次优先 |
| 最短路 | ❌ 不能保证 | ✅ 能保证 |
| 内存占用 | 较省内存 | 较多（存一整层） |
| 适用场景 | 排列组合、连通块 | 最短路、拓扑排序 |

---

## 本章小结

1. BFS用队列实现，层层扩展
2. 用`vis`数组避免重复访问
3. BFS能找到**最短路径**（在无权图中）
4. BFS适合：迷宫最短路、层序遍历、拓扑排序
5. DFS适合：全排列、组合、连通块、递归深搜
"""
    ),

    (
        "贪心算法",
        "greedy",
        "algorithm", 3, 12,
        """# 贪心算法

## 本章简介

贪心算法在每一步都做出当前最优的选择，期望通过局部最优达到全局最优。本章介绍贪心的思想、证明方法及典型应用。

---

## 1. 贪心思想

### 什么是贪心

在解决问题时，每一步都选择**当前状态下最优**的选择，不考虑全局，不回退。

### 贪心 vs 动态规划

| 特征 | 贪心 | 动态规划 |
|------|------|----------|
| 选择 | 只看当前最优 | 考虑所有子问题 |
| 最优性 | 需要证明 | 保证最优 |
| 效率 | 通常O(n) | 通常O(n²)或更高 |

---

## 2. 经典问题：活动选择

### 问题描述

有n个活动，每个活动有开始和结束时间，选择最多不重叠的活动。

### 贪心策略

**选择结束时间最早的活动**——给后面的活动留更多时间。

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Activity {
    int start, end;
};

bool cmp(Activity a, Activity b) {
    return a.end < b.end;  // 按结束时间排序
}

int main() {
    int n = 5;
    Activity acts[] = {
        {1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 9}
    };

    sort(acts, acts + n, cmp);

    int cnt = 0;
    int lastEnd = 0;

    for (int i = 0; i < n; i++) {
        if (acts[i].start >= lastEnd) {
            cnt++;
            lastEnd = acts[i].end;
            cout << "选择活动：" << i << endl;
        }
    }

    cout << "最多选择：" << cnt << endl;
    return 0;
}
```

---

## 3. 经典问题：钱币找零

### 问题描述

用最少数量的纸币找零。

### 策略：优先用大面额

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int money = 73;  // 需要找73元
    int coins[] = {100, 50, 20, 10, 5, 1};  // 纸币面额
    int count = 0;

    for (int c : coins) {
        if (money >= c) {
            int num = money / c;
            count += num;
            money -= num * c;
            if (num > 0) cout << c << "元：" << num << "张" << endl;
        }
    }

    cout << "总共" << count << "张" << endl;
    return 0;
}
```

---

## 4. 经典问题：区间调度

### 问题：选择最多不相交的区间

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Interval {
    int start, end;
};

bool cmp(Interval a, Interval b) {
    return a.end < b.end;
}

int main() {
    Interval segs[] = {
        {1, 3}, {2, 5}, {4, 7}, {6, 9}, {8, 10}
    };
    int n = 5;

    sort(segs, segs + n, cmp);

    int cnt = 0;
    int lastEnd = 0;

    for (int i = 0; i < n; i++) {
        if (segs[i].start >= lastEnd) {
            cnt++;
            lastEnd = segs[i].end;
        }
    }

    cout << "最多区间数：" << cnt << endl;  // 3
    return 0;
}
```

---

## 5. 经典问题：哈夫曼编码（了解）

使用最小堆，每次合并重量最小的两棵树。

```cpp
#include <queue>
#include <iostream>
using namespace std;

int main() {
    int a[] = {2, 3, 6, 7, 10, 13};
    priority_queue<long long, vector<long long>, greater<long long>> pq;

    for (int x : a) pq.push(x);

    long long cost = 0;
    while (pq.size() > 1) {
        long long x = pq.top(); pq.pop();
        long long y = pq.top(); pq.pop();
        cost += x + y;
        pq.push(x + y);
    }

    cout << "最小代价：" << cost << endl;
    return 0;
}
```

---

## 6. 贪心算法的证明

贪心算法容易写错，需要证明。

### 证明方法：交换论证

假设存在一个最优解O，我们的贪心解是G：
1. 比较O和G的第一个不同选择
2. 证明把O的那个选择换成G的选择，不会更差
3. 通过若干次交换，可以把O变成G，且代价不增加
4. 因此G也是最优的

**例**：活动选择——选择结束最早的，交换后后面活动开始时间不会更晚。

---

## 本章小结

1. 贪心：每步最优，期望全局最优
2. 需要证明贪心选择性质和最优子结构
3. 典型问题：活动选择、区间调度、货币找零、哈夫曼编码
4. 贪心代码通常简洁高效
5. 不能用贪心时考虑动态规划
"""
    ),

    (
        "前缀和与差分",
        "prefix-sum",
        "algorithm", 4, 13,
        """# 前缀和与差分

## 本章简介

前缀和与差分是处理区间查询的高效技巧，将O(n)查询优化到O(1)，是竞赛中的必备技能。

---

## 1. 一维前缀和

### 什么是前缀和

`prefix[i]` = a[1] + a[2] + ... + a[i]

```cpp
int n = 10;
int a[11] = {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
int prefix[11];

// 构建前缀和
for (int i = 1; i <= n; i++) {
    prefix[i] = prefix[i-1] + a[i];
}

// 查询区间和：a[l]+...+a[r] = prefix[r] - prefix[l-1]
int l = 3, r = 7;
int sum = prefix[r] - prefix[l-1];
cout << sum << endl;  // 5+7+9+11+13 = 45
```

### 核心公式

```
区间[l, r]的元素和 = prefix[r] - prefix[l-1]
```

---

## 2. 差分数组

### 什么是差分

差分是前缀和的逆运算。

```cpp
int n = 10;
int a[11] = {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
int diff[12] = {0};

// 构建差分数组
diff[1] = a[1];
for (int i = 2; i <= n; i++) {
    diff[i] = a[i] - a[i-1];
}

// 通过差分还原前缀和（还原a数组）
int还原[11];
还原[1] = diff[1];
for (int i = 2; i <= n; i++) {
    还原[i] = 还原[i-1] + diff[i];
}
```

### 差分的核心用途：区间修改

如果要对区间[l, r]中的每个元素加上k：

```cpp
diff[l] += k;
diff[r+1] -= k;  // r之后的位置要抵消
```

最后对diff求前缀和，就得到了修改后的数组。

**例子**：把a[2..5]都加3
```cpp
diff[2] += 3;   // 从第2项开始加3
diff[6] -= 3;   // 第6项开始减3（抵消）
// 求前缀和后：第2、3、4、5项都被加了3
```

---

## 3. 二维前缀和

### 公式

```
S[x][y] = a[1][1] + ... + a[x][y]（左上角矩阵的和）

子矩阵 (x1,y1) 到 (x2,y2) 的和 =
S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
```

```cpp
int a[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 5, 6, 7, 8},
    {0, 9, 10,11,12},
    {0, 13,14,15,16}
};

int S[5][5] = {0};

// 构建二维前缀和
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= 4; j++) {
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + a[i][j];
    }
}

// 查询(2,2)到(3,3)的和
int x1=2, y1=2, x2=3, y2=3;
int sum = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1];
cout << sum << endl;  // 6+7+10+11 = 34
```

---

## 4. 典型应用

### 应用1：静态区间和查询

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    int a[100005];
    int prefix[100005] = {0};

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        prefix[i] = prefix[i-1] + a[i];
    }

    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << prefix[r] - prefix[l-1] << endl;
    }

    return 0;
}
```

---

## 本章小结

1. 一维前缀和：`sum(l,r) = prefix[r] - prefix[l-1]`，查询O(1)
2. 差分数组：对区间批量加减，只需修改2个点
3. 二维前缀和：子矩阵和 = 四个角的前缀和组合
4. 前缀和是竞赛必备技巧，大幅降低查询复杂度
"""
    ),

    (
        "动态规划基础（一维DP）",
        "dynamic-programming",
        "algorithm", 5, 14,
        """# 动态规划基础（一维DP）

## 本章简介

动态规划（DP）是竞赛中最重要的算法之一。本章介绍DP的核心思想、状态定义、状态转移方程，通过经典例题一步步掌握DP。

---

## 1. 什么是动态规划

### 核心思想

把原问题分解为**重叠的子问题**，通过保存子问题的解避免重复计算。

### 三个关键要素

1. **状态**：`dp[i]`——问题的某个阶段
2. **转移**：`dp[i] = f(dp[...])`——从一个状态到另一个状态
3. **初始化**：`dp[0]`或`dp[1]`——边界条件

### DP vs 递归+记忆化

```cpp
// 递归（自顶向下）+记忆化
int memo[100];
int fib(int n) {
    if (n <= 2) return 1;
    if (memo[n]) return memo[n];
    return memo[n] = fib(n-1) + fib(n-2);
}

// 动态规划（自底向上）
int fibDP(int n) {
    if (n <= 2) return 1;
    int dp[100] = {0};
    dp[1] = dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}
```

---

## 2. 经典例题：爬楼梯

### 问题

一次爬1阶或2阶，到第n阶有多少种方法？

### 分析

- `dp[i]`：到达第i阶的方法数
- `dp[i] = dp[i-1] + dp[i-2]`（从i-1走1步或从i-2走2步）
- `dp[1]=1, dp[2]=2`

```cpp
int climbStairs(int n) {
    if (n <= 2) return n;
    int dp[1000] = {0};
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}
```

---

## 3. 经典例题：最大子段和

### 问题

给定整数数组，找连续子序列的最大和（至少包含一个元素）。

### 分析

- `dp[i]`：以第i个元素结尾的最大子段和
- 如果`dp[i-1] < 0`，不如从i重新开始
- `dp[i] = max(a[i], dp[i-1] + a[i])`

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int maxSubArray(int a[], int n) {
    int dp[10000];
    dp[0] = a[0];
    int ans = dp[0];

    for (int i = 1; i < n; i++) {
        dp[i] = max(a[i], dp[i-1] + a[i]);
        ans = max(ans, dp[i]);
    }

    return ans;
}

int main() {
    int a[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << maxSubArray(a, 9) << endl;  // 6（{4,-1,2,1}）
    return 0;
}
```

---

## 4. 经典例题：打家劫舍

### 问题

不能偷连续的两家，能偷到的最大金额。

### 分析

- `dp[i]`：偷到第i家时的最大金额
- `dp[i] = max(dp[i-1], dp[i-2] + money[i])`（不偷或偷）

```cpp
int rob(int money[], int n) {
    if (n == 0) return 0;
    if (n == 1) return money[0];

    int dp[1000];
    dp[0] = money[0];
    dp[1] = max(money[0], money[1]);

    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i-1], dp[i-2] + money[i]);
    }

    return dp[n-1];
}
```

---

## 5. 经典例题：最长上升子序列（LIS）

### 问题

找到数组中最长的严格递增子序列长度。

### 分析

- `dp[i]`：以`a[i]`结尾的最长上升子序列长度
- `dp[i] = max(dp[j] + 1)`，其中`j < i`且`a[j] < a[i]`

```cpp
#include <algorithm>
using namespace std;

int lengthOfLIS(int a[], int n) {
    int dp[10000] = {0};
    int ans = 0;

    for (int i = 0; i < n; i++) {
        dp[i] = 1;  // 自己成一个序列
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        ans = max(ans, dp[i]);
    }

    return ans;
}
```

---

## 6. DP解题步骤总结

```
1. 定义状态：dp[i]表示什么
2. 找出状态转移方程
3. 确定初始化（边界）
4. 确定遍历顺序
5. 举例验证
```

---

## 本章小结

1. DP核心：状态+转移+初始化
2. 自底向上比递归+记忆化更高效
3. 爬楼梯：`dp[i] = dp[i-1] + dp[i-2]`
4. 最大子段和：`dp[i] = max(a[i], dp[i-1]+a[i])`
5. 打家劫舍：`dp[i] = max(dp[i-1], dp[i-2]+money[i])`
6. LIS：`dp[i] = max(dp[j]+1)`（j < i且a[j] < a[i]）
"""
    ),

    (
        "初等数论",
        "number-theory",
        "math", 4, 15,
        """# 初等数论

## 本章简介

数论是CSP-J的重要内容。本章介绍质数、约数、模运算、欧几里得算法和埃氏筛法。

---

## 1. 质数判定

### 试除法

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

**优化**：只需判断到`√n`，时间复杂度O(√n)。

---

## 2. 埃氏筛法（求1~n所有质数）

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> sieve(int n) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) primes.push_back(i);
    }
    return primes;
}
```

**时间复杂度**：O(n log log n)

---

## 3. 欧几里得算法（最大公约数）

### 辗转相除法

```cpp
// 递归版本
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// 迭代版本（更高效）
int gcdIter(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

### 性质

- `gcd(a, b) = gcd(b, a % b)`
- `gcd(a, 0) = a`
- `lcm(a, b) = a * b / gcd(a, b)`（最小公倍数）

---

## 4. 模运算

### 基本性质

```cpp
// 加法：(a + b) % mod = ((a % mod) + (b % mod)) % mod
// 减法：(a - b) % mod = ((a % mod) - (b % mod) + mod) % mod
// 乘法：(a * b) % mod = ((a % mod) * (b % mod)) % mod
```

### 快速幂（模幂运算）

```cpp
// 计算 a^e % mod，时间复杂度 O(log e)
long long modPow(long long a, long long e, long long mod) {
    long long res = 1;
    a %= mod;
    while (e > 0) {
        if (e & 1) res = res * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return res;
}
```

---

## 5. 唯一分解定理

任何一个大于1的整数都可以唯一分解为质数的乘积。

```cpp
// 分解质因数
void factor(int n) {
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            cout << i << " ";
            n /= i;
        }
    }
    if (n > 1) cout << n << endl;
}

// 60 = 2^2 × 3^1 × 5^1
```

---

## 6. 扩展欧几里得算法

求`ax + by = gcd(a, b)`的解。

```cpp
int exgcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int g = exgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
```

---

## 本章小结

1. 质数判定：试除到√n
2. 埃氏筛法：O(n log log n)求所有质数
3. 欧几里得算法：辗转相除求gcd，O(log min(a,b))
4. 模运算：加/减/乘都可以先取模再算
5. 快速幂：O(log e)计算a^e % mod
6. 唯一分解：任何数可唯一分解为质数乘积
"""
    ),

    (
        "排列组合与杨辉三角",
        "permutations-and-combinations",
        "math", 4, 16,
        """# 排列组合与杨辉三角

## 本章简介

排列组合是计数问题的基础，杨辉三角是组合数的几何表示，在竞赛中应用广泛。

---

## 1. 加法原理与乘法原理

- **加法原理**：完成一件事有n类方法，第i类有mᵢ种，则总方法数为m₁+m₂+...+mₙ
- **乘法原理**：完成一件事分n步，第i步有mᵢ种，则总方法数为m₁×m₂×...×mₙ

---

## 2. 排列数

从n个不同元素中取出m个排成一排，有序。

```
A(n,m) = n! / (n-m)! = n × (n-1) × ... × (n-m+1)
```

```cpp
// 计算排列数
long long A(int n, int m) {
    long long res = 1;
    for (int i = 0; i < m; i++) {
        res *= (n - i);
    }
    return res;
}
```

---

## 3. 组合数

从n个不同元素中取出m个，不考虑顺序。

```
C(n,m) = n! / (m! × (n-m)!)
```

### 递推公式（杨辉三角）

```
C(n,m) = C(n-1,m) + C(n-1,m-1)
C(n,0) = C(n,n) = 1
```

```cpp
// 预处理组合数（杨辉三角）
long long C[100][100];

for (int i = 0; i <= 100; i++) {
    C[i][0] = C[i][i] = 1;
    for (int j = 1; j < i; j++) {
        C[i][j] = C[i-1][j] + C[i-1][j-1];
    }
}

// C[n][m]就是答案
cout << C[5][2] << endl;  // 10
```

### 逆元优化（大组合数）

```cpp
#include <iostream>
using namespace std;

const long long MOD = 1e9+7;
const int MAXN = 1e6+5;

long long fac[MAXN];  // 阶乘
long long inv[MAXN];  // 逆元

long long modPow(long long a, long long e) {
    long long res = 1;
    while (e) {
        if (e & 1) res = res * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return res;
}

void init() {
    fac[0] = 1;
    for (int i = 1; i < MAXN; i++)
        fac[i] = fac[i-1] * i % MOD;
    inv[MAXN-1] = modPow(fac[MAXN-1], MOD-2);
    for (int i = MAXN-2; i >= 0; i--)
        inv[i] = inv[i+1] * (i+1) % MOD;
}

long long C(int n, int m) {
    if (m > n) return 0;
    return fac[n] * inv[m] % MOD * inv[n-m] % MOD;
}
```

---

## 4. 杨辉三角

```
row 0:         1
row 1:        1 1
row 2:       1 2 1
row 3:      1 3 3 1
row 4:     1 4 6 4 1
row 5:   1 5 10 10 5 1
```

### 打印前n行

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 10;
    for (int i = 0; i < n; i++) {
        // 打印空格（居中）
        for (int s = 0; s < n - i - 1; s++) cout << "  ";
        for (int j = 0; j <= i; j++) {
            if (j) cout << "  ";
            if (i == 0 || j == 0)
                cout << 1;
            else
                cout << C(i, j);
        }
        cout << endl;
    }
    return 0;
}
```

---

## 5. 典型应用

### 路径计数

```cpp
// 从(0,0)到(m,n)，只能向右或向下走多少条路？
// 答案 = C(m+n, m) 或 C(m+n, n)
cout << C(5+3, 5) << endl;  // 56条路
```

---

## 本章小结

1. 加法原理：分类相加，乘法原理：分步相乘
2. 排列数A(n,m) = n!/(n-m)!，组合数C(n,m) = n!/(m!(n-m)!)
3. 杨辉三角递推：C(i,j) = C(i-1,j) + C(i-1,j-1)
4. 大组合数用阶乘+逆元：O(n)预处理，O(1)查询
5. 常见问题：路径计数、选择方案数
"""
    ),

]


def main():
    from app.core.database import SessionLocal
    from app.models.chapter import Chapter

    db = SessionLocal()
    count = 0

    for title, slug, cat_slug, difficulty, order, content in CHAPTERS:
        # 找category_id
        cat = db.query(Category).filter(Category.slug == cat_slug).first()
        if not cat:
            print(f"警告：分类{cat_slug}不存在，跳过章节《{title}》")
            continue

        # 检查是否已存在
        existing = db.query(Chapter).filter(Chapter.slug == slug).first()
        if existing:
            print(f"已存在，跳过：{slug}")
            continue

        chapter = Chapter(
            title=title,
            slug=slug,
            content=content,
            difficulty=difficulty,
            order=order,
            category_id=cat.id,
        )
        db.add(chapter)
        count += 1

    db.commit()
    print(f"\\n✅ 成功插入 {count} 个章节")
    db.close()


if __name__ == "__main__":
    main()
