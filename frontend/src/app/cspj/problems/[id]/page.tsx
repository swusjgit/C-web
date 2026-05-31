import Link from "next/link";
import { notFound } from "next/navigation";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { cspjProblems, getProblemById } from "@/data/cspjProblems";
import { getChapterBySlug } from "@/lib/staticChapters";

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

export const dynamicParams = false;

export function generateStaticParams() {
  return cspjProblems.map((problem) => ({ id: problem.id }));
}

function SampleBlock({ title, value }: { title: string; value: string }) {
  return (
    <div>
      <div className="mb-2 text-sm font-semibold text-[#1e293b]">{title}</div>
      <pre className="overflow-x-auto rounded-lg bg-[#0f172a] p-4 text-sm leading-6 text-[#e2e8f0]">
        <code>{value}</code>
      </pre>
    </div>
  );
}

export default async function ProblemDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const problem = getProblemById(id);

  if (!problem) {
    notFound();
  }

  const diff = difficultyConfig[problem.difficulty];
  const relatedChapters = problem.relatedSlugs
    .map((slug) => getChapterBySlug(slug))
    .filter(Boolean);

  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:px-6 lg:px-8">
      <div className="mb-6 flex items-center gap-2 text-sm text-[#94a3b8]">
        <Link href="/cspj/problems" className="hover:text-[#2563eb]">精选题单</Link>
        <span>/</span>
        <span className="font-mono text-[#64748b]">{problem.id}</span>
      </div>

      <header className="mb-8 rounded-xl border border-[#e2e8f0] bg-white p-6">
        <div className="mb-4 flex flex-wrap items-center gap-2">
          <Badge variant={diff.variant}>{diff.label}</Badge>
          <Badge variant="outline">{problem.stage}</Badge>
          <Badge variant="secondary">{problem.source}</Badge>
        </div>
        <h1 className="text-2xl font-bold leading-tight text-[#0f172a] sm:text-3xl">
          {problem.id}. {problem.title}
        </h1>
        <p className="mt-3 text-sm leading-6 text-[#64748b]">{problem.objective}</p>
        <div className="mt-4 flex flex-wrap gap-2">
          {problem.tags.map((tag) => (
            <span key={tag} className="rounded-full bg-[#f8fafc] px-3 py-1 text-xs text-[#64748b]">
              #{tag}
            </span>
          ))}
        </div>
      </header>

      <div className="grid gap-6 lg:grid-cols-[1fr_280px]">
        <main className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>题目描述</CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              <p className="text-sm leading-7 text-[#334155]">{problem.prompt}</p>
              <section>
                <h2 className="mb-2 text-base font-semibold text-[#0f172a]">输入格式</h2>
                <p className="text-sm leading-7 text-[#334155]">{problem.input}</p>
              </section>
              <section>
                <h2 className="mb-2 text-base font-semibold text-[#0f172a]">输出格式</h2>
                <p className="text-sm leading-7 text-[#334155]">{problem.output}</p>
              </section>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>样例</CardTitle>
            </CardHeader>
            <CardContent className="grid gap-5 md:grid-cols-2">
              <SampleBlock title="样例输入" value={problem.sampleInput} />
              <SampleBlock title="样例输出" value={problem.sampleOutput} />
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>思路提示</CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2">
                {problem.hints.map((hint) => (
                  <li key={hint} className="flex gap-2 text-sm leading-6 text-[#334155]">
                    <span className="mt-2 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-[#2563eb]" />
                    <span>{hint}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </main>

        <aside className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle>练习方式</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3 text-sm leading-6 text-[#475569]">
              <p>先在本地 IDE 写代码，用样例手动测试，再尝试自己补 2-3 组边界数据。</p>
              <p>自动评测模块接入前，这里作为题面和训练目标索引使用。</p>
            </CardContent>
          </Card>

          {relatedChapters.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle>关联章节</CardTitle>
              </CardHeader>
              <CardContent className="space-y-2">
                {relatedChapters.map((chapter) => (
                  chapter && (
                    <Link
                      key={chapter.slug}
                      href={`/cspj/tutorials/${chapter.slug}`}
                      className="block rounded-lg border border-[#e2e8f0] px-3 py-2 text-sm text-[#475569] hover:border-[#2563eb] hover:text-[#2563eb]"
                    >
                      {chapter.order}. {chapter.title}
                    </Link>
                  )
                ))}
              </CardContent>
            </Card>
          )}

          <Link href="/cspj/problems">
            <Button variant="outline" className="w-full">返回题单</Button>
          </Link>
        </aside>
      </div>
    </div>
  );
}
