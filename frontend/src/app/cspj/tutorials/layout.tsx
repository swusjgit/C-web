"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { getChapterGroups, type ChapterGroup as Group } from "@/lib/staticChapters";

const CATEGORY_COLORS: Record<string, string> = {
  basics: "text-emerald-500",
  cpp: "text-blue-500",
  "data-structure": "text-purple-500",
  algorithm: "text-orange-500",
  math: "text-pink-500",
};

const CATEGORY_DOT_COLORS: Record<string, string> = {
  basics: "bg-emerald-500",
  cpp: "bg-blue-500",
  "data-structure": "bg-purple-500",
  algorithm: "bg-orange-500",
  math: "bg-pink-500",
};

export default function TutorialsLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [groups, setGroups] = useState<Group[]>([]);
  const [expandedCats, setExpandedCats] = useState<Record<string, boolean>>({});
  const [sidebarOpen, setSidebarOpen] = useState(false);

  useEffect(() => {
    const sorted = getChapterGroups();
    setGroups(sorted);
    const expanded: Record<string, boolean> = {};
    for (const g of sorted) expanded[g.slug] = true;
    setExpandedCats(expanded);
  }, []);

  const currentSlug = pathname.replace("/cspj/tutorials/", "");
  const currentGroup = groups.find((g) => g.chapters.some((c) => c.slug === currentSlug));

  const toggleCat = (slug: string) => {
    setExpandedCats((prev) => ({ ...prev, [slug]: !prev[slug] }));
  };

  return (
    <div className="flex min-h-[calc(100vh-80px)]">
      {/* 移动端遮罩 */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black/30 z-20 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* 侧边栏 - 桌面端固定 */}
      <aside
        className={`
          fixed lg:sticky top-20 left-0 z-30 w-72 max-w-[85vw] h-[calc(100vh-80px)] overflow-y-auto bg-white border-r border-[#e2e8f0]
          transform transition-transform duration-200
          ${sidebarOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0 lg:static lg:z-auto"}
        `}
      >
        {/* 移动端关闭按钮 */}
        <div className="lg:hidden flex items-center justify-between p-4 border-b border-[#e2e8f0]">
          <span className="text-sm font-medium text-[#334155]">章节导航</span>
          <button onClick={() => setSidebarOpen(false)} className="p-1 text-[#64748b] hover:text-[#334155]">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="p-4 flex-1">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-xs font-semibold text-[#94a3b8] uppercase tracking-wider">教程目录</span>
          </div>

          {groups.length === 0 ? (
            <div className="space-y-3">
              {[1, 2, 3, 4, 5].map((i) => (
                <div key={i} className="animate-pulse">
                  <div className="h-4 bg-[#f1f5f9] rounded w-24 mb-2" />
                  <div className="h-3 bg-[#f8fafc] rounded w-32 ml-3" />
                </div>
              ))}
            </div>
          ) : (
            <nav className="space-y-1">
              {groups.map((group) => {
                const isActive = group.slug === currentGroup?.slug;
                const isExpanded = expandedCats[group.slug] ?? true;

                return (
                  <div key={group.slug} className="mb-1">
                    <button
                      onClick={() => toggleCat(group.slug)}
                      className={`w-full flex items-center gap-2 px-2 py-1.5 rounded text-left text-sm font-medium transition-colors ${
                        isActive
                          ? `${CATEGORY_COLORS[group.slug]}`
                          : "text-[#64748b] hover:text-[#334155] hover:bg-[#f8fafc]"
                      }`}
                    >
                      <span className={`w-2 h-2 rounded-full shrink-0 ${CATEGORY_DOT_COLORS[group.slug]} ${isActive ? "opacity-100" : "opacity-50"}`} />
                      <span className="flex-1 truncate">{group.name}</span>
                      <svg
                        className={`w-3 h-3 shrink-0 transition-transform ${isExpanded ? "rotate-90" : ""}`}
                        fill="none" stroke="currentColor" viewBox="0 0 24 24"
                      >
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                      </svg>
                    </button>

                    {isExpanded && (
                      <div className="ml-4 mt-0.5 border-l-2 border-[#e2e8f0] pl-2 space-y-0.5">
                        {group.chapters.map((ch) => {
                          const isCurrent = ch.slug === currentSlug;
                          return (
                            <Link
                              key={ch.slug}
                              href={`/cspj/tutorials/${ch.slug}`}
                              onClick={() => setSidebarOpen(false)}
                              className={`block px-2 py-1 rounded text-xs transition-colors truncate ${
                                isCurrent
                                  ? "bg-[#eff6ff] text-[#2563eb] font-medium"
                                  : "text-[#64748b] hover:text-[#334155] hover:bg-[#f8fafc]"
                              }`}
                              title={ch.title}
                            >
                              <span className="text-[#94a3b8] mr-1">{ch.order}.</span>
                              {ch.title}
                            </Link>
                          );
                        })}
                      </div>
                    )}
                  </div>
                );
              })}
            </nav>
          )}
        </div>
      </aside>

      {/* 移动端打开侧边栏按钮 */}
      <button
        onClick={() => setSidebarOpen(true)}
        className="fixed bottom-6 left-4 z-20 lg:hidden bg-[#2563eb] text-white p-3 rounded-full shadow-lg"
        aria-label="打开目录"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      {/* 主内容 */}
      <main className="flex-1 min-w-0">{children}</main>
    </div>
  );
}
