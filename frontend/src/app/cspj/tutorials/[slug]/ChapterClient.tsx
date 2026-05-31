"use client";

import Image from "next/image";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { getChapterSyllabusMeta } from "@/data/cspjSyllabus";
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

function isTableSeparator(line: string) {
  return /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line);
}

function parseTableRow(line: string) {
  return line
    .trim()
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
}

function MarkdownImage({ alt, src, inline = false }: { alt: string; src: string; inline?: boolean }) {
  const image = (
    <Image
      src={src}
      alt={alt}
      width={1400}
      height={900}
      className="h-auto w-full object-contain"
      sizes="(max-width: 768px) 100vw, 880px"
      onError={(e) => {
        (e.target as HTMLImageElement).style.display = "none";
      }}
    />
  );

  if (inline) {
    return (
      <span className="my-2 block w-full max-w-[880px] overflow-hidden rounded-xl border border-[#e2e8f0] bg-white shadow-sm">
        {image}
      </span>
    );
  }

  return (
    <figure className="my-5 block w-full max-w-[880px] overflow-hidden rounded-xl border border-[#e2e8f0] bg-white shadow-sm">
      {image}
      {alt ? (
        <figcaption className="px-4 py-2 text-xs text-[#64748b]">
          {alt}
        </figcaption>
      ) : null}
    </figure>
  );
}

// 渲染 Markdown 内容（支持图片、标题、列表、表格、代码块、加粗）
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

    // 页面顶部已经有正式标题，正文里的一级标题不再重复显示。
    if (line.startsWith("# ")) {
      i++;
      continue;
    }

    // 分隔线
    if (/^\s*---+\s*$/.test(line)) {
      result.push(<hr key={`hr-${key++}`} className="my-8 border-[#e2e8f0]" />);
      i++;
      continue;
    }

    // Markdown 表格
    if (line.trim().startsWith("|") && lines[i + 1] && isTableSeparator(lines[i + 1])) {
      const headers = parseTableRow(line);
      const rows: string[][] = [];
      i += 2;

      while (i < lines.length && lines[i].trim().startsWith("|")) {
        rows.push(parseTableRow(lines[i]));
        i++;
      }

      result.push(
        <div key={`table-${key++}`} className="my-5 overflow-x-auto rounded-lg border border-[#e2e8f0] bg-white">
          <table className="w-full min-w-[520px] border-collapse text-sm">
            <thead className="bg-[#f8fafc]">
              <tr>
                {headers.map((header, index) => (
                  <th key={`${header}-${index}`} className="border-b border-[#e2e8f0] px-4 py-3 text-left font-semibold text-[#0f172a]">
                    {renderInline(header)}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((row, rowIndex) => (
                <tr key={`row-${rowIndex}`} className="border-t border-[#f1f5f9]">
                  {headers.map((_, cellIndex) => (
                    <td key={`cell-${rowIndex}-${cellIndex}`} className="px-4 py-3 align-top leading-6 text-[#334155]">
                      {renderInline(row[cellIndex] ?? "")}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
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

    // 无序列表
    if (line.startsWith("- ") || line.startsWith("* ")) {
      const items: string[] = [];
      while (i < lines.length && (lines[i].startsWith("- ") || lines[i].startsWith("* "))) {
        items.push(lines[i].slice(2));
        i++;
      }
      result.push(
        <ul key={`ul-${key++}`} className="mb-4 space-y-1.5 pl-5">
          {items.map((item, itemIndex) => (
            <li key={`${item}-${itemIndex}`} className="list-disc text-[#334155] leading-7">
              {renderInline(item)}
            </li>
          ))}
        </ul>
      );
      continue;
    }

    // 有序列表
    const orderedMatch = line.match(/^\d+\.\s+(.+)$/);
    if (orderedMatch) {
      const items: string[] = [];
      while (i < lines.length) {
        const itemMatch = lines[i].match(/^\d+\.\s+(.+)$/);
        if (!itemMatch) break;
        items.push(itemMatch[1]);
        i++;
      }
      result.push(
        <ol key={`ol-${key++}`} className="mb-4 space-y-1.5 pl-5">
          {items.map((item, itemIndex) => (
            <li key={`${item}-${itemIndex}`} className="list-decimal text-[#334155] leading-7">
              {renderInline(item)}
            </li>
          ))}
        </ol>
      );
      continue;
    }

    // Markdown 图片语法：![](url)
    const imgMatch = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
    if (imgMatch) {
      result.push(
        <MarkdownImage
          key={`img-${key++}`}
          src={imgMatch[2]}
          alt={imgMatch[1]}
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
        <MarkdownImage
          key={`inline-img-${key++}`}
          src={match[2]}
          alt={match[1]}
          inline
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

  const syllabusMeta = getChapterSyllabusMeta(chapter);

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
          <Badge variant="outline" className="text-xs">
            大纲 {syllabusMeta.code}
          </Badge>
        </div>
      </header>

      <section className="mb-8 rounded-xl border border-[#dbeafe] bg-[#eff6ff] p-5">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wide text-[#2563eb]">大纲定位</p>
            <h2 className="mt-1 text-lg font-semibold text-[#0f172a]">{syllabusMeta.label}</h2>
            <p className="mt-2 text-sm leading-6 text-[#475569]">{syllabusMeta.target}</p>
          </div>
          <Badge className="w-fit bg-white text-[#2563eb] shadow-sm">
            {syllabusMeta.code}
          </Badge>
        </div>

        <div className="mt-5 grid gap-4 md:grid-cols-[1.4fr_1fr]">
          <div>
            <p className="mb-2 text-sm font-semibold text-[#1e293b]">学完要能做到</p>
            <ul className="space-y-2">
              {syllabusMeta.checkpoints.map((checkpoint) => (
                <li key={checkpoint} className="flex gap-2 text-sm leading-6 text-[#334155]">
                  <span className="mt-2 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-[#2563eb]" />
                  <span>{checkpoint}</span>
                </li>
              ))}
            </ul>
          </div>
          <div className="rounded-lg bg-white p-4">
            <p className="mb-2 text-sm font-semibold text-[#1e293b]">练习建议</p>
            <p className="text-sm leading-6 text-[#475569]">{syllabusMeta.practice}</p>
          </div>
        </div>
      </section>

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
