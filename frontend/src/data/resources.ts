export type DownloadResource = {
  title: string;
  description: string;
  fileName: string;
  href: string;
  size: string;
  type: "Word 文档" | "PDF 课件";
  category: "真题资料" | "专题课件";
  stage: string;
  accent: "blue" | "emerald" | "amber" | "cyan" | "indigo";
  featured?: boolean;
  tags: string[];
};

export const downloadResources: DownloadResource[] = [
  {
    title: "CSP-J 一轮真题整理索引（2019-2025）",
    description: "按年份整理 CSP-J 一轮真题入口，适合课前布置、错题定位和阶段复盘。",
    fileName: "csp-j-2019-2025-round1-problem-index.docx",
    href: "/downloads/csp-j-2019-2025-round1-problem-index.docx",
    size: "约 41 KB",
    type: "Word 文档",
    category: "真题资料",
    stage: "一轮复盘",
    accent: "blue",
    tags: ["真题索引", "2019-2025", "一轮复习"],
  },
  {
    title: "CSP-J 一轮答案解析汇总（2019-2025）",
    description: "配套答案解析资料，用于讲评订正、查漏补缺和自我核对。",
    fileName: "csp-j-2019-2025-round1-answer-analysis.docx",
    href: "/downloads/csp-j-2019-2025-round1-answer-analysis.docx",
    size: "约 40 KB",
    type: "Word 文档",
    category: "真题资料",
    stage: "订正讲评",
    accent: "emerald",
    tags: ["答案解析", "2019-2025", "订正讲评"],
  },
  {
    title: "筛选素数",
    description: "围绕素数筛法建立数论基础，适合衔接循环、数组和复杂度意识。",
    fileName: "csp-j-prime-sieve.pdf",
    href: "/downloads/csp-j-prime-sieve.pdf",
    size: "约 2.7 MB",
    type: "PDF 课件",
    category: "专题课件",
    stage: "数论入门",
    accent: "cyan",
    tags: ["素数", "筛法", "数组"],
  },
  {
    title: "数论专题",
    description: "整理 gcd、lcm、整除、质因数等常见考点，适合专题课集中突破。",
    fileName: "csp-j-number-theory.pdf",
    href: "/downloads/csp-j-number-theory.pdf",
    size: "约 4.3 MB",
    type: "PDF 课件",
    category: "专题课件",
    stage: "专题提升",
    accent: "indigo",
    tags: ["gcd/lcm", "整除", "质因数"],
  },
  {
    title: "CSP-J C++ 基础知识",
    description: "覆盖 CSP-J 所需 C++ 基础语法与常用知识，是一轮复习的主干课件。",
    fileName: "csp-j-cpp-basics.pdf",
    href: "/downloads/csp-j-cpp-basics.pdf",
    size: "约 17 MB",
    type: "PDF 课件",
    category: "专题课件",
    stage: "基础主线",
    accent: "blue",
    featured: true,
    tags: ["C++ 基础", "语法", "一轮主线"],
  },
  {
    title: "树与图专题",
    description: "从树、图的基本概念进入遍历与建模，为后续搜索题打基础。",
    fileName: "csp-j-tree-graph.pdf",
    href: "/downloads/csp-j-tree-graph.pdf",
    size: "约 8.8 MB",
    type: "PDF 课件",
    category: "专题课件",
    stage: "结构建模",
    accent: "emerald",
    tags: ["树", "图", "遍历"],
  },
  {
    title: "CSP-J 排列组合",
    description: "梳理计数思想和排列组合基础，帮助学生处理简单计数与枚举题。",
    fileName: "csp-j-combinatorics.pdf",
    href: "/downloads/csp-j-combinatorics.pdf",
    size: "约 2.3 MB",
    type: "PDF 课件",
    category: "专题课件",
    stage: "计数思维",
    accent: "amber",
    tags: ["排列组合", "计数", "枚举"],
  },
];
