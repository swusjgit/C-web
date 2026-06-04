import Link from "next/link";
import Image from "next/image";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { cspjProblems, getProblemsByStage } from "@/data/cspjProblems";
import { assetPath } from "@/lib/assetPath";

const difficultyConfig: Record<
  number,
  { label: string; variant: "success" | "info" | "secondary" | "warning" | "default" }
> = {
  1: { label: "基础", variant: "success" },
  2: { label: "入门", variant: "info" },
  3: { label: "进阶", variant: "secondary" },
  4: { label: "提高", variant: "warning" },
  5: { label: "挑战", variant: "default" },
};

const practiceFlow = [
  "先看题面，圈出输入输出和样例变化",
  "用 1-2 组小数据手算，再决定变量和结构",
  "写完后补边界数据，确认空、极小、极大情况",
  "通过后复盘错因，把同类题归到一个知识点",
];

export default function ProblemsPage() {
  const stageGroups = getProblemsByStage();
  const tagCount = new Set(cspjProblems.flatMap((problem) => problem.tags)).size;

  return (
    <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="mb-8 grid gap-6 lg:grid-cols-[1fr_360px] lg:items-center">
        <div>
          <Badge variant="info" className="mb-3">CSP-J 入门级训练</Badge>
          <h1 className="text-2xl font-bold text-[#0f172a]">精选题单</h1>
          <p className="mt-2 max-w-2xl text-sm leading-6 text-[#64748b]">
            先按 NOI 2025 入门级大纲整理基础练习题，帮助你把教程知识点落到代码里。当前题目用于本地练习，在线提交和自动评测会在后续版本接入。
          </p>

          <div className="mt-6 grid grid-cols-3 gap-3 sm:max-w-[420px]">
            <div className="rounded-lg border border-[#e2e8f0] bg-white p-3 text-center">
              <div className="text-lg font-bold text-[#0f172a]">{cspjProblems.length}</div>
              <div className="mt-1 text-xs text-[#64748b]">道题目</div>
            </div>
            <div className="rounded-lg border border-[#e2e8f0] bg-white p-3 text-center">
              <div className="text-lg font-bold text-[#0f172a]">{stageGroups.length}</div>
              <div className="mt-1 text-xs text-[#64748b]">个主题</div>
            </div>
            <div className="rounded-lg border border-[#e2e8f0] bg-white p-3 text-center">
              <div className="text-lg font-bold text-[#0f172a]">{tagCount}</div>
              <div className="mt-1 text-xs text-[#64748b]">类标签</div>
            </div>
          </div>
        </div>

        <div className="relative min-h-[220px] overflow-hidden rounded-xl border border-[#e2e8f0] bg-white">
          <Image
            src={assetPath("/img/generated/cspj-practice-desk.jpg")}
            alt="CSP-J 练习场景插图"
            fill
            sizes="(min-width: 1024px) 360px, 100vw"
            className="object-cover"
          />
        </div>
      </div>

      <section className="mb-8 grid gap-3 rounded-xl border border-[#dbeafe] bg-[#eff6ff] p-4 md:grid-cols-4">
        {practiceFlow.map((item, index) => (
          <div key={item} className="flex gap-3">
            <span className="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-full bg-white font-mono text-xs font-semibold text-[#2563eb]">
              {index + 1}
            </span>
            <p className="text-sm leading-6 text-[#475569]">{item}</p>
          </div>
        ))}
      </section>

      <div className="mb-6 flex flex-wrap gap-2">
        {["语法", "数组", "字符串", "排序", "前缀和", "二分", "BFS", "DP", "gcd", "素数", "图遍历", "高精度"].map((tag) => (
          <Badge key={tag} variant="outline" className="bg-white text-[#475569]">
            {tag}
          </Badge>
        ))}
      </div>

      <div className="space-y-8">
        {stageGroups.map(({ stage, problems }) => (
          <section key={stage}>
            <div className="mb-3 flex items-center justify-between gap-4">
              <h2 className="text-lg font-semibold text-[#0f172a]">{stage}</h2>
              <span className="text-sm text-[#94a3b8]">{problems.length} 题</span>
            </div>

            <div className="space-y-3">
              {problems.map((problem) => {
                const diff = difficultyConfig[problem.difficulty];
                return (
                  <Link key={problem.id} href={`/cspj/problems/${problem.id}`} className="block group">
                    <Card className="transition-all hover:border-[#2563eb] hover:shadow-md">
                      <CardContent className="flex flex-col gap-4 p-4 sm:flex-row sm:items-center">
                        <span className="font-mono text-sm text-[#64748b] sm:w-16">{problem.id}</span>
                        <div className="min-w-0 flex-1">
                          <div className="flex flex-wrap items-center gap-2">
                            <h3 className="font-medium text-[#0f172a] group-hover:text-[#2563eb]">
                              {problem.title}
                            </h3>
                            <Badge variant={diff.variant} className="text-xs">
                              {diff.label}
                            </Badge>
                          </div>
                          <p className="mt-1 text-sm leading-6 text-[#64748b]">{problem.objective}</p>
                          <div className="mt-2 flex flex-wrap gap-2">
                            {problem.tags.map((tag) => (
                              <span key={tag} className="text-xs text-[#94a3b8]">#{tag}</span>
                            ))}
                          </div>
                        </div>
                        <span className="text-sm font-medium text-[#2563eb]">查看题面</span>
                      </CardContent>
                    </Card>
                  </Link>
                );
              })}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}
