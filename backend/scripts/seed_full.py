#!/usr/bin/env python3
"""按NOI 2025入门级大纲重建47章节"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.category import Category

# (title, slug, cat_slug, difficulty, order, content_md)
CHAPTERS = [

    # ============================================================
    # 一、基础知识与编程环境（basics）全部难度1
    # ============================================================

    ("计算机系统组成与基本操作", "computer-basics", "basics", 1, 1,
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
del file.txt           #删除文件
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
"""),

    ("程序设计语言基础", "language-basics", "basics", 1, 2,
"""# 程序设计语言基础

## 本章简介
介绍程序设计语言的基本概念，包括标识符、关键字、常量、变量、表达式等核心元素。

---

## 1. 标识符与关键字

### 标识符

程序中用来命名变量、函数、类等的名称：

```cpp
int age;        // age 是标识符
double score;   // score 是标识符
int main() {}   // main 是标识符
```

**命名规则**：
- 由字母、数字、下划线组成
- 不能以数字开头
- 区分大小写
- 不能使用关键字

### 关键字

C++保留的具有特殊含义的词，如：`int`、`if`、`for`、`while`、`return`等。

---

## 2. 常量与变量

### 常量

固定不变的值：
```cpp
const int WEEK = 7;       // 整型常量
const double PI = 3.14159; // 浮点常量
const char grade = 'A';   // 字符常量
```

### 变量

可以改变值的存储空间：
```cpp
int age = 15;        // 整数变量
double score = 92.5; // 小数变量
char grade = 'A';   // 字符变量
bool passed = true; // 布尔变量
```

---

## 3. 基本数据类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `int` | 整数 | `int a = 10;` |
| `long long` | 大整数 | `long long b = 1e12;` |
| `float` | 单精度浮点 | `float f = 3.14f;` |
| `double` | 双精度浮点 | `double d = 3.14159;` |
| `char` | 字符 | `char c = 'A';` |
| `bool` | 布尔 | `bool ok = true;` |

---

## 4. 表达式与运算符

```cpp
int a = 10, b = 3;

a + b;   // 加法：13
a - b;   // 减法：7
a * b;   // 乘法：30
a / b;   // 除法：3（整数除法）
a % b;   // 取余：1

// 关系运算
a > b;   // 1 (true)
a == b;  // 0 (false)

// 逻辑运算
(a > 5) && (b < 5);  // 1 (true)
!(a == b);            // 1 (true)

// 三目运算
(a > b) ? a : b;  // 10
```

---

## 5. 程序设计语言的发展

| 语言 | 特点 | 应用场景 |
|------|------|---------|
| C | 面向过程，贴近硬件 | 系统编程、嵌入式 |
| **C++** | 在C基础上增加面向对象 | 算法竞赛、游戏开发 |
| Java | 跨平台，面向对象 | 企业应用、Android |
| Python | 简洁易懂，库丰富 | AI、数据分析、Web |

**CSP-J/CSP-S指定语言：C++**

---

## 本章小结

1. 标识符：变量/函数/类的名称，遵守命名规则
2. 常量：`const`定义，值不可改变
3. 变量：可变的存储空间，先声明后使用
4. 6种基本类型：int、long long、float、double、char、bool
5. 运算符：算术(`+−* /%`)、关系(`> < == !=`)、逻辑(`&& || !`)、三目(`?:`)
"""),

    ("进制与编码", "base-and-encoding", "basics", 1, 3,
"""# 进制与编码

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

十进制转二进制（除2取余）：
```
11 ÷ 2 = 5 余 1
 5 ÷ 2 = 2 余 1
 2 ÷ 2 = 1 余 0
 1 ÷ 2 = 0 余 1
 → 1011₂
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
"""),

    ("第一个C++程序与Dev-C++使用", "first-program", "basics", 1, 4,
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
"""),

    ("g++编译与调试入门", "gpp-and-debug", "basics", 1, 5,
"""# g++编译与调试入门

## 本章简介
介绍Linux命令行下使用g++编译器编译运行C++程序，以及基本的调试概念。

---

## 1. g++编译命令

```bash
g++ -o program program.cpp
# program.cpp 是源文件
# -o program 指定输出可执行文件名为 program
```

### 常用编译选项

| 选项 | 说明 |
|------|------|
| `-o <file>` | 指定输出文件名 |
| `-Wall` | 开启所有警告 |
| `-g` | 包含调试信息（用于gdb） |
| `-O2` | 开启二级优化 |
| `-std=c++17` | 使用C++17标准 |

```bash
g++ -Wall -o program program.cpp  # 编译并显示所有警告
./program                          # 运行程序
```

---

## 2. 多文件编译

```bash
g++ -o main main.cpp func.cpp utils.cpp
```

---

## 3. 编译过程

```
源文件(.cpp) → 预处理(.i) → 编译(.s) → 汇编(.o) → 链接 → 可执行文件
```

---

## 4. Code::Blocks（Linux IDE）

1. 官网下载Linux版Code::Blocks
2. 新建项目 → Console Application
3. 编写代码，按F9编译运行
4. 设置断点：点击行号左侧，F8调试

---

## 5. 常见编译错误

| 错误信息 | 原因 |
|---------|------|
| `undefined reference to 'main'` | 缺少main函数 |
| `permission denied` | 没有可执行权限，执行`chmod +x program` |
| `fatal error: xxx.h: No such file` | 头文件路径不对 |

```bash
chmod +x program   # 添加执行权限
./program          # 运行
```

---

## 本章小结

1. `g++ -o program source.cpp` 编译C++程序
2. `-Wall`显示所有警告，`-g`包含调试信息
3. 常见错误：缺分号、大小写、头文件路径
4. `chmod +x`给程序加执行权限
"""),

    ("枚举法", "enumeration", "basics", 1, 6,
"""# 枚举法

## 本章简介
枚举法（Brute Force）是最基础的算法思想，通过逐一列举所有可能的情况来找到答案。

---

## 1. 枚举法思想

枚举报：把所有可能的情况逐一验证，不重不漏。

**关键**：确定枚举的范围和条件。

---

## 2. 经典例题：找出所有水仙花数

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

## 3. 枚举优化

### 例题：判断素数（枚举到√n）

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {  // 只枚举到√n
        if (n % i == 0) return false;
    }
    return true;
}
```

优化前：枚举到n（n次）  
优化后：枚举到√n（约√n次）

---

## 本章小结

1. 枚举法：确定范围，逐一验证
2. 关键优化：缩小枚举范围，减少无效计算
3. 判断素数只需枚举到√n
4. 竞赛中能用枚举就不用复杂算法
"""),

    ("模拟法", "simulation", "basics", 1, 7,
"""# 模拟法

## 本章简介
模拟法根据题目描述，用代码逐步模拟过程，是竞赛中常用的高效解题方法。

---

## 1. 模拟法思想

**按照题目的描述，一步一步用代码翻译出来。**

核心：读懂题目 → 翻译成代码 → 运行验证

---

## 2. 例题：计算日期第二天

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

## 3. 例题：模拟纸牌洗牌

```cpp
#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    int a[105] = {0}, b[105] = {0};

    for (int i = 1; i <= n; i++) cin >> a[i];

    int step; cin >> step;
    while (step--) {
        // 模拟洗牌：前一半和后一半交叉
        int cnt = 1;
        for (int i = 1; i <= n/2; i++) {
            b[cnt++] = a[i];
            b[cnt++] = a[i + n/2];
        }
        for (int i = 1; i <= n; i++) a[i] = b[i];
    }

    for (int i = 1; i <= n; i++) cout << a[i] << " ";
    return 0;
}
```

---

## 本章小结

1. 模拟法：把题目描述翻译成代码，逐步执行
2. 关键是读懂题意，不要自己想当然
3. 注意边界条件：日期进位、数组越界等
4. 模拟法是CSP-J第一题最常见的题型
"""),

    # ============================================================
    # 二、C++程序设计（cpp）
    # ============================================================

    ("变量、数据类型与常量", "variables", "cpp", 2, 1,
"""# 变量、数据类型与常量

## 本章简介
介绍C++中变量的声明与使用、基本数据类型、以及常量的概念。

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
"""),

    ("输入输出与表达式", "io-and-expressions", "cpp", 2, 2,
"""# 输入输出与表达式

## 本章简介
学习C++的标准输入输出和表达式的使用。

---

## 1. cin输入

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;  // 输入两个整数，空格或回车分隔
    cout << a + b << endl;
    return 0;
}
```

---

## 2. 格式化输出

```cpp
#include <iomanip>
using namespace std;

double pi = 3.1415926;
cout << fixed << setprecision(2) << pi << endl;  // 3.14
cout << hex << 255 << endl;   // ff（十六进制）
cout << oct << 255 << endl;   // 377（八进制）
cout << dec << 255 << endl;   // 255（十进制）
```

---

## 3. 复合赋值运算

```cpp
int a = 10;
a += 5;   // a = a + 5 = 15
a -= 3;   // a = a - 3 = 12
a *= 2;   // a = a * 2 = 24
a /= 4;   // a = a / 4 = 6
a %= 4;   // a = a % 4 = 2
```

---

## 4. 自增自减

```cpp
int a = 5, b;

b = a++;  // b=5, a=6  先赋值后自增
b = ++a;  // a=7, b=7  先自增后赋值

b = a--;  // b=7, a=6  先赋值后自减
b = --a;  // a=5, b=5  先自减后赋值
```

---

## 本章小结

1. `cin >>`输入，`cout <<`输出
2. `setprecision(n)`控制浮点数小数位
3. `hex/oct/dec`控制进制输出
4. `a++` vs `++a`：前者先赋值后自增，后者相反
"""),

    ("分支结构与switch语句", "if-switch", "cpp", 2, 3,
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
"""),

    ("循环结构", "loops", "cpp", 2, 4,
"""# 循环结构

## 本章简介
循环是程序设计中最重要的结构之一。本章介绍`for`、`while`、`do-while`三种循环。

---

## 1. for循环

```cpp
for (int i = 1; i <= 10; i++) {
    cout << i << " ";
}
// 输出：1 2 3 4 5 6 7 8 9 10
```

---

## 2. while循环

```cpp
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
    if (i == 5) break;      // 遇到5就停止
    if (i % 2 == 0) continue; // 跳过偶数
    cout << i << " ";  // 输出：1 3
}
```

---

## 5. 循环嵌套：九九乘法表

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
"""),

    ("do-while与break、continue", "loop-control", "cpp", 2, 5,
"""# do-while与break、continue

## 本章简介
详细介绍do-while循环，以及break和continue的控制流程。

---

## 1. do-while：先执行后判断

与while的区别：循环体至少执行一次。

```cpp
int choice;
do {
    cout << "1. 开始游戏" << endl;
    cout << "2. 退出" << endl;
    cin >> choice;
} while (choice != 1 && choice != 2);
// 用户输入1或2才退出循环
```

---

## 2. break：跳出循环

```cpp
// 在数组中找第一个大于100的数
for (int i = 0; i < n; i++) {
    if (a[i] > 100) {
        cout << "找到了：" << i << endl;
        break;  // 找到后停止搜索
    }
}
```

---

## 3. continue：跳过本次

```cpp
// 打印1~100中所有不能被3整除的数
for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0) continue;  // 跳过能被3整除的
    cout << i << " ";
}
```

---

## 4. 死循环与退出

```cpp
// 方式1：while(true) + break
while (true) {
    int x; cin >> x;
    if (x == 0) break;
    cout << x * 2 << endl;
}

// 方式2：for(;;) + break
for (;;) {
    int x; cin >> x;
    if (x == 0) break;
    cout << x * 2 << endl;
}
```

---

## 本章小结

1. `break`：立即跳出整个循环
2. `continue`：跳过本次循环，继续下一次
3. `do-while`：先执行后判断，最少执行一次
4. 死循环用`while(true)`或`for(;;)`，配合`break`退出
"""),

    ("多层循环与穷举优化", "nested-loops", "cpp", 3, 6,
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

**不优化**：枚举所有900个三位数。  
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
"""),

    ("数组与一维数组", "array-1d", "cpp", 2, 7,
"""# 数组与一维数组

## 本章简介
介绍一维数组的基本使用，包括声明、初始化、遍历和常见操作。

---

## 1. 声明与初始化

```cpp
int a[10];               // 声明10个整数
int b[5] = {1, 2, 3, 4, 5};     // 完全初始化
int c[5] = {1, 2};              // 部分初始化，未填的为0
int d[] = {10, 20, 30};         // 自动确定大小（3个元素）
```

---

## 2. 遍历与基本操作

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

## 本章小结

1. 数组下标从0开始
2. `sizeof(a)/sizeof(a[0])`计算数组长度
3. 数组适合批量存储和批量处理
"""),

    ("二维数组与多维数组", "array-2d", "cpp", 3, 8,
"""# 二维数组与多维数组

## 本章简介
介绍二维数组的声明、初始化和遍历，以及基本应用。

---

## 1. 声明与初始化

```cpp
int a[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

// 部分初始化
int b[3][4] = {{1}, {0, 2}, {0, 0, 3}};
```

---

## 2. 遍历

```cpp
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        cout << a[i][j] << " ";
    }
    cout << endl;
}
```

---

## 3. 应用：矩阵运算

```cpp
// 矩阵转置
int n = 3;
int a[3][3] = {{1,2,3},{4,5,6},{7,8,9}};

for (int i = 0; i < n; i++) {
    for (int j = i+1; j < n; j++) {
        swap(a[i][j], a[j][i]);
    }
}
```

---

## 4. 杨辉三角（二维数组应用）

```cpp
int n = 10;
int a[11][11] = {0};

for (int i = 1; i <= n; i++) {
    a[i][1] = a[i][i] = 1;
    for (int j = 2; j < i; j++) {
        a[i][j] = a[i-1][j-1] + a[i-1][j];
    }
}
```

---

## 本章小结

1. 二维数组：`类型 数组名[行数][列数]`
2. 双重循环遍历，行列分别处理
3. 可用于矩阵运算、表格数据处理
"""),

    ("字符数组与string类", "string", "cpp", 2, 9,
"""# 字符数组与string类

## 本章简介
介绍字符数组和string类的字符串处理方法。

---

## 1. 字符数组

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

## 2. string类（推荐）

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

1. 字符数组用`\\0`结尾，string类更安全易用
2. string常用：`length`、`+`拼接、`substr`、`find`
3. 竞赛中推荐使用string类处理字符串
"""),

    ("函数定义与调用", "function-basics", "cpp", 2, 10,
"""# 函数定义与调用

## 本章简介
学习函数的定义、调用和参数传递。

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

## 本章小结

1. 函数：`返回类型 函数名(参数) { 函数体; return值; }`
2. 值传递：函数内修改不影响实参
3. 递归：函数调用自身，必须有终止条件
"""),

    ("函数参数传递：传值与传引用", "function-params", "cpp", 3, 11,
"""# 函数参数传递：传值与传引用

## 本章简介
详细讲解值传递、指针传递和引用传递的区别与应用场景。

---

## 1. 值传递（pass by value）

```cpp
void swap(int a, int b) {
    int t = a; a = b; b = t;  // 只交换副本，原值不变
}
```

---

## 2. 指针传递（pass by pointer）

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

## 3. 引用传递（pass by reference）

```cpp
void swap(int& a, int& b) {
    int t = a;
    a = b;
    b = t;
}

int main() {
    int x = 3, y = 5;
    swap(x, y);  // 直接传变量名
    cout << x << " " << y << endl;  // 5 3
    return 0;
}
```

---

## 4. 对比总结

| 传递方式 | 语法 | 能修改实参 | 推荐度 |
|---------|------|-----------|--------|
| 值传递 | `void f(int a)` | ❌ | 一般用于只读 |
| 指针传递 | `void f(int* a)` | ✅ | C风格 |
| 引用传递 | `void f(int& a)` | ✅ | **C++推荐** |

---

## 本章小结

1. 值传递：传副本，原变量不变
2. 指针传递：传地址，通过`*p`修改
3. **引用传递**：最简洁，推荐使用
4. 引用可以理解为变量的别名
"""),

    ("变量作用域与递归函数", "scope-and-recursion", "cpp", 2, 12,
"""# 变量作用域与递归函数

## 本章简介
学习变量的作用域规则和递归函数的设计方法。

---

## 1. 作用域

```cpp
int x = 10;  // 全局变量

int main() {
    int x = 20;  // 局部变量，遮蔽全局变量
    cout << x << endl;      // 20（局部优先）
    cout << ::x << endl;    // 10（用::访问全局）
    return 0;
}
```

---

## 2. 递归函数

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
```

---

## 本章小结

1. 全局变量整个文件有效，局部变量只在函数内有效
2. 递归：函数调用自身，必须有终止条件，否则栈溢出
3. 递归深度过大时考虑用循环或增大栈空间
"""),

    ("结构体与联合体", "struct-union", "cpp", 3, 13,
"""# 结构体与联合体

## 本章简介
介绍结构体和联合体的定义与使用。

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
```

---

## 3. 联合体

联合体的所有成员**共享同一块内存**：

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
    data.c = 'A';              // i的值也被覆盖了
    return 0;
}
```

---

## 本章小结

1. 结构体：自定义数据类型，封装多个不同类型字段
2. 联合体：所有成员共享内存，同时只能用一个
"""),

    ("指针基础", "pointers-basics", "cpp", 4, 14,
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
cout << p[2] << endl;       // 30（p[2] == *(p+2)）
```

---

## 3. 指针作为函数参数

```cpp
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}
```

---

## 本章小结

1. 指针：存储地址的变量，`int* p = &a;`
2. `*p`读取地址中的值，`&a`获取变量地址
3. 数组名是首元素地址，指针运算`p+i`偏移i个元素
"""),

    ("指针与数组、字符串", "pointer-array-string", "cpp", 4, 15,
"""# 指针与数组、字符串

## 本章简介
深入讲解指针与数组、字符串的关系。

---

## 1. 指针算术

```cpp
int a[] = {10, 20, 30, 40, 50};
int* p = a;  // 指向a[0]

p++;          // 指向a[1]，值20
p += 2;       // 指向a[3]，值40
cout << *p << endl;  // 40
```

---

## 2. 字符指针

```cpp
const char* s = "Hello";  // 字符串常量

cout << s << endl;  // 输出Hello
cout << s[1] << endl;  // e

// 注意：字符串常量不能修改
// s[0] = 'h';  // 错误！
```

---

## 3. 指针与const

```cpp
int a = 10;
const int* p = &a;  // 不能通过p修改a的值
// (*p) = 20;  // 错误！但可以直接修改a
```

---

## 本章小结

1. 指针算术：`p+n`、`p-n`、`p++`、`p--`
2. 字符指针指向字符串常量，不可修改
3. `const int* p`表示指针指向的内容不可修改
"""),

    ("结构体指针与函数指针", "pointer-to-struct", "cpp", 4, 16,
"""# 结构体指针与函数指针

## 本章简介
介绍结构体指针的使用和函数指针的概念。

---

## 1. 结构体指针

```cpp
struct Student {
    string name;
    int score;
};

Student stu = {"张三", 90};
Student* ps = &stu;

cout << ps->name << endl;     // 张三（用->访问成员）
cout << (*ps).score << endl;  // 90（等价写法）
```

---

## 2. 指针数组

```cpp
int* arr[3];  // 3个int指针组成的数组
int a = 1, b = 2, c = 3;
arr[0] = &a; arr[1] = &b; arr[2] = &c;
cout << *arr[0] << endl;  // 1
```

---

## 本章小结

1. 结构体指针用`->`访问成员，等价于`(*p).member`
2. 指针数组：每个元素都是指针
3. 指针使数据和函数都可以被动态操作
"""),

    ("引用", "reference", "cpp", 5, 17,
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
    swap(x, y);
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
"""),

    ("文件操作与重定向", "file-operations", "cpp", 2, 18,
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

## 2. 重定向（竞赛常用）

```cpp
// freopen重定向
freopen("input.txt", "r", stdin);   // 从文件读
freopen("output.txt", "w", stdout); // 写到文件

// 恢复标准输入输出
freopen("/dev/tty", "r", stdin);
freopen("/dev/tty", "w", stdout);
```

---

## 本章小结

1. `ifstream`读文件，`ofstream`写文件
2. `freopen`实现输入输出重定向，竞赛中常用
3. 文件路径可以是相对路径或绝对路径
"""),

    ("STL：min、max、swap、sort", "stl-algorithm", "cpp", 3, 19,
"""# STL：min、max、swap、sort

## 本章简介
STL是C++标准库的重要组成部分。本章介绍四个最常用的算法函数。

---

## 1. min、max、swap

```cpp
#include <algorithm>
cout << min(3, 7) << endl;           // 3
cout << max(3, 7) << endl;           // 7
swap(3, 7);                          // 交换

// 三个数的最值
cout << min({3, 1, 7}) << endl;     // 1（c++11初始化列表）
```

---

## 2. sort排序

```cpp
#include <algorithm>
#include <vector>
using namespace std;

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
```

---

## 本章小结

1. `min(a,b)`返回较小值，`max(a,b)`返回较大值
2. `swap(a,b)`交换两个变量的值
3. `sort(begin, end)`默认升序，`greater<int>()`降序
4. `sort`是竞赛中最高效的排序，O(n log n)
"""),

    ("STL：stack、queue、list、vector", "stl-container", "cpp", 4, 20,
"""# STL：stack、queue、list、vector

## 本章简介
详细介绍四种STL容器的基本操作和应用场景。

---

## 1. vector向量（最常用）

```cpp
#include <vector>
using namespace std;

vector<int> v = {3, 1, 4};

v.push_back(5);     // 尾部添加
v.insert(v.begin()+1, 7);  // 在第2个位置插入7
sort(v.begin(), v.end());  // 排序

for (int x : v) cout << x << " ";  // 1 3 4 5 7
```

---

## 2. stack栈（LIFO）

```cpp
#include <stack>
stack<int> s;
s.push(1); s.push(2); s.push(3);
s.top();   // 3（栈顶）
s.pop();  // 出栈
```

---

## 3. queue队列（FIFO）

```cpp
#include <queue>
queue<int> q;
q.push(1); q.push(2); q.push(3);
q.front();  // 1（队首）
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
```

---

## 本章小结

1. `vector`：动态数组，支持随机访问，**首选**
2. `stack`：LIFO，括号匹配、表达式求值
3. `queue`：FIFO，BFS、按序处理
4. `list`：双向链表，插入删除O(1)，不支持随机访问
"""),

    # ============================================================
    # 三、数据结构（data-structure）
    # ============================================================

    ("单链表", "linked-list", "data-structure", 3, 1,
"""# 单链表

## 本章简介
链表是线性数据结构，通过指针链接节点。本章介绍单链表的实现。

---

## 1. 节点定义

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
    if (!head) { head = newNode; return; }
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

## 本章小结

1. 链表节点 = 数据 + 指针
2. 头插O(1)，尾插O(n)，按值删除O(n)
3. 与数组对比：插入快但访问慢
4. 用`new`分配内存后要`delete`释放
"""),

    ("双向链表与循环链表", "dlist-cyclelist", "data-structure", 3, 2,
"""# 双向链表与循环链表

## 本章简介
介绍双向链表和循环链表的结构与基本操作。

---

## 1. 双向链表节点

```cpp
struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int x) : data(x), prev(nullptr), next(nullptr) {}
};
```

---

## 2. 循环链表

首尾相接的链表：

```cpp
struct CNode {
    int data;
    CNode* next;
};

// 建立循环链表：1->2->3->1
CNode* create(int a[], int n) {
    CNode* head = new CNode(a[0]);
    CNode* p = head;
    for (int i = 1; i < n; i++) {
        p->next = new CNode(a[i]);
        p = p->next;
    }
    p->next = head;  // 尾指向头
    return head;
}
```

---

## 3. 约瑟夫问题（循环链表经典应用）

```cpp
int josephus(int n, int m) {
    list<int> L;
    for (int i = 1; i <= n; i++) L.push_back(i);
    auto it = L.begin();
    while (L.size() > 1) {
        for (int i = 1; i < m; i++) {
            it++;
            if (it == L.end()) it = L.begin();
        }
        it = L.erase(it);  // 删除当前
        if (it == L.end()) it = L.begin();
    }
    return L.front();
}
```

---

## 本章小结

1. 双向链表：每个节点有prev和next，删除更方便
2. 循环链表：尾节点的next指向头，适合环状问题
3. 约瑟夫问题是循环链表的经典应用
"""),

    ("栈", "stack", "data-structure", 3, 3,
"""# 栈

## 本章简介
栈是"后进先出"的数据结构，是算法竞赛中的重要工具。

---

## 1. 栈的基本操作

```cpp
#include <stack>
using namespace std;

stack<int> s;

s.push(1);   // 入栈：{1}
s.push(2);   // 入栈：{1,2}
s.push(3);   // 入栈：{1,2,3}

cout << s.top() << endl;   // 看栈顶：3
s.pop();                    // 出栈：{1,2}

cout << s.size() << endl;   // 2
cout << s.empty() << endl;   // false
```

---

## 2. 应用：括号匹配

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
            if ((c==')'&&top!='(') || (c==']'&&top!='[') || (c=='}'&&top!='{'))
                return false;
            st.pop();
        }
    }
    return st.empty();
}
```

---

## 本章小结

1. 栈（LIFO）：`push`入栈，`pop`出栈，`top`看栈顶
2. 适合：括号匹配、表达式求值、函数调用栈
3. 括号匹配：左括号入栈，右括号匹配弹出
"""),

    ("队列", "queue", "data-structure", 3, 4,
"""# 队列

## 本章简介
队列是"先进先出"的数据结构，是BFS和调度算法的核心。

---

## 1. 队列基本操作

```cpp
#include <queue>
using namespace std;

queue<int> q;

q.push(1);   // 入队：{1}
q.push(2);   // 入队：{1,2}
q.push(3);   // 入队：{1,2,3}

cout << q.front() << endl;   // 看队首：1
cout << q.back() << endl;    // 看队尾：3
q.pop();                      // 出队：{2,3}
```

---

## 2. 应用：BFS广度优先搜索

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

1. 队列（FIFO）：`push`入队，`pop`出队，`front`看队首
2. 适合：BFS、层序遍历、任务调度
3. BFS用队列，DFS用栈或递归
"""),

    ("树与二叉树基础", "tree-basics", "data-structure", 3, 5,
"""# 树与二叉树基础

## 本章简介
树是一种层次结构，二叉树是最常用的树形结构。

---

## 1. 树的基本概念

- **节点**：树中的每个元素
- **根节点**：树的顶端，没有父节点
- **叶子节点**：没有子节点的节点
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

## 本章小结

1. 树是层次结构，二叉树每个节点最多两个子节点
2. 二叉树第i层最多2^(i-1)个节点
3. 完全二叉树：除最后一层外每层满节点，最后一层左对齐
"""),

    ("二叉树的表示与存储", "tree-storage", "data-structure", 4, 6,
"""# 二叉树的表示与存储

## 本章简介
介绍二叉树的链式存储结构和数组表示方法。

---

## 1. 链式存储（最常用）

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

---

## 2. 完全二叉树的数组表示

完全二叉树可以用数组高效存储：

| 父节点 | 左孩子 | 右孩子 |
|--------|--------|--------|
| `i` | `2i` | `2i+1` |

```cpp
int tree[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};  // 0号位不用

int parent(int i) { return i/2; }
int leftChild(int i) { return 2*i; }
int rightChild(int i) { return 2*i+1; }

// 判断是否为叶子节点
bool isLeaf(int i, int n) {
    return leftChild(i) > n;
}
```

---

## 本章小结

1. 完全二叉树用数组存储：父节点i，左孩子2i，右孩子2i+1
2. 数组存储更省内存，适合完全二叉树
3. 链式存储适合任意二叉树
"""),

    ("二叉树的遍历", "tree-traversal", "data-structure", 4, 7,
"""# 二叉树的遍历

## 本章简介
介绍二叉树的四种遍历方式：前序、中序、后序和层序。

---

## 1. 前序遍历（根-左-右）

```cpp
void preOrder(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";
    preOrder(root->left);
    preOrder(root->right);
}
```

---

## 2. 中序遍历（左-根-右）

```cpp
void inOrder(TreeNode* root) {
    if (!root) return;
    inOrder(root->left);
    cout << root->val << " ";
    inOrder(root->right);
}
```

**中序遍历BST是有序序列！**

---

## 3. 后序遍历（左-右-根）

```cpp
void postOrder(TreeNode* root) {
    if (!root) return;
    postOrder(root->left);
    postOrder(root->right);
    cout << root->val << " ";
}
```

---

## 4. 层序遍历（队列）

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
4. **中序遍历BST是有序序列**
"""),

    ("完全二叉树与堆", "complete-binary-tree", "data-structure", 4, 8,
"""# 完全二叉树与堆

## 本章简介
介绍完全二叉树的性质和堆数据结构。

---

## 1. 完全二叉树性质

- 除最后一层外，每层节点数都达到最大
- 最后一层节点都集中在左边
- 可用数组存储，节省空间

---

## 2. 堆（Heap）

堆是一棵完全二叉树，分为最大堆和最小堆：

| 类型 | 特点 |
|------|------|
| 最大堆 | 父节点 ≥ 子节点，根是最大值 |
| 最小堆 | 父节点 ≤ 子节点，根是最小值 |

---

## 3. 堆的向下调整

```cpp
// 向下调整：从pos位置向下调整
void heapifyDown(int heap[], int n, int pos) {
    while (true) {
        int largest = pos;
        int left = 2*pos, right = 2*pos+1;
        if (left <= n && heap[left] > heap[largest]) largest = left;
        if (right <= n && heap[right] > heap[largest]) largest = right;
        if (largest == pos) break;
        swap(heap[pos], heap[largest]);
        pos = largest;
    }
}
```

---

## 4. 堆排序

```cpp
void heapSort(int a[], int n) {
    // 建堆：从最后一个非叶子节点向上调整
    for (int i = n/2; i >= 1; i--)
        heapifyDown(a, n, i);

    // 逐个取出堆顶
    for (int i = n; i >= 2; i--) {
        swap(a[1], a[i]);
        heapifyDown(a, i-1, 1);
    }
}
```

---

## 本章小结

1. 完全二叉树：除最后一层外每层满节点，最后一层左对齐
2. 最大堆：父节点≥子节点，根是最大值
3. 堆排序：O(n log n)，建堆O(n)
"""),

    ("哈夫曼树与哈夫曼编码", "huffman", "data-structure", 4, 9,
"""# 哈夫曼树与哈夫曼编码

## 本章简介
哈夫曼树是带权路径长度最短的二叉树，哈夫曼编码是变长编码的基础。

---

## 1. 基本概念

- **树的带权路径长度（WPL）**：所有叶子节点的权值×路径长度之和
- **哈夫曼树**：WPL最小的二叉树

---

## 2. 构造哈夫曼树（贪心）

每次合并权值最小的两棵树：

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

## 3. 哈夫曼编码

高频字符用短码，低频字符用长码：

| 字符 | 频率 | 编码 |
|------|------|------|
| A | 45 | 0 |
| B | 13 | 101 |
| C | 12 | 100 |
| D | 16 | 111 |
| E | 9 | 1101 |
| F | 5 | 1100 |

---

## 本章小结

1. 哈夫曼树：WPL最小的树，用最小堆构造
2. 哈夫曼编码：前缀编码，高频字符短码
3. 核心思想：贪心——每次合并最小的两棵树
"""),

    ("二叉搜索树", "bst", "data-structure", 4, 10,
"""# 二叉搜索树

## 本章简介
二叉搜索树（BST）是一种特殊二叉树，左子树所有节点 < 根 < 右子树所有节点。

---

## 1. BST定义

左子树所有节点 < 根节点 < 右子树所有节点。

**中序遍历BST得到有序序列！**

---

## 2. 查找

```cpp
TreeNode* searchBST(TreeNode* root, int target) {
    if (!root || root->val == target) return root;
    if (target < root->val)
        return searchBST(root->left, target);
    else
        return searchBST(root->right, target);
}
```

---

## 3. 插入

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

## 4. 删除

```cpp
TreeNode* deleteBST(TreeNode* root, int val) {
    if (!root) return nullptr;
    if (val < root->val) root->left = deleteBST(root->left, val);
    else if (val > root->val) root->right = deleteBST(root->right, val);
    else {
        if (!root->left) return root->right;
        if (!root->right) return root->left;
        TreeNode* minNode = root->right;
        while (minNode->left) minNode = minNode->left;
        root->val = minNode->val;
        root->right = deleteBST(root->right, minNode->val);
    }
    return root;
}
```

---

## 本章小结

1. BST：左<根<右，中序遍历得到有序序列
2. 查找/插入/删除：O(log n)（平衡时），最坏O(n)（退化成链表）
3. 退化成链表时效率低，需要平衡树（AVL/红黑树）
"""),

    ("图的存储：邻接矩阵与邻接表", "graph-storage", "data-structure", 4, 11,
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
"""),

    ("图的遍历：DFS与BFS", "graph-traversal", "data-structure", 4, 12,
"""# 图的遍历：DFS与BFS

## 本章简介
介绍图的深度优先遍历和广度优先遍历。

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

## 本章小结

1. 图的DFS/BFS与树类似，必须用`vis`避免重复访问
2. 连通分量：遍历所有未访问节点，DFS一次计一个分量
3. DFS适合连通性检测，BFS适合最短路
"""),

    # ============================================================
    # 四、算法（algorithm）
    # ============================================================

    ("贪心算法", "greedy", "algorithm", 3, 1,
"""# 贪心算法

## 本章简介
贪心算法每一步都做出当前最优选择，期望达到全局最优。

---

## 1. 贪心算法思想

每一步都选择当前最优解，不回头，不考虑整体最优的全局证明（竞赛中常用）。

**关键**：要能证明贪心策略正确性！

---

## 2. 经典例题：活动选择

每次选最早结束的兼容活动：

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

## 3. 找零钱问题

```cpp
// 货币面值为：100, 50, 20, 10, 5, 1
int coins[] = {100, 50, 20, 10, 5, 1};
int count = 0;

for (int c : coins) {
    count += amount / c;
    amount %= c;
}
```

---

## 本章小结

1. 贪心：每步最优，需证明能导致全局最优
2. 活动选择：按结束时间排序，选最早结束的
3. 贪心不总是正确，使用前要思考证明
"""),

    ("递推与动态规划入门", "recurrence-dp", "algorithm", 3, 2,
"""# 递推与动态规划入门

## 本章简介
递推和DP是竞赛中最重要的算法思想。

---

## 1. 递推

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

---

## 2. 动态规划初步

DP三要素：**状态、转移、初始化**。

### 例题：最大子段和

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

### 例题：打家劫舍

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

1. 递推：找规律建公式，从已知推到未知
2. DP核心：状态+转移+初始化
3. 最大子段和：`dp[i]=max(a[i], dp[i-1]+a[i])`
4. 打家劫舍：`dp[i]=max(dp[i-1], dp[i-2]+money[i])`
"""),

    ("简单一维DP", "dp-1d", "algorithm", 4, 3,
"""# 简单一维DP

## 本章简介
深入讲解一维动态规划的经典例题。

---

## 1. 斐波那契数列

```cpp
int fib(int n) {
    if (n <= 2) return 1;
    int a = 1, b = 1;
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

---

## 2. 最长上升子序列（LIS）

```cpp
int LIS(int a[], int n) {
    int dp[1000] = {0};
    int ans = 0;
    for (int i = 0; i < n; i++) {
        dp[i] = 1;  // 自己
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i])
                dp[i] = max(dp[i], dp[j] + 1);
        }
        ans = max(ans, dp[i]);
    }
    return ans;
}
```

---

## 3. 合唱队形（NOIP2005）

```cpp
// 求：满足先递增再递减的最多人数
// 思路：求每个位置左边最长递增、右边最长递减，取最大值
```

---

## 本章小结

1. LIS：O(n²)DP，逐个比较前面的数
2. 状态设计：`dp[i]`表示以i结尾的最优解
3. 转移：枚举分割点或前驱状态
"""),

    ("简单背包DP", "knapsack", "algorithm", 5, 4,
"""# 简单背包DP

## 本章简介
介绍0-1背包和完全背包的解法。

---

## 1. 0-1背包

每件物品只能选0或1次：

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

## 2. 完全背包

每件物品可以选无限次：

```cpp
int knapsackComplete(int w[], int v[], int n, int C) {
    int dp[1005] = {0};

    for (int i = 0; i < n; i++) {
        for (int c = w[i]; c <= C; c++) {
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
        }
    }

    return dp[C];
}
```

**关键**：内层循环**正序**。

---

## 本章小结

1. 0-1背包：内层倒序，每件物品选一次
2. 完全背包：内层正序，每件物品可选无限次
3. 空间优化：一维dp，容量从大到小/小到大遍历
"""),

    ("简单区间DP", "interval-dp", "algorithm", 5, 5,
"""# 简单区间DP

## 本章简介
区间DP处理在一个区间上进行的优化问题。

---

## 1. 区间DP模板

```cpp
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

## 2. 例题：合并石子

```cpp
// 合并相邻两堆石子，代价为重量之和，求最小总代价
int stoneMerge(int w[], int n) {
    int prefix[105] = {0};
    for (int i = 1; i <= n; i++) prefix[i] = prefix[i-1] + w[i];

    int dp[105][105] = {0};

    for (int len = 2; len <= n; len++) {
        for (int i = 1; i + len - 1 <= n; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                dp[i][j] = min(dp[i][j],
                    dp[i][k] + dp[k+1][j] + prefix[j] - prefix[i-1]);
            }
        }
    }
    return dp[1][n];
}
```

---

## 本章小结

1. 区间DP：枚举长度，再枚举起点和分割点
2. `dp[i][j]`表示区间[i,j]的最优解
3. 外层枚举长度，内层枚举起点的合并点
"""),

    ("深度优先搜索（DFS）", "dfs", "algorithm", 5, 6,
"""# 深度优先搜索（DFS）

## 本章简介
DFS是搜索问题的核心算法，用递归实现深度优先。

---

## 1. DFS基本模板

```cpp
void dfs(int state) {
    if (终止条件) {
        记录答案;
        return;
    }

    for (每种选择) {
        if (选择可行 && !vis[选择]) {
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
3. 迷宫：4方向扩展，边界检查
4. 剪枝：提前排除无效搜索可大幅提升效率
"""),

    ("广度优先搜索（BFS）", "bfs", "algorithm", 5, 7,
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
"""),

    ("Flood Fill", "flood-fill", "algorithm", 5, 8,
"""# Flood Fill（洪水填充）

## 本章简介
Flood Fill是一种区域填充算法，常用于连通块计数。

---

## 1. DFS版Flood Fill

```cpp
int n, m;
int a[10][10];
bool vis[10][10];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

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
3. 4方向扩展，注意边界判断
4. 常用于：迷宫连通块、岛屿计数
"""),

    # ============================================================
    # 五、数学与其他（math）
    # ============================================================

    ("进位制转换", "base-conversion", "math", 1, 1,
"""# 进位制转换

## 本章简介
学习二进制、八进制、十进制、十六进制之间的相互转换方法。

---

## 1. 十进制转其他进制

**除基取余法**：

```cpp
// 十进制转二进制
string decToBin(int n) {
    if (n == 0) return "0";
    string s;
    while (n > 0) {
        s = char('0' + (n % 2)) + s;
        n /= 2;
    }
    return s;
}

// 十进制转十六进制
string decToHex(int n) {
    if (n == 0) return "0";
    string s, hex = "0123456789ABCDEF";
    while (n > 0) {
        s = hex[n % 16] + s;
        n /= 16;
    }
    return s;
}
```

---

## 2. 其他进制转十进制

**按权展开**：

```cpp
int binToDec(string s) {
    int result = 0;
    for (char c : s) {
        result = result * 2 + (c - '0');
    }
    return result;
}
```

---

## 3. 二进制与八进制、十六进制

```cpp
// 二进制 -> 八进制（每3位一组）
// 1101011₂ = 001 101 011 = 153₈

// 二进制 -> 十六进制（每4位一组）
// 1101011₂ = 0110 1011 = 6B₁₆
```

---

## 本章小结

1. 十进制转其他进制：除基取余，倒序取余
2. 其他进制转十进制：按权展开
3. 二进制↔八进制：3位一组；二进制↔十六进制：4位一组
"""),

    ("ASCII码与字符处理", "ascii", "math", 2, 2,
"""# ASCII码与字符处理

## 本章简介
ASCII码用数字表示字符，是字符处理的基础。

---

## 1. ASCII码表（关键值）

| 字符 | ASCII |
|------|-------|
| `'0'`~`'9'` | 48~57 |
| `'A'`~`'Z'` | 65~90 |
| `'a'`~`'z'` | 97~122 |

---

## 2. 字符运算

```cpp
char c = 'A';
cout << (int)c << endl;      // 65
cout << (char)(c + 1) << endl; // 'B'
cout << (char)('a' - 32) << endl; // 'A'（大写转小写）
cout << (char)('A' + 32) << endl; // 'a'（小写转大写）
```

---

## 3. 字符分类

```cpp
#include <cctype>
isalpha('A');   // 1 字母
isdigit('5');   // 1 数字
isupper('A');   // 1 大写
islower('a');   // 1 小写
toupper('a');   // 'A'
tolower('A');   // 'a'
```

---

## 本章小结

1. `'A'`=65, `'a'`=97, `'0'`=48
2. 大写转小写：`+32`，小写转大写：`-32`
3. `<cctype>`提供字符分类和转换函数
"""),

    ("集合与加法原理、乘法原理", "set-ppp", "math", 2, 3,
"""# 集合与加法原理、乘法原理

## 本章简介
计数问题的基础，竞赛中经常用到。

---

## 1. 集合（C++ set）

```cpp
#include <set>
using namespace std;

int main() {
    set<int> s;
    s.insert(3);
    s.insert(1);
    s.insert(4);
    s.insert(1);  // 重复，不插入

    for (int x : s) cout << x << " ";  // 自动排序：1 3 4
    return 0;
}
```

---

## 2. 加法原理

完成一件事有**n类**方法，第i类有mᵢ种，总方法数：
```
m₁ + m₂ + ... + mₙ
```

**例**：从A地到B地，汽车3班，火车2班，飞机1班，共3+2+1=6种方式。

---

## 3. 乘法原理

完成一件事需要**n步**，第i步有mᵢ种，总方法数：
```
m₁ × m₂ × ... × mₙ
```

**例**：上衣4件，裤子3条，共有4×3=12种搭配方式。

---

## 本章小结

1. 加法原理：**分类**相加（每类方法都能独立完成这件事）
2. 乘法原理：**分步**相乘（每步缺一不可）
3. 竞赛中常结合排列组合使用
"""),

    ("排列与组合", "permutation-combination", "math", 4, 4,
"""# 排列与组合

## 本章简介
介绍排列数和组合数的计算方法。

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

---

## 3. 阶乘+逆元（用于大组合数）

```cpp
const long long MOD = 1e9+7;

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

## 本章小结

1. 排列A(n,m)：考虑顺序
2. 组合C(n,m)：不考虑顺序
3. 杨辉三角：递推C(n,m)=C(n-1,m)+C(n-1,m-1)
4. 大组合数用阶乘+逆元，O(n)预处理，O(1)查询
"""),

    ("杨辉三角", "pascals-triangle", "math", 4, 5,
"""# 杨辉三角

## 本章简介
杨辉三角是组合数的几何表示，有丰富的数学性质。

---

## 1. 基本性质

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
```

性质：
- 第n行第k个数 = C(n-1, k-1)
- 左右对称
- 每个数等于肩上两数之和

---

## 2. 递推构建

```cpp
int n = 10;
int a[11][11] = {0};

for (int i = 1; i <= n; i++) {
    a[i][1] = a[i][i] = 1;
    for (int j = 2; j < i; j++) {
        a[i][j] = a[i-1][j-1] + a[i-1][j];
    }
}
```

---

## 3. 应用

```cpp
// 路径计数：从(0,0)到(m,n)，只能向右或向下
// 路径数 = C(m+n, n)
cout << C(m+n, n) << endl;

// 找规律递推
// 例：爬楼梯，每次1步或2步
// f(n) = f(n-1) + f(n-2)
```

---

## 本章小结

1. 杨辉三角第n行第k个数 = C(n-1, k-1)
2. 构建：两端为1，中间等于肩上两数之和
3. 组合数学的基础工具
"""),

    ("模运算与取余", "mod", "math", 3, 6,
"""# 模运算与取余

## 本章简介
模运算是数论的基础，在密码学和竞赛中应用广泛。

---

## 1. 基本模运算

```cpp
int a = 17, b = 5;

cout << a % b << endl;    // 2（17除以5余2）
cout << (-7 % 3) << endl; // -1（负数取余，符号与被除数一致）

// 模运算性质
// (a + b) % mod = (a % mod + b % mod) % mod
// (a * b) % mod = (a % mod) * (b % mod) % mod
```

---

## 2. 快速幂取模

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

## 3. 模运算技巧

```cpp
// 判断奇偶
if (n % 2 == 0) // 偶数
else            // 奇数

// 循环数组
int next = (i + 1) % n;

// 大数取模
int modOfBigNumber(string s, int mod) {
    int r = 0;
    for (char c : s) {
        r = (r * 10 + (c - '0')) % mod;
    }
    return r;
}
```

---

## 本章小结

1. 模运算：`a % b`取余，注意负数结果符号
2. 快速幂：O(log e)计算a^e % mod
3. 性质：(a+b)%mod = (a%mod+b%mod)%mod，可防溢出
"""),

    ("整数唯一分解定理", "unique-factorization", "math", 3, 7,
"""# 整数唯一分解定理

## 本章简介
任何大于1的整数都可以唯一分解为质数的乘积。

---

## 1. 基本分解

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

## 2. 求约数个数

若 n = p₁^a₁ × p₂^a₂ × ... × pk^ak，则：

```
约数个数 = (a₁+1)(a₂+1)...(ak+1)
```

```cpp
int divisorCount(int n) {
    int cnt = 1;
    for (int i = 2; i * i <= n; i++) {
        int power = 0;
        while (n % i == 0) {
            n /= i;
            power++;
        }
        if (power > 0) cnt *= (power + 1);
    }
    if (n > 1) cnt *= 2;
    return cnt;
}
```

---

## 本章小结

1. 唯一分解：任何数可分解为质数乘积
2. 分解质因数：试除到√n
3. 约数个数公式：∏(aᵢ+1)
"""),

    ("欧几里得算法", "euclidean", "math", 3, 8,
"""# 欧几里得算法

## 本章简介
欧几里得算法（辗转相除法）是求最大公约数的最快方法。

---

## 1. 最大公约数（GCD）

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
```

---

## 2. 最小公倍数（LCM）

```cpp
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // 先除后乘避免溢出
}
```

---

## 3. 扩展欧几里得算法

求 ax + by = gcd(a,b) 的一组解：

```cpp
int exgcd(int a, int b, int& x, int& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    int x1, y1;
    int g = exgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
```

---

## 本章小结

1. gcd(a,b)=gcd(b,a%b)，O(log min(a,b))
2. lcm(a,b) = a/gcd(a,b)×b
3. 扩展欧几里得：求逆元，解同余方程
"""),

    ("埃氏筛与线性筛", "sieve", "math", 4, 9,
"""# 埃氏筛与线性筛

## 本章简介
介绍两种高效求质数的算法。

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
"""),

    ("高精度计算", "high-precision", "math", 4, 10,
"""# 高精度计算

## 本章简介
当整数超出long long范围时，用字符串模拟计算。

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
    return res;
}
```

---

## 本章小结

1. 高精度：字符串存储，按位计算
2. 加法：逆序逐位相加，处理进位
3. 记得去除前导0（保留"0"本身）
"""),

    ("前缀和与差分", "prefix-difference", "math", 4, 11,
"""# 前缀和与差分

## 本章简介
前缀和用于O(1)查询区间和，差分用于高效批量区间修改。

---

## 1. 一维前缀和

```cpp
int a[11] = {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
int prefix[11];

for (int i = 1; i <= 10; i++) {
    prefix[i] = prefix[i-1] + a[i];
}

// 查询区间[3,7]的和
int l = 3, r = 7;
int sum = prefix[r] - prefix[l-1];  // 5+7+9+11+13 = 45
```

---

## 2. 差分

差分是前缀和的逆运算：

```cpp
// 对区间[l, r]中每个元素加k
diff[l] += k;
diff[r+1] -= k;
// 求前缀和后，a[l]~a[r]都被加了k
```

---

## 本章小结

1. 前缀和：`prefix[i] = sum(a[1]~a[i])`
2. 区间和：`sum(l,r) = prefix[r] - prefix[l-1]`，O(1)查询
3. 差分：区间[l,r]+k → `diff[l]+=k, diff[r+1]-=k`
4. 适合多次查询和批量修改的场景
"""),

    ("二分查找与二分答案", "binary-search", "math", 4, 12,
"""# 二分查找与二分答案

## 本章简介
二分查找是O(log n)高效查找算法，二分答案把求最优值转化为判定问题。

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

把求最优值问题转化为判定问题：

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

// 二分搜索答案
int lo = 0, hi = 1e9;
while (lo < hi) {
    int mid = (lo + hi) / 2;
    if (can(weights, n, days, mid)) hi = mid;
    else lo = mid + 1;
}
```

---

## 本章小结

1. 二分查找：O(log n)，数组必须有序
2. `mid = left + (right - left) / 2`防溢出
3. 二分答案：答案有单调性时，将求最优转为判定
"""),

    ("倍增与快速幂", "doubling", "math", 4, 13,
"""# 倍增与快速幂

## 本章简介
倍增思想用于快速跳过多个状态，快速幂是其经典应用。

---

## 1. 快速幂

O(log e)计算 a^e：

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

## 2. 矩阵快速幂

```cpp
struct Matrix {
    long long a[2][2];
    Matrix operator*(const Matrix& b) {
        Matrix r;
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++) {
                r.a[i][j] = 0;
                for (int k = 0; k < 2; k++)
                    r.a[i][j] = (r.a[i][j] + a[i][k] * b.a[k][j]) % MOD;
            }
        return r;
    }
};

Matrix mpow(Matrix A, long long e) {
    Matrix R = {{{1,0},{0,1}}};  // 单位矩阵
    while (e) {
        if (e & 1) R = R * A;
        A = A * A;
        e >>= 1;
    }
    return R;
}
```

---

## 本章小结

1. 快速幂：O(log e)计算a^e % mod
2. 核心：指数按二进制拆分
3. 矩阵快速幂可加速线性递推（斐波那契等）
"""),

    ("初中代数基础", "middle-school-algebra", "math", 1, 14,
"""# 初中代数基础

## 本章简介
复习初中代数基础，为竞赛中的数学推导打基础。

---

## 1. 代数运算

```cpp
// 完全平方公式
// (a+b)² = a² + 2ab + b²
// (a-b)² = a² - 2ab + b²

// 平方差公式
// a² - b² = (a+b)(a-b)

// 十字相乘法
// x² + (p+q)x + pq = (x+p)(x+q)
```

---

## 2. 不等式

```cpp
// 一元二次不等式
// x² - 5x + 6 > 0
// (x-2)(x-3) > 0
// 解：x < 2 或 x > 3
```

---

## 3. 例题：求根公式

```cpp
// 一元二次方程 ax² + bx + c = 0
double delta = b*b - 4*a*c;
if (delta >= 0) {
    double x1 = (-b + sqrt(delta)) / (2*a);
    double x2 = (-b - sqrt(delta)) / (2*a);
    cout << x1 << " " << x2 << endl;
}
```

---

## 本章小结

1. 完全平方、平方差、十字相乘法要熟练
2. 不等式解法：先因式分解，找零点
3. 求根公式：delta = b²-4ac
"""),

    ("初中几何基础", "middle-school-geometry", "math", 1, 15,
"""# 初中几何基础

## 本章简介
复习初中几何基础，包括三角形、圆、矩形等常见图形的性质。

---

## 1. 三角形

- **内角和**：180°
- **面积**：S = 底×高÷2
- **海伦公式**：S = √[p(p-a)(p-b)(p-c)]，其中p=(a+b+c)/2

```cpp
// 海伦公式
double heron(double a, double b, double c) {
    double p = (a + b + c) / 2;
    return sqrt(p * (p-a) * (p-b) * (p-c));
}
```

---

## 2. 矩形与正方形

- 矩形面积：S = 长 × 宽
- 正方形面积：S = 边长²
- 对角线长：√(a²+b²)

---

## 3. 圆

- 圆面积：S = πr²
- 圆周长：C = 2πr

```cpp
const double PI = acos(-1);
double area = PI * r * r;
double circumference = 2 * PI * r;
```

---

## 本章小结

1. 三角形面积：底×高÷2，或海伦公式
2. 矩形：长×宽，正方形：边长²
3. 圆：πr²，2πr
4. 竞赛中常把几何问题转化为代数计算
"""),

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
        print(f"✅ {cat_slug} | {difficulty}级 | {order:02d} | {title}")

    db.commit()
    print(f"\n共插入 {count} 个章节")
    db.close()


if __name__ == "__main__":
    main()
