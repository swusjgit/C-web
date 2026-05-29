#!/usr/bin/env python3
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.category import Category

CHAPTERS = [

    (
        "二分查找与二分答案",
        "binary-search",
        "algorithm", 4, 17,
        """# 二分查找与二分答案

## 本章简介

二分查找是竞赛中最常用的高效查找算法，能在O(log n)时间内从有序数组中找到目标。本章还介绍二分答案——将最优化问题转化为判定问题来求解。

---

## 1. 二分查找

### 适用条件

数组**有序**，查找某个值。

### 模板（左闭右闭区间）

```cpp
#include <iostream>
using namespace std;

// 在升序数组a中查找目标值target，返回下标，不存在返回-1
int binarySearch(int a[], int n, int target) {
    int left = 0, right = n - 1;

    while (left <= right) {          // 左闭右闭，left==right时区间仍有效
        int mid = left + (right - left) / 2;  // 防止(left+right)溢出

        if (a[mid] == target) {
            return mid;
        } else if (a[mid] < target) {
            left = mid + 1;          // 目标在右半区
        } else {
            right = mid - 1;         // 目标在左半区
        }
    }

    return -1;  // 未找到
}

int main() {
    int a[] = {1, 3, 5, 7, 9, 11, 13, 15};
    cout << binarySearch(a, 8, 7) << endl;   // 3
    cout << binarySearch(a, 8, 6) << endl;   // -1
    return 0;
}
```

---

## 2. lower_bound与upper_bound

### lower_bound：查找第一个≥目标值的位置

```cpp
int lower_bound(int a[], int n, int target) {
    int left = 0, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (a[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

### upper_bound：查找第一个>目标值的位置

```cpp
int upper_bound(int a[], int n, int target) {
    int left = 0, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (a[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

---

## 3. 二分答案

### 核心思想

答案具有单调性时，把求解问题转化为"判断答案是否可行"。

```
求最小值 → 判断"<=x是否可行" → 二分最小值
求最大值 → 判断">=x是否可行" → 二分最大值
```

### 例题：分配最大载重

```cpp
#include <iostream>
using namespace std;

// 判断能否以mid为最大载重完成任务
bool canShip(int weights[], int n, int days, int mid) {
    int need = 1, cur = 0;
    for (int i = 0; i < n; i++) {
        if (cur + weights[i] <= mid) {
            cur += weights[i];
        } else {
            need++;
            cur = weights[i];
            if (need > days) return false;
        }
    }
    return true;
}

int shipWithinDays(int weights[], int n, int days) {
    int left = 0, right = 0;
    for (int i = 0; i < n; i++) {
        left = max(left, weights[i]);  // 最少要能载最重的一件
        right += weights[i];           // 最多载所有货物总和
    }

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (canShip(weights, n, days, mid)) {
            right = mid;               // 可以完成，试试更小的载重
        } else {
            left = mid + 1;           // 不行，必须更大
        }
    }
    return left;
}
```

---

## 4. 浮点数二分

```cpp
// 求解sqrt(x)，精度1e-7
double mySqrt(double x) {
    double left = 0, right = max(1.0, x);
    while (right - left > 1e-7) {
        double mid = (left + right) / 2;
        if (mid * mid >= x) {
            right = mid;
        } else {
            left = mid;
        }
    }
    return left;
}
```

---

## 5. 例题：查找峰值

峰值是比邻居大的元素，O(log n)解法：

```cpp
int findPeakElement(int a[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (a[mid] < a[mid + 1]) {
            left = mid + 1;  // 峰值在右边
        } else {
            right = mid;     // 峰值在当前位置或左边
        }
    }
    return left;
}
```

---

## 本章小结

1. 二分查找：O(log n)，要求数组有序
2. `mid = left + (right - left) / 2`防溢出
3. `lower_bound`：第一个≥目标的位置
4. `upper_bound`：第一个>目标的位置
5. 二分答案：将优化问题转化为判定问题，利用单调性二分答案
"""
    ),

    (
        "排序算法",
        "sorting-algorithms",
        "algorithm", 4, 18,
        """# 排序算法

## 本章简介

排序是基础中的基础。本章介绍四种O(n²)排序算法和三种计数排序，重点理解原理和稳定性。

---

## 1. 冒泡排序

### 核心思想

相邻元素比较交换，每趟把最大（最小）元素"冒"到序列一端。

```cpp
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;  // 提前结束
    }
}
```

**稳定性**：✅ 稳定（相等不交换）

---

## 2. 选择排序

### 核心思想

每趟选择剩余未排序部分的最小（最大）元素，放到已排序部分末尾。

```cpp
void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[minIdx]) minIdx = j;
        }
        swap(a[i], a[minIdx]);
    }
}
```

**稳定性**：❌ 不稳定（交换会改变相等元素的相对位置）

---

## 3. 插入排序

### 核心思想

像整理扑克牌，把每个元素插入到已排序部分的正确位置。

```cpp
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}
```

**稳定性**：✅ 稳定
**特点**：数据接近有序时效率很高（最优O(n)）

---

## 4. 计数排序

### 核心思想

统计每个值出现的次数，适用于范围较小的整数排序。**不是比较排序**。

```cpp
#include <iostream>
using namespace std;

// 计数排序：适用于0~maxVal的整数
void countingSort(int a[], int n, int maxVal) {
    int count[1005] = {0};  // 统计每个值的出现次数

    // 统计
    for (int i = 0; i < n; i++) {
        count[a[i]]++;
    }

    // 累加（确定每个元素的位置）
    for (int i = 1; i <= maxVal; i++) {
        count[i] += count[i - 1];
    }

    // 输出（需要额外数组）
    int b[1005];
    for (int i = n - 1; i >= 0; i--) {
        b[--count[a[i]]] = a[i];
    }

    for (int i = 0; i < n; i++) a[i] = b[i];
}

int main() {
    int a[] = {4, 2, 2, 8, 3, 3, 1};
    countingSort(a, 7, 8);
    for (int x : a) cout << x << " ";  // 1 2 2 3 3 4 8
    return 0;
}
```

**时间复杂度**：O(n + k)，k为数据范围
**稳定性**：✅ 稳定（从后往前遍历保证）

---

## 5. 排序算法对比

| 算法 | 时间复杂度 | 空间复杂度 | 稳定性 |
|------|-----------|-----------|--------|
| 冒泡排序 | O(n²) | O(1) | ✅ |
| 选择排序 | O(n²) | O(1) | ❌ |
| 插入排序 | O(n²)/O(n) | O(1) | ✅ |
| 计数排序 | O(n+k) | O(k) | ✅ |

---

## 本章小结

1. 冒泡：相邻交换，大的泡泡冒到右边
2. 选择：每趟选最小，放到已排序末尾
3. 插入：像整理扑克牌，逐个插入已排序部分
4. 计数排序：非比较排序，用计数数组，O(n+k)
5. 稳定性：相等元素的相对顺序是否保持
"""
    ),

    (
        "高精度计算",
        "high-precision",
        "algorithm", 4, 19,
        """# 高精度计算

## 本章简介

C++的基本数据类型有范围限制（int约±21亿，long long约±9×10¹⁸）。当需要处理更大整数时，需要使用高精度计算（字符串模拟）。

---

## 1. 大整数运算的需求

```cpp
// 超出long long范围的计算示例
long long a = 9999999999999999999LL;
long long b = 1;
// a + b 可能溢出！
```

---

## 2. 高精度加法

### 核心思想

用字符串存储数字，模拟竖式计算。

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 大整数加法：字符串形式
string add(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int carry = 0;
    string result;

    for (size_t i = 0; i < max(a.size(), b.size()); i++) {
        int da = (i < a.size()) ? a[i] - '0' : 0;
        int db = (i < b.size()) ? b[i] - '0' : 0;
        int sum = da + db + carry;
        result.push_back('0' + (sum % 10));
        carry = sum / 10;
    }

    if (carry > 0) result.push_back('0' + carry);
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    string a = "123456789";
    string b = "987654321";
    cout << add(a, b) << endl;  // 1111111110
}
```

---

## 3. 高精度乘法（乘以单精度）

### 字符串乘以int

```cpp
string multiply(string num, int factor) {
    reverse(num.begin(), num.end());

    int carry = 0;
    string result;

    for (size_t i = 0; i < num.size() || carry; i++) {
        int d = (i < num.size()) ? num[i] - '0' : 0;
        int prod = d * factor + carry;
        result.push_back('0' + (prod % 10));
        carry = prod / 10;
    }

    reverse(result.begin(), result.end());
    // 去除前导0
    while (result.size() > 1 && result[0] == '0') {
        result.erase(0, 1);
    }

    return result;
}

int main() {
    cout << multiply("123456", 9) << endl;  // 1111104
}
```

---

## 4. 高精度乘法（大整数×大整数）

```cpp
string multiplyBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    vector<int> result(a.size() + b.size(), 0);

    for (size_t i = 0; i < a.size(); i++) {
        for (size_t j = 0; j < b.size(); j++) {
            result[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }

    int carry = 0;
    for (size_t i = 0; i < result.size(); i++) {
        int sum = result[i] + carry;
        result[i] = sum % 10;
        carry = sum / 10;
    }

    string s;
    for (int d : result) {
        s.push_back('0' + d);
    }
    reverse(s.begin(), s.end());

    while (s.size() > 1 && s[0] == '0') s.erase(0, 1);
    return s;
}

int main() {
    cout << multiplyBig("123456789", "987654321") << endl;
    // 输出：121932631112635269
}
```

---

## 5. 高精度减法

```cpp
string subtract(string a, string b) {
    // 确保 a >= b
    if (a.size() < b.size() || (a.size() == b.size() && a < b)) {
        return "-" + subtract(b, a);
    }

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int carry = 0;
    string result;

    for (size_t i = 0; i < a.size(); i++) {
        int da = a[i] - '0';
        int db = (i < b.size()) ? b[i] - '0' : 0;
        int diff = da - carry - db;
        if (diff < 0) {
            diff += 10;
            carry = 1;
        } else {
            carry = 0;
        }
        result.push_back('0' + diff);
    }

    reverse(result.begin(), result.end());
    while (result.size() > 1 && result[0] == '0') result.erase(0, 1);
    return result;
}

int main() {
    cout << subtract("1000000", "1") << endl;  // 999999
}
```

---

## 本章小结

1. 高精度用字符串存储，按位计算
2. 加法：逐位相加，处理进位
3. 减法：确保大减小，逐位相减，处理借位
4. 乘法（大×小）：按位乘，累加进位
5. 乘法（大×大）：双重循环，最后统一处理进位
6. 记得去除前导0（但保留"0"本身）
"""
    ),

    (
        "进制转换",
        "base-conversion",
        "math", 3, 20,
        """# 进制转换

## 本章简介

计算机中常用二进制、八进制、十六进制。本章介绍它们与十进制之间的转换方法。

---

## 1. 十进制转其他进制

### 方法：除基取余法

```cpp
#include <iostream>
#include <stack>
using namespace std;

// 十进制转任意进制（2~16）
string toBase(int n, int base) {
    if (n == 0) return "0";

    string digits = "0123456789ABCDEF";
    string result;
    bool negative = (n < 0);
    n = abs(n);

    while (n > 0) {
        result.push_back(digits[n % base]);
        n /= base;
    }

    if (negative) result.push_back('-');
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    cout << toBase(10, 2) << endl;   // 1010
    cout << toBase(255, 16) << endl;  // FF
    cout << toBase(-42, 2) << endl;   // -101010
}
```

---

## 2. 其他进制转十进制

### 方法：按权展开

```cpp
#include <iostream>
using namespace std;

// 任意进制（2~16）转十进制
int fromBase(const string& s, int base) {
    int result = 0;
    for (char c : s) {
        int digit;
        if ('0' <= c && c <= '9') digit = c - '0';
        else digit = c - 'A' + 10;

        result = result * base + digit;
    }
    return result;
}

int main() {
    cout << fromBase("1010", 2) << endl;   // 10
    cout << fromBase("FF", 16) << endl;    // 255
}
```

---

## 3. 二进制与八进制/十六进制互转

### 技巧：每3位二进制=1位八进制，每4位二进制=1位十六进制

```cpp
#include <iostream>
#include <string>
using namespace std;

// 二进制字符串转八进制
string binToOct(const string& bin) {
    // 补齐前导0，使长度是3的倍数
    int len = bin.size();
    int pad = (3 - len % 3) % 3;
    string s = string(pad, '0') + bin;

    string result;
    for (size_t i = 0; i < s.size(); i += 3) {
        int val = (s[i]-'0')*4 + (s[i+1]-'0')*2 + (s[i+2]-'0');
        result.push_back('0' + val);
    }

    // 去掉前导0
    size_t pos = result.find_first_not_of('0');
    return (pos == string::npos) ? "0" : result.substr(pos);
}

// 八进制转二进制
string octToBin(const string& oct) {
    string result;
    for (char c : oct) {
        switch(c) {
            case '0': result += "000"; break;
            case '1': result += "001"; break;
            case '2': result += "010"; break;
            case '3': result += "011"; break;
            case '4': result += "100"; break;
            case '5': result += "101"; break;
            case '6': result += "110"; break;
            case '7': result += "111"; break;
        }
    }
    // 去掉前导0
    size_t pos = result.find_first_not_of('0');
    return (pos == string::npos) ? "0" : result.substr(pos);
}

int main() {
    cout << binToOct("11111111") << endl;   // 377
    cout << octToBin("377") << endl;         // 11111111
}
```

---

## 4. 位运算基础

### 六种位运算

```cpp
int a = 6, b = 3;  // 6=110, 3=011

cout << (a & b) << endl;   // 2 (110 & 011 = 010)
cout << (a | b) << endl;    // 7 (110 | 011 = 111)
cout << (a ^ b) << endl;    // 5 (110 ^ 011 = 101)
cout << (~a) << endl;       // -7（按位取反）
cout << (a << 1) << endl;   // 12（a*2，左移1位）
cout << (a >> 1) << endl;   // 3（a/2，右移1位）
```

### 常用操作

```cpp
int n = 12;  // 二进制：1100

// 判断第i位是否为1（从0开始）
bool isBit1 = (n >> i) & 1;

// 置第i位为1
n |= (1 << i);

// 置第i位为0
n &= ~(1 << i);

// 统计1的个数
int countOnes(int n) {
    int cnt = 0;
    while (n) {
        n &= (n - 1);  // 消除最低位的1
        cnt++;
    }
    return cnt;
}
```

---

## 本章小结

1. 十进制转其他进制：除基取余，倒序取余数
2. 其他进制转十进制：按权展开
3. 二进制↔八进制：每3位对应
4. 二进制↔十六进制：每4位对应
5. 位运算：`& | ^ ~ << >>`是竞赛必备技巧
"""
    ),

    (
        "结构体与链表",
        "struct-and-linked-list",
        "data-structure", 3, 21,
        """# 结构体与链表

## 本章简介

结构体是自定义数据类型的基础，链表是线性数据结构的核心。本章介绍结构体的使用和链表的手工实现。

---

## 1. 结构体基础

### 定义与使用

```cpp
#include <iostream>
#include <string>
using namespace std;

// 定义学生结构体
struct Student {
    string name;    // 姓名
    int age;        // 年龄
    int score;      // 成绩
};

int main() {
    // 定义结构体变量
    Student s1;
    s1.name = "张三";
    s1.age = 14;
    s1.score = 92;

    // 初始化
    Student s2 = {"李四", 15, 88};

    cout << s1.name << ": " << s1.score << "分" << endl;
    return 0;
}
```

---

## 2. 结构体与函数

```cpp
struct Point {
    int x, y;
};

// 传结构体（副本）
void printPoint(Point p) {
    cout << "(" << p.x << ", " << p.y << ")" << endl;
}

// 传引用（推荐，避免拷贝）
void movePoint(Point& p, int dx, int dy) {
    p.x += dx;
    p.y += dy;
}

// 返回结构体
Point midPoint(const Point& a, const Point& b) {
    return {(a.x + b.x) / 2, (a.y + b.y) / 2};
}
```

---

## 3. 单向链表

### 节点定义

```cpp
struct Node {
    int data;       // 数据
    Node* next;     // 指向下一个节点
};
```

### 创建节点

```cpp
// 在堆上创建新节点
Node* createNode(int val) {
    Node* p = new Node;  // 动态分配
    p->data = val;
    p->next = nullptr;
    return p;
}
```

### 链表基本操作

```cpp
// 头插法：插入到链表头部
void insertAtHead(Node*& head, int val) {
    Node* newNode = createNode(val);
    newNode->next = head;
    head = newNode;
}

// 尾插法：插入到链表尾部
void insertAtTail(Node*& head, int val) {
    Node* newNode = createNode(val);
    if (!head) {
        head = newNode;
        return;
    }
    Node* p = head;
    while (p->next) p = p->next;
    p->next = newNode;
}

// 按值删除
void deleteByValue(Node*& head, int val) {
    if (!head) return;
    if (head->data == val) {
        Node* tmp = head;
        head = head->next;
        delete tmp;
        return;
    }
    Node* p = head;
    while (p->next && p->next->data != val) {
        p = p->next;
    }
    if (p->next) {
        Node* tmp = p->next;
        p->next = tmp->next;
        delete tmp;
    }
}
```

---

## 4. 遍历链表

```cpp
void printList(Node* head) {
    Node* p = head;
    while (p) {
        cout << p->data;
        if (p->next) cout << " -> ";
        p = p->next;
    }
    cout << endl;
}

// 释放链表内存
void deleteList(Node*& head) {
    while (head) {
        Node* tmp = head;
        head = head->next;
        delete tmp;
    }
}
```

---

## 5. 双向链表（了解）

```cpp
struct DNode {
    int data;
    DNode* prev;
    DNode* next;
};
```

---

## 6. STL list简介

```cpp
#include <list>
using namespace std;

list<int> lst = {1, 2, 3, 4, 5};

lst.push_front(0);     // 头部插入
lst.push_back(6);       // 尾部插入
lst.insert(++lst.begin(), 10);  // 第二个位置插入10

lst.remove(3);          // 删除值为3的节点
lst.reverse();          // 反转

for (int x : lst) cout << x << " ";  // 0 1 2 4 5 6 10
```

---

## 本章小结

1. 结构体：自定义数据类型，封装多个不同类型字段
2. 链表：节点+指针，动态插入删除O(1)（知道位置时）
3. 头插/尾插/按值删除是链表基本操作
4. 使用`new`分配内存后要及时`delete`释放
5. STL `list`是双向链表，直接可用
"""
    ),

    (
        "二叉树基础",
        "binary-tree",
        "data-structure", 4, 22,
        """# 二叉树基础

## 本章简介

二叉树是树形结构的核心，每个节点最多有两个子节点。本章介绍二叉树的存储结构、遍历方式及常见应用。

---

## 1. 二叉树节点定义

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

---

## 2. 二叉树的遍历

### 前序遍历（根-左-右）

```cpp
void preOrder(TreeNode* root) {
    if (!root) return;
    cout << root->val << " ";
    preOrder(root->left);
    preOrder(root->right);
}
```

### 中序遍历（左-根-右）

```cpp
void inOrder(TreeNode* root) {
    if (!root) return;
    inOrder(root->left);
    cout << root->val << " ";
    inOrder(root->right);
}
```

### 后序遍历（左-右-根）

```cpp
void postOrder(TreeNode* root) {
    if (!root) return;
    postOrder(root->left);
    postOrder(root->right);
    cout << root->val << " ";
}
```

### 层序遍历（用队列）

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

## 3. 遍历的应用

### 求二叉树深度

```cpp
int treeDepth(TreeNode* root) {
    if (!root) return 0;
    return max(treeDepth(root->left), treeDepth(root->right)) + 1;
}
```

### 统计节点数

```cpp
int countNodes(TreeNode* root) {
    if (!root) return 0;
    return countNodes(root->left) + countNodes(root->right) + 1;
}
```

### 判断是否为二叉搜索树

```cpp
// BST中序遍历是有序的
bool isValidBST(TreeNode* root) {
    long long prev = -1e18;  // 用long long处理int边界
    return inOrderCheck(root, prev);
}

bool inOrderCheck(TreeNode* node, long long& prev) {
    if (!node) return true;
    if (!inOrderCheck(node->left, prev)) return false;
    if (node->val <= prev) return false;
    prev = node->val;
    return inOrderCheck(node->right, prev);
}
```

---

## 4. 二叉树的构造

### 根据前序+中序构造

```cpp
TreeNode* buildTree(vector<int>& pre, int preL, int preR,
                    vector<int>& in, int inL, int inR) {
    if (preL > preR) return nullptr;

    TreeNode* root = new TreeNode(pre[preL]);

    int inIdx = 0;
    for (int i = inL; i <= inR; i++) {
        if (in[i] == pre[preL]) { inIdx = i; break; }
    }

    int leftSize = inIdx - inL;

    root->left = buildTree(pre, preL + 1, preL + leftSize,
                           in, inL, inIdx - 1);
    root->right = buildTree(pre, preL + leftSize + 1, preR,
                            in, inIdx + 1, inR);
    return root;
}
```

---

## 5. 完全二叉树的性质

```cpp
// 判断是否是完全二叉树（层序遍历）
bool isCompleteTree(TreeNode* root) {
    queue<TreeNode*> q;
    q.push(root);
    bool reachedNull = false;

    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();

        if (!node) {
            reachedNull = true;
            continue;
        }
        if (reachedNull) return false;  // 空节点后还有非空节点

        q.push(node->left);
        q.push(node->right);
    }
    return true;
}
```

---

## 本章小结

1. 前序：根左右，中序：左根右，后序：左右根
2. 层序遍历用队列，前/中/后序用递归
3. 深度、节点数用递归求
4. BST中序遍历有序，可判断是否是BST
5. 前序+中序可唯一确定二叉树
"""
    ),

    (
        "图的存储与遍历",
        "graph",
        "data-structure", 4, 23,
        """# 图的存储与遍历

## 本章简介

图是竞赛中的重要数据结构。本章介绍两种存储方式和两种遍历方法。

---

## 1. 图的存储

### 邻接矩阵

适合稠密图（边多）。

```cpp
int n = 5;  // 顶点数
int g[100][100] = {0};  // g[i][j] = 1表示边(i,j)存在

// 添加无向边
void addEdge(int u, int v) {
    g[u][v] = g[v][u] = 1;
}
```

### 邻接表

适合稀疏图（边少）。

```cpp
#include <vector>
using namespace std;

vector<int> adj[100];  // adj[i]存储i的所有邻居

// 添加有向边
void addEdge(int u, int v) {
    adj[u].push_back(v);
}

// 添加无向边
void addUndirectedEdge(int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);
}
```

---

## 2. 图的DFS遍历

```cpp
#include <vector>
#include <iostream>
using namespace std;

int n = 5;
vector<int> adj[100];
bool vis[100];

void dfs(int u) {
    vis[u] = true;
    cout << u << " ";

    for (int v : adj[u]) {
        if (!vis[v]) {
            dfs(v);
        }
    }
}

int main() {
    // 建图：0-1-3, 0-2-4
    addUndirectedEdge(0, 1);
    addUndirectedEdge(0, 2);
    addUndirectedEdge(1, 3);
    addUndirectedEdge(2, 4);

    cout << "DFS: ";
    dfs(0);  // 输出：0 1 3 2 4
    return 0;
}
```

---

## 3. 图的BFS遍历

```cpp
#include <queue>
#include <iostream>
using namespace std;

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

## 4. 连通分量计数

```cpp
int countComponents(int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (!vis[i]) {
            cnt++;
            dfs(i);
        }
    }
    return cnt;
}
```

---

## 5. 例题：判断是否有环

```cpp
// DFS判断无向图是否有环
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

1. 邻接矩阵：二维数组，适合稠密图，O(1)查询边
2. 邻接表：vector数组，适合稀疏图，O(V+E)存储
3. 图的DFS/BFS与树类似，区别是要用`vis`避免重复访问
4. 连通分量：用`vis`计数，每遇到未访问节点就DFS一次
5. 环检测：DFS过程中遇到已访问的非父节点则有环
"""
    ),

    (
        "集合与容斥原理",
        "set-and-pie",
        "math", 4, 24,
        """# 集合与容斥原理

## 本章简介

容斥原理是计数中的重要技巧，用于处理"至少满足一个条件"的问题。

---

## 1. 集合基础

```cpp
#include <set>
using namespace std;

int main() {
    set<int> s;  // 集合（自动排序、去重）

    s.insert(3);
    s.insert(1);
    s.insert(4);
    s.insert(1);  // 重复，不插入

    for (int x : s) cout << x << " ";  // 1 3 4

    cout << s.count(3) << endl;  // 1（存在）
    cout << s.count(2) << endl;  // 0（不存在）

    s.erase(1);  // 删除
    return 0;
}
```

---

## 2. 容斥原理

### 核心公式

|A∪B∪C| = |A| + |B| + |C| - |A∩B| - |B∩C| - |C∩A| + |A∩B∩C|

### 例题：能被2或3整除的数

```cpp
// 在1~30中，能被2或3整除的数有多少个？

// |A| = floor(30/2) = 15（能被2整除）
// |B| = floor(30/3) = 10（能被3整除）
// |A∩B| = floor(30/6) = 5（能被6整除）
// |A∪B| = 15 + 10 - 5 = 20

int countDivisibleBy2or3(int n) {
    int a = n / 2;        // 能被2整除
    int b = n / 3;        // 能被3整除
    int ab = n / 6;       // 能被2和3同时整除（即能被6整除）
    return a + b - ab;
}
```

---

## 3. 三个集合的容斥

```cpp
// 在1~n中，能被a或b或c整除的数有多少个？
long long countDivisible(long long n, long long a, long long b, long long c) {
    long long A = n / a;
    long long B = n / b;
    long long C = n / c;
    long long AB = n / lcm(a, b);
    long long BC = n / lcm(b, c);
    long long AC = n / lcm(a, c);
    long long ABC = n / lcm(lcm(a, b), c);

    return A + B + C - AB - BC - AC + ABC;
}
```

---

## 4. 例题：CSP-J真题改编

**题目**：在1~1000中，不能被3、5、7整除的数有多少个？

```cpp
long long notDivisible() {
    // 总数 - 能被3或5或7整除的数
    long long total = 1000;

    long long A = 1000/3;   // 333
    long long B = 1000/5;   // 200
    long long C = 1000/7;   // 142

    long long AB = 1000/15;   // 66
    long long BC = 1000/35;    // 28
    long long AC = 1000/21;    // 47

    long long ABC = 1000/105;  // 9

    long long divisible = A + B + C - AB - BC - AC + ABC;
    return total - divisible;
}

int main() {
    cout << notDivisible() << endl;  // 457
}
```

---

## 本章小结

1. 容斥原理处理"至少满足一个条件"的计数
2. 两集合：|A∪B| = |A| + |B| - |A∩B|
3. 三集合：|A∪B∪C| = |A|+|B|+|C| - |AB|-|BC|-|CA| + |ABC|
4. 求交集中元素的个数：用最小公倍数lcm
5. 常见问题：能被某数整除的个数、满足某条件的计数
"""
    ),

    (
        "递推与递归",
        "recursion-and-recurrence",
        "algorithm", 3, 25,
        """# 递推与递归

## 本章简介

递推和递归是数学和计算机科学中最核心的思维方式。本章介绍它们的概念、区别和典型应用。

---

## 1. 递归与递推的区别

| 特征 | 递归（自顶向下） | 递推（自底向上） |
|------|----------------|----------------|
| 方向 | 从大问题到小问题 | 从小问题到大问题 |
| 实现 | 函数调用自身 | 循环迭代 |
| 效率 | 有重复计算（除非记忆化） | 高效 |
| 终止条件 | 必须有 | 必须有 |

---

## 2. 经典递推问题

### 斐波那契数列

```cpp
// 递推（推荐）
int fib(int n) {
    if (n <= 2) return 1;
    int a = 1, b = 1, c;
    for (int i = 3; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// 递归（简洁但效率低）
int fibRec(int n) {
    if (n <= 2) return 1;
    return fibRec(n-1) + fibRec(n-2);
}
```

### 爬楼梯的不同走法数

```cpp
// f(n) = f(n-1) + f(n-2)，边界：f(1)=1, f(2)=2
int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int t = a + b;
        a = b;
        b = t;
    }
    return b;
}
```

---

## 3. 错排问题

**问题**：n封信装进n个信封，全部装错有多少种？

```cpp
// D(n) = (n-1) * (D(n-1) + D(n-2))
// D(1)=0, D(2)=1
long long derangement(int n) {
    if (n == 1) return 0;
    if (n == 2) return 1;
    long long a = 0, b = 1;
    for (int i = 3; i <= n; i++) {
        long long c = (i - 1) * (a + b);
        a = b;
        b = c;
    }
    return b;
}
```

---

## 4. 卡特兰数

**应用**：出栈序列、括号匹配、二叉树形态数

```cpp
// h(n) = C(2n, n) / (n+1)
// 递推：h(n) = h(n-1) * (4n-2) / (n+1)
long long catalan(int n) {
    if (n <= 1) return 1;
    long long h = 1;
    for (int i = 2; i <= n; i++) {
        h = h * (4 * i - 2) / (i + 1);
    }
    return h;
}
```

---

## 5. 递归代码的通用模板

```cpp
// 返回值类型 函数名(参数) {
//     if (基准情况) return 结果;
//     return 函数名(缩小问题);
// }

// 汉诺塔
void hanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        cout << n << " from " << from << " to " << to << endl;
        return;
    }
    hanoi(n-1, from, aux, to);
    cout << n << " from " << from << " to " << to << endl;
    hanoi(n-1, aux, to, from);
}
```

---

## 本章小结

1. 递归：函数调用自身，简洁但注意栈溢出
2. 递推：循环迭代从已知推到未知，更高效
3. 斐波那契：f(n)=f(n-1)+f(n-2)
4. 错排：D(n)=(n-1)×(D(n-1)+D(n-2))
5. 卡特兰数：h(n)=C(2n,n)/(n+1)，用于计数问题
"""
    ),

    (
        "位运算进阶",
        "bit-manipulation",
        "algorithm", 3, 26,
        """# 位运算进阶

## 本章简介

位运算是竞赛中的重要技巧，能在O(1)时间内完成很多操作。本章介绍常用技巧和典型应用。

---

## 1. 常用位运算技巧

```cpp
int n = 12;  // 1100

// 取最低位的1
int lowbit = n & (-n);  // 100 (值为4)

// 消除最低位的1
int after = n & (n - 1);  // 1000 (值为8)

// 统计1的个数
int countOnes(int n) {
    int cnt = 0;
    while (n) {
        n &= (n - 1);  // 消除最低位的1
        cnt++;
    }
    return cnt;
}

// 判断是否为2的幂次
bool isPowerOf2(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}
```

---

## 2. 状态压缩

用整数的二进制位表示集合状态（最多20个元素）。

```cpp
// 用二进制位表示集合 {0, 2, 3}
// 00101 = 1<<0 + 1<<2 + 1<<3 = 13

int S = 0;
// 添加元素i到集合
S |= (1 << i);
// 删除元素i
S &= ~(1 << i);
// 判断i是否在集合中
if (S & (1 << i)) ...
// 集合大小
int sz = __builtin_popcount(S);
```

---

## 3. 枚举子集

```cpp
// 枚举集合S的所有子集
for (int sub = S; sub; sub = (sub - 1) & S) {
    // sub是S的一个非空子集
}
```

---

## 4. 异或的妙用

```cpp
// 交换两个数（不用临时变量）
a ^= b;
b ^= a;
a ^= b;

// 找出数组中唯一出现一次的数（其他都出现两次）
int findUnique(int a[], int n) {
    int x = 0;
    for (int i = 0; i < n; i++) {
        x ^= a[i];
    }
    return x;
}
```

---

## 本章小结

1. `n & (-n)` 取最低位的1
2. `n & (n-1)` 消除最低位的1
3. 状态压缩：用位表示集合，适合≤20个元素
4. `__builtin_popcount` 统计1的个数
5. 异或：相同为0，不同为1，可用于找唯一数、交换两数
"""
    ),

    (
        "模拟与枚举",
        "simulation-and-enumeration",
        "algorithm", 2, 27,
        """# 模拟与枚举

## 本章简介

模拟和枚举是最朴素的算法思想，却是CSP-J中最重要的解题手段。本章介绍如何用模拟和枚举解决实际问题。

---

## 1. 什么是模拟

根据题目描述，一步一步把现实过程用代码实现。

### 例题：打印日期

```cpp
// 输入年、月、日，输出第二天的日期
#include <iostream>
using namespace std;

int main() {
    int y, m, d;
    cin >> y >> m >> d;

    int days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
        days[2] = 29;  // 闰年
    }

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

## 2. 什么是枚举

把问题的所有可能情况逐一列举，判断是否满足条件。

### 枚举优化：避免重复

```cpp
// 错误：双重循环会重复
for (int i = 0; i < n; i++)
    for (int j = i; j < n; j++)  // j从i开始，避免重复

// 分数约分：枚举分子分母
for (int i = 1; i <= 100; i++) {
    for (int j = i + 1; j <= 100; j++) {  // j>i，保证分数最简
        if (gcd(i, j) == 1) {
            // i/j是最简分数
        }
    }
}
```

---

## 3. 枚举典型应用

### 数字三角形中的最大路径和

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[100][100];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> a[i][j];
        }
    }

    // 自底向上DP
    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            a[i][j] += max(a[i+1][j], a[i+1][j+1]);
        }
    }

    cout << a[0][0] << endl;
    return 0;
}
```

---

## 4. 模拟典型应用

### 大小写转换

```cpp
char c = 'A';
if ('A' <= c && c <= 'Z') c = c - 'A' + 'a';  // 转小写
if ('a' <= c && c <= 'z') c = c - 'a' + 'A';  // 转大写
```

---

## 本章小结

1. 模拟：把现实过程翻译成代码，按部就班执行
2. 枚举：列举所有可能，优化时用已知信息剪枝
3. 枚举时注意避免重复（j从i开始或用set去重）
4. 数字三角形用自底向上DP枚举路径
5. 模拟要注意边界条件和特殊情况（闰年、日期进位等）
"""
    ),

]


def main():
    from app.core.database import SessionLocal
    from app.models.chapter import Chapter

    db = SessionLocal()
    count = 0

    for title, slug, cat_slug, difficulty, order, content in CHAPTERS:
        cat = db.query(Category).filter(Category.slug == cat_slug).first()
        if not cat:
            print(f"警告：分类{cat_slug}不存在，跳过《{title}》")
            continue

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
    print(f"✅ 成功插入 {count} 个章节")
    db.close()


if __name__ == "__main__":
    main()
