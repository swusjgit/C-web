import Link from "next/link";
import Image from "next/image";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { chapterSummaries, getChapterGroups, type ChapterSummary as Chapter } from "@/lib/staticChapters";
import { getChapterSyllabusMeta, getSyllabusCoverage } from "@/data/cspjSyllabus";
import { assetPath } from "@/lib/assetPath";

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
  const coverage = getSyllabusCoverage(chapterSummaries);

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      {/* 顶部提示 */}
      <div className="mb-8 bg-white border border-[#dbeafe] rounded-lg overflow-hidden">
        <div className="grid gap-5 bg-[#eff6ff] p-5 md:grid-cols-[1fr_260px] md:items-center">
          <div>
            <Badge variant="info" className="mb-3">NOI 2025 入门级</Badge>
            <h1 className="text-xl font-bold text-[#0f172a] mb-2">教程中心</h1>
            <p className="text-sm text-[#1e40af] leading-6">
              按大纲模块组织现有 {chapterSummaries.length} 章内容。每章先给出学习目标和大纲位置，
              后续会逐步补齐例题、练习和测评。
            </p>
          </div>
          <div className="relative min-h-[140px] overflow-hidden rounded-lg border border-[#dbeafe] bg-white">
            <Image
              src={assetPath("/img/generated/cspj-roadmap-milestones.jpg")}
              alt="CSP-J 学习模块路线插图"
              fill
              sizes="(min-width: 768px) 260px, 100vw"
              className="object-cover"
            />
          </div>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-5 border-t border-[#dbeafe]">
          {coverage.map((item) => (
            <div key={item.slug} className="p-3 border-r last:border-r-0 border-[#e2e8f0]">
              <div className="text-xs font-semibold text-[#2563eb] mb-1">{item.code}</div>
              <div className="text-xs text-[#64748b] truncate">{item.name}</div>
              <div className="text-sm font-bold text-[#0f172a] mt-1">
                {item.availableCount}/{item.plannedCount}
              </div>
            </div>
          ))}
        </div>
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
                    const meta = getChapterSyllabusMeta(ch);
                    return (
                      <Link key={ch.slug} href={`/cspj/tutorials/${ch.slug}`}>
                        <Card
                          className={`h-full border-l-4 ${colors.border} hover:shadow-md hover:border-[#2563eb] transition-all cursor-pointer group`}
                        >
                          <CardContent className="p-4">
                            <div className="flex items-start justify-between gap-2 mb-2">
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
                            <div className="flex items-center gap-2 mb-2">
                              <Badge variant="outline" className="text-[11px] px-2 py-0">
                                {meta.code}
                              </Badge>
                              <span className="text-[11px] text-[#94a3b8] truncate">
                                {meta.label}
                              </span>
                            </div>
                            <p className="text-xs text-[#64748b] leading-5 line-clamp-2">
                              {meta.target}
                            </p>
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
