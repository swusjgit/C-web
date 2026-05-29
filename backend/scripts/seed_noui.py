#!/usr/bin/env python3
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.category import Category

# 所有章节数据：(title, slug, cat_slug, difficulty, order, content_md)
CHAPTERS = [

    # ============================================================
    # 难度1：基础知识与编程环境
    # ============================================================

    (
        "计算机系统组成与基本操作",
        "computer-basics",
        "syntax", 1, 1,
        """# 计算机系统组成与基本操作

## 本章简介

本章介绍计算机的基本构成、Windows/Linux操作系统基础操作、文件管理，以及竞赛环境简介。

---

## 1. 计算机基本构成

计算机由以下硬件组成：

| 硬件 | 作用 |
|------|------|
| **CPU**（中央处理器） | 执行计算和指令，计算机的大脑 |
| **内存**（RAM） | 临时存储程序和数据，断电后丢失 |
| **硬盘** | 永久存储数据，断电后保留 |
| **输入设备** | 键盘、鼠标等，向计算机输入信息 |
| **输出设备** | 显示器、打印机等，输出计算结果 |

**冯·诺依曼体系**：程序和数据都存在内存中，CPU从内存读取指令执行。

---

## 2. Windows基本操作

### 文件与目录操作

- **创建文件夹**：右键 → 新建文件夹，或 `mkdir` 命令
- **复制文件**：`Ctrl+C` 复制，`Ctrl+V` 粘贴
- **移动文件**：拖动或 `Ctrl+X` 剪切 + `Ctrl+V` 粘贴
- **删除文件**：`Delete` 删除到回收站，`Shift+Delete` 直接删除

### 常用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+C` | 复制 |
| `Ctrl+V` | 粘贴 |
| `Ctrl+Z` | 撤销 |
| `Ctrl+S` | 保存 |
| `Alt+Tab` | 切换窗口 |

### 命令行基础

打开"命令提示符"（Win+R → 输入`cmd`）：

```bash
cd Desktop              # 进入桌面
dir                    # 查看当前目录文件
mkdir myproject        # 创建文件夹
del file.txt           # 删除文件
```

---

## 3. Linux基本概念（了解）

| 命令 | 功能 |
|------|------|
| `ls` | 列出文件 |
| `cd` | 切换目录 |
| `mkdir` | 创建目录 |
| `rm` | 删除文件 |
| `cp` | 复制文件 |
| `mv` | 移动/重命名文件 |

---

## 4. 程序编译运行基本概念

### 编译型语言 vs 解释型语言

C++是**编译型语言**，源代码需要经过编译器翻译成机器码才能执行：

```
源代码(.cpp) → 预处理器 → 编译器 → 汇编器 → 链接器 → 可执行文件
```

### 第一个C++程序

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

**操作步骤**（Dev-C++）：
1. 打开Dev-C++ → 新建源代码
2. 输入上述代码
3. 按 `F11` 编译运行
4. 看到黑色控制台输出 `Hello, World!` 表示成功

---

## 5. NOI历史与竞赛规则（了解）

- **NOI**（全国青少年信息学奥林匹克）是中国最高级别的中学生信息学竞赛
- **CSP-J**（非专业级软件能力认证-入门级）是NOI系列的第一轮
- **CSP-S**是提高级
- 比赛形式：笔试+上机编程
- 评分：机器评测，AC（正确）得满分

---

## 本章小结

1. 计算机由CPU、内存、硬盘、I/O设备组成
2. Windows基本操作：文件管理、快捷键、命令行
3. C++是编译型语言，需要编译才能运行
4. Dev-C++是最适合初学者的Windows IDE
5. NOI/CSP是中国中学生信息学竞赛体系
"""
    ),

    (
        "位、字节、进制与编码",
        "bit-byte-and-base",
        "syntax", 1, 2,
        """# 位、字节、进制与编码

## 本章简介

计算机内部所有数据都用二进制表示。本章介绍位、字节的概念，以及二进制、八进制、十进制、十六进制之间的转换。

---

## 1. 位、字节与字

- **位（bit）**：最小单位，只能是0或1
- **字节（Byte）**：1 Byte = 8 bit
- **字（Word）**：CPU一次处理的数据单位（32位/64位系统）

常用换算：
```
1 KB = 1024 Byte
1 MB = 1024 KB
1 GB = 1024 MB
```

---

## 2. 二进制

计算机内部使用二进制（基数为2），每位只能是0或1。

二进制转十进制：
```
1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11₁₀
```

---

## 3. 八进制与十六进制

| 进制 | 基数 | 数字符号 |
|------|------|----------|
| 二进制 | 2 | 0, 1 |
| 八进制 | 8 | 0~7 |
| 十进制 | 10 | 0~9 |
| 十六进制 | 16 | 0~9, A~F |

### C++中的进制表示

```cpp
int a = 10;     // 十进制
int b = 0b1010; // 二进制（C++14）
int c = 012;    // 八进制（前缀0）
int d = 0xA;    // 十六进制（前缀0x）
```

---

## 4. ASCII码

ASCII码用0~127的数字表示英文字母和常用符号。

```cpp
#include <iostream>
using namespace std;

int main() {
    char c = 'A';
    cout << c << "的ASCII码是：" << (int)c << endl;
    // 输出：A的ASCII码是：65

    cout << (char)97 << endl;  // 输出：a
    return 0;
}
```

常用ASCII：
- `'0'`~`'9'`：48~57
- `'A'`~`'Z'`：65~90
- `'a'`~`'z'`：97~122

---

## 本章小结

1. 1字节=8位，int通常4字节，long long 8字节
2. 二进制每位权值是2的幂
3. C++支持二进制（0b）、八进制（0）、十六进制（0x）
4. ASCII码用数字表示字符，'A'=65，'0'=48
"""
    ),

    (
        "第一个C++程序与Dev-C++使用",
        "first-program-and-ide",
        "syntax", 1, 3,
        """# 第一个C++程序与Dev-C++使用

## 本章简介

通过编写和运行第一个C++程序，熟悉开发环境，理解程序的基本结构和调试方法。

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

| 代码 | 含义 |
|------|------|
| `#include <iostream>` | 引入输入输出库 |
| `using namespace std;` | 使用标准命名空间 |
| `int main()` | 定义主函数（程序入口） |
| `cout << ... << endl;` | 输出内容到屏幕 |
| `return 0;` | 返回0表示正常结束 |

---

## 2. Dev-C++使用方法

### 安装与配置

1. 从官网下载Dev-C++安装包
2. 安装时选择中文语言
3. 默认设置即可，无需额外配置

### 新建和运行程序

1. **新建**：文件 → 新建 → 源代码（或`Ctrl+N`）
2. **编写**：输入代码
3. **编译运行**：按`F11`（或工具栏"编译运行"按钮）
4. **保存**：按`Ctrl+S`保存为`.cpp`文件

### 调试方法

- **编译错误**：红色文字指出错误行和原因，逐个修复
- **逻辑错误**：运行结果与预期不符，用`cout`在关键位置输出变量值
- **F8**设置断点，**F7**单步执行

---

## 3. 常见错误

```cpp
// ❌ 大小写错误
Cout << "Hello";  // C是大写

// ✅ 正确
cout << "Hello";

// ❌ 忘记分号
cout << "Hello" << endl  // 少分号

// ❌ 中文括号
cout << "Hello"（ endl）； // 中文括号
```

---

## 本章小结

1. 程序结构：`头文件 → using namespace → main函数`
2. Dev-C++是Windows下最适合初学者的C++ IDE
3. `F11`编译运行，`F7`单步调试
4. 常见错误：大小写、缺分号、中文标点
"""
    ),

    # ============================================================
    # 难度2
    # ============================================================

    (
        "变量、数据类型与常量",
        "variables-data-types-constants",
        "syntax", 2, 4,
        """# 变量、数据类型与常量

## 本章简介

介绍C++中变量的声明与使用、基本数据类型、以及常量的概念。这是C++程序设计的基石。

---

## 1. 变量

变量是内存中的一块存储空间，用来保存数据。

```cpp
int age = 15;        // 整数变量
double score = 92.5; // 小数变量
char grade = 'A';    // 字符变量
bool passed = true;  // 布尔变量
```

**命名规则**：
- 由字母、数字、下划线组成
- 不能以数字开头
- 区分大小写

---

## 2. 基本数据类型

### 整型

| 类型 | 大小 | 范围 |
|------|------|------|
| `int` | 4字节 | ±21亿 |
| `long long` | 8字节 | ±9×10¹⁸ |

```cpp
int a = 100000;
long long b = 1e12;
```

### 浮点型

```cpp
float f = 3.14f;      // 单精度
double d = 3.14159;   // 双精度，更常用
```

### 字符型与布尔型

```cpp
char c = 'A';    // 单引号
bool ok = true;  // true/false
```

---

## 3. 常量

```cpp
const int WEEK = 7;       // const常量（推荐）
#define PI 3.14159        // 宏定义（不推荐）
```

---

## 4. 基本运算

```cpp
int a = 10, b = 3;

cout << a + b << endl;   // 13 加
cout << a - b << endl;   // 7  减
cout << a * b << endl;   // 30 乘
cout << a / b << endl;   // 3  整数除法
cout << a % b << endl;   // 1  取余

// 关系运算
cout << (a > b) << endl;  // 1(true)

// 逻辑运算
cout << (a > 5 && b < 5) << endl;  // 1
cout << !(a == b) << endl;          // 1

// 三目运算
int max = (a > b) ? a : b;  // 10
```

---

## 本章小结

1. 变量：先声明后使用，遵守命名规则
2. 整型用`int/long long`，浮点用`double`，字符用`char`，布尔用`bool`
3. `const`定义常量，比`#define`更安全
4. 算术：`+ - * / %`；关系：`> < == !=`；逻辑：`&& || !`
5. 三目运算符：`条件 ? 值1 : 值2`
"""
    ),

    (
        "分支结构与switch语句",
        "if-and-switch",
        "syntax", 2, 5,
        """# 分支结构与switch语句

## 本章简介

学习使用`if`和`switch`实现程序的条件分支。

---

## 1. if分支

```cpp
int score;
cin >> score;

if (score >= 60) {
    cout << "及格" << endl;
} else {
    cout << "不及格" << endl;
}
```

### 多层条件

```cpp
if (score >= 90) cout << "优秀";
else if (score >= 80) cout << "良好";
else if (score >= 70) cout << "中等";
else if (score >= 60) cout << "及格";
else cout << "不及格";
```

---

## 2. switch语句

当需要对一个变量进行多个值的比较时，`switch`更清晰。

```cpp
char grade;
cin >> grade;

switch (grade) {
    case 'A':
        cout << "90~100分";
        break;
    case 'B':
        cout << "80~89分";
        break;
    case 'C':
        cout << "70~79分";
        break;
    case 'D':
        cout << "60~69分";
        break;
    default:
        cout << "成绩无效";
}
```

**注意**：
- `case`后是常量值，不是表达式
- `break`不能省略，否则会"穿透"
- `default`处理所有未匹配的情况

---

## 本章小结

1. `if-else`处理两个分支，`if-else if-else`处理多分支
2. `switch`适合等值分支判断，用`break`防止穿透
3. `&&`（与）、`||`（或）、`!`（非）用于复合条件
"""
    ),

    (
        "循环结构",
        "loops",
        "syntax", 2, 6,
        """# 循环结构

## 本章简介

循环是程序设计中最重要的结构之一。本章介绍`for`、`while`、`do-while`三种循环，以及循环嵌套。

---

## 1. for循环

```cpp
// 打印1到10
for (int i = 1; i <= 10; i++) {
    cout << i << " ";
}
// 输出：1 2 3 4 5 6 7 8 9 10
```

**执行顺序**：初始化→判断→循环体→更新→判断→...

---

## 2. while循环

```cpp
// 计算1+2+...+100
int sum = 0, i = 1;
while (i <= 100) {
    sum += i;
    i++;
}
cout << sum << endl;  // 5050
```

---

## 3. do-while循环

先执行再判断，保证至少执行一次：

```cpp
int n;
do {
    cin >> n;
} while (n < 1 || n > 100);
```

---

## 4. break和continue

```cpp
for (int i = 1; i <= 10; i++) {
    if (i == 5) break;      // 遇到5就停止整个循环
    if (i % 2 == 0) continue; // 跳过偶数
    cout << i << " ";  // 输出：1 3
}
```

---

## 5. 循环嵌套：打印九九乘法表

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

1. `for`适合已知循环次数，`while`适合条件驱动
2. `do-while`先执行再判断，至少执行一次
3. `break`跳出整个循环，`continue`跳过本次
4. 循环嵌套常用于二维图案和表格打印
"""
    ),

    (
        "数组与字符串",
        "arrays-and-strings",
        "syntax", 2, 7,
        """# 数组与字符串

## 本章简介

介绍一维数组、二维数组的基本使用，以及字符数组和string类的字符串处理。

---

## 1. 一维数组

### 声明与初始化

```cpp
int a[10];               // 声明10个整数
int b[5] = {1, 2, 3, 4, 5};     // 完全初始化
int c[5] = {1, 2};              // 部分初始化，未填的为0
int d[] = {10, 20, 30};         // 自动确定大小（3个元素）
```

### 遍历与基本操作

```cpp
int score[5] = {85, 92, 78, 96, 88};

// 遍历
for (int i = 0; i < 5; i++) {
    cout << score[i] << " ";
}

// 求最大值
int max = score[0];
for (int i = 1; i < 5; i++) {
    if (score[i] > max) max = score[i];
}
cout << "最大：" << max << endl;

// 数组长度
int len = sizeof(score) / sizeof(score[0]);  // 5
```

---

## 2. 二维数组

```cpp
int a[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

// 遍历
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        cout << a[i][j] << " ";
    }
    cout << endl;
}
```

---

## 3. 字符数组

```cpp
char s1[] = {'H', 'e', 'l', 'l', 'o', '\\0'};  // 加\\0表示字符串结束
char s2[] = "Hello";  // 更简洁的写法

cout << s2 << endl;  // 输出Hello

// 字符串长度
int len = 0;
while (s2[len] != '\\0') len++;
cout << len << endl;  // 5
```

---

## 4. string类（推荐）

```cpp
#include <string>
using namespace std;

string s = "Hello";

// 长度
cout << s.length() << endl;  // 5

// 拼接
s += " World";
cout << s << endl;  // Hello World

// 字符访问
cout << s[0] << endl;  // H

// 子串
cout << s.substr(0, 5) << endl;  // Hello

// 查找
int pos = s.find("World");  // 6
```

---

## 本章小结

1. 数组下标从0开始
2. `sizeof(a)/sizeof(a[0])`计算数组长度
3. 字符数组用`\\0`结尾，string类更安全易用
4. string常用：`length`、`+`拼接、`substr`、`find`
"""
    ),

    (
        "函数与作用域",
        "functions-and-scope",
        "syntax", 2, 8,
        """# 函数与作用域

## 本章简介

学习函数的定义、调用、参数传递方式以及变量作用域。

---

## 1. 函数基础

### 定义与调用

```cpp
// 求最大值
int maxValue(int a, int b) {
    if (a > b) return a;
    return b;
}

int main() {
    cout << maxValue(3, 7) << endl;  // 7
    return 0;
}
```

---

## 2. 参数传递：值传递

```cpp
void doubleIt(int x) {
    x = x * 2;  // 只改变副本
}

int main() {
    int a = 5;
    doubleIt(a);
    cout << a << endl;  // 仍然是5，值传递不改变原变量
    return 0;
}
```

---

## 3. 作用域

```cpp
int x = 10;  // 全局变量

int main() {
    int x = 20;  // 局部变量，遮蔽全局变量
    cout << x << endl;      // 20（局部优先）
    cout << ::x << endl;    // 10（用::访问全局）
    return 0;
}
```

### 局部变量与全局变量

- **局部变量**：在函数内部声明，只在函数内有效
- **全局变量**：在所有函数外部声明，整个文件都有效

---

## 4. 递归函数

函数调用自身叫递归，必须有终止条件：

```cpp
// 阶乘
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// 斐波那契
int fib(int n) {
    if (n <= 2) return 1;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    cout << factorial(5) << endl;  // 120
    cout << fib(6) << endl;        // 8
    return 0;
}
```

---

## 本章小结

1. 函数：`返回类型 函数名(参数) { 函数体; return值; }`
2. 值传递：函数内修改不影响实参
3. 全局变量整个文件有效，局部变量只在函数内有效
4. 递归：函数调用自身，必须有终止条件，否则栈溢出
"""
    ),

    (
        "文件操作与重定向",
        "file-operations",
        "syntax", 2, 9,
        """# 文件操作与重定向

## 本章简介

学习C++的文件读写操作，以及输入输出重定向。

---

## 1. 文件读写

```cpp
#include <fstream>
using namespace std;

int main() {
    // 写入文件
    ofstream fout("output.txt");
    fout << "Hello, File!" << endl;
    fout << 123 << endl;
    fout.close();

    // 读取文件
    ifstream fin("input.txt");
    string s;
    int n;
    fin >> s >> n;
    cout << s << " " << n << endl;
    fin.close();

    return 0;
}
```

---

## 2. 重定向（在文件操作中）

```cpp
// freopen重定向（竞赛常用）
freopen("input.txt", "r", stdin);   // 从文件读
freopen("output.txt", "w", stdout); // 写到文件

// 恢复标准输入输出
freopen("/dev/tty", "r", stdin);
freopen("/dev/tty", "w", stdout);
```

---

## 3. 文本文件与二进制文件

```cpp
// 文本模式（默认）
ofstream fout("a.txt");
fout << 12345 << endl;  // 写入字符'1''2''3''4''5'

// 二进制模式
ofstream fout("a.bin", ios::binary);
int x = 12345;
fout.write((char*)&x, sizeof(x));  // 写入4字节
```

---

## 本章小结

1. `ifstream`读文件，`ofstream`写文件
2. `freopen`实现输入输出重定向，竞赛中常用
3. 文本模式：可读字符；二进制模式：按字节读写
"""
    ),

    (
        "枚举法与模拟法",
        "enumeration-and-simulation",
        "algorithm", 1, 10,
        """# 枚举法与模拟法

## 本章简介

枚举法和模拟法是最基础的算法思想，在CSP-J中应用广泛。

---

## 1. 枚举法（Brute Force）

逐一列举所有可能的情况，验证每个解是否符合条件。

### 例题：找出所有水仙花数

水仙花数：3位数，每位数字的立方和等于自身。

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 100; i <= 999; i++) {
        int a = i / 100;       // 百位
        int b = i / 10 % 10;   // 十位
        int c = i % 10;        // 个位
        if (a*a*a + b*b*b + c*c*c == i) {
            cout << i << " ";  // 153 370 371 407
        }
    }
    return 0;
}
```

---

## 2. 模拟法

根据题目描述，用代码逐步模拟过程。

### 例题：计算日期第二天

```cpp
#include <iostream>
using namespace std;

int main() {
    int y, m, d;
    cin >> y >> m >> d;

    int days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) days[2] = 29;

    d++;
    if (d > days[m]) {
        d = 1;
        m++;
        if (m > 12) {
            m = 1;
            y++;
        }
    }

    cout << y << "-" << m << "-" << d << endl;
    return 0;
}
```

---

## 本章小结

1. 枚举法：列举所有可能，找满足条件的解
2. 模拟法：把题目描述翻译成代码，逐步执行
3. 枚举时注意范围和剪枝，避免超时
"""
    ),

    (
        "位运算基础",
        "bit-operations",
        "syntax", 2, 11,
        """# 位运算基础

## 本章简介

位运算是直接对二进制位进行操作的运算，是竞赛中的重要技巧。

---

## 1. 六种基本位运算

```cpp
int a = 6, b = 3;  // a=110, b=011

cout << (a & b) << endl;   // 2 (110 & 011 = 010)
cout << (a | b) << endl;    // 7 (110 | 011 = 111)
cout << (a ^ b) << endl;    // 5 (110 ^ 011 = 101)
cout << (~a) << endl;       // -7（按位取反）
cout << (a << 1) << endl;   // 12（a×2，左移1位）
cout << (a >> 1) << endl;   // 3（a÷2，右移1位）
```

---

## 2. 常用位运算技巧

```cpp
int n = 12;  // 1100

// 取最低位的1
int lowbit = n & (-n);  // 4 (0100)

// 消除最低位的1
int after = n & (n - 1);  // 8 (1000)

// 判断是否为2的幂次
bool isPowerOf2(int x) {
    return x > 0 && (x & (x - 1)) == 0;
}

// 统计1的个数
int countOnes(int x) {
    int cnt = 0;
    while (x) {
        x &= (x - 1);
        cnt++;
    }
    return cnt;
}
```

---

## 本章小结

1. `&`（与）、`|`（或）、`^`（异或）、`~`（取反）、`<<`（左移）、`>>`（右移）
2. `n & (-n)` 取最低位的1
3. `n & (n-1)` 消除最低位的1，可用于判断2的幂、统计1的个数
4. 左移n位=乘2ⁿ，右移n位=除2ⁿ（向下取整）
"""
    ),

    (
        "集合、加法原理与乘法原理",
        "set-and-ppp",
        "math", 2, 12,
        """# 集合、加法原理与乘法原理

## 本章简介

这是计数问题的基础，竞赛中经常用到。

---

## 1. 集合（Set）

C++中使用`set`容器表示集合：

```cpp
#include <set>
#include <iostream>
using namespace std;

int main() {
    set<int> s;
    s.insert(3);
    s.insert(1);
    s.insert(4);
    s.insert(1);  // 重复，不插入

    for (int x : s) cout << x << " ";  // 自动排序：1 3 4

    cout << s.count(3) << endl;  // 1（存在）
    cout << s.count(2) << endl;  // 0（不存在）

    return 0;
}
```

---

## 2. 加法原理

完成一件事有**n类**方法，第i类有mᵢ种，则总方法数为：
```
m₁ + m₂ + ... + mₙ
```

**例**：从A地到B地，汽车3班，火车2班，飞机1班，共3+2+1=6种方式。

---

## 3. 乘法原理

完成一件事需要**n步**，第i步有mᵢ种，则总方法数为：
```
m₁ × m₂ × ... × mₙ
```

**例**：上衣4件，裤子3条，共有4×3=12种搭配方式。

---

## 本章小结

1. 加法原理：**分类**相加（每类方法都能独立完成这件事）
2. 乘法原理：**分步**相乘（每步缺一不可）
3. 竞赛中常结合排列组合使用
"""
    ),

    # ============================================================
    # 难度3
    # ============================================================

    (
        "多层循环与穷举优化",
        "nested-loops",
        "syntax", 3, 13,
        """# 多层循环与穷举优化

## 本章简介

介绍多层循环的应用以及如何通过数学分析减少穷举量。

---

## 1. 多层循环

```cpp
// 打印所有三位数中的完全平方数
for (int i = 1; i <= 9; i++) {
    for (int j = 0; j <= 9; j++) {
        for (int k = 0; k <= 9; k++) {
            int n = i*100 + j*10 + k;
            int m = sqrt(n);
            if (m*m == n) cout << n << " ";
        }
    }
}
```

---

## 2. 优化穷举

### 例题：找出所有各位数字之和为15的三位数

**不优化**：枚举所有900个三位数，逐个检查。
**优化**：利用各位数字之和=15，减少内层范围。

```cpp
for (int i = 1; i <= 9; i++) {           // 百位1~9
    for (int j = 0; j <= 9; j++) {       // 十位0~9
        int k = 15 - i - j;              // 直接算个位
        if (k >= 0 && k <= 9) {
            cout << i*100 + j*10 + k << " ";
        }
    }
}
```

---

## 本章小结

1. 多层循环嵌套，外层控制位数/规模
2. 优化思路：用数学关系减少内层循环范围
3. 减少无效计算，提升效率
"""
    ),

    (
        "数学库函数与三角/对数/指数",
        "math-functions",
        "syntax", 3, 14,
        """# 数学库函数与三角/对数/指数

## 本章简介

介绍C++数学库`<cmath>`中常用的数学函数。

---

## 1. 绝对值与取整

```cpp
#include <cmath>
#include <iostream>
using namespace std;

int main() {
    // 绝对值
    cout << abs(-5) << endl;       // 5（整数）
    cout << fabs(-3.14) << endl;   // 3.14（浮点数）

    // 取整
    cout << floor(3.7) << endl;   // 3.0（向下取整）
    cout << ceil(3.2) << endl;    // 4.0（向上取整）
    cout << round(3.5) << endl;   // 4（四舍五入）
    cout << trunc(3.9) << endl;   // 3（截断取整）

    // 整数取整
    cout << 7/4 << endl;          // 1（整数除法，向零取整）

    return 0;
}
```

---

## 2. 平方根与幂函数

```cpp
#include <cmath>

cout << sqrt(16) << endl;   // 4.0（平方根）
cout << pow(2, 10) << endl;  // 1024.0（2的10次方）
cout << pow(9, 0.5) << endl; // 3.0（9的平方根）

// 立方根（C++17）
cout << cbrt(27) << endl;   // 3.0
```

---

## 3. 三角函数（弧度制）

```cpp
#include <cmath>

double pi = acos(-1);  // π

cout << sin(pi/2) << endl;  // 1.0
cout << cos(pi) << endl;    // -1.0
cout << tan(pi/4) << endl;  // 1.0

// 角度转弧度
double deg = 45;
double rad = deg * acos(-1) / 180;
cout << sin(rad) << endl;  // 0.707（sin45°）
```

---

## 4. 对数与指数

```cpp
cout << exp(1) << endl;       // 2.71828（e¹）
cout << log(exp(1)) << endl;  // 1.0（ln e）
cout << log10(100) << endl;   // 2.0（log₁₀）
cout << log2(8) << endl;      // 3.0（log₂）

// 注意：C++没有log₂直接函数，可用换底公式
// log₂(x) = log(x) / log(2)
cout << log(8) / log(2) << endl;  // 3.0
```

---

## 本章小结

1. `abs/fabs`求绝对值，`floor/ceil/round`取整
2. `sqrt`平方根，`pow(底,指数)`幂函数
3. 三角函数参数是**弧度**不是角度
4. `log`是自然对数（ln），`log10`是以10为底，`log₂`用换底公式
"""
    ),

    (
        "结构体与联合体",
        "struct-and-union",
        "syntax", 3, 15,
        """# 结构体与联合体

## 本章简介

结构体是自定义数据类型的基础，联合体是特殊的数据结构。

---

## 1. 结构体基础

```cpp
struct Student {
    string name;
    int age;
    int score;
};

int main() {
    Student s1;
    s1.name = "张三";
    s1.age = 14;
    s1.score = 92;

    Student s2 = {"李四", 15, 88};

    cout << s1.name << ": " << s1.score << endl;
    return 0;
}
```

---

## 2. 结构体数组

```cpp
struct Score {
    string name;
    int chinese;
    int math;
};

Score scores[3] = {
    {"张三", 90, 85},
    {"李四", 88, 92},
    {"王五", 95, 89}
};

// 按总分排序
for (int i = 0; i < 3; i++) {
    for (int j = i+1; j < 3; j++) {
        int s1 = scores[i].chinese + scores[i].math;
        int s2 = scores[j].chinese + scores[j].math;
        if (s1 < s2) swap(scores[i], scores[j]);
    }
}
```

---

## 3. 联合体

联合体的所有成员**共享同一块内存**，同一时间只能使用一个成员。

```cpp
union Data {
    int i;
    double d;
    char c;
};

int main() {
    Data data;
    data.i = 65;
    cout << data.i << endl;   // 65
    data.c = 'A';
    cout << data.c << endl;   // A（i的值也被覆盖了）
    return 0;
}
```

**应用场景**：节省内存（结构体中互斥使用的字段）。

---

## 本章小结

1. 结构体：自定义数据类型，封装多个不同类型字段
2. 结构体数组：存放多个结构体变量
3. 联合体：所有成员共享内存，同时只能用一个
"""
    ),

    (
        "STL：min/max/swap/sort",
        "stl-algorithms",
        "algorithm", 3, 16,
        """# STL：min/max/swap/sort

## 本章简介

STL是C++标准库的重要组成部分。本章介绍四个最常用的算法函数。

---

## 1. min、max、swap

```cpp
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    cout << min(3, 7) << endl;           // 3
    cout << max(3, 7) << endl;           // 7
    swap(3, 7);                          // 交换

    // 三个数的最值
    cout << min({3, 1, 7}) << endl;     // 1（c++11初始化列表）
    cout << max({3, 1, 7}) << endl;     // 7

    return 0;
}
```

---

## 2. sort排序

```cpp
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};

    // 升序排序
    sort(v.begin(), v.end());  // {1,1,2,3,4,5,6,9}

    // 降序排序
    sort(v.begin(), v.end(), greater<int>());

    // 自定义比较：按绝对值大小排序
    vector<int> v2 = {-3, 1, -4, 1, 5, -9};
    sort(v2.begin(), v2.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });
    // 结果：1,1,-3,-4,5,-9

    return 0;
}
```

---

## 3. 数组排序

```cpp
int a[] = {3, 1, 4, 1, 5, 9};
int n = 6;

sort(a, a + n);  // 数组首地址和尾后地址
for (int i = 0; i < n; i++) cout << a[i] << " ";
```

---

## 本章小结

1. `min(a,b)`返回较小值，`max(a,b)`返回较大值
2. `swap(a,b)`交换两个变量的值
3. `sort(begin, end)`默认升序，`greater<int>()`降序
4. `sort`是竞赛中最高效的排序，O(n log n)
"""
    ),

    (
        "前缀和",
        "prefix-sum",
        "algorithm", 3, 17,
        """# 前缀和

## 本章简介

前缀和是一种预处理技术，能在O(1)时间内快速计算区间和。

---

## 1. 一维前缀和

```cpp
int a[11] = {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
int prefix[11];

// 构建前缀和：prefix[i] = a[1]+...+a[i]
for (int i = 1; i <= 10; i++) {
    prefix[i] = prefix[i-1] + a[i];
}

// 查询区间[3,7]的和
int l = 3, r = 7;
int sum = prefix[r] - prefix[l-1];  // 5+7+9+11+13 = 45
```

---

## 2. 统计出现次数

```cpp
// 统计0~100中每个数出现的次数（已知序列）
int n; cin >> n;
int cnt[101] = {0};
for (int i = 0; i < n; i++) {
    int x; cin >> x;
    cnt[x]++;
}

// 前缀和：cnt[x]表示<=x的数出现了多少次
for (int i = 1; i <= 100; i++) cnt[i] += cnt[i-1];
```

---

## 本章小结

1. 前缀和数组：`prefix[i] = sum(a[1]~a[i])`
2. 区间和：`sum(l,r) = prefix[r] - prefix[l-1]`，O(1)查询
3. 预处理O(n)，多次查询时效率极高
"""
    ),

    (
        "栈与队列",
        "stack-and-queue",
        "data-structure", 3, 18,
        """# 栈与队列

## 本章简介

栈和队列是两种重要的线性数据结构，分别对应"后进先出"和"先进先出"。

---

## 1. stack栈（后进先出）

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
    return 0;
}
```

### 应用：括号匹配

```cpp
#include <stack>
#include <string>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{')
            st.push(c);
        else {
            if (st.empty()) return false;
            char top = st.top();
            if ((c==')'&&top!='(') || (c==']'&&top!='[') || (c=='}'&&top!'{'))
                return false;
            st.pop();
        }
    }
    return st.empty();
}
```

---

## 2. queue队列（先进先出）

```cpp
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    q.push(1);   // 入队：{1}
    q.push(2);   // 入队：{1,2}
    q.push(3);   // 入队：{1,2,3}

    cout << q.front() << endl;   // 看队首：1
    q.pop();                      // 出队：{2,3}

    return 0;
}
```

### 应用：BFS广度优先搜索

```cpp
queue<int> q;
q.push(start);
vis[start] = true;

while (!q.empty()) {
    int cur = q.front();
    q.pop();
    for (每个邻居) {
        if (!vis[邻居]) {
            q.push(邻居);
            vis[邻居] = true;
        }
    }
}
```

---

## 本章小结

1. 栈（LIFO）：`push`入栈，`pop`出栈，`top`看栈顶
2. 队列（FIFO）：`push`入队，`pop`出队，`front`看队首
3. 栈适合括号匹配、表达式求值
4. 队列适合BFS、按层次处理
"""
    ),

    (
        "链表",
        "linked-list",
        "data-structure", 3, 19,
        """# 链表

## 本章简介

链表是线性数据结构，通过指针链接节点。本章介绍单链表、双向链表和循环链表。

---

## 1. 单向链表节点定义

```cpp
struct Node {
    int data;
    Node* next;
    Node(int x) : data(x), next(nullptr) {}
};
```

---

## 2. 头插法（插入到头部）

```cpp
void insertHead(Node*& head, int val) {
    Node* newNode = new Node(val);
    newNode->next = head;
    head = newNode;
}
```

---

## 3. 尾插法（插入到尾部）

```cpp
void insertTail(Node*& head, int val) {
    Node* newNode = new Node(val);
    if (!head) {
        head = newNode;
        return;
    }
    Node* p = head;
    while (p->next) p = p->next;
    p->next = newNode;
}
```

---

## 4. 删除节点

```cpp
void deleteNode(Node*& head, int val) {
    if (!head) return;
    if (head->data == val) {
        Node* tmp = head;
        head = head->next;
        delete tmp;
        return;
    }
    Node* p = head;
    while (p->next && p->next->data != val) p = p->next;
    if (p->next) {
        Node* tmp = p->next;
        p->next = tmp->next;
        delete tmp;
    }
}
```

---

## 5. 遍历链表

```cpp
void printList(Node* head) {
    for (Node* p = head; p; p = p->next) {
        cout << p->data;
        if (p->next) cout << " -> ";
    }
    cout << endl;
}
```

---

## 6. 释放内存

```cpp
void deleteList(Node*& head) {
    while (head) {
        Node* tmp = head;
        head = head->next;
        delete tmp;
    }
}
```

---

## 本章小结

1. 链表节点 = 数据 + 指针
2. 头插O(1)，尾插O(n)（需遍历），按值删除O(n)
3. 与数组对比：插入快但访问慢（不能随机访问）
4. 用`new`分配内存后要`delete`释放，避免内存泄漏
"""
    ),

    (
        "树与二叉树基础",
        "tree-basics",
        "data-structure", 3, 20,
        """# 树与二叉树基础

## 本章简介

树是一种层次结构，二叉树是最常用的树形结构。本章介绍树的基本概念和二叉树的性质。

---

## 1. 树的基本概念

- **节点**：树中的每个元素
- **根节点**：树的顶端，没有父节点
- **叶子节点**：没有子节点的节点
- **父节点/子节点**：上一层是下一层的父节点
- **深度**：从根到该节点的路径长度
- **高度**：从该节点到最深叶子节点的距离

---

## 2. 二叉树

每个节点最多有两个子节点（左孩子、右孩子）。

### 节点定义

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

---

## 3. 二叉树的基本性质

1. 第i层最多有`2^(i-1)`个节点（根节点为第1层）
2. 深度为k的二叉树最多有`2^k - 1`个节点
3. 叶节点数 = 度为2的节点数 + 1（n₀ = n₂ + 1）

---

## 4. 完全二叉树

除最后一层外，每层节点数都达到最大，且最后一层的节点都集中在左边。

完全二叉树的数组表示：
- 父节点：`i`
- 左孩子：`2i`
- 右孩子：`2i+1`

```cpp
// 用数组存储完全二叉树
int tree[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};  // 0号位不用

int parent(int i) { return i/2; }
int leftChild(int i) { return 2*i; }
int rightChild(int i) { return 2*i+1; }
```

---

## 本章小结

1. 树是层次结构，二叉树每个节点最多两个子节点
2. 二叉树第i层最多2^(i-1)个节点
3. 完全二叉树：除最后一层外每层满节点，最后一层左对齐
4. 完全二叉树可以用数组高效存储
"""
    ),

    (
        "初等数论：模运算与唯一分解",
        "number-theory-basics",
        "math", 3, 21,
        """# 初等数论：模运算与唯一分解

## 本章简介

数论是CSP-J的重要内容。本章介绍模运算、整数唯一分解和欧几里得算法。

---

## 1. 模运算

```cpp
int a = 17, b = 5;

cout << a % b << endl;    // 2（17除以5余2）
cout << (-7 % 3) << endl; // -1（负数取余，符号与被除数一致）

// 模运算性质（竞赛常用）
// (a + b) % mod = (a % mod + b % mod) % mod
// (a * b) % mod = (a % mod) * (b % mod) % mod
```

---

## 2. 整数唯一分解定理

任何大于1的整数都可以唯一分解为质数的乘积。

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

int main() {
    factor(60);  // 2 2 3 5（60 = 2² × 3 × 5）
    return 0;
}
```

---

## 3. 欧几里得算法（最大公约数）

### 辗转相除法

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

// 迭代版
int gcdIter(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

// 最小公倍数
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // 先除后乘避免溢出
}
```

---

## 4. 质数判定

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

---

## 本章小结

1. 模运算：`a % b`取余，注意负数结果符号
2. 唯一分解：任何数可分解为质数乘积
3. 欧几里得算法：gcd(a,b)=gcd(b,a%b)，O(log min(a,b))
4. lcm(a,b) = a/gcd(a,b)×b
5. 质数判定：试除到√n
"""
    ),

    (
        "排序算法",
        "sorting-algorithms",
        "algorithm", 3, 22,
        """# 排序算法

## 本章简介

介绍四种O(n²)排序算法，理解原理和稳定性。

---

## 1. 冒泡排序

```cpp
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-1-i; j++) {
            if (a[j] > a[j+1]) swap(a[j], a[j+1]);
        }
    }
}
```

---

## 2. 选择排序

```cpp
void selectionSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i+1; j < n; j++) {
            if (a[j] < a[minIdx]) minIdx = j;
        }
        swap(a[i], a[minIdx]);
    }
}
```

---

## 3. 插入排序

```cpp
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = key;
    }
}
```

---

## 4. 计数排序

```cpp
void countingSort(int a[], int n, int maxVal) {
    int count[1005] = {0};

    for (int i = 0; i < n; i++) count[a[i]]++;

    for (int i = 0, idx = 0; i <= maxVal; i++) {
        while (count[i]--) a[idx++] = i;
    }
}
```

---

## 排序对比

| 算法 | 时间复杂度 | 空间 | 稳定性 |
|------|-----------|------|--------|
| 冒泡 | O(n²) | O(1) | ✅ |
| 选择 | O(n²) | O(1) | ❌ |
| 插入 | O(n²)/O(n) | O(1) | ✅ |
| 计数 | O(n+k) | O(k) | ✅ |

---

## 本章小结

1. 冒泡：相邻交换，每趟最大冒到右边
2. 选择：每趟选最小，与未排序首元素交换（不稳定）
3. 插入：像整理扑克牌，已排序部分逐一插入
4. 计数：非比较排序，统计出现次数，O(n+k)
"""
    ),

    # ============================================================
    # 难度4
    # ============================================================

    (
        "指针基础",
        "pointers-basics",
        "syntax", 4, 23,
        """# 指针基础

## 本章简介

指针是C/C++的核心概念。本章介绍指针的定义、使用和常见应用。

---

## 1. 指针的定义与使用

```cpp
int a = 10;
int* p = &a;  // p存储a的地址

cout << p << endl;   // a的地址
cout << *p << endl;  // 10（解引用，取值）
```

**&取地址，*解引用**——两者互为逆运算。

---

## 2. 指针与数组

```cpp
int a[] = {10, 20, 30, 40};
int* p = a;  // 数组名就是首元素地址

cout << *(p + 0) << endl;  // 10
cout << *(p + 1) << endl;  // 20
cout << p[2] << endl;       // 30（p[2] == *(p+2)

// 遍历
for (int* q = a; q < a + 4; q++) {
    cout << *q << " ";
}
```

---

## 3. 字符指针

```cpp
const char* s = "Hello";  // 字符串常量

cout << s << endl;  // 输出Hello
cout << s[1] << endl;  // e

// 注意：字符串常量不能修改
// s[0] = 'h';  // 错误！
```

---

## 4. 结构体指针

```cpp
struct Student {
    string name;
    int score;
};

Student stu = {"张三", 90};
Student* ps = &stu;

cout << ps->name << endl;    // 张三（用->访问成员）
cout << (*ps).score << endl; // 90（等价写法）
```

---

## 5. 指针作为函数参数

```cpp
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int x = 3, y = 5;
    swap(&x, &y);  // 传入地址
    cout << x << " " << y << endl;  // 5 3
    return 0;
}
```

---

## 本章小结

1. 指针：存储地址的变量，`int* p = &a;`
2. `*p`读取地址中的值，`&a`获取变量地址
3. 数组名是首元素地址，指针运算`p+i`偏移i个元素
4. 结构体指针用`->`访问成员
5. 指针参数可以修改实参（传入地址）
"""
    ),

    (
        "引用",
        "references",
        "syntax", 5, 24,
        """# 引用

## 本章简介

引用是C++的别名机制，是比指针更安全的传参方式。

---

## 1. 引用的基本使用

```cpp
int a = 10;
int& r = a;  // r是a的引用（别名）

r = 20;  // 修改r就是修改a
cout << a << endl;  // 20
```

---

## 2. 引用作为函数参数

```cpp
void swap(int& a, int& b) {
    int t = a;
    a = b;
    b = t;
}

int main() {
    int x = 3, y = 5;
    swap(x, y);  // 直接传变量名，不需要&取地址
    cout << x << " " << y << endl;  // 5 3
    return 0;
}
```

---

## 3. 引用vs指针

| 特征 | 引用 | 指针 |
|------|------|------|
| 语法 | `int& r = a;` | `int* p = &a;` |
| 空值 | 不存在（必须绑定对象） | 可以是nullptr |
| 修改 | 直接修改 | 需要`*p`解引用 |
| 安全性 | 更高 | 需注意空指针 |

**竞赛中推荐用引用代替指针**，语法更简洁。

---

## 本章小结

1. 引用是变量的别名，`int& r = a;`
2. 修改引用即修改原变量
3. 引用参数可以替代指针参数，更安全简洁
4. 引用必须在定义时初始化，不能重新绑定
"""
    ),

    (
        "STL：stack、queue、list、vector",
        "stl-containers",
        "data-structure", 4, 25,
        """# STL：stack、queue、list、vector

## 本章简介

详细介绍四种STL容器的基本操作和应用场景。

---

## 1. vector向量

```cpp
#include <vector>
using namespace std;

int main() {
    vector<int> v = {3, 1, 4};

    v.push_back(5);     // 尾部添加
    v.insert(v.begin()+1, 7);  // 在第2个位置插入7

    sort(v.begin(), v.end());  // 排序

    for (int x : v) cout << x << " ";  // 1 3 4 5 7
    return 0;
}
```

---

## 2. stack栈

```cpp
#include <stack>
stack<int> s;
s.push(1); s.push(2); s.push(3);
s.top();   // 3（栈顶）
s.pop();  // 出栈
s.size(); // 2
```

---

## 3. queue队列

```cpp
#include <queue>
queue<int> q;
q.push(1); q.push(2); q.push(3);
q.front();  // 1（队首）
q.back();   // 3（队尾）
q.pop();    // 出队
```

---

## 4. list双向链表

```cpp
#include <list>
list<int> lst = {1, 2, 3, 4, 5};

lst.push_front(0);      // 头部插入
lst.push_back(6);       // 尾部插入
lst.remove(3);          // 删除值为3的节点
lst.reverse();          // 反转链表

for (int x : lst) cout << x << " ";  // 0 1 2 4 5 6
```

---

## 本章小结

1. `vector`：动态数组，支持随机访问，首选
2. `stack`：LIFO，常用括号匹配、表达式求值
3. `queue`：FIFO，常用BFS、按序处理
4. `list`：双向链表，插入删除O(1)，不支持随机访问
"""
    ),

    (
        "二叉树存储与三种遍历",
        "binary-tree-traversal",
        "data-structure", 4, 26,
        """# 二叉树存储与三种遍历

## 本章简介

介绍二叉树的链式存储结构和前序、中序、后序三种遍历方式。

---

## 1. 节点定义

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

---

## 2. 递归遍历

### 前序（根-左-右）

```cpp
void preOrder(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";
    preOrder(root->left);
    preOrder(root->right);
}
```

### 中序（左-根-右）

```cpp
void inOrder(TreeNode* root) {
    if (!root) return;
    inOrder(root->left);
    cout << root->val << " ";
    inOrder(root->right);
}
```

### 后序（左-右-根）

```cpp
void postOrder(TreeNode* root) {
    if (!root) return;
    postOrder(root->left);
    postOrder(root->right);
    cout << root->val << " ";
}
```

---

## 3. 层序遍历（队列）

```cpp
#include <queue>
void levelOrder(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        cout << node->val << " ";
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
}
```

---

## 本章小结

1. 前序：根左右，中序：左根右，后序：左右根
2. 递归实现简单，需注意终止条件
3. 层序遍历用队列，保证按层次顺序
4. 中序遍历BST是有序序列
"""
    ),

    (
        "哈夫曼树与二叉搜索树",
        "huffman-and-bst",
        "data-structure", 4, 27,
        """# 哈夫曼树与二叉搜索树

## 本章简介

介绍两种特殊二叉树的构造和应用。

---

## 1. 哈夫曼树

### 概念

带权路径长度最短的二叉树（最优二叉树）。

### 构造方法（贪心）

每次合并权值最小的两棵树。

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

    cout << cost << endl;  // 最小带权路径长度
    return 0;
}
```

---

## 2. 二叉搜索树（BST）

### 定义

左子树所有节点 < 根节点 < 右子树所有节点。

### 查找

```cpp
TreeNode* searchBST(TreeNode* root, int target) {
    if (!root || root->val == target) return root;
    if (target < root->val)
        return searchBST(root->left, target);
    else
        return searchBST(root->right, target);
}
```

### 插入

```cpp
TreeNode* insertBST(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    if (val < root->val)
        root->left = insertBST(root->left, val);
    else
        root->right = insertBST(root->right, val);
    return root;
}
```

---

## 本章小结

1. 哈夫曼树：最小带权路径长度，用优先队列（最小堆）构造
2. BST：左<根<右，中序遍历得到有序序列
3. BST查找/插入：O(log n)（平衡时），最坏O(n)（退化成链表）
"""
    ),

    (
        "图的存储：邻接矩阵与邻接表",
        "graph-storage",
        "data-structure", 4, 28,
        """# 图的存储：邻接矩阵与邻接表

## 本章简介

介绍两种基本的图存储方式及其适用场景。

---

## 1. 邻接矩阵

适合稠密图（边多）。

```cpp
const int MAXN = 100;
int g[MAXN][MAXN] = {0};  // g[i][j]=1表示边(i,j)存在

void addEdge(int u, int v) {
    g[u][v] = g[v][u] = 1;  // 无向图
}

// 判断边
if (g[u][v]) cout << "边存在";
```

**空间复杂度**：O(V²)，适合V较小（≤500）的情况。

---

## 2. 邻接表

适合稀疏图（边少）。

```cpp
#include <vector>
using namespace std;

vector<int> adj[MAXN];  // adj[i]存储i的所有邻居

void addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);  // 无向图
}
```

**空间复杂度**：O(V+E)。

---

## 3. 对比与选择

| 存储方式 | 空间 | 查询边 | 适用场景 |
|----------|------|--------|----------|
| 邻接矩阵 | O(V²) | O(1) | 稠密图（E≈V²） |
| 邻接表 | O(V+E) | O(deg) | 稀疏图（E<<V²） |

**竞赛中一般用邻接表**。

---

## 本章小结

1. 邻接矩阵：二维数组，O(1)查边，但空间大
2. 邻接表：vector数组，空间O(V+E)，竞赛常用
3. 无向图：双向存边；有向图：单向存边
"""
    ),

    (
        "图遍历与连通分量",
        "graph-traversal",
        "algorithm", 4, 29,
        """# 图遍历与连通分量

## 本章简介

介绍图的DFS和BFS遍历，以及连通分量的计数方法。

---

## 1. 图的DFS

```cpp
bool vis[MAXN];

void dfs(int u) {
    vis[u] = true;
    cout << u << " ";
    for (int v : adj[u]) {
        if (!vis[v]) dfs(v);
    }
}
```

---

## 2. 图的BFS

```cpp
#include <queue>
void bfs(int start) {
    queue<int> q;
    q.push(start);
    vis[start] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " ";
        for (int v : adj[u]) {
            if (!vis[v]) {
                q.push(v);
                vis[v] = true;
            }
        }
    }
}
```

---

## 3. 连通分量计数

```cpp
int countComponents(int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (!vis[i]) {
            cnt++;
            dfs(i);  // 遍历整个连通分量
        }
    }
    return cnt;
}
```

---

## 4. 环检测（无向图）

```cpp
bool hasCycle(int u, int parent) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) {
            if (hasCycle(v, u)) return true;
        } else if (v != parent) {
            return true;  // 访问过的非父节点 = 有环
        }
    }
    return false;
}
```

---

## 本章小结

1. 图的DFS/BFS与树类似，必须用`vis`避免重复访问
2. 连通分量：遍历所有未访问节点，DFS一次计一个分量
3. 环检测：DFS中遇到已访问的非父节点则存在环
"""
    ),

    (
        "贪心与递推",
        "greedy-and-recurrence",
        "algorithm", 3, 30,
        """# 贪心与递推

## 本章简介

介绍贪心算法和递推两种基础算法思想。

---

## 1. 贪心算法

每一步都做出当前最优选择，期望达到全局最优。

### 例题：活动选择

```cpp
struct Act { int s, e; };
bool cmp(Act a, Act b) { return a.e < b.e; }

int main() {
    Act acts[] = {{1,4},{3,5},{0,6},{5,7},{3,9}};
    int n = 5;
    sort(acts, acts+n, cmp);

    int cnt = 0, lastEnd = 0;
    for (int i = 0; i < n; i++) {
        if (acts[i].s >= lastEnd) {
            cnt++;
            lastEnd = acts[i].e;
        }
    }
    cout << cnt << endl;  // 3
}
```

---

## 2. 递推

从已知推未知，逐步推导。

### 例题：爬楼梯

```cpp
// f(n) = f(n-1) + f(n-2)，边界：f(1)=1, f(2)=2
int climb(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

### 例题：错排问题

```
D(1)=0, D(2)=1
D(n) = (n-1) × (D(n-1) + D(n-2))
```

```cpp
long long D(int n) {
    if (n == 1) return 0;
    if (n == 2) return 1;
    long long a = 0, b = 1;
    for (int i = 3; i <= n; i++) {
        long long c = (i-1) * (a + b);
        a = b; b = c;
    }
    return b;
}
```

---

## 本章小结

1. 贪心：每步最优，需证明能导致全局最优
2. 递推：找规律建公式，从已知推到未知
3. 典型递推：斐波那契、爬楼梯、错排、卡特兰数
"""
    ),

    (
        "二分与倍增",
        "binary-search-and-doubling",
        "algorithm", 4, 31,
        """# 二分与倍增

## 本章简介

二分查找是O(log n)高效查找算法，倍增是快速幂和跳表的基础。

---

## 1. 二分查找

```cpp
int binarySearch(int a[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  // 防溢出
        if (a[mid] == target) return mid;
        else if (a[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

---

## 2. 二分答案

把求最优值问题转化为判定问题。

```cpp
// 判断能否以mid为最大载重完成运输
bool can(int weights[], int n, int days, int cap) {
    int need = 1, cur = 0;
    for (int i = 0; i < n; i++) {
        if (cur + weights[i] <= cap) cur += weights[i];
        else { need++; cur = weights[i]; }
    }
    return need <= days;
}
```

---

## 3. 倍增

快速幂：

```cpp
long long modPow(long long a, long long e, long long mod) {
    long long res = 1;
    a %= mod;
    while (e) {
        if (e & 1) res = res * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return res;
}
```

---

## 本章小结

1. 二分查找：O(log n)，数组必须有序
2. `mid = left + (right - left) / 2`防溢出
3. 二分答案：答案有单调性时，将求最优转为判定
4. 倍增：O(log e)计算a^e % mod
"""
    ),

    (
        "差分",
        "difference-array",
        "algorithm", 4, 32,
        """# 差分

## 本章简介

差分是前缀和的逆运算，用于高效批量区间修改。

---

## 1. 一维差分

### 差分数组构建

```cpp
int a[] = {0, 1, 3, 5, 7, 9};  // 原数组（下标从1开始）
int diff[7] = {0};

diff[1] = a[1];
for (int i = 2; i <= 5; i++) {
    diff[i] = a[i] - a[i-1];
}
```

### 区间修改

对区间[l, r]中每个元素加k：

```cpp
diff[l] += k;
diff[r+1] -= k;
// 求前缀和后，a[l]~a[r]都被加了k
```

---

## 2. 差分的核心应用

### 批量修改+单次查询

```cpp
int n = 5;
int diff[10] = {0};

// 把[2,4]区间加3
diff[2] += 3;
diff[5] -= 3;

// 求前缀和得到修改后的数组
int a[6];
a[1] = 0;  // 假设原数组第1个元素是0
for (int i = 1; i <= n; i++) {
    a[i] = a[i-1] + diff[i];
}
// a[2],a[3],a[4]已被加3
```

---

## 本章小结

1. 差分是前缀和的逆运算
2. 区间[l,r]+k：`diff[l]+=k, diff[r+1]-=k`
3. 求前缀和还原修改后的数组
4. 适合多次区间修改+查询最终结果的场景
"""
    ),

    (
        "高精度计算",
        "high-precision",
        "algorithm", 4, 33,
        """# 高精度计算

## 本章简介

当整数超出long long范围（±9×10¹⁸）时，用字符串模拟计算。

---

## 1. 高精度加法

```cpp
string add(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int carry = 0;
    string res;
    for (size_t i = 0; i < max(a.size(), b.size()); i++) {
        int da = (i < a.size()) ? a[i]-'0' : 0;
        int db = (i < b.size()) ? b[i]-'0' : 0;
        int sum = da + db + carry;
        res.push_back('0' + (sum % 10));
        carry = sum / 10;
    }
    if (carry) res.push_back('0' + carry);
    reverse(res.begin(), res.end());
    return res;
}
```

---

## 2. 高精度乘法（大整数×整数）

```cpp
string multiply(string num, int factor) {
    reverse(num.begin(), num.end());
    int carry = 0;
    string res;
    for (size_t i = 0; i < num.size() || carry; i++) {
        int d = (i < num.size()) ? num[i]-'0' : 0;
        int prod = d * factor + carry;
        res.push_back('0' + (prod % 10));
        carry = prod / 10;
    }
    reverse(res.begin(), res.end());
    while (res.size() > 1 && res[0] == '0') res.erase(0, 1);
    return res;
}
```

---

## 3. 高精度乘法（大整数×大整数）

```cpp
string multiplyBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    vector<int> res(a.size() + b.size(), 0);

    for (size_t i = 0; i < a.size(); i++) {
        for (size_t j = 0; j < b.size(); j++) {
            res[i+j] += (a[i]-'0') * (b[j]-'0');
        }
    }

    int carry = 0;
    for (size_t i = 0; i < res.size(); i++) {
        int sum = res[i] + carry;
        res[i] = sum % 10;
        carry = sum / 10;
    }

    string s;
    for (int d : res) s.push_back('0' + d);
    reverse(s.begin(), s.end());
    while (s.size() > 1 && s[0] == '0') s.erase(0, 1);
    return s;
}
```

---

## 本章小结

1. 高精度：字符串存储，按位计算
2. 加法：逆序逐位相加，处理进位
3. 乘法：双重循环，最后统一处理进位
4. 记得去除前导0（保留"0"本身）
"""
    ),

    (
        "埃氏筛与线性筛",
        "sieve",
        "math", 4, 34,
        """# 埃氏筛与线性筛

## 本章简介

介绍两种求质数的高效算法。

---

## 1. 埃氏筛法

```cpp
vector<int> sieve(int n) {
    vector<bool> isPrime(n+1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i*i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i*i; j <= n; j += i) {
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

## 2. 线性筛（欧拉筛）

```cpp
vector<int> linearSieve(int n) {
    vector<bool> isPrime(n+1, true);
    vector<int> primes;
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) primes.push_back(i);
        for (int p : primes) {
            if (i * p > n) break;
            isPrime[i * p] = false;
            if (i % p == 0) break;
        }
    }
    return primes;
}
```

**时间复杂度**：O(n)，每个合数只被筛一次。

---

## 本章小结

1. 埃氏筛：从i²开始标记i的倍数
2. 线性筛：每个合数被最小质因子筛掉，O(n)
3. 求1~n所有质数用筛法，比逐个判定快
"""
    ),

    (
        "排列与组合",
        "permutations-combinations",
        "math", 4, 35,
        """# 排列与组合

## 本章简介

介绍排列数、组合数的计算方法及其代码实现。

---

## 1. 排列数

从n个不同元素中取出m个排成一排：

```
A(n,m) = n! / (n-m)! = n × (n-1) × ... × (n-m+1)
```

```cpp
long long A(int n, int m) {
    long long res = 1;
    for (int i = 0; i < m; i++) res *= (n - i);
    return res;
}
```

---

## 2. 组合数

从n个不同元素中取出m个，不考虑顺序：

```
C(n,m) = n! / (m! × (n-m)!)
```

### 杨辉三角递推

```cpp
long long C[101][101];

for (int i = 0; i <= 100; i++) {
    C[i][0] = C[i][i] = 1;
    for (int j = 1; j < i; j++) {
        C[i][j] = C[i-1][j] + C[i-1][j-1];
    }
}
```

### 阶乘+逆元（用于大组合数）

```cpp
const long long MOD = 1e9+7;

long long fac[1000005], inv[1000005];

long long modPow(long long a, long long e) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

long long Cbig(int n, int m) {
    if (m > n) return 0;
    return fac[n] * inv[m] % MOD * inv[n-m] % MOD;
}
```

---

## 3. 排列组合的应用

### 路径计数

```
从(0,0)到(m,n)，只能向右或向下走
路径数 = C(m+n, m) = C(m+n, n)
```

---

## 本章小结

1. 排列A(n,m)：考虑顺序
2. 组合C(n,m)：不考虑顺序
3. 杨辉三角：递推公式C(n,m)=C(n-1,m)+C(n-1,m-1)
4. 大组合数用阶乘+逆元+O(n)预处理，O(1)查询
"""
    ),

    (
        "动态规划入门",
        "dynamic-programming-intro",
        "algorithm", 4, 36,
        """# 动态规划入门

## 本章简介

动态规划（DP）是竞赛中最重要的算法。本章介绍DP的基本思想和一维DP的经典例题。

---

## 1. DP基本思想

把问题分解为重叠子问题，保存子问题的解避免重复计算。

**三个要素**：
1. **状态**：`dp[i]`表示什么
2. **转移**：`dp[i] = f(dp[...])`
3. **初始化**：边界条件

---

## 2. 经典例题：最大子段和

```cpp
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
```

---

## 3. 经典例题：打家劫舍

```cpp
int rob(int money[], int n) {
    if (n == 1) return money[0];
    if (n == 2) return max(money[0], money[1]);

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

## 本章小结

1. DP核心：状态+转移+初始化
2. 最大子段和：`dp[i]=max(a[i], dp[i-1]+a[i])`
3. 打家劫舍：`dp[i]=max(dp[i-1], dp[i-2]+money[i])`
4. 自底向上循环比递归+记忆化更高效
"""
    ),

    (
        "简单背包与区间DP",
        "knapsack-and-interval-dp",
        "algorithm", 5, 37,
        """# 简单背包与区间DP

## 本章简介

介绍0-1背包和区间DP的基本解法。

---

## 1. 0-1背包

**问题**：n件物品，每件重量w[i]，价值v[i]，容量为C，求最大价值（每件物品只能选0或1次）。

```cpp
int knapsack01(int w[], int v[], int n, int C) {
    int dp[1005] = {0};

    for (int i = 0; i < n; i++) {
        for (int c = C; c >= w[i]; c--) {
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
        }
    }

    return dp[C];
}
```

**关键**：内层循环**倒序**，确保每件物品只选一次。

---

## 2. 简单区间DP

**问题**：合并石子（最少代价）

```cpp
// 区间DP模板
for (int len = 2; len <= n; len++) {          // 区间长度
    for (int i = 1; i + len - 1 <= n; i++) {  // 起点
        int j = i + len - 1;                   // 终点
        dp[i][j] = INF;
        for (int k = i; k < j; k++) {          // 分割点
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost);
        }
    }
}
```

---

## 本章小结

1. 0-1背包：每件物品选0或1次，内层倒序遍历
2. 区间DP：枚举区间长度，再枚举起点和分割点
3. 状态：`dp[i][j]`表示区间[i,j]的最优解
"""
    ),

    # ============================================================
    # 难度5
    # ============================================================

    (
        "深度优先搜索（DFS）",
        "dfs",
        "algorithm", 5, 38,
        """# 深度优先搜索（DFS）

## 本章简介

DFS是搜索问题的核心算法。本章介绍DFS的思想、实现及典型应用。

---

## 1. DFS基本模板

```cpp
void dfs(int state) {
    if (终止条件) {
        记录答案;
        return;
    }

    for (每种选择) {
        if (选择可行) {
            做选择;
            dfs(state + 1);
            撤销选择;  // 回溯
        }
    }
}
```

---

## 2. 全排列

```cpp
int n = 3;
int used[11];
int path[11];

void dfs(int step) {
    if (step > n) {
        for (int i = 1; i <= n; i++) cout << path[i] << " ";
        cout << endl;
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            used[i] = 1;
            path[step] = i;
            dfs(step + 1);
            used[i] = 0;  // 撤销
        }
    }
}
```

---

## 3. 组合问题

```cpp
void combine(int start, int depth) {
    if (depth == k) {
        for (int i = 0; i < k; i++) cout << path[i] << " ";
        cout << endl;
        return;
    }
    for (int i = start; i <= n; i++) {
        path[depth] = i;
        combine(i + 1, depth + 1);
    }
}
```

---

## 4. 迷宫问题

```cpp
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

bool dfs(int x, int y) {
    if (x == 4 && y == 4) return true;
    vis[x][y] = 1;
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir], ny = y + dy[dir];
        if (nx>=0 && nx<5 && ny>=0 && ny<5 && !maze[nx][ny] && !vis[nx][ny]) {
            if (dfs(nx, ny)) return true;
        }
    }
    return false;
}
```

---

## 本章小结

1. DFS核心：递归+回溯，用vis避免重复访问
2. 全排列：标记已用数字，path记录路径
3. 组合：从start开始避免重复
4. 迷宫：4方向扩展，边界检查
5. 剪枝：提前排除无效搜索可大幅提升效率
"""
    ),

    (
        "广度优先搜索（BFS）",
        "bfs",
        "algorithm", 5, 39,
        """# 广度优先搜索（BFS）

## 本章简介

BFS层层扩展，能在无权图中找到最短路径。

---

## 1. BFS基本模板

```cpp
#include <queue>
void bfs(起点) {
    queue<状态> q;
    q.push(起点);
    vis[起点] = true;

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();

        if (到达目标) { 处理答案; }

        for (每种扩展) {
            if (扩展合法 && !vis[扩展]) {
                q.push(扩展);
                vis[扩展] = true;
            }
        }
    }
}
```

---

## 2. BFS求最短路

```cpp
struct Node { int x, y, dist; };

int bfs() {
    queue<Node> q;
    q.push({0, 0, 0});
    vis[0][0] = true;

    while (!q.empty()) {
        Node cur = q.front();
        q.pop();

        if (cur.x == 4 && cur.y == 4) return cur.dist;

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];
            if (可通行 && !vis[nx][ny]) {
                q.push({nx, ny, cur.dist + 1});
                vis[nx][ny] = true;
            }
        }
    }
    return -1;
}
```

---

## 3. BFS与DFS对比

| 特征 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈（递归） | 队列 |
| 搜索顺序 | 深度优先 | 层次优先 |
| 最短路 | ❌ | ✅ |
| 内存 | 较省 | 较多 |

---

## 本章小结

1. BFS用队列，层层扩展，能找到**最短路径**
2. 用`vis`数组避免重复访问
3. BFS适合：迷宫最短路、层序遍历、拓扑排序
4. DFS适合：全排列、组合、连通块、递归深搜
"""
    ),

    (
        "Flood Fill",
        "flood-fill",
        "algorithm", 5, 40,
        """# Flood Fill（洪水填充）

## 本章简介

Flood Fill是一种区域填充算法，常用于图像处理和连通块计数。

---

## 1. 基本Flood Fill（DFS版）

```cpp
int a[10][10];  // 0=未填，1=墙，2=已填
bool vis[10][10];
int n, m;

void fill(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m) return;
    if (vis[x][y] || a[x][y] == 1) return;

    vis[x][y] = true;
    fill(x+1, y);
    fill(x-1, y);
    fill(x, y+1);
    fill(x, y-1);
}
```

---

## 2. BFS版Flood Fill

```cpp
void bfsFill(int sx, int sy) {
    queue<pair<int,int>> q;
    q.push({sx, sy});
    vis[sx][sy] = true;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (nx>=0 && nx<n && ny>=0 && ny<m && !vis[nx][ny] && a[nx][ny]!=1) {
                vis[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}
```

---

## 3. 连通块计数

```cpp
int countComponents() {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!vis[i][j] && a[i][j] != 1) {
                bfsFill(i, j);
                cnt++;
            }
        }
    }
    return cnt;
}
```

---

## 本章小结

1. Flood Fill：从起点出发，填充所有连通的格子
2. DFS版适合小区域，BFS版适合大区域（避免栈溢出）
3. 4方向扩展（上下左右），注意边界判断
4. 常用于：迷宫连通块、岛屿计数、图像填充
"""
    ),

]


def main():
    from app.core.database import SessionLocal
    from app.models.chapter import Chapter

    db = SessionLocal()
    count = 0

    for (title, slug, cat_slug, difficulty, order, content) in CHAPTERS:
        cat = db.query(Category).filter(Category.slug == cat_slug).first()
        if not cat:
            print(f"⚠️ 跳过《{title}》（分类{cat_slug}不存在）")
            continue

        existing = db.query(Chapter).filter(Chapter.slug == slug).first()
        if existing:
            print(f"已存在：{slug}")
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
        print(f"✅ {difficulty}级 {order:02d} - {title}")

    db.commit()
    print(f"\n共插入 {count} 个章节")
    db.close()


if __name__ == "__main__":
    main()
