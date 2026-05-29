#!/usr/bin/env python3
"""严格按照NOI 2025入门级大纲重建教程"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.category import Category

# ================================================================
# 格式：(title, slug, cat_slug, difficulty, order, content_md)
# 大纲顺序严格按五大部分 + 罗马数字章节编号
# ================================================================

CHAPTERS = [

    # ============================================================
    # 一、基础知识与编程环境（全难度1）
    # ============================================================

    ("计算机基本构成", "computer-components", "basics", 1, 1,
"""# 计算机基本构成

## 本章简介
了解计算机的硬件组成，理解CPU、内存、硬盘、输入输出设备的作用。

---

## 1. 计算机硬件组成

| 硬件 | 作用 |
|------|------|
| **CPU**（中央处理器） | 执行计算和指令，计算机的大脑 |
| **内存**（RAM） | 临时存储程序和数据，断电后丢失 |
| **硬盘** | 永久存储数据，断电后保留 |
| **输入设备** | 键盘、鼠标等，向计算机输入信息 |
| **输出设备** | 显示器、打印机等，输出计算结果 |

---

## 2. 冯·诺依曼体系

程序和数据都存储在内存中，CPU从内存读取指令执行：

```
源代码 → 编译 → 可执行文件 → 加载到内存 → CPU执行
```

---

## 3. 常见存储单位

| 单位 | 换算 |
|------|------|
| 1 Byte | = 8 bit |
| 1 KB | = 1024 Byte |
| 1 MB | = 1024 KB |
| 1 GB | = 1024 MB |
| 1 TB | = 1024 GB |

---

## 本章小结

1. 计算机五大硬件：CPU、内存、硬盘、输入设备、输出设备
2. CPU负责计算，内存临时存储，硬盘永久存储
3. 程序必须加载到内存才能被CPU执行
"""),

    ("Windows与Linux基本操作", "os-basics", "basics", 1, 2,
"""# Windows与Linux基本操作

## 本章简介
掌握Windows和Linux操作系统的基本概念和常用操作。

---

## 1. Windows基本操作

### 文件管理
- **新建文件夹**：右键 → 新建文件夹
- **复制**：`Ctrl+C` 复制，`Ctrl+V` 粘贴
- **移动**：拖动或 `Ctrl+X` 剪切 + `Ctrl+V` 粘贴
- **删除**：`Delete` 进回收站，`Shift+Delete` 直接删除

### 常用快捷键
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+C` | 复制 |
| `Ctrl+V` | 粘贴 |
| `Ctrl+Z` | 撤销 |
| `Ctrl+S` | 保存 |
| `Alt+Tab` | 切换窗口 |

### 命令行（CMD）
```bash
cd Desktop              # 进入桌面
dir                    # 查看当前目录
mkdir myproject        # 创建文件夹
del file.txt           # 删除文件
```

---

## 2. Linux基本概念

| 命令 | 功能 |
|------|------|
| `ls` | 列出文件 |
| `cd` | 切换目录 |
| `mkdir` | 创建目录 |
| `rm` | 删除文件 |
| `cp` | 复制文件 |
| `mv` | 移动/重命名 |

---

## 本章小结

1. Windows：图形界面操作 + CMD命令行
2. Linux：命令行操作为主，常用命令要熟记
3. 文件管理是编程的基础，要熟练操作
"""),

    ("计算机网络与Internet", "network-basics", "basics", 1, 3,
"""# 计算机网络与Internet

## 本章简介
了解计算机网络的基本概念和Internet的简单原理。

---

## 1. 网络基本概念

- **IP地址**：计算机在网络中的唯一标识（如192.168.1.1）
- **域名**：方便记忆的网址（如www.example.com）
- **HTTP/HTTPS**：网页传输协议
- **DNS**：域名解析，将域名转换为IP地址

---

## 2. 浏览器与网页

- **URL**：统一资源定位符（如 https://www.example.com）
- **HTML**：网页标记语言
- **刷新**：F5 或 Ctrl+R

---

## 3. 竞赛相关网络使用

- **洛谷**：信息学竞赛在线评测平台 https://www.luogu.com
- **Codeforces**：国际竞赛平台
- **OI Wiki**：信息学知识百科 https://oi-wiki.org

---

## 本章小结

1. IP地址是计算机在网络中的唯一标识
2. 浏览器通过HTTP/HTTPS协议访问网页
3. 学会使用洛谷、OI Wiki等竞赛学习网站
"""),

    ("计算机历史与用途", "computer-history", "basics", 1, 4,
"""# 计算机历史与用途

## 本章简介
了解计算机的发展简史和主要应用领域。

---

## 1. 计算机发展简史

| 时代 | 代表人物/机器 | 特点 |
|------|-------------|------|
| 1940s | ENIAC | 第一台电子计算机 |
| 1950s-60s | IBM | 晶体管计算机 |
| 1970s | Altair 8800 | 个人计算机诞生 |
| 1980s | IBM PC | 个人计算机普及 |
| 1990s-今 | Internet | 互联网时代 |

---

## 2. 计算机的应用领域

- **科学计算**：天气预报、基因研究
- **信息管理**：银行、超市、企业系统
- **人工智能**：机器学习、深度学习
- **游戏娱乐**：电子游戏、电影特效
- **信息学竞赛**：算法与程序设计

---

## 本章小结

1. 计算机从1940年代的电子管发展到今天的个人计算机和互联网
2. 信息学竞赛使用计算机解决算法问题
3. 编程能力是信息时代的核心竞争力之一
"""),

    ("NOI及相关活动历史", "noi-history", "basics", 1, 5,
"""# NOI及相关活动历史

## 本章简介
了解NOI系列竞赛的由来和发展。

---

## 1. NOI系列竞赛体系

```
CSP-J（入门级）→ CSP-S（提高级）→ NOIP（省选）→ NOI（国赛）→ IOI（国际赛）
```

| 竞赛 | 全称 | 级别 |
|------|------|------|
| CSP-J | 非专业级软件能力认证-入门级 | 第一轮（笔试+上机） |
| CSP-S | 非专业级软件能力认证-提高级 | 第一轮 |
| NOIP | 全国青少年信息学奥林匹克联赛 | 各省自行组织 |
| NOI | 全国青少年信息学奥林匹克 | 全国决赛 |
| IOI | 国际信息学奥林匹克 | 国际比赛 |

---

## 2. CCF简介

**CCF**（中国计算机学会）主办NOI系列竞赛，是国内最权威的计算机竞赛组织。

---

## 3. NOI精神

- 公平竞争
- 创新精神
- 团队协作

---

## 本章小结

1. CSP-J/S是NOI系列的第一轮，是参赛门槛
2. NOI由中国计算机学会（CCF）主办
3. 通过CSP-J/S后才能参加NOIP省选
"""),

    ("NOI及相关活动规则", "noi-rules", "basics", 1, 6,
"""# NOI及相关活动规则

## 本章简介
了解CSP-J/S和NOI系列竞赛的比赛规则。

---

## 1. CSP-J/S比赛规则

| 项目 | 说明 |
|------|------|
| 参赛语言 | C++（推荐）、C、Pascal |
| 评测方式 | 机器评测，AC得满分 |
| 题型 | 选择题 + 程序设计题 |
| 评分 | 按测试点给分，部分分制 |

---

## 2. 竞赛纪律

- 禁止携带电子设备（除比赛用电脑）
- 不得访问任何参考资料
- 不得与他人交流
- 违反规则取消成绩

---

## 3. 竞赛技巧

1. 先读所有题目，选择性价比最高的先做
2. 每题先写暴力/部分分解法，再优化
3. 认真检查输入输出格式
4. 提交前先本地测试

---

## 本章小结

1. CSP-J/S采用机器评测，AC得满分
2. 竞赛中要合理分配时间，先易后难
3. 认真读题，注意输入输出格式
"""),

    ("位、字节与字", "bit-byte-word", "basics", 1, 7,
"""# 位、字节与字

## 本章简介
理解计算机底层的数据表示单位。

---

## 1. 位（bit）

- 最小存储单位，只能是0或1
- 计算机内部所有数据都用二进制表示

---

## 2. 字节（Byte）

- 1 Byte = 8 bit
- 字节是内存寻址的最小单位

---

## 3. 字（Word）

- CPU一次处理的数据单位
- 32位系统：1字 = 4字节
- 64位系统：1字 = 8字节

---

## 4. int与long long大小

| 类型 | 32位系统 | 64位系统 |
|------|----------|----------|
| int | 4字节 | 4字节 |
| long long | 8字节 | 8字节 |

---

## 本章小结

1. 位（bit）是最小单位，1字节=8位
2. int通常4字节（32位），long long 8字节
3. 不同数据类型占用不同大小的内存空间
"""),

    ("程序设计语言基础", "pl-basics", "basics", 1, 8,
"""# 程序设计语言基础

## 本章简介
了解程序设计语言的基本概念，包括编译型语言和解释型语言的区别。

---

## 1. 程序设计语言分类

| 类型 | 特点 | 代表语言 |
|------|------|----------|
| 编译型 | 先编译后运行，运行速度快 | **C++**、C |
| 解释型 | 逐行解释执行 | Python |
| 混合型 | 编译成中间码，解释执行 | Java、C# |

---

## 2. C++编译运行过程

```
源代码(.cpp) → 预处理器 → 编译器 → 汇编器 → 链接器 → 可执行文件
```

---

## 3. 第一个C++程序

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

---

## 4. 常见程序设计语言

| 语言 | 主要应用 |
|------|---------|
| **C++** | 算法竞赛、系统编程、游戏开发 |
| C | 操作系统、嵌入式 |
| Python | AI、数据分析、Web |
| Java | 企业应用、Android |

---

## 本章小结

1. C++是编译型语言，编译后运行速度快
2. 竞赛推荐使用C++，效率高、库丰富
3. 学习语言先掌握语法，再学数据结构和算法
"""),

    ("图形界面与文件操作", "gui-file-ops", "basics", 1, 9,
"""# 图形界面与文件操作

## 本章简介
掌握Windows图形界面操作和文件/目录管理。

---

## 1. Windows图形界面操作

### 文件与文件夹
- **新建**：右键 → 新建 → 文件夹/文档
- **重命名**：右键 → 重命名，或选中后按F2
- **复制/粘贴**：`Ctrl+C` / `Ctrl+V`
- **剪切/粘贴**：`Ctrl+X` / `Ctrl+V`
- **删除**：Delete（进回收站），`Shift+Delete`（直接删除）

### 多选操作
- `Ctrl+单击`：选中多个不连续文件
- `Shift+单击`：选中连续文件范围

---

## 2. 文件路径

- **绝对路径**：从盘符开始的完整路径 `C:\\Users\\Admin\\Desktop`
- **相对路径**：从当前目录出发的路径 `../src/main.cpp`

---

## 3. 竞赛中的文件操作

```cpp
#include <fstream>
ifstream fin("input.txt");   // 从文件读入
ofstream fout("output.txt"); // 输出到文件
```

---

## 本章小结

1. 熟练使用Windows资源管理器操作文件
2. 理解绝对路径和相对路径的区别
3. 竞赛中常用freopen或fstream读写文件
"""),

    ("Dev-C++使用", "dev-cpp", "basics", 1, 10,
"""# Dev-C++使用

## 本章简介
掌握Windows下最适合初学者的C++ IDE——Dev-C++的基本使用方法。

---

## 1. Dev-C++简介

Dev-C++是Windows下免费的C++集成开发环境，适合竞赛入门学习。

---

## 2. 基本使用

### 新建程序
1. 文件 → 新建 → 源代码（或`Ctrl+N`）
2. 编写代码
3. 保存为`.cpp`文件（`Ctrl+S`）

### 编译运行
- **F11**：编译运行（最常用）
- **F9**：编译（不运行）
- **F10**：运行（不编译）

---

## 3. 调试方法

- **F7**：单步执行（进入函数）
- **F8**：单步执行（跳过函数）
- **F4`：在当前行设置断点

---

## 4. 常见错误

| 错误 | 原因 |
|------|------|
| 红色波浪线 | 语法错误 |
| 橙色波浪线 | 警告 |
| 编译错误 | 查看错误行，逐一修复 |

---

## 本章小结

1. Dev-C++是Windows下最适合入门的C++ IDE
2. F11编译运行，F7单步调试
3. 遇到编译错误看错误提示，逐行修复
"""),

    ("Code-Blocks使用", "codeblocks", "basics", 1, 11,
"""# Code::Blocks使用

## 本章简介
了解Linux下常用的C++ IDE——Code::Blocks的基本使用方法。

---

## 1. Code::Blocks简介

Code::Blocks是跨平台的C++ IDE，支持Windows、Linux、macOS。

---

## 2. 基本使用

### 新建项目
1. File → New → Project → Console Application
2. 选择C++
3. 输入项目名称和路径
4. 选择编译器（GNU GCC Compiler）

### 编译运行
- **Ctrl+F9**：编译
- **Ctrl+F10**：运行
- **F9**：编译并运行

---

## 3. 调试

1. 点击行号左侧设置断点（红色圆点）
2. **F8**：开始调试
3. **F7**：单步执行
4. Watch窗口查看变量值

---

## 4. 与Dev-C++对比

| 功能 | Dev-C++ | Code::Blocks |
|------|---------|--------------|
| 平台 | Windows | 跨平台 |
| 调试 | 基础 | 更强大 |
| 推荐度 | Windows初学者 | 多平台用户 |

---

## 本章小结

1. Code::Blocks是跨平台的C++ IDE
2. 快捷键与Dev-C++略有不同
3. 竞赛中Windows推荐Dev-C++，Linux推荐Code::Blocks或g++
"""),

    ("g++编译基础", "gpp-basics", "basics", 1, 12,
"""# g++编译基础

## 本章简介
学习Linux命令行下使用g++编译器编译C++程序。

---

## 1. g++基本命令

```bash
g++ -o program source.cpp
# source.cpp 是源文件
# -o program 指定输出文件名
```

---

## 2. 常用选项

| 选项 | 说明 |
|------|------|
| `-o <file>` | 指定输出文件名 |
| `-Wall` | 显示所有警告 |
| `-g` | 包含调试信息（用于gdb） |
| `-O2` | 开启二级优化 |
| `-std=c++17` | 使用C++17标准 |

```bash
g++ -Wall -o program source.cpp   # 编译并显示警告
./program                          # 运行程序
```

---

## 3. 多文件编译

```bash
g++ -o main main.cpp func1.cpp func2.cpp
```

---

## 4. 常见问题

| 问题 | 解决方法 |
|------|----------|
| `permission denied` | `chmod +x program` 加执行权限 |
| `undefined reference to main` | 检查是否有main函数 |
| 编译成功但无输出 | 检查是否在当前目录运行 |

---

## 本章小结

1. `g++ -o program source.cpp` 编译C++程序
2. `-Wall`显示所有警告，有助于发现潜在问题
3. 记得给程序加执行权限（chmod +x）
"""),

    # ============================================================
    # 二、C++程序设计
    # 二.1 程序基本概念
    # ============================================================

    ("程序基本概念：标识符与关键字", "identifiers-keywords", "cpp", 1, 13,
"""# 程序基本概念：标识符与关键字

## 本章简介
理解C++中标识符和关键字的概念与规则。

---

## 1. 标识符

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

---

## 2. 关键字

C++保留的具有特殊含义的词：

```cpp
int, double, char, bool, if, else, for, while, do, switch,
case, default, break, continue, return, void, const, true, false,
#include, using, namespace, class, struct, enum, typedef, static, ...
```

---

## 3. 合法的标识符

```cpp
// ✅ 合法的标识符
int a1;
int _count;
int MAX_VALUE;
int studentAge;

// ❌ 非法的标识符
// int 1a;        // 不能以数字开头
// int my-age;    // 不能用连字符
// int int;       // 不能使用关键字
```

---

## 本章小结

1. 标识符是变量/函数/类的名称
2. 命名规则：字母/数字/下划线，不能以数字开头
3. 关键字是C++保留的，不能用作标识符
"""),

    ("常量、变量与字符串", "constants-variables", "cpp", 1, 14,
"""# 常量、变量与字符串

## 本章简介
学习常量、变量的概念和字符串的表示方法。

---

## 1. 常量

固定不变的值：
```cpp
const int WEEK = 7;       // 整型常量
const double PI = 3.14159; // 浮点常量
const char GRADE = 'A';   // 字符常量
```

---

## 2. 变量

可以改变的存储空间：
```cpp
int age = 15;        // 整数变量
double score = 92.5; // 小数变量
char grade = 'A';   // 字符变量
bool passed = true; // 布尔变量
```

---

## 3. 字符串

C++中字符串有两种表示方式：

### 字符数组
```cpp
char s[] = "Hello";
```

### string类（推荐）
```cpp
#include <string>
using namespace std;

string s = "Hello";
s = "World";
cout << s.length() << endl;  // 5
```

---

## 本章小结

1. 常量用`const`定义，值不可改变
2. 变量是可变的存储空间
3. 字符串推荐使用string类，比字符数组更安全
"""),

    ("头文件与名字空间", "header-namespace", "cpp", 2, 15,
"""# 头文件与名字空间

## 本章简介
理解C++头文件的概念和名字空间的作用。

---

## 1. 头文件

头文件用于引入标准库或自定义函数：

```cpp
#include <iostream>    // 标准输入输出
#include <string>      // 字符串
#include <vector>     // 动态数组
#include <algorithm>  // 算法（sort等）
#include <cmath>       // 数学函数
```

---

## 2. 名字空间（namespace）

避免名字冲突的机制：

```cpp
#include <iostream>
using namespace std;  // 使用标准名字空间

int main() {
    cout << "Hello";  // 不需要写 std::cout
    return 0;
}
```

---

## 3. 不用名字空间的写法

```cpp
#include <iostream>

int main() {
    std::cout << "Hello" << std::endl;
    return 0;
}
```

---

## 本章小结

1. `#include`引入头文件
2. `using namespace std;`引入标准名字空间
3. 竞赛代码中通常写`using namespace std;`简化代码
"""),

    ("编辑、编译、解释、调试", "compile-debug", "cpp", 2, 16,
"""# 编辑、编译、解释、调试

## 本章简介
理解程序的编辑、编译、解释、调试四种基本操作。

---

## 1. 编辑

将代码写入源文件（.cpp），使用文本编辑器或IDE编写。

---

## 2. 编译

将源代码翻译成机器码：

```
.cpp源文件 → 预处理器 → 编译器 → 汇编器 → 链接器 → 可执行文件
```

编译错误：语法错误，需修复后重新编译。

---

## 3. 解释

逐行解释执行，不生成独立可执行文件（如Python）。

---

## 4. 调试

发现并修复程序中的错误：

| 错误类型 | 特征 | 解决方法 |
|---------|------|----------|
| 编译错误 | 编译时不通过 | 看错误提示，修复语法 |
| 运行时错误 | 程序崩溃 | 加输出语句定位 |
| 逻辑错误 | 结果不对 | 人工检查算法，用测试用例验证 |

### 调试技巧
```cpp
// 在关键位置输出变量值
cout << "DEBUG: x=" << x << ", y=" << y << endl;
```

---

## 本章小结

1. 编译：源代码→机器码（C++是编译型语言）
2. 解释：逐行执行（Python是解释型语言）
3. 调试：用输出语句或IDE调试器定位错误
"""),

    # ============================================================
    # 二.2 基本数据类型（全难度1）
    # ============================================================

    ("整型与浮点型", "int-float-double", "cpp", 1, 17,
"""# 整型与浮点型

## 本章简介
掌握C++中整数和浮点数的表示方法。

---

## 1. 整型

| 类型 | 大小 | 范围 |
|------|------|------|
| `int` | 4字节 | ±21亿（-2³¹~2³¹-1） |
| `long long` | 8字节 | ±9×10¹⁸ |

```cpp
int a = 100000;
long long b = 1e12;      // 使用科学计数法
long long c = 1LL << 60; // 使用位运算
```

---

## 2. 浮点型

| 类型 | 大小 | 精度 |
|------|------|------|
| `float` | 4字节 | 约6位有效数字 |
| `double` | 8字节 | 约15位有效数字 |

```cpp
float f = 3.14f;      // float型常量加f后缀
double d = 3.14159;   // double更常用
```

---

## 3. 选择建议

- 整数运算：一般用`int`，超过21亿用`long long`
- 浮点运算：一般用`double`，精度足够

---

## 本章小结

1. `int`约±21亿，`long long`约±9×10¹⁸
2. 浮点数用`double`，精度更高
3. 竞赛中超过`int`范围记得用`long long`
"""),

    ("字符型与布尔型", "char-bool", "cpp", 1, 18,
"""# 字符型与布尔型

## 本章简介
学习字符类型char和布尔类型bool的使用。

---

## 1. 字符型（char）

```cpp
char c1 = 'A';       // 单引号
char c2 = 'x';
char c3 = '1';        // 字符'1'，不是数字1

cout << (int)c1 << endl;  // 65（ASCII码）
```

---

## 2. 布尔型（bool）

```cpp
bool a = true;   // 真（1）
bool b = false;  // 假（0）

cout << sizeof(bool) << endl;  // 1字节

// 逻辑运算返回bool
bool result = (3 > 2);  // true
```

---

## 3. ASCII码（部分）

| 字符 | ASCII |
|------|-------|
| `'0'`~`'9'` | 48~57 |
| `'A'`~`'Z'` | 65~90 |
| `'a'`~`'z'` | 97~122 |

---

## 本章小结

1. `char`用单引号，存储单个字符
2. `bool`只有true和false两个值
3. 字符在内存中以ASCII码（整数）形式存储
"""),

    # ============================================================
    # 二.3 程序基本语句
    # ============================================================

    ("输入输出与赋值", "io-and-assignment", "cpp", 2, 19,
"""# 输入输出与赋值

## 本章简介
学习C++的标准输入输出和赋值语句。

---

## 1. cin输入

```cpp
#include <iostream>
using namespace std;

int a, b;
cin >> a >> b;  // 输入两个整数

string name;
cin >> name;    // 输入字符串
```

---

## 2. cout输出

```cpp
cout << "Hello" << endl;
cout << "a + b = " << a + b << endl;
cout << 3.14159 << endl;
```

---

## 3. 格式化输出

```cpp
#include <iomanip>
cout << fixed << setprecision(2) << 3.14159 << endl;  // 3.14
cout << hex << 255 << endl;   // ff（十六进制）
cout << oct << 255 << endl;   // 377（八进制）
cout << dec << 255 << endl;   // 255（十进制）
```

---

## 4. 赋值语句

```cpp
int a = 10;    // 初始化
a = 20;        // 赋值

// 复合赋值
a += 5;   // a = a + 5 = 25
a -= 3;   // a = a - 3 = 22
a *= 2;   // a = a * 2 = 44
a /= 4;   // a = a / 4 = 11
a %= 3;   // a = a % 3 = 2
```

---

## 本章小结

1. `cin >>`输入，`cout <<`输出
2. `endl`换行，`setprecision`控制小数位
3. 复合赋值`+= -= *= /= %=`简化代码
"""),

    ("if与switch分支", "if-switch", "cpp", 2, 20,
"""# if与switch分支

## 本章简介
掌握if-else和switch两种分支结构。

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
    case 'A': cout << "90~100"; break;
    case 'B': cout << "80~89"; break;
    case 'C': cout << "70~79"; break;
    case 'D': cout << "60~69"; break;
    default: cout << "成绩无效";
}
```

**注意**：`break`不能省略，否则会"穿透"！

---

## 本章小结

1. `if-else`：处理两个分支或多层条件判断
2. `switch`：处理等值分支判断，必须加`break`
3. 条件用`&&`（与）、`||`（或）、`!`（非）连接
"""),

    ("for、while、do while循环", "loops", "cpp", 2, 21,
"""# for、while、do while循环

## 本章简介
掌握三种循环结构的使用场景。

---

## 1. for循环（已知次数）

```cpp
for (int i = 1; i <= 10; i++) {
    cout << i << " ";
}
// 输出：1 2 3 4 5 6 7 8 9 10
```

---

## 2. while循环（条件驱动）

```cpp
int sum = 0, i = 1;
while (i <= 100) {
    sum += i;
    i++;
}
cout << sum << endl;  // 5050
```

---

## 3. do-while循环（至少执行一次）

```cpp
int n;
do {
    cin >> n;
} while (n < 1 || n > 100);
```

---

## 4. 对比与选择

| 循环 | 适用场景 |
|------|---------|
| `for` | 已知循环次数 |
| `while` | 条件驱动 |
| `do-while` | 先执行再判断 |

---

## 本章小结

1. `for`适合已知次数的循环
2. `while`适合条件不确定的情况
3. `do-while`保证循环体至少执行一次
"""),

    ("多层循环", "nested-loops", "cpp", 3, 22,
"""# 多层循环

## 本章简介
掌握循环嵌套的使用，用于处理二维问题。

---

## 1. 基本嵌套

```cpp
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        cout << "(" << i << "," << j << ") ";
    }
    cout << endl;
}
```

---

## 2. 九九乘法表

```cpp
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        cout << j << "×" << i << "=" << i*j << "\\t";
    }
    cout << endl;
}
```

---

## 3. 穷举优化

**问题**：找所有各位数字之和为15的三位数。

```cpp
for (int i = 1; i <= 9; i++) {
    for (int j = 0; j <= 9; j++) {
        int k = 15 - i - j;
        if (k >= 0 && k <= 9) {
            cout << i*100 + j*10 + k << " ";
        }
    }
}
```

---

## 本章小结

1. 多层循环外层控制行，内层控制列
2. 优化：用数学关系减少内层循环次数
3. 竞赛中注意循环次数，避免超时
"""),

    # ============================================================
    # 二.4 基本运算
    # ============================================================

    ("算术、关系、逻辑运算", "arithmetic-logic", "cpp", 1, 23,
"""# 算术、关系、逻辑运算

## 本章简介
掌握C++中的算术、关系、逻辑运算。

---

## 1. 算术运算

```cpp
int a = 10, b = 3;
cout << a + b << endl;   // 13
cout << a - b << endl;   // 7
cout << a * b << endl;   // 30
cout << a / b << endl;   // 3（整数除法）
cout << a % b << endl;   // 1（取余）
```

---

## 2. 关系运算

```cpp
cout << (a > b) << endl;   // 1（true）
cout << (a == b) << endl;  // 0（false）
cout << (a != b) << endl;  // 1（true）
```

---

## 3. 逻辑运算

```cpp
bool p = true, q = false;
cout << (p && q) << endl;  // 0（与）
cout << (p || q) << endl;  // 1（或）
cout << (!p) << endl;       // 0（非）
```

---

## 4. 自增自减与三目运算

```cpp
int a = 5;
cout << (a++) << endl;  // 5（先输出后自增）
cout << (++a) << endl;  // 7（先自增后输出）

// 三目运算
int max = (a > b) ? a : b;
```

---

## 本章小结

1. 算术：`+ - * / %`，整数除法取整
2. 关系：`> < == != >= <=`，返回bool
3. 逻辑：`&&`（与）、`||`（或）、`!`（非）
4. 三目：`条件 ? 值1 : 值2`
"""),

    ("位运算", "bit-operations", "cpp", 2, 24,
"""# 位运算

## 本章简介
掌握C++中的六种位运算。

---

## 1. 六种基本位运算

```cpp
int a = 6, b = 3;  // a=110, b=011

cout << (a & b) << endl;   // 2 (110 & 011 = 010)
cout << (a | b) << endl;    // 7 (110 | 011 = 111)
cout << (a ^ b) << endl;    // 5 (110 ^ 011 = 101)
cout << (~a) << endl;       // -7（按位取反）
cout << (a << 1) << endl;   // 12（a×2）
cout << (a >> 1) << endl;   // 3（a÷2）
```

---

## 2. 常用位运算技巧

```cpp
// 取最低位的1：n & (-n)
int lowbit = n & (-n);  // 4 (0100)

// 消除最低位的1：n & (n-1)
int after = n & (n - 1);  // 8 (1000)

// 判断是否为2的幂次
bool isPowerOf2(int x) {
    return x > 0 && (x & (x - 1)) == 0;
}
```

---

## 本章小结

1. `&`（与）、`|`（或）、`^`（异或）、`~`（取反）
2. `<<`左移=乘2ⁿ，`>>`右移=除2ⁿ
3. `n & (-n)`取最低位的1，`n & (n-1)`消除最低位的1
"""),

    # ============================================================
    # 二.5 数学库常用函数
    # ============================================================

    ("数学库函数", "math-functions", "cpp", 3, 25,
"""# 数学库函数

## 本章简介
掌握`<cmath>`库中常用的数学函数。

---

## 1. 绝对值与取整

```cpp
#include <cmath>

cout << abs(-5) << endl;       // 5（整数）
cout << fabs(-3.14) << endl;   // 3.14（浮点）
cout << floor(3.7) << endl;   // 3.0（向下）
cout << ceil(3.2) << endl;    // 4.0（向上）
cout << round(3.5) << endl;    // 4（四舍五入）
cout << trunc(3.9) << endl;    // 3（截断）
```

---

## 2. 平方根与幂

```cpp
cout << sqrt(16) << endl;    // 4.0
cout << pow(2, 10) << endl;   // 1024.0
cout << cbrt(27) << endl;    // 3.0（C++17）
```

---

## 3. 三角函数（弧度制）

```cpp
double pi = acos(-1);
cout << sin(pi/2) << endl;  // 1.0
cout << cos(pi) << endl;     // -1.0
// 角度转弧度：rad = deg * π / 180
```

---

## 4. 对数与指数

```cpp
cout << exp(1) << endl;            // 2.71828（e¹）
cout << log(exp(1)) << endl;       // 1.0（ln）
cout << log10(100) << endl;        // 2.0（log₁₀）
// log₂(x)用换底公式
cout << log(8) / log(2) << endl;   // 3.0
```

---

## 本章小结

1. `abs/fabs`绝对值，`floor/ceil/round`取整
2. `sqrt`平方根，`pow(底,指数)`幂函数
3. 三角函数参数是**弧度**不是角度
4. `log`是自然对数，`log10`是以10为底
"""),

    # ============================================================
    # 二.6 结构化程序设计
    # ============================================================

    ("顺序、分支、循环结构", "program-structures", "cpp", 1, 26,
"""# 顺序、分支、循环结构

## 本章简介
理解程序的三种基本控制结构。

---

## 1. 顺序结构

从上到下依次执行：

```cpp
int a = 10;
int b = 20;
int c = a + b;  // 顺序执行
cout << c << endl;
```

---

## 2. 分支结构

根据条件选择执行路径：

```cpp
int score = 85;
if (score >= 60) {
    cout << "及格" << endl;
} else {
    cout << "不及格" << endl;
}
```

---

## 3. 循环结构

重复执行一段代码：

```cpp
for (int i = 1; i <= 5; i++) {
    cout << i << " ";
}
// 输出：1 2 3 4 5
```

---

## 4. 三种结构的组合

任何复杂程序都是由这三种基本结构组合而成。

---

## 本章小结

1. 顺序结构：逐条执行
2. 分支结构：if/switch条件选择
3. 循环结构：for/while/do-while重复执行
"""),

    ("模块化设计与流程图", "modular-design", "cpp", 2, 27,
"""# 模块化设计与流程图

## 本章简介
学习模块化程序设计和流程图的基本方法。

---

## 1. 模块化设计

将大问题分解为小问题，每个函数完成一个功能：

```cpp
// 交换两个数
void swap(int& a, int& b) {
    int t = a;
    a = b;
    b = t;
}

// 判断素数
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
```

---

## 2. 流程图符号

| 符号 | 含义 |
|------|------|
| 椭圆 | 开始/结束 |
| 平行四边形 | 输入/输出 |
| 菱形 | 判断/条件 |
| 矩形 | 处理/操作 |
| 箭头 | 执行方向 |

---

## 本章小结

1. 模块化：每个函数做一件事，代码更清晰
2. 流程图：用图形化方式描述算法逻辑
3. 竞赛中要养成画流程图再写代码的习惯
"""),

    # ============================================================
    # 二.7 数组
    # ============================================================

    ("一维数组", "array-1d", "cpp", 1, 28,
"""# 一维数组

## 本章简介
学习一维数组的声明、初始化和使用。

---

## 1. 声明与初始化

```cpp
int a[10];               // 声明10个整数
int b[5] = {1, 2, 3, 4, 5};     // 完全初始化
int c[5] = {1, 2};              // 部分初始化，未填的为0
int d[] = {10, 20, 30};         // 自动确定大小
```

---

## 2. 遍历

```cpp
int score[5] = {85, 92, 78, 96, 88};

for (int i = 0; i < 5; i++) {
    cout << score[i] << " ";
}
```

---

## 3. 基本操作

```cpp
// 求最大值
int max = score[0];
for (int i = 1; i < 5; i++)
    if (score[i] > max) max = score[i];

// 求和
int sum = 0;
for (int i = 0; i < 5; i++) sum += score[i];

// 数组长度
int len = sizeof(score) / sizeof(score[0]);  // 5
```

---

## 本章小结

1. 数组下标从0开始
2. `sizeof(a)/sizeof(a[0])`计算数组长度
3. 数组适合批量存储和批量处理
"""),

    ("二维数组与多维数组", "array-2d", "cpp", 3, 29,
"""# 二维数组与多维数组

## 本章简介
学习二维数组的声明、初始化和遍历。

---

## 1. 声明与初始化

```cpp
int a[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
```

---

## 2. 遍历

```cpp
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
        cout << a[i][j] << " ";
    }
    cout << endl;
}
```

---

## 3. 应用：杨辉三角

```cpp
int n = 10;
int a[11][11] = {0};

for (int i = 1; i <= n; i++) {
    a[i][1] = a[i][i] = 1;
    for (int j = 2; j < i; j++)
        a[i][j] = a[i-1][j-1] + a[i-1][j];
}
```

---

## 本章小结

1. 二维数组：`类型 数组名[行数][列数]`
2. 双重循环遍历，行列分别处理
3. 二维数组适合处理矩阵和表格数据
"""),

    # ============================================================
    # 二.8 字符串处理
    # ============================================================

    ("字符数组", "char-array", "cpp", 2, 30,
"""# 字符数组

## 本章简介
学习字符数组的基本操作。

---

## 1. 字符数组表示

```cpp
char s1[] = {'H', 'e', 'l', 'l', 'o', '\\0'};
char s2[] = "Hello";  // 更简洁，自动加\\0
```

---

## 2. 字符串长度

```cpp
char s[] = "Hello";
int len = 0;
while (s[len] != '\\0') len++;
cout << len << endl;  // 5
```

---

## 3. 字符串输入输出

```cpp
char name[100];
cin >> name;           // 读取一个单词（遇空格停止）
cout << name << endl;

// 读取一行（包含空格）
cin.getline(name, 100);
```

---

## 本章小结

1. 字符数组用`\\0`结尾表示字符串结束
2. `cin >>`遇空格停止，`cin.getline`可读整行
3. 竞赛中推荐使用string类，更安全方便
"""),

    ("string类", "string-class", "cpp", 2, 31,
"""# string类

## 本章简介
学习C++标准库string类的使用方法。

---

## 1. 基本操作

```cpp
#include <string>
using namespace std;

string s = "Hello";

// 长度
cout << s.length() << endl;  // 5
cout << s.size() << endl;     // 5

// 字符访问
cout << s[0] << endl;  // H
cout << s.at(1) << endl;  // e
```

---

## 2. 字符串拼接与比较

```cpp
string a = "Hello";
string b = "World";

string c = a + " " + b;  // "Hello World"
cout << c << endl;

cout << (a < b) << endl;  // 1（字典序比较）
```

---

## 3. 常用函数

```cpp
string s = "Hello World";

// 子串
cout << s.substr(0, 5) << endl;  // Hello

// 查找
int pos = s.find("World");  // 6
int pos2 = s.find("X");     // string::npos

// 替换
s.replace(6, 5, "C++");
cout << s << endl;  // Hello C++

// 插入
s.insert(5, "!");
cout << s << endl;  // Hello! World
```

---

## 本章小结

1. `string`类比字符数组更安全，功能更丰富
2. 常用函数：`length`、`substr`、`find`、`replace`
3. 竞赛中推荐使用`string`类处理字符串
"""),

    # ============================================================
    # 二.9 函数与递归
    # ============================================================

    ("函数定义与调用", "function-basics", "cpp", 2, 32,
"""# 函数定义与调用

## 本章简介
学习函数的定义、调用和参数传递。

---

## 1. 函数定义

```cpp
int maxValue(int a, int b) {
    if (a > b) return a;
    return b;
}
```

---

## 2. 函数调用

```cpp
int main() {
    int ans = maxValue(3, 7);
    cout << ans << endl;  // 7
    return 0;
}
```

---

## 3. 形参与实参

```cpp
// 形参：函数定义时的参数
void print(int x) {
    cout << x << endl;
}

// 实参：函数调用时的具体值
print(10);  // 10是实参
```

---

## 本章小结

1. 函数：`返回类型 函数名(参数) { 函数体; return值; }`
2. 先定义后调用，或先声明再调用
3. 形参是函数的输入，实参是调用时的具体值
"""),

    ("传值与传引用", "pass-by-value-reference", "cpp", 3, 33,
"""# 传值与传引用

## 本章简介
理解值传递和引用传递的区别。

---

## 1. 值传递

```cpp
void doubleIt(int x) {
    x = x * 2;  // 只改变副本
}

int main() {
    int a = 5;
    doubleIt(a);
    cout << a << endl;  // 仍然是5！
    return 0;
}
```

---

## 2. 引用传递

```cpp
void doubleIt(int& x) {
    x = x * 2;  // 直接修改原变量
}

int main() {
    int a = 5;
    doubleIt(a);
    cout << a << endl;  // 10！
    return 0;
}
```

---

## 3. 对比

| 方式 | 能否修改实参 | 推荐度 |
|------|------------|--------|
| 值传递 | ❌ | 一般只读参数 |
| 引用传递 | ✅ | 需要修改时用 |

---

## 本章小结

1. 值传递：传副本，原变量不变
2. **引用传递**：传变量的别名，可以修改原变量
3. 竞赛中引用传递用于需要修改实参的情况
"""),

    ("变量作用域", "scope", "cpp", 2, 34,
"""# 变量作用域

## 本章简介
理解局部变量、全局变量和作用域规则。

---

## 1. 局部变量

在函数内部声明，只在函数内有效：

```cpp
void func() {
    int x = 10;  // 局部变量
    cout << x << endl;
}
```

---

## 2. 全局变量

在所有函数外部声明，整个文件有效：

```cpp
int g = 100;  // 全局变量

void func() {
    cout << g << endl;  // 可以访问
}
```

---

## 3. 作用域规则

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

## 本章小结

1. 局部变量在函数内有效，全局变量整个文件有效
2. 同名局部变量会遮蔽全局变量
3. 用`::`可以显式访问全局变量
"""),

    ("递归函数", "recursion", "cpp", 2, 35,
"""# 递归函数

## 本章简介
学习递归函数的设计方法和经典例题。

---

## 1. 递归的条件

1. 有递归终止条件
2. 递归调用时规模缩小
3. 有返回值或副作用

---

## 2. 阶乘

```cpp
int factorial(int n) {
    if (n <= 1) return 1;     // 终止条件
    return n * factorial(n - 1);  // 规模缩小
}
```

---

## 3. 斐波那契数列

```cpp
int fib(int n) {
    if (n <= 2) return 1;     // 终止条件
    return fib(n - 1) + fib(n - 2);  // 调用自身
}
```

---

## 4. 递归求和

```cpp
int sum(int n) {
    if (n == 1) return 1;  // 终止
    return n + sum(n - 1);  // 递归
}
```

---

## 本章小结

1. 递归三要素：终止条件、规模缩小、有返回值
2. 递归深度过大会导致栈溢出
3. 斐波那契递归有大量重复计算，可用循环优化
"""),

    # ============================================================
    # 二.10 结构体与联合体
    # ============================================================

    ("结构体", "struct", "cpp", 3, 36,
"""# 结构体

## 本章简介
学习自定义数据类型——结构体的定义和使用。

---

## 1. 定义与使用

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

## 本章小结

1. 结构体：自定义数据类型，封装多个不同类型字段
2. 用`.`访问成员
3. 结构体数组适合管理批量同类型数据
"""),

    ("联合体", "union", "cpp", 3, 37,
"""# 联合体

## 本章简介
学习联合体的概念和使用场景。

---

## 1. 基本概念

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
    data.c = 'A';             // 写入char，i的值被覆盖
    cout << data.i << endl;   // 65（A的ASCII码）
    return 0;
}
```

---

## 2. 应用场景

- 节省内存：结构体中互斥使用的字段
- 底层编程：同一块内存不同解释

---

## 本章小结

1. 联合体所有成员共享同一块内存
2. 同一时间只能使用一个成员
3. 竞赛中使用较少，了解概念即可
"""),

    # ============================================================
    # 二.11 指针与引用
    # ============================================================

    ("指针基础", "pointers-basics", "cpp", 4, 38,
"""# 指针基础

## 本章简介
理解指针的概念和基本使用方法。

---

## 1. 指针的定义

```cpp
int a = 10;
int* p = &a;  // p存储a的地址

cout << p << endl;   // a的地址
cout << *p << endl;  // 10（解引用）
```

**&取地址，*解引用**——两者互为逆运算。

---

## 2. 指针与数组

```cpp
int a[] = {10, 20, 30, 40};
int* p = a;  // 数组名就是首元素地址

cout << *(p + 0) << endl;  // 10
cout << *(p + 1) << endl;  // 20
cout << p[2] << endl;       // 30
```

---

## 本章小结

1. 指针：存储地址的变量，`int* p = &a;`
2. `*p`读取地址中的值，`&a`获取变量地址
3. 数组名是首元素地址，指针运算`p+i`偏移i个元素
"""),

    ("指针与数组", "pointer-array", "cpp", 4, 39,
"""# 指针与数组

## 本章简介
深入理解指针与数组的关系。

---

## 1. 指针算术

```cpp
int a[] = {10, 20, 30, 40, 50};
int* p = a;

p++;          // 指向a[1]
p += 2;       // 指向a[3]
cout << *p << endl;  // 40
```

---

## 2. 指针与const

```cpp
const int* p = &a;  // 不能通过p修改a的值
int const* p2 = &a; // 等价
int* const p3 = &a; // p3不能指向其他地址
const int* const p4 = &a; // 都不能改
```

---

## 本章小结

1. 指针算术：`p+n`、`p-n`、`p++`、`p--`
2. `const int* p`指向的内容不可修改
3. 指针运算在数组遍历中很常用
"""),

    ("字符指针与字符串", "char-pointer", "cpp", 4, 40,
"""# 字符指针与字符串

## 本章简介
学习字符指针和字符串的关系。

---

## 1. 字符指针

```cpp
const char* s = "Hello";  // 指向字符串常量

cout << s << endl;  // 输出Hello
cout << s[1] << endl;  // e

// 注意：字符串常量不能修改
// s[0] = 'h';  // 错误！
```

---

## 2. 指针数组

```cpp
const char* names[] = {"Alice", "Bob", "Charlie"};

for (int i = 0; i < 3; i++) {
    cout << names[i] << endl;
}
```

---

## 本章小结

1. `const char*`指向字符串常量，不可修改
2. 指针数组：每个元素都是字符指针
3. 竞赛中string类更安全，一般不用字符指针
"""),

    ("结构体指针", "pointer-to-struct", "cpp", 4, 41,
"""# 结构体指针

## 本章简介
学习用指针操作结构体。

---

## 1. 结构体指针

```cpp
struct Student {
    string name;
    int score;
};

Student stu = {"张三", 90};
Student* ps = &stu;

cout << ps->name << endl;     // 张三（用->访问）
cout << (*ps).score << endl;  // 90（等价写法）
```

---

## 2. 指针数组

```cpp
Student* arr[3];
Student s1 = {"A", 90};
Student s2 = {"B", 85};

arr[0] = &s1;
arr[1] = &s2;

cout << arr[0]->score << endl;  // 90
```

---

## 本章小结

1. 结构体指针用`->`访问成员
2. `ps->member`等价于`(*ps).member`
3. 链表等数据结构大量使用结构体指针
"""),

    ("引用", "reference", "cpp", 5, 42,
"""# 引用

## 本章简介
学习C++的引用——变量的别名。

---

## 1. 基本使用

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
| 空值 | 不存在 | 可以是nullptr |
| 安全性 | 更高 | 需注意空指针 |

---

## 本章小结

1. 引用是变量的别名，`int& r = a;`
2. 修改引用即修改原变量
3. 竞赛中推荐用引用代替指针，更简洁安全
"""),

    # ============================================================
    # 二.12 文件及基本读写
    # ============================================================

    ("文件概念与文本文件操作", "file-text", "cpp", 2, 43,
"""# 文件概念与文本文件操作

## 本章简介
学习C++的文件操作。

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
    fin >> s;  // 读取一个单词
    cout << s << endl;
    fin.close();

    return 0;
}
```

---

## 2. 判断文件是否打开成功

```cpp
ifstream fin("data.txt");
if (!fin) {
    cout << "文件打开失败" << endl;
    return 1;
}
```

---

## 本章小结

1. `ofstream`写文件，`ifstream`读文件
2. 打开后要关闭，或使用RAII自动关闭
3. 读写前检查文件是否成功打开
"""),

    ("文本与二进制文件、重定向", "file-binary-redirect", "cpp", 2, 44,
"""# 文本与二进制文件、重定向

## 本章简介
理解文本文件和二进制文件的区别，以及竞赛中常用的重定向方法。

---

## 1. 重定向（竞赛常用）

```cpp
// 在程序开头加这两行，从文件读，写到文件
freopen("input.txt", "r", stdin);   // stdin重定向到input.txt
freopen("output.txt", "w", stdout); // stdout重定向到output.txt

// 之后就可以用cin/cout了，自动读写文件
int a, b;
cin >> a >> b;
cout << a + b << endl;
```

---

## 2. 二进制文件

```cpp
#include <fstream>
ofstream fout("data.bin", ios::binary);

int x = 12345;
fout.write((char*)&x, sizeof(x));  // 写入4字节

ifstream fin("data.bin", ios::binary);
fin.read((char*)&x, sizeof(x));
cout << x << endl;  // 12345
```

---

## 本章小结

1. `freopen`实现输入输出重定向，竞赛中常用
2. 二进制文件按字节读写，文本文件按字符读写
3. 竞赛题一般用freopen重定向文件
"""),

    # ============================================================
    # 二.13 STL模板
    # ============================================================

    ("STL：min、max、swap、sort", "stl-algorithm", "cpp", 3, 45,
"""# STL：min、max、swap、sort

## 本章简介
学习STL中最常用的四个算法函数。

---

## 1. min、max、swap

```cpp
#include <algorithm>
cout << min(3, 7) << endl;           // 3
cout << max(3, 7) << endl;           // 7
swap(3, 7);                           // 交换

// 三个数的最值
cout << min({3, 1, 7}) << endl;     // 1
cout << max({3, 1, 7}) << endl;     // 7
```

---

## 2. sort排序

```cpp
vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};

sort(v.begin(), v.end());  // 升序：1 1 2 3 4 5 6 9

// 降序
sort(v.begin(), v.end(), greater<int>());

// 自定义排序：按绝对值
sort(v.begin(), v.end(), [](int a, int b) {
    return abs(a) < abs(b);
});
```

---

## 本章小结

1. `min/max`返回最值，`swap`交换
2. `sort`是竞赛中最高效的排序，O(n log n)
3. `greater<int>()`实现降序
"""),

    ("STL：stack、queue、list、vector", "stl-container", "cpp", 4, 46,
"""# STL：stack、queue、list、vector

## 本章简介
学习四种最常用的STL容器。

---

## 1. vector（动态数组）

```cpp
#include <vector>
vector<int> v = {3, 1, 4};

v.push_back(5);     // 尾部添加
v.insert(v.begin()+1, 7);  // 中间插入
sort(v.begin(), v.end());  // 排序
```

---

## 2. stack（栈）

```cpp
#include <stack>
stack<int> s;
s.push(1); s.push(2); s.push(3);
cout << s.top() << endl;  // 3
s.pop();  // 出栈
```

---

## 3. queue（队列）

```cpp
#include <queue>
queue<int> q;
q.push(1); q.push(2); q.push(3);
cout << q.front() << endl;  // 1
q.pop();  // 出队
```

---

## 4. list（双向链表）

```cpp
#include <list>
list<int> lst = {1, 2, 3, 4, 5};
lst.push_front(0);   // 头部插入
lst.remove(3);       // 删除值为3的节点
```

---

## 本章小结

1. `vector`：首选，动态数组，支持随机访问
2. `stack`：LIFO，适合括号匹配、表达式求值
3. `queue`：FIFO，适合BFS、任务调度
4. `list`：双向链表，插入删除O(1)，不支持随机访问
"""),

    # ============================================================
    # 三、数据结构
    # 三.1 线性结构
    # ============================================================

    ("单链表、双向链表、循环链表", "linked-lists", "data-structure", 3, 47,
"""# 单链表、双向链表、循环链表

## 本章简介
学习三种基本链表结构的原理和实现。

---

## 1. 单链表节点

```cpp
struct Node {
    int data;
    Node* next;
    Node(int x) : data(x), next(nullptr) {}
};
```

---

## 2. 单链表操作

```cpp
// 头插法
void insertHead(Node*& head, int val) {
    Node* newNode = new Node(val);
    newNode->next = head;
    head = newNode;
}

// 遍历
for (Node* p = head; p; p = p->next) {
    cout << p->data << " ";
}
```

---

## 3. 双向链表

```cpp
struct DNode {
    int data;
    DNode* prev;
    DNode* next;
};
```

---

## 4. 循环链表

首尾相接的链表，常用场景是约瑟夫问题：

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
        it = L.erase(it);
        if (it == L.end()) it = L.begin();
    }
    return L.front();
}
```

---

## 本章小结

1. 单链表：单向next，适合频繁插入删除
2. 双向链表：prev+next，删除更方便
3. 循环链表：首尾相接，适合环状问题
"""),

    ("栈", "stack-ds", "data-structure", 3, 48,
"""# 栈

## 本章简介
学习栈数据结构的原理和竞赛中的应用。

---

## 1. 基本操作

```cpp
#include <stack>
stack<int> s;

s.push(1);   // 入栈
s.push(2);
s.push(3);

cout << s.top() << endl;  // 3（栈顶）
s.pop();  // 出栈，不返回值
```

---

## 2. 应用：括号匹配

```cpp
bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c=='('||c=='['||c=='{') st.push(c);
        else {
            if (st.empty()) return false;
            char top = st.top();
            if ((c==')'&&top!='(')||(c==']'&&top!='[')||(c=='}'&&top!='{')) return false;
            st.pop();
        }
    }
    return st.empty();
}
```

---

## 本章小结

1. 栈（LIFO）：`push`入栈，`pop`出栈，`top`看栈顶
2. 括号匹配是栈的经典应用
3. 表达式求值也用栈实现
"""),

    ("队列", "queue-ds", "data-structure", 3, 49,
"""# 队列

## 本章简介
学习队列的原理和BFS中的应用。

---

## 1. 基本操作

```cpp
#include <queue>
queue<int> q;

q.push(1); q.push(2); q.push(3);
cout << q.front() << endl;  // 1（队首）
cout << q.back() << endl;   // 3（队尾）
q.pop();  // 出队
```

---

## 2. 应用：BFS广度优先搜索

```cpp
queue<int> q;
q.push(start);
vis[start] = true;

while (!q.empty()) {
    int cur = q.front(); q.pop();
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
2. BFS用队列，DFS用栈或递归
3. 队列还用于任务调度、层序遍历
"""),

    # ============================================================
    # 三.2 简单树
    # ============================================================

    ("树的定义与概念", "tree-definition", "data-structure", 3, 50,
"""# 树的定义与概念

## 本章简介
理解树的基本概念和术语。

---

## 1. 树的基本术语

| 术语 | 含义 |
|------|------|
| 节点 | 树中的每个元素 |
| 根节点 | 没有父节点的节点 |
| 叶子节点 | 没有子节点的节点 |
| 父节点/子节点 | 上下层关系 |
| 深度 | 从根到该节点的边数 |
| 高度 | 从该节点到最深叶子节点的边数 |

---

## 2. 二叉树

每个节点最多有两个子节点：

- **左孩子、右孩子**
- **满二叉树**：每层都满节点
- **完全二叉树**：除最后一层外满节点，最后一层左对齐

---

## 本章小结

1. 树是层次结构，有根节点和叶子节点
2. 二叉树每个节点最多两个子节点
3. 竞赛中主要使用二叉树
"""),

    ("树的表示与存储", "tree-storage", "data-structure", 4, 51,
"""# 树的表示与存储

## 本章简介
学习二叉树的存储方式。

---

## 1. 链式存储

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

---

## 2. 完全二叉树的数组存储

父节点i，左孩子2i，右孩子2i+1：

```cpp
int tree[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};  // 0号位不用

int parent(int i) { return i/2; }
int leftChild(int i) { return 2*i; }
int rightChild(int i) { return 2*i+1; }
```

---

## 本章小结

1. 链式存储适合任意二叉树
2. 完全二叉树用数组存储最省空间
3. 数组存储：父节点i → 左孩子2i，右孩子2i+1
"""),

    ("二叉树基本性质", "binary-tree-properties", "data-structure", 3, 52,
"""# 二叉树基本性质

## 本章简介
掌握二叉树的重要性质。

---

## 1. 基本性质

1. 第i层最多有`2^(i-1)`个节点（根为第1层）
2. 深度为k的二叉树最多有`2^k - 1`个节点
3. **叶节点数 = 度为2的节点数 + 1**（n₀ = n₂ + 1）

---

## 2. 完全二叉树的性质

若完全二叉树有n个节点：

- 最后一个有孩子的节点编号 = `n/2`（向下取整）
- 深度 = `⌊log₂n⌋ + 1`

---

## 本章小结

1. 二叉树第i层最多2^(i-1)个节点
2. n₀ = n₂ + 1是竞赛常考性质
3. 完全二叉树适合用数组存储
"""),

    ("二叉树遍历", "binary-tree-traversal", "data-structure", 4, 53,
"""# 二叉树遍历

## 本章简介
学习二叉树的四种遍历方式。

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
        TreeNode* node = q.front(); q.pop();
        cout << node->val << " ";
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
}
```

---

## 本章小结

1. 前序：根左右，中序：左根右，后序：左右根
2. **中序遍历BST是有序序列**
3. 层序遍历用队列，保证按层次顺序
"""),

    ("完全二叉树与堆", "heap", "data-structure", 4, 54,
"""# 完全二叉树与堆

## 本章简介
学习堆数据结构的原理和实现。

---

## 1. 堆的定义

堆是一棵完全二叉树：
- **最大堆**：父节点 ≥ 子节点，根是最大值
- **最小堆**：父节点 ≤ 子节点，根是最小值

---

## 2. 向下调整

```cpp
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

## 3. 堆排序

```cpp
void heapSort(int a[], int n) {
    // 建堆：从最后一个非叶子节点向上
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

1. 最大堆父节点≥子节点，根是最大值
2. 堆排序：O(n log n)，建堆O(n)
3. 竞赛中可以用堆做第k大/小问题
"""),

    ("哈夫曼树", "huffman", "data-structure", 4, 55,
"""# 哈夫曼树

## 本章简介
学习哈夫曼树的构造和哈夫曼编码。

---

## 1. 基本概念

- **WPL**（带权路径长度）：所有叶子节点的权值×路径长度之和
- **哈夫曼树**：WPL最小的二叉树

---

## 2. 构造哈夫曼树（贪心）

每次合并权值最小的两棵树：

```cpp
#include <queue>
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
    cout << cost << endl;  // 最小WPL
    return 0;
}
```

---

## 3. 哈夫曼编码

高频字符用短码，低频用长码，前缀编码：

| 字符 | 频率 | 编码 |
|------|------|------|
| A | 45 | 0 |
| B | 13 | 101 |
| C | 12 | 100 |

---

## 本章小结

1. 哈夫曼树WPL最小，用最小堆构造
2. 核心：贪心，每次合并最小的两棵树
3. 哈夫曼编码是前缀编码，高频短码
"""),

    ("二叉搜索树", "bst", "data-structure", 4, 56,
"""# 二叉搜索树

## 本章简介
学习二叉搜索树（BST）的定义、查找、插入和删除。

---

## 1. BST定义

左子树所有节点 < 根 < 右子树所有节点。

**中序遍历BST得到有序序列！**

---

## 2. 查找

```cpp
TreeNode* searchBST(TreeNode* root, int target) {
    if (!root || root->val == target) return root;
    if (target < root->val) return searchBST(root->left, target);
    return searchBST(root->right, target);
}
```

---

## 3. 插入

```cpp
TreeNode* insertBST(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    if (val < root->val) root->left = insertBST(root->left, val);
    else root->right = insertBST(root->right, val);
    return root;
}
```

---

## 本章小结

1. BST：左<根<右，中序遍历得到有序序列
2. 查找/插入/删除：O(log n)（平衡时）
3. 最坏O(n)（退化成链表），需要平衡树
"""),

    # ============================================================
    # 三.3 简单图
    # ============================================================

    ("邻接矩阵", "adjacency-matrix", "data-structure", 4, 57,
"""# 邻接矩阵

## 本章简介
学习用邻接矩阵存储图。

---

## 1. 定义

用二维数组表示图中顶点之间的边：

```cpp
const int MAXN = 100;
int g[MAXN][MAXN] = {0};

void addEdge(int u, int v) {
    g[u][v] = g[v][u] = 1;  // 无向图
}

void addDirEdge(int u, int v) {
    g[u][v] = 1;  // 有向图
}
```

---

## 2. 特点

| 特点 | 说明 |
|------|------|
| 空间复杂度 | O(V²)，V为顶点数 |
| 查询边 | O(1)，直接g[u][v] |
| 适用场景 | 稠密图（边多） |

---

## 本章小结

1. 邻接矩阵：二维数组，`g[u][v]=1`表示边(u,v)存在
2. 空间O(V²)，适合稠密图
3. 竞赛中V≤500时可用邻接矩阵
"""),

    ("邻接表", "adjacency-list", "data-structure", 4, 58,
"""# 邻接表

## 本章简介
学习用邻接表存储图。

---

## 1. 定义

用数组+链表存储每个顶点的邻居：

```cpp
#include <vector>
vector<int> adj[MAXN];  // adj[i]存储i的所有邻居

void addEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);  // 无向图
}
```

---

## 2. 特点

| 特点 | 说明 |
|------|------|
| 空间复杂度 | O(V+E) |
| 查询边 | O(deg)，遍历邻居 |
| 适用场景 | 稀疏图（边少） |

---

## 本章小结

1. 邻接表：每个顶点一个list，存所有邻居
2. 空间O(V+E)，竞赛中大多数图用邻接表
3. C++中用`vector<int> adj[N]`实现
"""),

    # ============================================================
    # 四、算法
    # 四.1 算法概念与描述
    # ============================================================

    ("算法概念", "algorithm-concept", "algorithm", 1, 59,
"""# 算法概念

## 本章简介
理解算法的定义和基本特征。

---

## 1. 算法的定义

**算法**：解决特定问题的有限步骤。

---

## 2. 算法的特征

| 特征 | 说明 |
|------|------|
| 有穷性 | 有限步骤内结束 |
| 确定性 | 每一步有明确定义 |
| 可行性 | 能被计算机执行 |
| 输入 | 有零个或多个输入 |
| 输出 | 有一个或多个输出 |

---

## 3. 算法复杂度

| 复杂度 | 规模上限 |
|--------|---------|
| O(1) | 常数时间 |
| O(log n) | 对数时间 |
| O(n) | 线性时间 |
| O(n log n) | 线性对数 |
| O(n²) | 平方时间 |
| O(2ⁿ) | 指数时间 |

---

## 本章小结

1. 算法是解决问题的有限步骤
2. 复杂度是评价算法优劣的主要标准
3. 竞赛中O(n log n)是最常用的排序复杂度
"""),

    ("算法描述", "algorithm-description", "algorithm", 2, 60,
"""# 算法描述

## 本章简介
学习用自然语言、流程图和伪代码描述算法。

---

## 1. 自然语言

用日常语言描述算法步骤：

```
1. 读取n
2. 如果n是负数，转第5步
3. 计算n的平方
4. 输出结果
5. 结束
```

---

## 2. 流程图

用标准化图形描述算法流程：

```
开始 → 输入n → n≥0? → 是 → 计算n² → 输出
                  ↓否
                输出0 → 结束
```

---

## 3. 伪代码

用类似代码的语言描述算法：

```
function findMax(a, n):
    max = a[0]
    for i = 1 to n-1:
        if a[i] > max:
            max = a[i]
    return max
```

---

## 本章小结

1. 自然语言：直观但易歧义
2. 流程图：图形化，清晰直观
3. 伪代码：接近代码，最常用
"""),

    # ============================================================
    # 四.2 入门算法
    # ============================================================

    ("枚举法", "enumeration", "algorithm", 1, 61,
"""# 枚举法

## 本章简介
学习枚举法的思想和应用。

---

## 1. 枚举法思想

逐一列举所有可能的情况，验证每个解是否符合条件。

**关键**：确定枚举的范围和条件。

---

## 2. 经典例题：水仙花数

```cpp
for (int i = 100; i <= 999; i++) {
    int a = i / 100;
    int b = i / 10 % 10;
    int c = i % 10;
    if (a*a*a + b*b*b + c*c*c == i)
        cout << i << " ";  // 153 370 371 407
}
```

---

## 3. 优化：缩小枚举范围

判断素数只需枚举到√n：

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
```

---

## 本章小结

1. 枚举法：确定范围，逐一验证
2. 关键优化：缩小枚举范围
3. 判断素数只需试除到√n
"""),

    ("模拟法", "simulation", "algorithm", 1, 62,
"""# 模拟法

## 本章简介
学习根据题目描述用代码逐步模拟过程的方法。

---

## 1. 模拟法思想

**按照题目的描述，一步一步用代码翻译出来。**

---

## 2. 例题：计算日期第二天

```cpp
int main() {
    int y, m, d;
    cin >> y >> m >> d;

    int days[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    if ((y%4==0 && y%100!=0) || y%400==0) days[2] = 29;

    d++;
    if (d > days[m]) {
        d = 1;
        m++;
        if (m > 12) { m = 1; y++; }
    }
    cout << y << "-" << m << "-" << d << endl;
}
```

---

## 3. 模拟纸牌洗牌

```cpp
int main() {
    int n; cin >> n;
    int a[105] = {0}, b[105] = {0};
    for (int i = 1; i <= n; i++) cin >> a[i];
    int step; cin >> step;
    while (step--) {
        int cnt = 1;
        for (int i = 1; i <= n/2; i++) {
            b[cnt++] = a[i];
            b[cnt++] = a[i + n/2];
        }
        for (int i = 1; i <= n; i++) a[i] = b[i];
    }
    for (int i = 1; i <= n; i++) cout << a[i] << " ";
}
```

---

## 本章小结

1. 模拟法：把题目描述翻译成代码
2. 关键是读懂题意，不要自己想当然
3. CSP-J第一题最常见的题型
"""),

    # ============================================================
    # 四.3 基础算法
    # ============================================================

    ("贪心算法", "greedy", "algorithm", 3, 63,
"""# 贪心算法

## 本章简介
学习贪心算法的思想和经典应用。

---

## 1. 贪心思想

每一步都选择当前最优解，不回头。

**关键**：要能证明贪心策略能导致全局最优！

---

## 2. 活动选择（经典）

```cpp
struct Act { int s, e; };
bool cmp(Act a, Act b) { return a.e < b.e; }

int main() {
    Act acts[] = {{1,4},{3,5},{0,6},{5,7},{3,9}};
    int n = 5;
    sort(acts, acts+n, cmp);
    int cnt = 0, lastEnd = 0;
    for (int i = 0; i < n; i++)
        if (acts[i].s >= lastEnd) { cnt++; lastEnd = acts[i].e; }
    cout << cnt << endl;  // 3
}
```

---

## 3. 找零钱

```cpp
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

    ("递推", "recurrence", "algorithm", 3, 64,
"""# 递推

## 本章简介
学习递推思想，从已知推未知。

---

## 1. 递推思想

从已知的初始值出发，利用递推公式逐步推导。

---

## 2. 爬楼梯

```cpp
int climb(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        a = b; b = c;
    }
    return b;
}
```

---

## 3. 错排问题

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

1. 递推：找规律建公式，从已知推到未知
2. 斐波那契、爬楼梯、错排都是经典递推
3. 递推和递归公式往往互逆
"""),

    ("递归", "recursion-dp", "algorithm", 4, 65,
"""# 递归

## 本章简介
学习递归算法的设计和应用。

---

## 1. 递归的两个条件

1. 有递归终止条件
2. 递归调用时规模缩小

---

## 2. 全排列（递归实现）

```cpp
int n = 3, used[11], path[11];

void dfs(int step) {
    if (step > n) {
        for (int i = 1; i <= n; i++) cout << path[i];
        cout << endl;
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            used[i] = 1; path[step] = i;
            dfs(step + 1);
            used[i] = 0;
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

## 本章小结

1. 递归：函数调用自身，必须有终止条件
2. 全排列：标记已用数字，path记录路径
3. 组合：从start开始避免重复
"""),

    ("二分查找", "binary-search-algo", "algorithm", 4, 66,
"""# 二分查找

## 本章简介
学习二分查找算法和二分答案。

---

## 1. 二分查找

```cpp
int binarySearch(int a[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] == target) return mid;
        else if (a[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

---

## 2. 二分答案

把求最优值转化为判定问题：

```cpp
bool can(int weights[], int n, int days, int cap) {
    int need = 1, cur = 0;
    for (int i = 0; i < n; i++) {
        if (cur + weights[i] <= cap) cur += weights[i];
        else { need++; cur = weights[i]; }
    }
    return need <= days;
}

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
2. `mid = left + (right-left)/2`防溢出
3. 二分答案：答案有单调性时，将求最优转为判定
"""),

    ("倍增", "doubling", "algorithm", 4, 67,
"""# 倍增

## 本章简介
学习倍增思想和快速幂。

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
            for (int j = 0; j < 2; j++)
                r.a[i][j] = 0, a[i][k]*b.a[k][j]);
        return r;
    }
};
```

---

## 本章小结

1. 快速幂：O(log e)，指数按二进制拆分
2. 矩阵快速幂可加速线性递推
3. 倍增思想：跳过多个状态，快速逼近目标
"""),

    # ============================================================
    # 四.4 算法策略
    # ============================================================

    ("前缀和", "prefix-sum", "algorithm", 3, 68,
"""# 前缀和

## 本章简介
学习前缀和用于O(1)区间查询。

---

## 1. 一维前缀和

```cpp
int a[11] = {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
int prefix[11];

for (int i = 1; i <= 10; i++)
    prefix[i] = prefix[i-1] + a[i];

// 查询区间[3,7]的和
int l = 3, r = 7;
int sum = prefix[r] - prefix[l-1];  // 45
```

---

## 2. 二维前缀和

```cpp
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + a[i][j];

// 查询子矩阵和
int sum = ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1];
```

---

## 本章小结

1. 前缀和：`prefix[i] = sum(a[1]~a[i])`
2. 区间和：`sum(l,r) = prefix[r] - prefix[l-1]`
3. 预处理O(n)，多次查询O(1)
"""),

    ("差分", "difference", "algorithm", 4, 69,
"""# 差分

## 本章简介
学习差分用于高效批量区间修改。

---

## 1. 差分数组

差分是前缀和的逆运算：

```cpp
int a[11] = {0, 1, 3, 5, 7};
int diff[11] = {0};
diff[1] = a[1];
for (int i = 2; i <= 5; i++)
    diff[i] = a[i] - a[i-1];
```

---

## 2. 区间修改

对区间[l, r]中每个元素加k：

```cpp
diff[l] += k;
diff[r+1] -= k;
// 求前缀和后，a[l]~a[r]都被加了k
```

---

## 本章小结

1. 差分是前缀和的逆运算
2. 区间[l,r]+k → `diff[l]+=k, diff[r+1]-=k`
3. 适合多次区间修改+最终结果的场景
"""),

    # ============================================================
    # 四.5 数值处理
    # ============================================================

    ("高精度计算", "high-precision", "algorithm", 4, 70,
"""# 高精度计算

## 本章简介
学习用字符串模拟超出long long范围的整数计算。

---

## 1. 高精度加法

```cpp
string add(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    int carry = 0, i = 0;
    string res;
    while (i < max(a.size(), b.size()) || carry) {
        int da = i < a.size() ? a[i]-'0' : 0;
        int db = i < b.size() ? b[i]-'0' : 0;
        int sum = da + db + carry;
        res.push_back('0' + (sum % 10));
        carry = sum / 10;
        i++;
    }
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
        int d = i < num.size() ? num[i]-'0' : 0;
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
3. 去除前导0（保留"0"本身）
"""),

    # ============================================================
    # 四.6 排序算法
    # ============================================================

    ("排序基本概念", "sorting-basics", "algorithm", 3, 71,
"""# 排序基本概念

## 本章简介
理解排序的基本概念和评价标准。

---

## 1. 排序的定义

将n个数据按关键字递增（或递减）排列。

---

## 2. 稳定排序

相同关键字的元素排序后相对顺序不变：

| 排序算法 | 时间复杂度 | 空间 | 稳定性 |
|---------|-----------|------|--------|
| 冒泡排序 | O(n²) | O(1) | ✅ |
| 选择排序 | O(n²) | O(1) | ❌ |
| 插入排序 | O(n²) | O(1) | ✅ |
| 计数排序 | O(n+k) | O(k) | ✅ |
| sort | O(n log n) | O(1) | ❌ |

---

## 3. 竞赛中的选择

- 一般数据：`sort`（C++ STL）
- 特殊场景：计数排序、基数排序

---

## 本章小结

1. 稳定排序：相同元素相对顺序不变
2. 竞赛中直接用`sort`最方便
3. 了解各排序原理是为了在特定场景下选择最优
"""),

    ("冒泡、选择、插入、计数排序", "sorting-algorithms", "algorithm", 3, 72,
"""# 冒泡、选择、插入、计数排序

## 本章简介
学习四种基础排序算法。

---

## 1. 冒泡排序

```cpp
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-1-i; j++)
            if (a[j] > a[j+1]) swap(a[j], a[j+1]);
}
```

---

## 2. 选择排序

```cpp
void selectionSort(int a[], int n) {
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i+1; j < n; j++)
            if (a[j] < a[minIdx]) minIdx = j;
        swap(a[i], a[minIdx]);
    }
}
```

---

## 3. 插入排序

```cpp
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) a[j+1] = a[j--];
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
    for (int i = 0, idx = 0; i <= maxVal; i++)
        while (count[i]--) a[idx++] = i;
}
```

---

## 本章小结

1. 冒泡：相邻交换，每趟最大冒到右边
2. 选择：每趟选最小，与未排序首元素交换（不稳定）
3. 插入：像整理扑克牌，已排序部分逐一插入
4. 计数：非比较排序，O(n+k)，适合整数范围小的情况
"""),

    # ============================================================
    # 四.7 搜索算法
    # ============================================================

    ("深度优先搜索（DFS）", "dfs-algo", "algorithm", 5, 73,
"""# 深度优先搜索（DFS）

## 本章简介
学习DFS的递归实现和经典应用。

---

## 1. DFS基本模板

```cpp
void dfs(int state) {
    if (终止条件) { 记录答案; return; }
    for (每种选择) {
        if (可行 && !vis) {
            做选择;
            dfs(state + 1);
            撤销选择;
        }
    }
}
```

---

## 2. 迷宫问题

```cpp
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

bool dfs(int x, int y) {
    if (x == 4 && y == 4) return true;
    vis[x][y] = true;
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir], ny = y + dy[dir];
        if (nx>=0&&nx<5&&ny>=0&&ny<5&&!maze[nx][ny]&&!vis[nx][ny])
            if (dfs(nx, ny)) return true;
    }
    return false;
}
```

---

## 本章小结

1. DFS：递归深入，用vis避免重复访问
2. 全排列、组合、迷宫、连通块都用DFS
3. 剪枝可大幅提升效率
"""),

    ("广度优先搜索（BFS）", "bfs-algo", "algorithm", 5, 74,
"""# 广度优先搜索（BFS）

## 本章简介
学习BFS用于最短路和层序扩展。

---

## 1. BFS基本模板

```cpp
queue<int> q;
q.push(start); vis[start] = true;
while (!q.empty()) {
    int cur = q.front(); q.pop();
    for (每个邻居) {
        if (合法 && !vis[邻居]) {
            q.push(邻居); vis[邻居] = true;
        }
    }
}
```

---

## 2. BFS求最短路

```cpp
struct Node { int x, y, dist; };
queue<Node> q;
q.push({0, 0, 0}); vis[0][0] = true;
while (!q.empty()) {
    Node cur = q.front(); q.pop();
    if (cur.x == 4 && cur.y == 4) return cur.dist;
    for (int dir = 0; dir < 4; dir++) {
        int nx = cur.x + dx[dir], ny = cur.y + dy[dir];
        if (可通行 && !vis[nx][ny]) {
            q.push({nx, ny, cur.dist + 1});
            vis[nx][ny] = true;
        }
    }
}
```

---

## 3. DFS vs BFS

| 特征 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈（递归） | 队列 |
| 最短路 | ❌ | ✅ |
| 内存 | 较省 | 较多 |

---

## 本章小结

1. BFS用队列，层层扩展，能找到**最短路径**
2. BFS适合：迷宫最短路、层序遍历
3. DFS适合：全排列、组合、连通块
"""),

    # ============================================================
    # 四.8 图论算法
    # ============================================================

    ("图的DFS与BFS遍历", "graph-dfs-bfs", "algorithm", 4, 75,
"""# 图的DFS与BFS遍历

## 本章简介
学习图的深度优先和广度优先遍历。

---

## 1. 图的DFS

```cpp
bool vis[MAXN];
void dfs(int u) {
    vis[u] = true;
    cout << u << " ";
    for (int v : adj[u])
        if (!vis[v]) dfs(v);
}
```

---

## 2. 图的BFS

```cpp
#include <queue>
void bfs(int start) {
    queue<int> q;
    q.push(start); vis[start] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << " ";
        for (int v : adj[u])
            if (!vis[v]) q.push(v), vis[v] = true;
    }
}
```

---

## 3. 连通分量计数

```cpp
int countComponents(int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++)
        if (!vis[i]) { cnt++; bfs(i); }
    return cnt;
}
```

---

## 本章小结

1. 图的DFS/BFS与树类似，必须用`vis`避免重复访问
2. 连通分量：BFS一次遍历计一个分量
3. 竞赛中图论题优先用BFS（最短路）或DFS（连通性）
"""),

    ("Flood Fill", "flood-fill", "algorithm", 5, 76,
"""# Flood Fill

## 本章简介
学习洪水填充算法用于连通块计数。

---

## 1. DFS版Flood Fill

```cpp
int n, m;
int a[10][10];
bool vis[10][10];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void fill(int x, int y) {
    if (x<0||x>=n||y<0||y>=m) return;
    if (vis[x][y]||a[x][y]==1) return;
    vis[x][y] = true;
    fill(x+1,y); fill(x-1,y); fill(x,y+1); fill(x,y-1);
}
```

---

## 2. BFS版Flood Fill

```cpp
void bfsFill(int sx, int sy) {
    queue<pair<int,int>> q;
    q.push({sx, sy}); vis[sx][sy] = true;
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = x+dx[dir], ny = y+dy[dir];
            if (nx>=0&&nx<n&&ny>=0&&ny<m&&!vis[nx][ny]&&a[nx][ny]!=1)
                q.push({nx, ny}), vis[nx][ny] = true;
        }
    }
}
```

---

## 3. 连通块计数

```cpp
int countComponents() {
    int cnt = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (!vis[i][j] && a[i][j] != 1)
                bfsFill(i, j), cnt++;
    return cnt;
}
```

---

## 本章小结

1. Flood Fill：从起点出发，填充所有连通格子
2. DFS版适合小区域，BFS版适合大区域
3. 常用于：岛屿计数、迷宫连通块
"""),

    # ============================================================
    # 四.9 动态规划
    # ============================================================

    ("DP基本思路", "dp-basics", "algorithm", 4, 77,
"""# DP基本思路

## 本章简介
学习动态规划的三要素和基本解题步骤。

---

## 1. DP三要素

| 要素 | 含义 |
|------|------|
| 状态 | `dp[i]`表示什么 |
| 转移 | `dp[i] = f(dp[...])` |
| 初始化 | 边界条件 |

---

## 2. 解题步骤

1. 确定状态（`dp`数组的含义）
2. 找转移方程
3. 确定初始值
4. 确定计算顺序
5. 优化（如需要）

---

## 3. 经典例题：最大子段和

```cpp
int maxSubArray(int a[], int n) {
    int dp[10000];
    dp[0] = a[0];
    int ans = dp[0];
    for (int i = 1; i < n; i++)
        dp[i] = max(a[i], dp[i-1] + a[i]),
        ans = max(ans, dp[i]);
    return ans;
}
```

---

## 本章小结

1. DP核心：状态+转移+初始化
2. 重叠子问题+最优子结构=可用DP
3. 最大子段和：`dp[i]=max(a[i], dp[i-1]+a[i])`
"""),

    ("简单一维DP", "dp-1d", "algorithm", 4, 78,
"""# 简单一维DP

## 本章简介
通过更多例题加深对一维DP的理解。

---

## 1. 打家劫舍

```cpp
int rob(int money[], int n) {
    if (n == 1) return money[0];
    if (n == 2) return max(money[0], money[1]);
    int dp[1000];
    dp[0] = money[0];
    dp[1] = max(money[0], money[1]);
    for (int i = 2; i < n; i++)
        dp[i] = max(dp[i-1], dp[i-2] + money[i]);
    return dp[n-1];
}
```

---

## 2. 最长上升子序列（LIS）

```cpp
int LIS(int a[], int n) {
    int dp[1000] = {0}, ans = 0;
    for (int i = 0; i < n; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++)
            if (a[j] < a[i]) dp[i] = max(dp[i], dp[j] + 1);
        ans = max(ans, dp[i]);
    }
    return ans;
}
```

---

## 本章小结

1. `dp[i]`表示以i结尾的最优解
2. 打家劫舍：`dp[i]=max(dp[i-1], dp[i-2]+money[i])`
3. LIS：O(n²)DP，逐个比较前驱
"""),

    ("简单背包DP", "knapsack-dp", "algorithm", 5, 79,
"""# 简单背包DP

## 本章简介
学习0-1背包和完全背包的解法。

---

## 1. 0-1背包

每件物品选0或1次：

```cpp
int knapsack01(int w[], int v[], int n, int C) {
    int dp[1005] = {0};
    for (int i = 0; i < n; i++)
        for (int c = C; c >= w[i]; c--)
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
    return dp[C];
}
```

**关键**：内层**倒序**，每件物品只选一次。

---

## 2. 完全背包

每件物品可选无限次：

```cpp
int knapsackComplete(int w[], int v[], int n, int C) {
    int dp[1005] = {0};
    for (int i = 0; i < n; i++)
        for (int c = w[i]; c <= C; c++)
            dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
    return dp[C];
}
```

**关键**：内层**正序**，每件物品可选无限次。

---

## 本章小结

1. 0-1背包：内层倒序，每件物品选一次
2. 完全背包：内层正序，每件物品可选无限次
3. 一维dp：空间优化到O(C)
"""),

    ("简单区间DP", "interval-dp", "algorithm", 5, 80,
"""# 简单区间DP

## 本章简介
学习区间DP的模板和合并石子问题。

---

## 1. 区间DP模板

```cpp
for (int len = 2; len <= n; len++)           // 枚举长度
    for (int i = 1; i + len - 1 <= n; i++) { // 枚举起点了
        int j = i + len - 1;                   // 终点
        dp[i][j] = INF;
        for (int k = i; k < j; k++)           // 枚举分割点
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost);
    }
```

---

## 2. 合并石子

```cpp
int stoneMerge(int w[], int n) {
    int prefix[105] = {0};
    for (int i = 1; i <= n; i++) prefix[i] = prefix[i-1] + w[i];
    int dp[105][105] = {0};
    for (int len = 2; len <= n; len++)
        for (int i = 1; i + len - 1 <= n; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++)
                dp[i][j] = min(dp[i][j],
                    dp[i][k] + dp[k+1][j] + prefix[j] - prefix[i-1]);
        }
    return dp[1][n];
}
```

---

## 本章小结

1. 区间DP：外层枚举长度，内层枚举起点和分割点
2. `dp[i][j]`表示区间[i,j]的最优解
3. 合并石子是区间DP的经典问题
"""),

    # ============================================================
    # 五、数学与其他
    # 五.1 数及其运算
    # ============================================================

    ("数及其运算", "numbers", "math", 1, 81,
"""# 数及其运算

## 本章简介
理解自然数、整数、有理数、实数的概念和运算。

---

## 1. 数集

| 数集 | 符号 | 包含 |
|------|------|------|
| 自然数 | N | 0, 1, 2, 3... |
| 整数 | Z | ...-2, -1, 0, 1, 2... |
| 有理数 | Q | p/q (q≠0) |
| 实数 | R | 有理数+无理数 |

---

## 2. 基本运算律

- 交换律：a+b = b+a, a×b = b×a
- 结合律：(a+b)+c = a+(b+c)
- 分配律：a×(b+c) = a×b + a×c

---

## 3. C++中的整数运算

```cpp
int a = 7, b = 2;
cout << a + b << endl;  // 9
cout << a - b << endl;  // 5
cout << a * b << endl;  // 14
cout << a / b << endl;  // 3（整数除法，向零取整）
cout << a % b << endl;  // 1（余数）
```

---

## 本章小结

1. N、Z、Q、R是数学中最基本的数集
2. C++整数除法向零取整，负数除法要注意
3. `%`取余运算在算法中经常用到
"""),

    ("进制转换", "base-conversion", "math", 1, 82,
"""# 进制转换

## 本章简介
学习二进制、八进制、十进制、十六进制之间的转换。

---

## 1. 十进制转其他进制

**除基取余，倒序取余**：

```cpp
string decToBin(int n) {
    if (n == 0) return "0";
    string s;
    while (n > 0) {
        s = char('0' + (n % 2)) + s;
        n /= 2;
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
    for (char c : s)
        result = result * 2 + (c - '0');
    return result;
}
```

---

## 3. 二进制与八进制、十六进制

```cpp
// 二进制→八进制：每3位一组
// 1101011₂ = 001 101 011 = 153₈

// 二进制→十六进制：每4位一组
// 1101011₂ = 0110 1011 = 6B₁₆
```

---

## 本章小结

1. 十进制转其他进制：除基取余
2. 其他进制转十进制：按权展开
3. 二进制↔八进制：3位一组；二进制↔十六进制：4位一组
"""),

    # ============================================================
    # 五.2 初等数学
    # ============================================================

    ("初中代数", "middle-school-algebra", "math", 1, 83,
"""# 初中代数

## 本章简介
复习初中代数基础。

---

## 1. 代数公式

```cpp
// 完全平方
// (a+b)² = a² + 2ab + b²
// (a-b)² = a² - 2ab + b²

// 平方差
// a² - b² = (a+b)(a-b)

// 十字相乘
// x² + (p+q)x + pq = (x+p)(x+q)
```

---

## 2. 一元二次方程

```cpp
// ax² + bx + c = 0
// Δ = b² - 4ac
// x = (-b ± √Δ) / 2a

double a = 1, b = -5, c = 6;
double delta = b*b - 4*a*c;
double x1 = (-b + sqrt(delta)) / (2*a);
double x2 = (-b - sqrt(delta)) / (2*a);
```

---

## 3. 不等式

```cpp
// x² - 5x + 6 > 0
// (x-2)(x-3) > 0
// 解：x < 2 或 x > 3
```

---

## 本章小结

1. 完全平方、平方差、十字相乘法要熟练
2. 求根公式：Δ = b²-4ac
3. 竞赛中的数学题往往需要代数变形
"""),

    ("初中几何", "middle-school-geometry", "math", 1, 84,
"""# 初中几何

## 本章简介
复习初中几何基础。

---

## 1. 三角形

- **内角和**：180°
- **面积**：S = 底×高÷2
- **海伦公式**：S = √[p(p-a)(p-b)(p-c)]，p=(a+b+c)/2

---

## 2. 矩形与圆

```cpp
// 矩形面积 = 长 × 宽
// 圆面积 = πr²，周长 = 2πr

const double PI = acos(-1);
double area = PI * r * r;
double circumference = 2 * PI * r;
```

---

## 3. 勾股定理

```
a² + b² = c²（直角三角形）
```

---

## 本章小结

1. 三角形面积：底×高÷2，或海伦公式
2. 圆：πr²，2πr
3. 竞赛中常把几何问题转化为代数计算
"""),

    # ============================================================
    # 五.3 初等数论
    # ============================================================

    ("取整与模运算", "floor-mod", "math", 3, 85,
"""# 取整与模运算

## 本章简介
学习取整运算和模运算的性质。

---

## 1. 取整运算

```cpp
#include <cmath>
cout << floor(3.7) << endl;   // 3（向下取整）
cout << ceil(3.2) << endl;  // 4（向上取整）
cout << round(3.5) << endl;  // 4（四舍五入）
cout << trunc(3.9) << endl;  // 3（截断取整）
```

---

## 2. 模运算

```cpp
cout << 17 % 5 << endl;    // 2
cout << (-7 % 3) << endl; // -1（符号与被除数一致）

// 模运算性质
// (a + b) % mod = (a%mod + b%mod) % mod
// (a * b) % mod = (a%mod) * (b%mod) % mod
```

---

## 3. 应用：循环数组

```cpp
int next = (i + 1) % n;  // 循环右移
int prev = (i - 1 + n) % n;  // 循环左移
```

---

## 本章小结

1. `floor`向下，`ceil`向上，`round`四舍五入
2. 模运算常用于周期问题和取余判定
3. `(a+b)%mod = (a%mod+b%mod)%mod`可防溢出
"""),

    ("整数唯一分解定理", "unique-factorization", "math", 3, 86,
"""# 整数唯一分解定理

## 本章简介
理解唯一分解定理并实现分解质因数。

---

## 1. 定理

任何大于1的整数都可以唯一分解为质数的乘积：

```
n = p₁^a₁ × p₂^a₂ × ... × pk^ak
```

---

## 2. 分解质因数

```cpp
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

## 3. 求约数个数

若 n = p₁^a₁ × ... × pk^ak，则：

```
约数个数 = (a₁+1)(a₂+1)...(ak+1)
```

---

## 本章小结

1. 唯一分解：每个数可分解为质数乘积
2. 分解质因数：试除到√n
3. 约数个数公式：∏(aᵢ+1)
"""),

    ("欧几里得算法", "euclidean-algorithm", "math", 3, 87,
"""# 欧几里得算法

## 本章简介
学习求最大公约数的辗转相除法和扩展欧几里得算法。

---

## 1. 最大公约数（GCD）

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
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

## 3. 扩展欧几里得

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

1. `gcd(a,b)=gcd(b,a%b)`，O(log min(a,b))
2. `lcm(a,b) = a/gcd(a,b)×b`
3. 扩展欧几里得：求逆元，解同余方程
"""),

    ("埃氏筛与线性筛", "sieve-eratosthenes", "math", 4, 88,
"""# 埃氏筛与线性筛

## 本章简介
学习两种高效求质数的方法。

---

## 1. 埃氏筛

```cpp
vector<int> sieve(int n) {
    vector<bool> isPrime(n+1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i*i <= n; i++)
        if (isPrime[i])
            for (int j = i*i; j <= n; j += i)
                isPrime[j] = false;
    vector<int> primes;
    for (int i = 2; i <= n; i++)
        if (isPrime[i]) primes.push_back(i);
    return primes;
}
```

---

## 2. 线性筛

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

---

## 本章小结

1. 埃氏筛：O(n log log n)，从i²开始标记
2. 线性筛：O(n)，每个合数只被最小质因子筛一次
3. 求1~n所有质数用筛法，比逐个判定快
"""),

    # ============================================================
    # 五.4 离散与组合数学
    # ============================================================

    ("集合", "set-theory", "math", 2, 89,
"""# 集合

## 本章简介
理解集合的概念和C++中的实现。

---

## 1. 集合的概念

集合是确定的对象的全体，用大括号表示：

```cpp
{1, 2, 3, 4, 5}
{a, b, c}
```

---

## 2. C++ set

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

    cout << s.count(3) << endl;  // 1（存在）
    cout << s.count(2) << endl;  // 0（不存在）

    return 0;
}
```

---

## 3. 集合运算

| 运算 | 说明 |
|------|------|
| 并集 | 所有元素的集合 |
| 交集 | 共同元素的集合 |
| 差集 | 属于A不属于B的元素 |

---

## 本章小结

1. 集合：无序不重复的元素集合
2. C++的`set`自动排序，支持插入、查找
3. 集合运算是组合数学的基础
"""),

    ("加法原理与乘法原理", "addition-multiplication", "math", 2, 90,
"""# 加法原理与乘法原理

## 本章简介
计数问题的基础。

---

## 1. 加法原理

完成一件事有**n类**方法，第i类有mᵢ种：

```
总方法数 = m₁ + m₂ + ... + mₙ
```

**例**：A→B：汽车3班，火车2班，飞机1班，共3+2+1=6种。

---

## 2. 乘法原理

完成一件事需要**n步**，第i步有mᵢ种：

```
总方法数 = m₁ × m₂ × ... × mₙ
```

**例**：上衣4件，裤子3条：4×3=12种搭配。

---

## 3. 综合应用

**例**：密码要求：首位是字母（26种），末位是数字（10种），中间3位任选（36³种）。

```
总数 = 26 × 36³ × 10
```

---

## 本章小结

1. 加法原理：**分类**相加（每类方法都能独立完成）
2. 乘法原理：**分步**相乘（每步缺一不可）
3. 竞赛中常结合排列组合一起使用
"""),

    ("排列与组合", "permutations-combinations", "math", 4, 91,
"""# 排列与组合

## 本章简介
学习排列数和组合数的计算。

---

## 1. 排列数

从n个不同元素中取m个排成一排：

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

从n个不同元素中取m个，不考虑顺序：

```
C(n,m) = n! / (m! × (n-m)!)
```

---

## 3. 杨辉三角递推

```cpp
long long C[101][101];
for (int i = 0; i <= 100; i++) {
    C[i][0] = C[i][i] = 1;
    for (int j = 1; j < i; j++)
        C[i][j] = C[i-1][j] + C[i-1][j-1];
}
```

---

## 本章小结

1. 排列A(n,m)：考虑顺序
2. 组合C(n,m)：不考虑顺序
3. 杨辉三角：C(n,m)=C(n-1,m)+C(n-1,m-1)
"""),

    ("杨辉三角", "yanghui-triangle", "math", 4, 92,
"""# 杨辉三角

## 本章简介
学习杨辉三角的性质和应用。

---

## 1. 基本性质

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
```

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
    for (int j = 2; j < i; j++)
        a[i][j] = a[i-1][j-1] + a[i-1][j];
}
```

---

## 3. 路径计数应用

从(0,0)到(m,n)，只能向右或向下：

```
路径数 = C(m+n, n)
```

---

## 本章小结

1. 杨辉三角第n行第k个数 = C(n-1, k-1)
2. 构建：两端为1，中间 = 肩上两数之和
3. 组合数学的基础工具
"""),

    # ============================================================
    # 五.5 其他
    # ============================================================

    ("ASCII码", "ascii-codes", "math", 2, 93,
"""# ASCII码

## 本章简介
学习ASCII编码及其在C++中的应用。

---

## 1. ASCII码表（常用）

| 字符 | ASCII |
|------|-------|
| `'0'`~`'9'` | 48~57 |
| `'A'`~`'Z'` | 65~90 |
| `'a'`~`'z'` | 97~122 |

---

## 2. 字符运算

```cpp
char c = 'A';
cout << (int)c << endl;       // 65
cout << (char)(c + 1) << endl; // 'B'
cout << (char)('a' - 32) << endl; // 'A'

// 大小写转换
cout << (char)('a' + 32) << endl; // 'A'
cout << (char)('A' - 32) << endl; // 'a'
```

---

## 3. 字符分类函数

```cpp
#include <cctype>
isalpha('A');   // 1（字母）
isdigit('5');   // 1（数字）
isupper('A');   // 1（大写）
islower('a');   // 1（小写）
toupper('a');   // 'A'
tolower('A');   // 'a'
```

---

## 本章小结

1. 'A'=65, 'a'=97, '0'=48
2. 大写转小写：+32；小写转大写：-32
3. `<cctype>`提供字符分类和转换函数
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
        print(f"✅ [{cat_slug}] d{difficulty} {order:02d} - {title}")

    db.commit()
    print(f"\n共插入 {count} 个章节")
    db.close()


if __name__ == "__main__":
    main()
