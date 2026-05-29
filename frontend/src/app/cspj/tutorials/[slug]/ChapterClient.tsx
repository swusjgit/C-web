"use client";

import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import type { Chapter } from "@/lib/staticChapters";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { atomDark } from "react-syntax-highlighter/dist/cjs/styles/prism";

const DIFF_NAMES: Record<number, string> = { 1: "基础", 2: "入门", 3: "进阶", 4: "提高", 5: "竞赛" };
const DIFF_COLORS: Record<number, string> = {
  1: "bg-green-100 text-green-700",
  2: "bg-blue-100 text-blue-700",
  3: "bg-yellow-100 text-yellow-700",
  4: "bg-orange-100 text-orange-700",
  5: "bg-red-100 text-red-700",
};

// 渲染 Markdown 内容（支持图片、标题、列表、代码块、加粗）
function renderContent(content: string) {
  // 统一处理 \r\n（Windows）和 \r（旧Mac）行尾
  const lines = content.replace(/\r\n?|\n/g, "\n").split("\n");
  const result: React.ReactNode[] = [];
  let i = 0;
  let key = 0;

  while (i < lines.length) {
    const line = lines[i];

    // 代码块开始/结束
    if (line.startsWith("```")) {
      if (result.length > 0 && (result[result.length - 1] as any)?.type?.name === "div") {
        // 关闭代码块
        const lastDiv = result[result.length - 1] as any;
        if (lastDiv?.props?.className === "code-block") {
          result.pop();
          i++;
          continue;
        }
      }
      // 开始代码块
      const lang = line.slice(3).trim() || "cpp";
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].startsWith("```")) {
        codeLines.push(lines[i]);
        i++;
      }
      result.push(
        <div key={`code-${key++}`} className="code-block">
          <div className="my-5 rounded-xl overflow-hidden">
            <SyntaxHighlighter
              style={atomDark}
              language={lang}
              customStyle={{ margin: 0, borderRadius: "0.75rem", fontSize: "0.875rem" }}
              showLineNumbers={codeLines.length > 5}
            >
              {codeLines.join("\n")}
            </SyntaxHighlighter>
          </div>
        </div>
      );
      i++;
      continue;
    }

    // 空行
    if (line.trim() === "") {
      i++;
      continue;
    }

    // 二级标题
    if (line.startsWith("## ")) {
      result.push(
        <h2 key={`h2-${key++}`} className="text-xl font-bold text-[#0f172a] mt-10 mb-4 pb-2 border-b border-[#e2e8f0]">
          {renderInline(line.slice(3))}
        </h2>
      );
      i++;
      continue;
    }

    // 三级标题
    if (line.startsWith("### ")) {
      result.push(
        <h3 key={`h3-${key++}`} className="text-base font-semibold text-[#1e293b] mt-7 mb-2">
          {renderInline(line.slice(4))}
        </h3>
      );
      i++;
      continue;
    }

    // 列表项
    if (line.startsWith("- ") || line.startsWith("* ")) {
      result.push(
        <li key={`li-${key++}`} className="text-[#334155] leading-7 ml-4 mb-1">
          {renderInline(line.slice(2))}
        </li>
      );
      i++;
      continue;
    }

    // Markdown 图片语法：![](url)
    const imgMatch = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
    if (imgMatch) {
      result.push(
        <img
          key={`img-${key++}`}
          src={imgMatch[2]}
          alt={imgMatch[1]}
          style={{ width: "100%", maxWidth: "700px", height: "auto", borderRadius: "0.75rem", marginTop: "1rem", marginBottom: "1rem", display: "block" }}
          onError={(e) => { (e.target as HTMLImageElement).style.display = "none"; }}
        />
      );
      i++;
      continue;
    }

    // 独立 HTML img 标签
    if (line.trim().startsWith("<img")) {
      result.push(
        <div key={`html-${key++}`} dangerouslySetInnerHTML={{ __html: line.trim() }} />
      );
      i++;
      continue;
    }

    // 普通段落
    result.push(
      <p key={`p-${key++}`} className="text-[#334155] leading-7 mb-4">
        {renderInline(line)}
      </p>
    );
    i++;
  }

  return result;
}

// 渲染行内元素（加粗、行内代码）
function renderInline(text: string): React.ReactNode[] {
  const parts: React.ReactNode[] = [];
  let remaining = text;
  let key = 0;

  while (remaining) {
    // 优先匹配更短的标记，避免无限循环
    // 图片（整行）
    const imgM = remaining.match(/!\[([^\]]*)\]\(([^)]+)\)/);
    // 行内代码
    const codeM = remaining.match(/`([^`]+)`/);
    // 加粗
    const boldM = remaining.match(/\*\*([^*]+)\*\*/);

    let earliest: { match: RegExpMatchArray; type: string } | null = null;
    if (imgM) earliest = { match: imgM, type: "img" };
    if (codeM && (!earliest || (codeM.index ?? 0) < earliest.match.index!)) earliest = { match: codeM, type: "code" };
    if (boldM && (!earliest || (boldM.index ?? 0) < earliest.match.index!)) earliest = { match: boldM, type: "bold" };

    if (!earliest) {
      if (remaining) parts.push(remaining);
      break;
    }

    const { match, type } = earliest;
    const idx = match.index!;

    if (idx > 0) {
      parts.push(remaining.slice(0, idx));
    }

    if (type === "img") {
      parts.push(
        <img
          key={`inline-img-${key++}`}
          src={match[2]}
          alt={match[1]}
          style={{ width: "100%", maxWidth: "700px", height: "auto", borderRadius: "0.75rem", marginTop: "0.5rem", marginBottom: "0.5rem", display: "block" }}
          onError={(e) => { (e.target as HTMLImageElement).style.display = "none"; }}
        />
      );
    } else if (type === "code") {
      parts.push(
        <code key={`code-${key++}`} className="text-[#be185d] bg-[#fdf4ff] px-1.5 py-0.5 rounded text-sm">
          {match[1]}
        </code>
      );
    } else if (type === "bold") {
      parts.push(<strong key={`bold-${key++}`} className="font-semibold text-[#0f172a]">{match[1]}</strong>);
    }

    remaining = remaining.slice(idx + match[0].length);
  }

  return parts;
}

export default function ChapterClient({ chapter }: { chapter: Chapter | null }) {
  if (!chapter) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <h1 className="text-xl font-bold text-[#1e293b] mb-4">章节不存在</h1>
        <Link href="/cspj/tutorials">
          <Button variant="outline">← 返回教程目录</Button>
        </Link>
      </div>
    );
  }

  return (
    <article className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* 面包屑 */}
      <div className="flex items-center gap-2 text-sm text-[#94a3b8] mb-6">
        <Link href="/cspj/tutorials" className="hover:text-[#2563eb] transition-colors">
          教程目录
        </Link>
        <span>/</span>
        <span className="text-[#64748b]">{chapter.category_name}</span>
        <span>/</span>
        <span className="text-[#334155] truncate">{chapter.title}</span>
      </div>

      {/* 标题 */}
      <header className="mb-8 pb-6 border-b border-[#e2e8f0]">
        <h1 className="text-2xl sm:text-3xl font-bold text-[#0f172a] leading-tight mb-3">
          {chapter.order}. {chapter.title}
        </h1>
        <div className="flex flex-wrap items-center gap-2">
          <Badge className={`text-xs ${DIFF_COLORS[chapter.difficulty]}`}>
            难度 {chapter.difficulty} · {DIFF_NAMES[chapter.difficulty]}
          </Badge>
          <Badge className="bg-[#f1f5f9] text-[#64748b] text-xs">
            {chapter.category_name}
          </Badge>
        </div>
      </header>

      {/* 正文 */}
      <div className="space-y-0">
        {renderContent(chapter.content)}
      </div>

      {/* 底部 */}
      <footer className="mt-10 pt-6 border-t border-[#e2e8f0]">
        <Link href="/cspj/tutorials">
          <Button variant="outline" size="sm" className="text-[#64748b]">
            ← 返回教程目录
          </Button>
        </Link>
      </footer>
    </article>
  );
}
