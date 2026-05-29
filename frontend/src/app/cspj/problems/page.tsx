import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";

const problems = [
  {
    id: "P1001",
    title: "A+B Problem",
    difficulty: 1,
    tags: ["入门", "模拟"],
    acceptRate: 89,
  },
  {
    id: "P1002",
    title: "大整数加法",
    difficulty: 2,
    tags: ["高精度", "字符串"],
    acceptRate: 76,
  },
  {
    id: "P1003",
    title: "快速排序",
    difficulty: 3,
    tags: ["排序", "分治"],
    acceptRate: 68,
  },
  {
    id: "P1004",
    title: "01背包问题",
    difficulty: 4,
    tags: ["动态规划", "背包"],
    acceptRate: 55,
  },
  {
    id: "P1005",
    title: "迷宫最短路",
    difficulty: 4,
    tags: ["BFS", "图论"],
    acceptRate: 52,
  },
  {
    id: "P1006",
    title: "完全背包问题",
    difficulty: 4,
    tags: ["动态规划", "背包"],
    acceptRate: 48,
  },
  {
    id: "P1007",
    title: "图的深度优先遍历",
    difficulty: 3,
    tags: ["DFS", "图论"],
    acceptRate: 63,
  },
  {
    id: "P1008",
    title: "二叉树遍历",
    difficulty: 3,
    tags: ["二叉树", "数据结构"],
    acceptRate: 61,
  },
  {
    id: "P1009",
    title: "栈的应用",
    difficulty: 2,
    tags: ["栈", "数据结构"],
    acceptRate: 71,
  },
  {
    id: "P1010",
    title: "CSP-J 2023 T1",
    difficulty: 2,
    tags: ["历年真题", "模拟"],
    acceptRate: 72,
  },
  {
    id: "P1011",
    title: "CSP-J 2023 T2",
    difficulty: 3,
    tags: ["历年真题", "贪心"],
    acceptRate: 58,
  },
  {
    id: "P1012",
    title: "CSP-J 2023 T4",
    difficulty: 5,
    tags: ["历年真题", "搜索", "DP"],
    acceptRate: 31,
  },
];

const difficultyConfig: Record<number, { label: string; variant: "success" | "info" | "warning" | "default" | "secondary" }> = {
  1: { label: "入门", variant: "success" },
  2: { label: "普及-", variant: "info" },
  3: { label: "普及/普及+", variant: "secondary" },
  4: { label: "普及+/提高", variant: "warning" },
  5: { label: "提高+", variant: "default" },
};

export default function ProblemsPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-[#0f172a] mb-1">在线题库</h1>
        <p className="text-sm text-[#64748b]">
          共 {problems.length} 道题目，涵盖 CSP-J 所有知识点
        </p>
      </div>

      {/* 筛选栏 */}
      <div className="flex flex-wrap gap-2 mb-6">
        <Badge variant="default" className="cursor-pointer">全部</Badge>
        {[1, 2, 3, 4, 5].map((d) => (
          <Badge key={d} variant="outline" className="cursor-pointer hover:bg-[#f1f5f9]">
            难度{d}
          </Badge>
        ))}
      </div>

      {/* 题目列表 */}
      <div className="space-y-3">
        {problems.map((problem) => {
          const diff = difficultyConfig[problem.difficulty];
          return (
            <Link key={problem.id} href={`/cspj/problems/${problem.id}`} className="block group">
              <Card className="hover:border-[#2563eb] hover:shadow-sm transition-all">
                <CardContent className="p-4 flex items-center gap-4">
                  <span className="font-mono text-sm text-[#64748b] w-16">{problem.id}</span>
                  <div className="flex-1 min-w-0">
                    <h3 className="font-medium text-[#0f172a] group-hover:text-[#2563eb] truncate">
                      {problem.title}
                    </h3>
                    <div className="flex items-center gap-2 mt-0.5">
                      {problem.tags.map((tag) => (
                        <span key={tag} className="text-xs text-[#94a3b8]">#{tag}</span>
                      ))}
                    </div>
                  </div>
                  <div className="flex items-center gap-3 flex-shrink-0">
                    <Badge variant={diff.variant} className="text-xs">
                      {diff.label}
                    </Badge>
                    <span className="text-xs text-[#64748b] w-12 text-right">
                      {problem.acceptRate}% AC
                    </span>
                  </div>
                </CardContent>
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
