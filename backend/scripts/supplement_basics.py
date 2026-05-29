#!/usr/bin/env python3
"""补充第一分类"基础知识与编程环境"12章的详细内容"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.category import Category

UPDATES = {

    "computer-components": """# 计算机基本构成

## 本章简介
本章介绍计算机的五大硬件组成、各自作用，以及冯·诺依曼体系结构。这是理解计算机工作原理的入门课。

---

## 1. 计算机硬件五大组成部分

### CPU（中央处理器）

- **全称**：Central Processing Unit（中央处理器）
- **地位**：计算机的大脑，负责执行所有计算和指令
- **主要指标**：主频（GHz）、核心数、缓存大小
- **常见品牌**：Intel（酷睿系列）、AMD（锐龙系列）、Apple（M系列芯片）

### 内存（RAM）

- **全称**：Random Access Memory（随机存取存储器）
- **作用**：临时存储正在运行的程序和数据
- **特点**：读写速度快，断电后数据丢失（易失性）
- **容量**：常见 8GB、16GB、32GB
- **速度**：DDR4 → DDR5（越新越快）

### 硬盘（Storage）

- **作用**：永久存储数据，断电后数据保留
- **类型对比**：

| 类型 | 速度 | 价格 | 容量 |
|------|------|------|------|
| HDD（机械硬盘） | 较慢（~100MB/s） | 便宜 | 大（TB级） |
| SSD（固态硬盘） | 快（~500MB/s+） | 较贵 | 适中（512GB~2TB） |
| NVMe SSD | 极快（~3000MB/s+） | 更贵 | 适中 |

### 输入设备（Input）

向计算机输入信息的设备：

| 设备 | 说明 |
|------|------|
| 键盘 | 文字和命令输入 |
| 鼠标 | 指向和点击操作 |
| 扫描仪 | 纸质文档数字化 |
| 麦克风 | 声音输入 |
| 触摸屏 | 直接触控输入 |

### 输出设备（Output）

将计算结果呈现给用户的设备：

| 设备 | 说明 |
|------|------|
| 显示器 | 图像和文字显示 |
| 打印机 | 纸质输出 |
| 扬声器 | 声音输出 |
| 投影仪 | 大画面显示 |

---

## 2. 冯·诺依曼体系

1946年，冯·诺依曼提出了现代计算机的基本架构：

```
程序和数据 → 存储器 → CPU（运算器+控制器） → 输出设备
     ↑                                           ↓
     ←←←←←←←←←← 控制信号 ←←←←←←←←←←←←←←←←←←←
```

**核心思想**：
- 程序和数据都存储在内存中
- CPU从内存读取指令执行
- 指令和数据以二进制形式存储

---

## 3. 程序运行全过程

```cpp
// 源代码
#include <iostream>
int main() {
    std::cout << "Hello";
    return 0;
}
```

```
源代码.cpp
    ↓ 编译（Compiler）
目标代码.obj
    ↓ 链接（Linker）
可执行文件.exe
    ↓ 加载（Loader）
内存中的程序
    ↓ CPU执行
输出结果
```

---

## 4. 常见存储单位换算

| 单位 | 全称 | 换算 |
|------|------|------|
| bit（位） | binary digit | 最小的数据单位，0或1 |
| Byte（字节） | Byte | 1 Byte = 8 bit |
| KB（千字节） | Kilobyte | 1 KB = 1024 Byte |
| MB（兆字节） | Megabyte | 1 MB = 1024 KB |
| GB（吉字节） | Gigabyte | 1 GB = 1024 MB |
| TB（太字节） | Terabyte | 1 TB = 1024 GB |

---

## 5. 数据的二进制表示

计算机内部所有数据都用二进制（0和1）表示：

```
十进制 42 → 二进制 101010
十进制 255 → 二进制 11111111（1字节最大值）
```

---

## 本章小结

1. 计算机五大硬件：CPU（计算）、内存（临时存储）、硬盘（永久存储）、输入设备、输出设备
2. CPU是计算机的大脑，内存是CPU的工作台，硬盘是仓库
3. 冯·诺依曼体系：程序和数据存在内存，CPU从内存取指令执行
4. 1字节 = 8位，存储单位以1024为进制（2¹⁰）
""",

    "os-basics": """# Windows与Linux基本操作

## 本章简介
Windows和Linux是最常用的两类操作系统。本章介绍它们的基本概念和常用操作命令。

---

## 1. 操作系统概述

**操作系统（OS）**是管理计算机硬件和软件资源的系统软件，是用户与计算机之间的桥梁。

常见操作系统：
- **桌面端**：Windows（最普及）、macOS、Linux
- **移动端**：Android、iOS
- **服务器端**：Linux（最主流，占90%+服务器市场）

---

## 2. Windows基本操作

### 文件管理

| 操作 | 图形界面 | 命令行 |
|------|---------|--------|
| 新建文件夹 | 右键 → 新建 → 文件夹 | `mkdir 文件夹名` |
| 复制文件 | Ctrl+C / Ctrl+V | `copy 源 目标` |
| 移动文件 | 拖动 或 Ctrl+X+V | `move 源 目标` |
| 删除文件 | Delete / Shift+Delete | `del 文件名` / `rd 文件夹名` |
| 重命名 | 右键 → 重命名 或 F2 | `ren 原名 新名` |

### 常用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl + C` | 复制 |
| `Ctrl + V` | 粘贴 |
| `Ctrl + X` | 剪切 |
| `Ctrl + Z` | 撤销 |
| `Ctrl + S` | 保存 |
| `Ctrl + A` | 全选 |
| `Ctrl + F` | 查找 |
| `Alt + Tab` | 切换窗口 |
| `Win + D` | 显示桌面 |
| `Win + E` | 打开文件资源管理器 |
| `Ctrl + Shift + Esc` | 打开任务管理器 |

### Windows命令行（CMD）

1. 打开方式：Win+R → 输入`cmd` → 回车

2. 常用命令：

```bash
# 切换目录
cd Desktop              # 进入桌面
cd ..                  # 返回上级目录
cd C:\\Users           # 进入指定路径

# 查看当前目录内容
dir

# 创建文件夹
mkdir myproject

# 删除文件
del file.txt

# 清屏
cls

# 查看IP配置
ipconfig

# ping测试网络
ping www.luogu.com
```

---

## 3. Linux基本概念

Linux是一种开源操作系统内核，基于Unix设计。

### 目录结构

```
/                   # 根目录
├── home/          # 用户主目录
├── usr/           # 系统程序
├── etc/           # 配置文件
├── var/           # 变量文件（日志等）
├── bin/           # 可执行程序
└── root/          # 超级用户主目录
```

### 常用命令

| 命令 | 全称 | 功能 |
|------|------|------|
| `ls` | list | 列出文件 |
| `cd` | change directory | 切换目录 |
| `pwd` | print working directory | 显示当前目录 |
| `mkdir` | make directory | 创建目录 |
| `rm` | remove | 删除文件/目录 |
| `cp` | copy | 复制文件 |
| `mv` | move | 移动/重命名 |
| `cat` | concatenate | 查看文件内容 |
| `grep` | global regular expression print | 搜索文本 |

```bash
# 基本使用
ls -la              # 列出所有文件（含隐藏文件）
cd /home/user       # 切换到指定目录
pwd                 # 显示当前路径

# 文件操作
mkdir project       # 创建文件夹
rm -rf project      # 强制删除文件夹
cp a.txt b.txt     # 复制文件
mv old.txt new.txt  # 重命名/移动

# 查看文件
cat file.txt        # 一次性显示文件所有内容
head -n 20 file.txt # 显示前20行
tail -n 50 file.txt # 显示后50行
```

---

## 4. 文件权限（Linux）

```bash
ls -l
# 输出示例：
# -rw-r--r-- 1 user group 4096 Apr 24 10:00 file.txt

# drwxr-xr-x
# d: 目录  -: 文件
# rwx: 所有者权限（读+写+执行）
# r-x: 组权限（读+执行）
# r-x: 其他用户权限（读+执行）
```

修改权限：
```bash
chmod 755 script.sh   # 数字方式
chmod +x script.sh    # 添加执行权限
```

---

## 5. 竞赛环境选择

| 场景 | 推荐系统 | 说明 |
|------|---------|------|
| CSP-J初赛 | Windows | 笔试为主 |
| CSP-J复赛 | Windows（Dev-C++） | 国内主流 |
| 进阶训练 | Linux（Ubuntu） | 更接近竞赛环境 |
| macOS | 可以用，但部分竞赛环境不兼容 | 需注意 |

---

## 本章小结

1. 操作系统是用户与计算机硬件之间的桥梁
2. Windows：图形界面+CMD命令行，常用Ctrl+C/V快捷键
3. Linux：命令行为主，必备命令：ls、cd、mkdir、rm、cp、mv
4. 竞赛推荐Windows+Dev-C++环境
""",

    "network-basics": """# 计算机网络与Internet

## 本章简介
了解计算机网络的基本概念、Internet原理，以及竞赛学习常用的在线平台。

---

## 1. 网络基本概念

### IP地址

IP地址是计算机在网络中的唯一标识：

```
IPv4地址示例：192.168.1.100
IPv6地址示例：2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

- **IPv4**：4段数字，每段0-255，共约42亿个地址
- **IPv6**：新一代协议，地址近乎无限

### 域名（Domain Name）

域名是IP地址的易记别名：

| 域名 | 实际用途 |
|------|---------|
| www.google.com | Google搜索 |
| www.baidu.com | 百度搜索 |
| www.luogu.com | 洛谷（信息学竞赛） |
| oi-wiki.org | OI Wiki知识百科 |

**DNS**（域名系统）负责将域名转换为IP地址。

### 端口号

一台计算机上运行多个网络服务，端口号用于区分：

| 端口 | 服务 |
|------|------|
| 80 | HTTP网页 |
| 443 | HTTPS（加密网页） |
| 22 | SSH远程登录 |
| 3306 | MySQL数据库 |
| 8000 | 本地Web服务常用端口 |

---

## 2. HTTP与HTTPS

- **HTTP**（HyperText Transfer Protocol）：超文本传输协议，用于浏览器访问网页
- **HTTPS**：HTTP的安全版本，数据加密传输

```
# HTTP请求流程
浏览器 → 发送HTTP请求 → 服务器
         ↓
    服务器处理请求
         ↓
浏览器 ← 返回HTTP响应 ← 服务器
```

---

## 3. 竞赛学习常用网站

### 洛谷（luogu.com）

**国内最权威的信息学竞赛学习平台**

| 功能 | 说明 |
|------|------|
| 在线评测 | 提交代码，机器评测 |
| 题库 | 涵盖CSP-J/S、NOIP各级题目 |
| 题解 | 众多选手分享的解题思路 |
| 比赛 | 定期举办在线比赛 |
| 社区 | 交流学习经验 |

### OI Wiki（oi-wiki.org）

**信息学竞赛知识百科**

- 系统梳理算法和数据结构知识
- 配有代码示例
- 持续更新维护
- 完全免费开源

### Codeforces

**国际顶级竞赛平台**

- 定期举办全球在线比赛（每周1-2场）
- 题目质量高，英文题目
- 全球排名系统
- 适合进阶训练

### AtCoder

**日本竞赛平台**

- 题目质量高，风格独特
- ABC（AtCoder Beginner Contest）适合入门
- 从易到难体系完整

---

## 4. 如何使用洛谷

1. **注册账号**：访问 luogu.com 注册
2. **搜索题目**：在题库中搜索关键词
3. **提交代码**：选择语言，粘贴代码，提交
4. **查看结果**：

| 结果 | 含义 |
|------|------|
| AC（Accepted） | ✅ 正确，通过 |
| WA（Wrong Answer） | ❌ 答案错误 |
| TLE（Time Limit Exceeded） | ⏱️ 超时 |
| MLE（Memory Limit Exceeded） | 💾 超内存 |
| RE（Runtime Error） | 💥 运行时错误 |
| CE（Compile Error） | 🔴 编译错误 |

---

## 5. 搜索引擎的使用

学会用搜索引擎解决编程问题：

```bash
# 好的搜索方式
"Dev-C++ 编译错误" site:luogu.com
"C++ 排序算法" oi-wiki.org
"CSP-J 2023 真题"

# 优先看官方文档和权威教程
```

---

## 本章小结

1. IP地址是计算机在网络中的唯一标识
2. DNS将域名解析为IP地址
3. HTTP/HTTPS是网页传输协议
4. 洛谷是国内CSP-J/S学习首选平台
5. OI Wiki是算法知识百科
""",

    "computer-history": """# 计算机历史与用途

## 本章简介
了解计算机的发展简史、主要应用领域，以及信息学竞赛在其中的位置。

---

## 1. 计算机发展简史

### 第一代（1940s-1950s）：电子管时代

| 事件 | 年份 |
|------|------|
| ENIAC诞生（第一台电子计算机） | 1946 |
| 冯·诺依曼体系提出 | 1946 |
| UNIVAC（第一台商用计算机） | 1951 |

**特点**：体积巨大（ENIAC占地170平方米），耗电惊人，速度慢。

### 第二代（1960s）：晶体管时代

- 晶体管取代电子管
- 计算机体积缩小，可靠性提高
- 成本下降，开始商业化应用

### 第三代（1970s）：集成电路时代

- 小规模集成电路（IC）
- 出现了操作系统（OS）
- 个人计算机萌芽

### 第四代（1980s-今）：大规模集成电路时代

| 时代 | 特点 |
|------|------|
| 1980s | IBM PC诞生，个人计算机普及 |
| 1990s | Windows操作系统，互联网兴起 |
| 2000s | 多核CPU，笔记本电脑普及 |
| 2010s | 移动互联网，云计算 |
| 2020s | AI爆发，量子计算研究 |

---

## 2. 计算机的应用领域

### 科学计算
- 天气预报（超级计算机模拟大气运动）
- 基因研究（DNA序列分析）
- 物理模拟（粒子对撞实验）

### 人工智能
- 机器学习：让计算机从数据中学习
- 深度学习：神经网络在图像/语音/自然语言中的应用
- 大模型（LLM）：如ChatGPT、DeepSeek

### 信息学竞赛

**信息学竞赛**是利用计算机解决算法问题的比赛：

```
学习路径：
编程入门 → 算法基础 → 数据结构 → 竞赛训练
   ↓           ↓           ↓           ↓
 语法学习    枚举/模拟    栈/队列/树   刷题+比赛
```

### 竞赛体系（从小到大）

| 竞赛 | 说明 |
|------|------|
| CSP-J | 非专业级软件能力认证-入门级 |
| CSP-S | 非专业级软件能力认证-提高级 |
| NOIP | 全国青少年信息学奥林匹克联赛（省级） |
| NOI | 全国青少年信息学奥林匹克（国赛） |
| IOI | 国际信息学奥林匹克（全球） |

---

## 3. 为什么学信息学

1. **锻炼逻辑思维能力**：解决问题能力的核心
2. **升学优势**：CSP-J/S获奖可助力升学
3. **培养耐心**：调试程序的过程培养耐心
4. **未来竞争力**：编程能力是未来工作的加分项
5. **有趣**：做出成果的成就感很强

---

## 4. 信息学竞赛选手的一天

```cpp
// 学习日程示例
6:00 起床
7:30 学校早读
8:00-17:30 学校上课
18:00-22:00 信息学训练
  ├── 复习当天知识点
  ├── 刷题练习
  └── 订正错题
22:30 休息
```

---

## 本章小结

1. 计算机从1946年ENIAC发展到今天，经历了四代
2. 冯·诺依曼体系是现代计算机的理论基础
3. 信息学竞赛体系：CSP-J/S → NOIP → NOI → IOI
4. 学习编程不仅是为了竞赛，更能培养解决问题的能力
""",

    "noi-history": """# NOI及相关活动历史

## 本章简介
了解NOI（中国全国青少年信息学奥林匹克）系列竞赛的由来和发展。

---

## 1. CCF简介

**CCF**（中国计算机学会，China Computer Federation）成立于1962年，是国内计算机领域最具影响力的学术组织之一。

**CCF主办的重要竞赛**：
- CSP-J/S（非专业级软件能力认证）
- NOIP（全国青少年信息学奥林匹克联赛）
- NOI（全国青少年信息学奥林匹克）
- CTA（大学生程序设计竞赛）

---

## 2. NOI系列竞赛体系

### 入门级：CSP-J

```
CSP-J/S → NOIP → 省队选拔 → NOI → NOI金牌 → IOI
（入门）  （省级）（国家）  （国家）  （国际）
```

| 竞赛 | 全称 | 参赛资格 | 时间 |
|------|------|---------|------|
| CSP-J | 非专业级软件能力认证-入门级 | 初中+高中 | 每年10月 |
| CSP-S | 非专业级软件能力认证-提高级 | 初中+高中 | 每年10月 |
| NOIP | 全国青少年信息学奥林匹克联赛 | 高中生（部分省初中） | 每年11-12月 |
| NOI | 全国青少年信息学奥林匹克 | 各省省队 | 每年7月 |
| IOI | 国际信息学奥林匹克 | 各国家代表队 | 每年7-8月 |

---

## 3. NOI历史

| 年份 | 事件 |
|------|------|
| 1984 | 第一届全国青少年计算机竞赛在北京举行 |
| 1989 | 首届NOI举办 |
| 1995 | CCF正式接管NOI |
| 2000年至今 | NOI发展为国内最高级别中学生信息学竞赛 |

---

## 4. 著名选手介绍

### 中国IOI金牌选手（部分）

| 年份 | 选手 | 获奖情况 |
|------|------|---------|
| 2024 | 虞皓翔（浙江） | IOI金牌 |
| 2023 | 许庭强（浙江） | IOI金牌 |
| 2022 | 刘梓非（江苏） | IOI金牌 |

### 他们的共同特点

- **数学基础扎实**：竞赛核心能力
- **大量刷题训练**：积累经验
- **善于总结归纳**：形成自己的知识体系
- **心理素质好**：比赛中能稳定发挥

---

## 5. 如何科学备赛

### 阶段一：入门（6个月~1年）
- 学习C++语法
- 掌握基础算法（枚举、模拟、排序）
- 刷CSP-J真题

### 阶段二：进阶（1~2年）
- 学习数据结构（栈、队列、树、图）
- 深入算法（DFS/BFS、贪心、DP）
- 参加各类在线比赛

### 阶段三：冲刺（比赛前）
- 专项训练弱项
- 做真题模拟
- 调整心态

---

## 本章小结

1. CCF（中国计算机学会）主办NOI系列竞赛
2. 竞赛体系：CSP-J/S → NOIP → NOI → IOI
3. CSP-J/S是第一轮门槛，NOIP是省级联赛
4. 科学的备赛规划比盲目刷题更重要
""",

    "noi-rules": """# NOI及相关活动规则

## 本章简介
详细了解CSP-J/S和NOI系列竞赛的比赛规则、评分标准和应试技巧。

---

## 1. CSP-J/S比赛规则

### 比赛时间与形式

| 项目 | CSP-J（入门级） | CSP-S（提高级） |
|------|----------------|----------------|
| 第一轮（初赛） | 笔试，2.5小时 | 笔试，2.5小时 |
| 第二轮（复赛） | 上机编程，3.5小时 | 上机编程，4小时 |

### 初赛（笔试）

- **题型**：选择题 + 阅读程序题 + 完善程序题
- **内容**：计算机基础知识、算法常识、程序理解
- **分值**：满分100分
- **晋级**：按成绩排名，比例由CCF统一规定

### 复赛（上机编程）

- **语言**：C++（推荐）、C、Pascal
- **题目数量**：4道题（从易到难）
- **评测方式**：机器评测，10~20个测试点/题
- **评分**：按测试点给分，部分分解法也能得分

---

## 2. NOIP比赛规则

### 赛制

| 项目 | 说明 |
|------|------|
| 参赛资格 | 高中生（部分省初中生可参加） |
| 比赛时间 | 每年11-12月 |
| 比赛时长 | 4小时，4道题 |
| 评测方式 | 机器评测 |

### 晋级规则

```
NOIP一等奖（前5%~10%）
    ↓
省队选拔（前3~5名）
    ↓
NOI（全国决赛）
```

---

## 3. 竞赛评分标准

### 竞赛常用评分方式

| 方式 | 说明 |
|------|------|
| **ACM/ICPC制** | 每题通过得1分，按做题数量排名 |
| **IOI制** | 每题多个测试点，按通过比例给分 |

CSP-J/S采用**IOI制**，按测试点给分。

### 测试点分布

一道题通常有10~20个测试点：
- 前1~3个：大数据，专为部分分解法设计（20~30分）
- 中间测试点：中等规模（40~50分）
- 最后1~3个：大规模数据，需高效算法（20~30分）

---

## 4. 竞赛应试技巧

### 读题策略

1. **先读所有题目**：对4道题的难度有个整体判断
2. **预估性价比**：哪个题容易拿分先做哪个
3. **注意数据范围**：从数据范围反推算法需求

### 时间分配

```
4小时 = 240分钟
├── 读题 + 确定顺序：10分钟
├── 第一题（简单）：30~40分钟
├── 第二题（中等）：40~60分钟
├── 第三题（较难）：50~70分钟
└── 第四题（最难）：留40~60分钟

# 提示：不要死磕一道题！
```

### 代码编写规范

```cpp
// ✅ 好的习惯
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // 读入
    int n; cin >> n;
    // 核心算法
    // ...
    return 0;
}

// ❌ 不好的习惯
#include <iostream.h>  // 老式写法
void main() {           // 应该用int main
    // 没有ios加速
    // ...
}
```

---

## 5. 常见错误避免

1. **文件操作错误**：复赛要用文件读入输出（freopen或fstream）
2. **数组越界**：数组开大一点（n+5或2n）
3. **数据类型错误**：超过21亿用long long
4. **死循环**：调试时记得程序能正常结束
5. **freopen忘记删**：本地测试用文件，提交时也要用

---

## 本章小结

1. CSP-J/S分初赛（笔试）和复赛（上机编程）
2. 复赛采用机器评测，按测试点给分
3. 竞赛策略：先读所有题，确定性价比最高的先做
4. 注意文件读入输出格式！复赛必须读写文件
""",

    "bit-byte-word": """# 位、字节与字

## 本章简介
理解计算机底层的数据表示单位，这是理解计算机存储和计算原理的基础。

---

## 1. 位（Bit）

**位（bit）**是计算机中表示数据的最小单位，只能是0或1。

```
二进制数字系统：0 和 1
```

**为什么计算机用二进制？**
- 物理上容易实现（电路的开/关、电压的高/低）
- 运算规则简单：0+0=0，0+1=1，1+1=0（进位1）
- 抗干扰能力强

---

## 2. 字节（Byte）

**字节（Byte）**是计算机存储的基本单位：

```
1 Byte = 8 bit
```

一个字节可以表示256个不同的值（0~255，或-128~127）。

### 字节的常见用途

| 存储内容 | 占用字节数 | 示例 |
|---------|-----------|------|
| 英文字符 | 1字节 | 'A' = 65 |
| 汉字 | 2~4字节 | "你好" UTF-8编码占6字节 |
| 整数（int） | 4字节 | ~±21亿 |
| 长整数（long long） | 8字节 | ~±9×10¹⁸ |
| 单精度浮点（float） | 4字节 | 约6位有效数字 |
| 双精度浮点（double） | 8字节 | 约15位有效数字 |

---

## 3. 字（Word）

**字（Word）**是CPU一次处理的数据单位：

| 系统类型 | 字长 | 说明 |
|---------|------|------|
| 32位系统 | 4字节 | CPU一次处理32位数据 |
| 64位系统 | 8字节 | CPU一次处理64位数据 |

**注意**：我们常说的"32位系统""64位系统"指的就是CPU的字长。

---

## 4. 存储单位换算

```
1 KB = 1024 Byte  = 2¹⁰ Byte
1 MB = 1024 KB    = 2²⁰ Byte  ≈ 100万字节
1 GB = 1024 MB    = 2³⁰ Byte  ≈ 10亿字节
1 TB = 1024 GB    = 2⁴⁰ Byte  ≈ 1万亿字节
```

> **为什么是1024而不是1000？**
> 因为计算机使用二进制，1024 = 2¹⁰，是2的整数次幂。

---

## 5. 二进制的直观理解

### 1位能表示多少种状态？
```
1 bit = 2种（0或1）
2 bit = 4种（00, 01, 10, 11）
3 bit = 8种
8 bit（1 Byte） = 256种
```

### 二进制与十进制对应

| 二进制 | 十进制 |
|--------|--------|
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |
| ... | ... |
| 1111 | 15 |

### 常见二进制值

| 十进制 | 二进制 |
|--------|--------|
| 1 | 00000001 |
| 7 | 00000111 |
| 15 | 00001111 |
| 31 | 00011111 |
| 63 | 00111111 |
| 127 | 01111111 |
| 255 | 11111111 |

---

## 6. C++中的数据类型大小

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "char:       " << sizeof(char)       << " Byte" << endl;   // 1
    cout << "short:      " << sizeof(short)      << " Byte" << endl;   // 2
    cout << "int:        " << sizeof(int)         << " Byte" << endl;   // 4
    cout << "long long:  " << sizeof(long long)  << " Byte" << endl;   // 8
    cout << "float:      " << sizeof(float)       << " Byte" << endl;  // 4
    cout << "double:     " << sizeof(double)      << " Byte" << endl;  // 8
    cout << "int*:       " << sizeof(int*)       << " Byte" << endl;  // 8（64位系统指针为8字节）
    return 0;
}
```

---

## 本章小结

1. **位（bit）**：最小单位，0或1
2. **字节（Byte）**：存储基本单位，1 Byte = 8 bit
3. **字（Word）**：CPU一次处理的数据单位，32位/64位系统
4. 存储单位换算：1 KB = 1024 Byte，1 MB = 1024 KB
5. int占4字节约±21亿，long long占8字节约±9×10¹⁸
""",

    "pl-basics": """# 程序设计语言基础

## 本章简介
了解程序设计语言的分类、C++的编译运行过程，以及竞赛中常用的C++标准。

---

## 1. 程序设计语言分类

### 按执行方式分类

| 类型 | 特点 | 代表语言 |
|------|------|---------|
| **编译型** | 先编译后运行，运行速度快 | **C++**、C、Rust |
| **解释型** | 逐行解释执行，无需编译 | Python、JavaScript |
| **混合型** | 编译成中间码，解释执行 | Java、C# |

**C++是编译型语言**，这是它成为竞赛首选的原因之一：**运行速度快**。

### 按编程范式分类

| 范式 | 特点 | 代表语言 |
|------|------|---------|
| 面向过程 | 以过程/函数为中心 | C、Pascal |
| 面向对象 | 以对象为中心 | C++、Java、Python |
| 函数式 | 数学函数风格 | Haskell、Lisp |
| 逻辑式 | 规则推理 | Prolog |

C++支持**多范式**：面向过程 + 面向对象 + 泛型编程。

---

## 2. C++编译运行过程

```
源代码.cpp
    │
    ▼ 预处理（Preprocess）
预处理后的代码.i
    │
    ▼ 编译（Compile）
汇编代码.s
    │
    ▼ 汇编（Assemble）
目标代码.o（机器码）
    │
    ▼ 链接（Link）
可执行文件.exe
    │
    ▼ 加载（Load）
内存 → CPU执行
```

### 各阶段的作用

1. **预处理**：展开头文件（#include）、处理宏（#define）
2. **编译**：检查语法，生成汇编代码
3. **汇编**：将汇编代码转成机器码（.o文件）
4. **链接**：将多个.o文件合并成可执行文件，连接库函数

---

## 3. 第一个C++程序详解

```cpp
#include <iostream>        // ① 引入输入输出库
using namespace std;       // ② 使用标准名字空间

int main() {               // ③ 主函数（程序入口）
    cout << "Hello, World!" << endl;  // ④ 输出
    return 0;               // ⑤ 返回0表示正常结束
}
```

### 代码详解

| 代码 | 含义 |
|------|------|
| `#include <iostream>` | 告诉编译器要使用标准输入输出库 |
| `using namespace std;` | 允许直接写`cout`而不是`std::cout` |
| `int main()` | 定义主函数，返回int（整数）类型 |
| `cout <<` | 输出到屏幕 |
| `<< endl` | 换行（end line） |
| `return 0;` | 返回0表示程序正常结束 |

### 为什么是`int main`而不是`void main`？

- C++标准要求`main`必须返回`int`类型
- `return 0`返回给操作系统表示程序正常退出
- 竞赛中所有代码都应写成`int main() { ... return 0; }`

---

## 4. C++标准

| 标准 | 年份 | 特性 |
|------|------|------|
| C++98 | 1998 | 第一个ISO标准 |
| C++03 | 2003 | 修正版 |
| C++11 | 2011 | 重大更新：auto、范围for、lambda |
| C++14 | 2014 | 改进：泛型lambda |
| **C++17** | 2017 | 结构化绑定、if constexpr |
| **C++20** | 2020 | concepts、ranges、协程 |
| C++23 | 2023 | 最新标准 |

**竞赛推荐使用C++17**，稳定且功能丰富。

### g++指定标准

```bash
g++ -std=c++17 -o program source.cpp
```

---

## 5. 常用头文件一览

| 头文件 | 用途 |
|--------|------|
| `<iostream>` | 标准输入输出（cin、cout） |
| `<vector>` | 动态数组 |
| `<string>` | 字符串 |
| `<algorithm>` | 算法（sort、max、min） |
| `<cmath>` | 数学函数 |
| `<stack>` | 栈 |
| `<queue>` | 队列 |
| `<map>` | 映射 |
| `<set>` | 集合 |
| `<bits/stdc++.h>` | 万能头文件（竞赛常用，但非标准） |

### 万能头文件

```cpp
#include <bits/stdc++.h>  // 包含几乎所有常用STL
```

> 注意：`<bits/stdc++.h>`不是C++标准的一部分，竞赛环境一般支持，但不推荐日常开发使用。

---

## 6. 竞赛代码模板

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 题目读入
    int n;
    cin >> n;

    // 算法实现
    // ...

    return 0;
}
```

---

## 本章小结

1. C++是编译型语言，运行速度快，是竞赛首选
2. 编译过程：预处理→编译→汇编→链接→可执行文件
3. `int main()`必须返回int，`return 0`表示正常结束
4. 推荐使用C++17标准
5. 竞赛代码模板：`ios::sync_with_stdio(false)`加速输入输出
""",

    "gui-file-ops": """# 图形界面与文件操作

## 本章简介
掌握Windows图形界面操作、文件路径概念，以及C++中的文件读写方法。

---

## 1. Windows图形界面操作

### 文件与文件夹操作

| 操作 | 鼠标方式 | 快捷键 |
|------|---------|--------|
| 新建文件夹 | 右键 → 新建 → 文件夹 | - |
| 重命名 | 右键 → 重命名 或 F2 | - |
| 复制 | Ctrl+C | - |
| 粘贴 | Ctrl+V | - |
| 剪切 | Ctrl+X | - |
| 全选 | - | Ctrl+A |
| 保存 | - | Ctrl+S |
| 撤销 | - | Ctrl+Z |

### 多选文件

- **不连续选择**：`Ctrl + 单击`每个要选的文件
- **连续选择**：单击第一个，然后`Shift + 单击`最后一个

### 资源管理器

打开资源管理器：`Win + E`

常用功能：
- 左侧导航栏快速切换目录
- 右上角搜索框搜索文件
- 地址栏直接输入路径

---

## 2. 文件路径

### 绝对路径与相对路径

**绝对路径**：从盘符开始的完整路径

```
Windows示例：
C:\\Users\\Admin\\Desktop\\test.cpp
D:\\Code\\project\\main.cpp

Linux/macOS示例：
/home/user/Desktop/test.cpp
/Users/admin/Desktop/test.cpp
```

**相对路径**：从当前目录出发的路径

```
.          # 当前目录
..         # 上级目录
./src      # 当前目录下的src文件夹
../output  # 上级目录下的output文件夹
```

### Windows路径分隔符注意

```cpp
// ❌ 错误
"C:\\Users\\Admin\\file.txt"  // 字符串中\需要转义

// ✅ 正确
"C:\\\\Users\\\\Admin\\\\file.txt"  // 双重反斜杠
// 或者直接用正斜杠
"C:/Users/Admin/file.txt"  // Windows也支持正斜杠！
```

---

## 3. C++文件操作

### 方法一：freopen重定向（竞赛最常用）

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    // 只需要在程序开头加这两行
    freopen("input.txt", "r", stdin);   // 从input.txt读入
    freopen("output.txt", "w", stdout); // 输出到output.txt

    int a, b;
    cin >> a >> b;          // 实际从input.txt读
    cout << a + b << endl;  // 实际输出到output.txt

    return 0;
}
```

### 方法二：fstream（更通用）

```cpp
#include <fstream>
using namespace std;

int main() {
    ifstream fin("input.txt");   // 打开输入文件
    ofstream fout("output.txt"); // 打开输出文件

    if (!fin) {
        cout << "文件打开失败" << endl;
        return 1;
    }

    int a, b;
    fin >> a >> b;           // 从文件读
    fout << a + b << endl;   // 写到文件

    fin.close();             // 关闭文件
    fout.close();

    return 0;
}
```

### 方法三：命令行参数（竞赛进阶用法）

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]) {
    // argc: 参数个数，argv[]: 参数列表
    if (argc >= 2) {
        freopen(argv[1], "r", stdin);   // 第一个参数是输入文件
    }
    if (argc >= 3) {
        freopen(argv[2], "w", stdout); // 第二个参数是输出文件
    }

    int n; cin >> n;
    cout << n * 2 << endl;
    return 0;
}
```

使用方法：
```bash
./a.out input.txt output.txt
```

---

## 4. 文件操作注意事项

| 注意事项 | 说明 |
|---------|------|
| 文件名大小写 | Windows不区分，Linux区分！注意一致性 |
| 文件路径 | 相对路径是相对于程序运行的目录，不是源文件目录 |
| 中文路径 | 尽量避免使用中文文件名 |
| 读写模式 | `"r"`只读，`"w"`写（会覆盖） |

---

## 5. 竞赛中的文件操作

### 复赛必须用文件读入！

很多同学本地测试用cin/cout没问题，但复赛要求读文件：

```cpp
// ✅ 推荐方式：在代码开头加判断，生产环境用文件
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
```

编译时加`-D LOCAL`用于本地测试，不加则用标准输入输出：
```bash
g++ -D LOCAL -o program source.cpp  # 本地测试
g++ -o program source.cpp           # 提交版本
```

---

## 本章小结

1. Windows文件操作：Ctrl+C/V复制粘贴，F2重命名
2. 相对路径`.`当前目录，`..`上级目录
3. 竞赛最常用`freopen`读写文件
4. 复赛必须读写文件，不要只依赖cin/cout
5. 注意Windows路径分隔符`\\`或直接用`/`
""",

    "dev-cpp": """# Dev-C++使用

## 本章简介
Dev-C++是Windows下最适合CSP-J竞赛的集成开发环境（IDE）。本章详细介绍其使用方法。

---

## 1. Dev-C++简介与安装

### 为什么要用Dev-C++？

- **免费开源**：完全免费，无需破解
- **体积小**：几十MB，安装快速
- **界面简洁**：适合初学者
- **竞赛兼容**：CSP-J/S官方推荐环境之一

### 安装步骤

1. 官网下载：https://www.bloodshed.net/（或搜索Dev-C++中文站）
2. 运行安装程序，一路下一步即可
3. 安装时选择中文语言
4. 选择GNU GCC编译器

---

## 2. 基本使用

### 新建源文件

1. **方式一**：文件 → 新建 → 源代码（Ctrl+N）
2. **方式二**：直接开始写代码

### 保存文件

- **保存**：`Ctrl + S`（保存到指定位置，建议先保存再编译）
- **另存为**：`Ctrl + Shift + S`
- **建议**：在桌面或专门文件夹建立项目目录

### 编译运行

| 按键 | 功能 |
|------|------|
| **F11** | 编译运行（最常用！） |
| F9 | 仅编译 |
| F10 | 仅运行（不重新编译） |
| Ctrl+F11 | 编译并以管理员身份运行 |

### 编译运行流程（F11）

```
代码 → 编译 → 链接 → 生成exe → 运行 → 显示结果
```

---

## 3. 调试功能

### 设置断点

1. 在代码行号左侧单击，会出现红色圆点
2. 断点处程序会暂停，方便检查

### 单步执行

| 按键 | 功能 |
|------|------|
| F7 | 单步执行（进入函数） |
| F8 | 单步执行（跳过函数） |
| Shift+F7 | 执行到下一个断点 |
| F4 | 执行到光标所在行 |

### 查看变量值

调试时，将鼠标移到变量上，会显示当前值。也可以在"调试"窗口手动添加监视变量。

---

## 4. 常见问题与解决

### 编译错误

红色文字提示错误：
```
[Error] expected ';' before 'return'
```
- 解决：看错误行及其附近，补全分号或修复语法

### 橙色警告

橙色文字是警告，不影响运行但可能有问题：
```
[Warning] 'a' is used uninitialized in this function
```
- 解决：初始化所有变量

### 闪退问题

程序运行完就关闭，看不到输出：

```cpp
// 方法一：在return前加暂停
#include <bits/stdc++.h>
using namespace std;

int main() {
    cout << "Hello" << endl;
    system("pause");  // Windows暂停，等用户按任意键继续
    return 0;
}
```

```cpp
// 方法二（推荐）：不用额外代码，直接Ctrl+F5运行（"执行不调试"）
```

---

## 5. Dev-C++设置优化

### 建议开启的选项

1. **工具 → 编译选项 → 编译时加入以下命令**：
   ```
   -static -s
   ```
   使生成的可执行文件不依赖外部DLL，更容易在不同电脑运行。

2. **工具 → 编辑器选项 → 自动缩进**：开启

3. **工具 → 格式化代码**：Ctrl+Shift+A（格式化代码）

### 代码补全

编辑 → 编辑器选项 → 自动补全：
- 勾选"启用代码补全"
- 设置补全延迟时间（如200ms）

---

## 6. 标准代码模板（Dev-C++）

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // ===== 在此下方开始写代码 =====

    int n;
    cin >> n;
    cout << n << endl;

    // ===== 在此上方结束代码 =====
    
    return 0;
}
```

---

## 7. Dev-C++ vs 其他IDE

| IDE | 平台 | 优点 | 缺点 |
|------|------|------|------|
| Dev-C++ | Windows | 轻量、免费、竞赛推荐 | 功能较简单 |
| Code::Blocks | 跨平台 | 功能较强 | 界面较复杂 |
| Visual Studio | Windows | 功能强大 | 体积太大，竞赛不常用 |
| CLion | 跨平台 | 专业 | 收费，需要配置 |

**竞赛推荐**：Windows用户使用Dev-C++，Linux用户使用g++命令行或Code::Blocks。

---

## 本章小结

1. Dev-C++是Windows下最适合竞赛入门的IDE
2. **F11**是最高频的快捷键：编译运行
3. 调试用**F7**单步执行，F8跳过函数
4. 防止闪退：用`Ctrl+F5`运行，或加`system("pause")`
5. 养成好习惯：先保存（Ctrl+S）再编译运行（F11）
""",

    "codeblocks": """# Code::Blocks使用

## 本章简介
Code::Blocks是跨平台的C++ IDE，支持Windows、Linux、macOS。本章介绍其基本使用。

---

## 1. Code::Blocks简介与安装

### 下载地址

- 官网：https://www.codeblocks.org/
- 下载版本：选择 **codeblocks-xx.xx-setup.exe**（带mingw的版本）

### 系统要求

- Windows 7/8/10/11
- 约100MB磁盘空间
- 需要安装mingw编译器（一般和CB打包在一起）

---

## 2. 基本操作

### 新建项目

1. **File → New → Project**
2. 选择 **Console Application**（控制台程序）
3. 点击 **Go**
4. 选择 **C++**
5. 输入项目名称和路径
6. 选择编译器（GNU GCC Compiler）
7. 点击 **Finish**

### 新建源文件

1. **File → New → Empty file**
2. 保存为`.cpp`文件（Ctrl+S）
3. 将文件添加到项目中（右键项目 → Add Files）

### 编译运行

| 按键 | 功能 |
|------|------|
| **Ctrl+F9** | 编译（不运行） |
| **Ctrl+F10** | 运行（不编译） |
| **F9** | 编译并运行 |
| Ctrl+Shift+F9 | 编译当前文件 |

---

## 3. 调试功能

### 设置断点

1. 在代码行号左侧单击，出现蓝色圆点
2. 或者按F4在光标位置设置断点

### 调试面板

| 面板 | 内容 |
|------|------|
| Watches | 监视变量值 |
| Call stack | 函数调用栈 |
| Threads | 线程信息（一般不用） |
| Registers | CPU寄存器（高级） |

### 调试快捷键

| 按键 | 功能 |
|------|------|
| F8 | 开始调试 |
| F4 | 运行到光标 |
| F7 | 单步执行（进入函数） |
| Shift+F7 | 单步执行（跳过函数） |
| Ctrl+F7 | 添加监视变量 |
| F5 | 启用/禁用断点 |

---

## 4. 项目管理

### 项目结构

```
项目名/
├── main.cpp          # 主程序
├── 源文件/
│   ├── func1.cpp
│   └── func2.cpp
├── 头文件/
│   ├── func1.h
│   └── func2.h
└── 编译产物/
```

### 多文件项目

```cpp
// main.cpp
#include <bits/stdc++.h>
using namespace std;

int maxValue(int a, int b);  // 函数声明

int main() {
    cout << maxValue(3, 7) << endl;
    return 0;
}

// func1.cpp
int maxValue(int a, int b) {  // 函数定义
    return (a > b) ? a : b;
}
```

在Code::Blocks中：
1. 新建Empty file → 保存为`func1.cpp`
2. 右键项目 → Add Files → 加入`func1.cpp`

---

## 5. 编译选项配置

### 设置C++标准

1. **Project → Build options**
2. 在 **Compiler settings → Other options** 中添加：
   ```
   -std=c++17
   ```

### 优化选项

| 选项 | 说明 |
|------|------|
| `-O1` | 基础优化 |
| `-O2` | 常用优化（推荐） |
| `-O3` | 激进优化 |
| `-Ofast` | 最激进（含fast-math） |

### 竞赛建议配置

```
Compiler flags: -static -s -std=c++17 -O2 -pipe
```

---

## 6. 常见问题解决

### 编译成功但无法运行

检查是否将源文件正确添加到项目中。

### 调试时变量值不显示

确保是**Debug**模式（不是Release模式）。

切换方式：**Build → Select target → Debug**

### 中文乱码

如果源文件含中文注释保存后乱码：

1. **Settings → Editor**
2. Encoding settings → 设为 **UTF-8** 或 **GBK**

---

## 7. Code::Blocks vs Dev-C++对比

| 特性 | Code::Blocks | Dev-C++ |
|------|--------------|---------|
| 平台支持 | Windows/Linux/macOS | 主要Windows |
| 调试功能 | 更强大 | 较基础 |
| 体积 | ~100MB | ~50MB |
| 多项目支持 | 更好 | 一般 |
| 竞赛推荐度 | ⭐⭐⭐ | ⭐⭐⭐⭐（Windows） |

---

## 本章小结

1. Code::Blocks是跨平台的C++ IDE
2. 新建项目选Console Application，选C++
3. F9编译运行，F8开始调试
4. 调试时用Watch窗口查看变量值
5. Linux用户推荐Code::Blocks，Windows用户优先Dev-C++
""",

    "gpp-basics": """# g++编译基础

## 本章简介
g++是Linux和竞赛环境中最常用的C++编译器。本章介绍其基本使用和常用选项。

---

## 1. g++简介

**g++**是GNU C++ Compiler，是GCC（GNU Compiler Collection）中的C++编译器。

- Linux/macOS自带
- Windows可通过MinGW或WSL安装
- CSP-J/S复赛评测环境使用g++

---

## 2. 基本编译命令

### 最简单的编译

```bash
g++ -o program source.cpp
./program
```

- `source.cpp`是源文件
- `-o program`指定输出可执行文件名为`program`
- `./program`运行程序

### 如果不加-o选项

```bash
g++ source.cpp
./a.out   # 默认生成a.out
```

---

## 3. 常用编译选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `-o <file>` | 指定输出文件名 | `-o program` |
| `-Wall` | 显示所有警告（推荐常开） | `-Wall` |
| `-g` | 包含调试信息（gdb用） | `-g` |
| `-O0/1/2/3` | 优化级别 | `-O2` |
| `-std=c++17` | 指定C++标准 | `-std=c++17` |
| `-static` | 静态链接，不依赖外部库 | `-static` |
| `-s` | 去除符号表，减小文件大小 | `-s` |
| `-w` | 禁止所有警告 | `-w` |
| `-I<dir>` | 添加头文件搜索路径 | `-I./include` |

### 竞赛推荐编译命令

```bash
g++ -std=c++17 -O2 -pipe -static -s -Wall -o program source.cpp
```

解释：
- `-std=c++17`：使用C++17标准
- `-O2`：二级优化
- `-pipe`：用管道代替临时文件，加快编译
- `-static`：静态链接，程序不依赖外部库
- `-s`：去除调试信息，减小文件大小
- `-Wall`：显示所有警告

---

## 4. 常见编译错误

### 未定义的引用

```bash
/tmp/ccXXXX.o: In function `main':
main.cpp:(.text+0x10): undefined reference to `sqrt'
collect2: error: ld returned 1 exit status
```

**原因**：链接数学库失败（`sqrt`在`libm`中）

**解决**：加`-lm`选项链接数学库
```bash
g++ -o program source.cpp -lm
```

### 未找到main函数

```bash
/usr/bin/ld: /tmp/ccXXXX.o: undefined reference to `main'
```

**原因**：没有`main`函数，或`main`拼写错误

**解决**：检查代码中是否有`int main()`函数

### 权限被拒绝

```bash
bash: ./program: Permission denied
```

**原因**：文件没有执行权限

**解决**：
```bash
chmod +x program    # 添加执行权限
./program          # 再运行
```

---

## 5. 多文件编译

### 一起编译

```bash
g++ -o program main.cpp func1.cpp func2.cpp
```

### 分别编译（适合大项目）

```bash
# 编译每个源文件为目标文件
g++ -c -o main.o main.cpp
g++ -c -o func1.o func1.cpp
g++ -c -o func2.o func2.cpp

# 链接所有目标文件
g++ -o program main.o func1.o func2.o
```

`-c`选项表示只编译不链接，生成`.o`目标文件。

---

## 6. 编译过程详解

用`-v`选项查看详细编译过程：

```bash
g++ -v -o program source.cpp
```

输出会显示预处理、编译、汇编、链接的全过程。

### 分解编译

```bash
# 预处理（展开头文件、宏替换）
g++ -E source.cpp -o source.i

# 编译（生成汇编代码）
g++ -S source.i -o source.s

# 汇编（生成目标文件）
g++ -c source.s -o source.o

# 链接（生成可执行文件）
g++ source.o -o program
```

---

## 7. Windows上使用g++

### 方式一：MinGW

1. 下载MinGW（Minimalist GNU for Windows）
2. 安装后把`bin`目录加入环境变量
3. 打开CMD即可使用

```bash
g++ --version   # 验证安装
```

### 方式二：WSL（Windows Subsystem for Linux）

1. 启用WSL功能
2. 安装Ubuntu（或其他Linux发行版）
3. 在Ubuntu中使用原生g++

### 方式三：MSYS2

```bash
pacman -S mingw-w64-gcc   # 安装g++
```

---

## 8. 竞赛环境验证

在本地Linux环境验证代码编译：

```bash
# 检查g++版本
g++ --version
# 应显示 gcc version x.x.x

# 测试编译
g++ -std=c++17 -O2 -Wall -static -o program source.cpp
echo $?   # 输出0表示编译成功

# 运行测试
./program < input.txt > output.txt
```

---

## 本章小结

1. `g++ -o program source.cpp`是最基本的编译命令
2. 竞赛推荐：`-std=c++17 -O2 -Wall -static -s`
3. 链接数学库：加`-lm`选项
4. 多文件编译：`g++ -o program a.cpp b.cpp c.cpp`
5. 遇到`Permission denied`：用`chmod +x`加执行权限
""",

}


def main():
    from app.core.database import SessionLocal
    from app.models.chapter import Chapter
    db = SessionLocal()
    count = 0
    for slug, content in UPDATES.items():
        chapter = db.query(Chapter).filter(Chapter.slug == slug).first()
        if not chapter:
            print(f"⚠️ 未找到：{slug}")
            continue
        old_len = len(chapter.content)
        chapter.content = content
        count += 1
        print(f"✅ {chapter.order:02d} {chapter.title} ({old_len}→{len(content)}字)")
    db.commit()
    print(f"\n共更新 {count} 章")
    db.close()


if __name__ == "__main__":
    main()
