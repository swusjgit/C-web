import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { chapterSummaries, getChapterGroups, type ChapterSummary as Chapter } from "@/lib/staticChapters";

interface Group {
  slug: string;
  name: string;
  chapters: Chapter[];
}

const CAT_COLORS: Record<string, { bg: string; text: string; border: string; dot: string }> = {
  basics: { bg: "bg-emerald-50", text: "text-emerald-700", border: "border-emerald-200", dot: "bg-emerald-500" },
  cpp: { bg: "bg-blue-50", text: "text-blue-700", border: "border-blue-200", dot: "bg-blue-500" },
  "data-structure": { bg: "bg-purple-50", text: "text-purple-700", border: "border-purple-200", dot: "bg-purple-500" },
  algorithm: { bg: "bg-orange-50", text: "text-orange-700", border: "border-orange-200", dot: "bg-orange-500" },
  math: { bg: "bg-pink-50", text: "text-pink-700", border: "border-pink-200", dot: "bg-pink-500" },
};

const DIFF_NAMES: Record<number, string> = { 1: "基础", 2: "入门", 3: "进阶", 4: "提高", 5: "竞赛" };
const DIFF_COLORS: Record<number, string> = {
  1: "bg-green-100 text-green-700",
  2: "bg-blue-100 text-blue-700",
  3: "bg-yellow-100 text-yellow-700",
  4: "bg-orange-100 text-orange-700",
  5: "bg-red-100 text-red-700",
};

export default function TutorialsPage() {
  const groups: Group[] = getChapterGroups();

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      {/* 顶部提示 */}
      <div className="mb-8 p-4 bg-[#eff6ff] rounded-xl border border-[#bfdbfe]">
        <p className="text-sm text-[#1e40af]">
          📖 点击左侧「目录」或下方分类卡片，开始学习。按 <strong>NOI 2025 大纲</strong> 编排，共{" "}
          <strong>{chapterSummaries.length}</strong> 章。
          {" "}每个分类均可展开查看章节列表。
        </p>
      </div>

      {groups.length === 0 ? (
        <div className="text-center py-12 text-[#64748b]">
          <p>暂无章节数据，请检查后端服务是否正常运行。</p>
        </div>
      ) : (
        <div className="space-y-8">
          {groups.map((group) => {
            const colors = CAT_COLORS[group.slug] || CAT_COLORS.cpp;
            return (
              <section key={group.slug}>
                {/* 分类标题 */}
                <div className="flex items-center gap-3 mb-4">
                  <span className={`w-3 h-3 rounded-full ${colors.dot}`} />
                  <h2 className={`text-lg font-bold ${colors.text}`}>{group.name}</h2>
                  <Badge variant="outline" className={`text-xs ${colors.text} ${colors.border}`}>
                    {group.chapters.length} 章
                  </Badge>
                </div>

                {/* 章节网格 */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                  {group.chapters.map((ch) => {
                    const diffColor = DIFF_COLORS[ch.difficulty] || DIFF_COLORS[1];
                    return (
                      <Link key={ch.slug} href={`/cspj/tutorials/${ch.slug}`}>
                        <Card
                          className={`h-full border-l-4 ${colors.border} hover:shadow-md hover:border-[#2563eb] transition-all cursor-pointer group`}
                        >
                          <CardContent className="p-4">
                            <div className="flex items-start justify-between gap-2">
                              <div className="flex-1 min-w-0">
                                <div className="flex items-center gap-1.5 mb-1">
                                  <span className="text-xs text-[#94a3b8]">{ch.order}.</span>
                                  <span className="text-sm font-medium text-[#1e293b] group-hover:text-[#2563eb] transition-colors truncate">
                                    {ch.title}
                                  </span>
                                </div>
                              </div>
                              <Badge className={`text-xs shrink-0 ${diffColor}`}>
                                d{ch.difficulty}
                              </Badge>
                            </div>
                          </CardContent>
                        </Card>
                      </Link>
                    );
                  })}
                </div>
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}
