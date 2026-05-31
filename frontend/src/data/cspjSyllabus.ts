import type { ChapterSummary } from "@/lib/staticChapters";

export interface SyllabusModule {
  slug: string;
  code: string;
  name: string;
  focus: string;
  chapterSlugs: string[];
  missing: string[];
}

export interface ChapterSyllabusMeta {
  code: string;
  label: string;
  target: string;
  checkpoints: string[];
  practice: string;
}

export const syllabusModules: SyllabusModule[] = [
  {
    slug: "basics",
    code: "2.1.1",
    name: "基础知识与编程环境",
    focus: "理解计算机、操作系统、网络、竞赛规则和 C++ 编译运行环境。",
    chapterSlugs: ["computer-basics", "language-basics", "base-and-encoding", "first-program", "gpp-and-debug"],
    missing: ["计算机网络与 Internet", "计算机历史与常见用途", "NOI/CSP 规则", "位、字节与字"],
  },
  {
    slug: "cpp",
    code: "2.1.2",
    name: "C++程序设计",
    focus: "掌握变量、语句、数组、字符串、函数、结构体、指针引用、文件与常用 STL。",
    chapterSlugs: [
      "variables",
      "io-and-expressions",
      "if-switch",
      "loops",
      "loop-control",
      "nested-loops",
      "array-1d",
      "array-2d",
      "string",
      "function-basics",
      "function-params",
      "scope-and-recursion",
      "struct-union",
      "pointers-basics",
      "pointer-array-string",
      "pointer-to-struct",
      "reference",
      "file-operations",
      "stl-algorithm",
      "stl-container",
    ],
    missing: ["流程图与伪代码", "cmath 常用函数"],
  },
  {
    slug: "data-structure",
    code: "2.1.3",
    name: "数据结构",
    focus: "理解线性结构、简单树、完全二叉树、哈夫曼树、二叉搜索树和图的存储。",
    chapterSlugs: [
      "linked-list",
      "dlist-cyclelist",
      "stack",
      "queue",
      "tree-basics",
      "tree-storage",
      "tree-traversal",
      "complete-binary-tree",
      "huffman",
      "bst",
      "graph-storage",
      "graph-traversal",
    ],
    missing: [],
  },
  {
    slug: "algorithm",
    code: "2.1.4",
    name: "算法",
    focus: "从枚举、模拟过渡到贪心、递推、递归、二分、搜索、图遍历和基础动态规划。",
    chapterSlugs: [
      "enumeration",
      "simulation",
      "greedy",
      "recurrence-dp",
      "dp-1d",
      "knapsack",
      "interval-dp",
      "dfs",
      "bfs",
      "flood-fill",
      "prefix-difference",
      "binary-search",
      "doubling",
      "high-precision",
    ],
    missing: ["排序基础：冒泡、选择、插入、计数排序", "高精度整数除以单精度整数"],
  },
  {
    slug: "math",
    code: "2.1.5",
    name: "数学与其他",
    focus: "补齐进制、初等数学、初等数论、集合、计数原理、排列组合、杨辉三角和 ASCII。",
    chapterSlugs: [
      "base-conversion",
      "middle-school-algebra",
      "middle-school-geometry",
      "ascii",
      "set-ppp",
      "permutation-combination",
      "pascals-triangle",
      "mod",
      "unique-factorization",
      "euclidean",
      "sieve",
    ],
    missing: ["自然数、整数、有理数、实数", "整除、因数、倍数、素数与合数"],
  },
];

export const roadmapStages = [
  {
    weeks: "第 1-2 周",
    name: "语法和环境打底",
    goal: "能独立写出输入输出、分支、循环和数组程序。",
    tasks: ["完成基础知识与 C++ 前 8 章", "每天 3 道语法小题", "整理常见编译错误"],
  },
  {
    weeks: "第 3-4 周",
    name: "数组、字符串、函数",
    goal: "能处理序列、表格、字符串和简单模块化代码。",
    tasks: ["补完字符串、函数、结构体", "练习模拟与枚举", "开始代码阅读题"],
  },
  {
    weeks: "第 5-6 周",
    name: "基础算法和数学",
    goal: "掌握排序、前缀和、二分、gcd、素数筛等常考工具。",
    tasks: ["补算法与数学核心章节", "每章至少 2 道编程题", "建立错题本"],
  },
  {
    weeks: "第 7-8 周",
    name: "搜索、DP 和真题",
    goal: "能识别 DFS/BFS/简单 DP 场景，完成 CSP-J 中后段题训练。",
    tasks: ["集中训练搜索和一维/背包 DP", "做近年真题", "每周一次限时模拟"],
  },
];

export const studyPrinciples = [
  {
    title: "先读题，再写代码",
    body: "每道题先圈出输入、输出、限制条件和样例含义，再决定用分支、循环、数组还是搜索。",
  },
  {
    title: "小数据手算一遍",
    body: "写代码前用纸笔模拟 1-2 组很小的数据，确认变量如何变化，能减少很多调试时间。",
  },
  {
    title: "每题都要复盘",
    body: "通过后记录关键思路、错因和边界数据；没通过时先定位是读题、算法还是代码细节的问题。",
  },
];

export const weeklyPracticePlan = [
  "周一到周三：跟教程学一个小知识点，每天写 2-3 道短题。",
  "周四到周五：做同主题变式题，把输入输出、边界情况和复杂度说清楚。",
  "周末：限时完成一组综合练习，整理错题和下周要补的章节。",
];

const chapterMeta: Record<string, ChapterSyllabusMeta> = {
  "computer-basics": {
    code: "2.1.1",
    label: "计算机基本构成、操作系统与竞赛环境",
    target: "知道程序在计算机中如何被编辑、编译和运行。",
    checkpoints: ["能说出 CPU、内存、硬盘和 I/O 设备的作用", "能完成常见文件操作", "理解 CSP-J 使用机器评测"],
    practice: "用自己的话画一张“代码到运行结果”的流程图。",
  },
  "language-basics": {
    code: "2.1.2.1",
    label: "程序基本概念",
    target: "理解标识符、关键字、常量、变量、表达式和字符串。",
    checkpoints: ["能判断合法变量名", "能区分常量和变量", "能解释表达式求值顺序"],
    practice: "列出 5 个合法变量名和 3 个非法变量名，并说明原因。",
  },
  "base-and-encoding": {
    code: "2.1.5.1",
    label: "进制与编码",
    target: "掌握二、八、十、十六进制的互相转换。",
    checkpoints: ["会按位权展开", "会用短除法转换进制", "知道 ASCII 与字符编码的关系"],
    practice: "把 2025 转成二进制和十六进制。",
  },
  "first-program": {
    code: "2.1.1",
    label: "IDE 与第一个 C++ 程序",
    target: "能独立新建、保存、编译、运行 C++ 程序。",
    checkpoints: ["能解释 main 函数", "能使用 cin/cout", "能定位常见编译错误"],
    practice: "写一个读入姓名并输出问候语的小程序。",
  },
  "gpp-and-debug": {
    code: "2.1.1",
    label: "g++ 编译与调试",
    target: "理解命令行编译的基本形式和错误信息。",
    checkpoints: ["会使用 g++ source.cpp -o app", "能区分编译错误和运行错误", "知道多文件编译的基本概念"],
    practice: "把一个 Hello World 程序用 g++ 编译运行。",
  },
  enumeration: {
    code: "2.1.4.2",
    label: "入门算法：枚举法",
    target: "能用穷举思想列出所有可能并筛选答案。",
    checkpoints: ["能确定枚举范围", "能设计判定条件", "知道枚举复杂度会随范围增长"],
    practice: "枚举所有两位数，找出个位与十位和为 10 的数。",
  },
  simulation: {
    code: "2.1.4.2",
    label: "入门算法：模拟法",
    target: "能按题意逐步更新状态，写出清晰的过程代码。",
    checkpoints: ["能拆解操作步骤", "能设计状态变量", "能处理边界条件"],
    practice: "模拟一次排队叫号过程。",
  },
};

function fallbackMeta(chapter: ChapterSummary): ChapterSyllabusMeta {
  const syllabusModule = syllabusModules.find((item) => item.slug === chapter.category_slug);
  const moduleCode = syllabusModule?.code ?? "2.1";
  const moduleName = syllabusModule?.name ?? "CSP-J 入门级";

  return {
    code: moduleCode,
    label: moduleName,
    target: `掌握「${chapter.title}」在 CSP-J 入门级中的基本概念和常见用法。`,
    checkpoints: [
      "能复述本章核心概念",
      "能读懂本章示例代码",
      "能完成 2-3 道同类型基础练习",
    ],
    practice: "学习后用 10 分钟写一段本章主题的最小示例程序。",
  };
}

export function getChapterSyllabusMeta(chapter: ChapterSummary): ChapterSyllabusMeta {
  return chapterMeta[chapter.slug] ?? fallbackMeta(chapter);
}

export function getSyllabusCoverage(chapters: ChapterSummary[]) {
  return syllabusModules.map((syllabusModule) => {
    const available = syllabusModule.chapterSlugs.filter((slug) => chapters.some((chapter) => chapter.slug === slug));
    return {
      ...syllabusModule,
      availableCount: available.length,
      plannedCount: syllabusModule.chapterSlugs.length + syllabusModule.missing.length,
      missingCount: syllabusModule.missing.length,
    };
  });
}
