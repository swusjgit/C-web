import type { Metadata } from "next";
import Link from "next/link";
import {
  Archive,
  ArrowRight,
  BookOpenCheck,
  Download,
  FileText,
  FolderOpen,
  GraduationCap,
  Layers,
  Library,
  NotebookTabs,
  Target,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { downloadResources, type DownloadResource } from "@/data/resources";
import { assetPath } from "@/lib/assetPath";

export const metadata: Metadata = {
  title: "资料下载 | 数据谷中学C++学习网站",
  description: "CSP-J 备考资料下载，包括真题整理、答案解析和专题课件。",
};

const categoryCopy = {
  真题资料: {
    eyebrow: "真题与订正",
    description: "适合阶段测评后定位题目、核对答案、整理错题。",
    icon: NotebookTabs,
  },
  专题课件: {
    eyebrow: "课堂讲义",
    description: "覆盖 C++ 基础、数论、树图、排列组合等一轮专题。",
    icon: GraduationCap,
  },
} satisfies Record<DownloadResource["category"], { eyebrow: string; description: string; icon: typeof NotebookTabs }>;

const accentStyles = {
  blue: {
    surface: "bg-blue-50 text-blue-700 border-blue-100",
    bar: "bg-[#2563eb]",
    hover: "hover:border-blue-300",
  },
  emerald: {
    surface: "bg-emerald-50 text-emerald-700 border-emerald-100",
    bar: "bg-emerald-500",
    hover: "hover:border-emerald-300",
  },
  amber: {
    surface: "bg-amber-50 text-amber-700 border-amber-100",
    bar: "bg-amber-500",
    hover: "hover:border-amber-300",
  },
  cyan: {
    surface: "bg-cyan-50 text-cyan-700 border-cyan-100",
    bar: "bg-cyan-500",
    hover: "hover:border-cyan-300",
  },
  indigo: {
    surface: "bg-indigo-50 text-indigo-700 border-indigo-100",
    bar: "bg-indigo-500",
    hover: "hover:border-indigo-300",
  },
} satisfies Record<DownloadResource["accent"], { surface: string; bar: string; hover: string }>;

const resourceStats = [
  { label: "全部资料", value: `${downloadResources.length} 份`, icon: Library },
  { label: "专题课件", value: `${downloadResources.filter((item) => item.category === "专题课件").length} 份`, icon: GraduationCap },
  { label: "真题资料", value: `${downloadResources.filter((item) => item.category === "真题资料").length} 份`, icon: NotebookTabs },
  { label: "文件体量", value: "约 35 MB", icon: Archive },
];

const categoryOrder: DownloadResource["category"][] = ["专题课件", "真题资料"];
const featuredResource = downloadResources.find((resource) => resource.featured) ?? downloadResources[0];

function ResourceCard({ resource }: { resource: DownloadResource }) {
  const styles = accentStyles[resource.accent];

  return (
    <Card className={`relative overflow-hidden transition-all hover:-translate-y-0.5 hover:shadow-md ${styles.hover}`}>
      <div className={`absolute inset-x-0 top-0 h-1 ${styles.bar}`} />
      <CardContent className="p-5">
        <div className="mb-4 flex items-start justify-between gap-4">
          <div className="flex min-w-0 gap-3">
            <div className={`flex h-11 w-11 flex-shrink-0 items-center justify-center rounded-lg border ${styles.surface}`}>
              <FileText className="h-5 w-5" />
            </div>
            <div className="min-w-0">
              <div className="mb-1 flex flex-wrap gap-2">
                <Badge variant="secondary">{resource.type}</Badge>
                <Badge variant="outline">{resource.stage}</Badge>
              </div>
              <h3 className="text-base font-semibold leading-6 text-[#0f172a]">{resource.title}</h3>
            </div>
          </div>
        </div>

        <p className="min-h-[48px] text-sm leading-6 text-[#64748b]">{resource.description}</p>

        <div className="mt-4 flex flex-wrap gap-2">
          {resource.tags.map((tag) => (
            <span key={tag} className="rounded-full bg-[#f1f5f9] px-2.5 py-1 text-xs text-[#475569]">
              {tag}
            </span>
          ))}
        </div>

        <div className="mt-5 flex flex-col gap-3 border-t border-[#e2e8f0] pt-4 sm:flex-row sm:items-center sm:justify-between">
          <div className="text-xs leading-5 text-[#64748b]">
            <div className="font-medium text-[#334155]">{resource.size}</div>
            <div className="break-all">{resource.fileName}</div>
          </div>
          <Button asChild className="w-full bg-[#2563eb] hover:bg-[#1d4ed8] sm:w-auto">
            <a href={assetPath(resource.href)} download={resource.fileName}>
              <Download />
              下载
            </a>
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}

export default function ResourcesPage() {
  return (
    <div className="bg-[#f8fafc]">
      <section className="border-b border-[#dbeafe] bg-white">
        <div className="mx-auto grid max-w-7xl gap-8 px-4 py-10 sm:px-6 lg:grid-cols-[1.1fr_0.9fr] lg:px-8">
          <div>
            <Badge variant="info" className="mb-4">
              CSP-J 资料库
            </Badge>
            <h1 className="mb-3 text-3xl font-bold text-[#0f172a]">资料</h1>
            <p className="max-w-2xl text-sm leading-6 text-[#64748b]">
              这里集中整理 CSP-J 一轮备考资料，包含专题课件、真题索引和答案解析。
              学生可以按专题复习，老师也可以直接用于课堂讲评和阶段复盘。
            </p>

            <div className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
              {resourceStats.map((stat) => {
                const Icon = stat.icon;
                return (
                  <div key={stat.label} className="rounded-lg border border-[#e2e8f0] bg-[#f8fafc] p-3">
                    <div className="mb-2 flex items-center gap-2 text-xs font-medium text-[#64748b]">
                      <Icon className="h-4 w-4 text-[#2563eb]" />
                      {stat.label}
                    </div>
                    <div className="text-lg font-bold text-[#0f172a]">{stat.value}</div>
                  </div>
                );
              })}
            </div>

            <div className="mt-6 flex flex-wrap gap-3">
              <Link href="/cspj/tutorials">
                <Button variant="outline" className="border-[#cbd5e1]">
                  <BookOpenCheck />
                  配合教程学习
                </Button>
              </Link>
              <Link href="/cspj/problems">
                <Button variant="outline" className="border-[#cbd5e1]">
                  <ArrowRight />
                  进入训练题库
                </Button>
              </Link>
            </div>
          </div>

          <div className="rounded-xl border border-[#c7d2fe] bg-gradient-to-br from-[#eff6ff] via-white to-[#ecfeff] p-6">
            <div className="mb-5 flex items-center justify-between gap-4">
              <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-white text-[#2563eb] shadow-sm">
                <Target className="h-6 w-6" />
              </div>
              <Badge variant="success">推荐先看</Badge>
            </div>
            <div className="mb-2 text-xs font-semibold text-[#2563eb]">{featuredResource.stage}</div>
            <h2 className="mb-3 text-xl font-bold leading-7 text-[#0f172a]">{featuredResource.title}</h2>
            <p className="mb-5 text-sm leading-6 text-[#475569]">{featuredResource.description}</p>
            <div className="mb-6 flex flex-wrap gap-2">
              {featuredResource.tags.map((tag) => (
                <span key={tag} className="rounded-full bg-white px-2.5 py-1 text-xs text-[#475569] shadow-sm">
                  {tag}
                </span>
              ))}
            </div>
            <Button asChild className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]">
              <a href={assetPath(featuredResource.href)} download={featuredResource.fileName}>
                <Download />
                下载主课件
              </a>
            </Button>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid gap-4 md:grid-cols-2">
          {categoryOrder.map((category) => {
            const copy = categoryCopy[category];
            const Icon = copy.icon;
            const count = downloadResources.filter((resource) => resource.category === category).length;

            return (
              <div key={category} className="rounded-lg border border-[#e2e8f0] bg-white p-5">
                <div className="mb-3 flex items-center gap-3">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-[#f1f5f9] text-[#2563eb]">
                    <Icon className="h-5 w-5" />
                  </div>
                  <div>
                    <div className="text-xs font-semibold text-[#2563eb]">{copy.eyebrow}</div>
                    <h2 className="text-base font-bold text-[#0f172a]">{category}</h2>
                  </div>
                </div>
                <p className="text-sm leading-6 text-[#64748b]">{copy.description}</p>
                <div className="mt-4 flex items-center gap-2 text-xs font-medium text-[#475569]">
                  <Layers className="h-4 w-4 text-[#2563eb]" />
                  {count} 份资料
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {categoryOrder.map((category) => {
        const copy = categoryCopy[category];
        const resources = downloadResources.filter((resource) => resource.category === category);

        return (
          <section key={category} className="mx-auto max-w-7xl px-4 pb-10 sm:px-6 lg:px-8">
            <div className="mb-5 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
              <div>
                <div className="mb-1 text-xs font-semibold text-[#2563eb]">{copy.eyebrow}</div>
                <h2 className="text-xl font-bold text-[#0f172a]">{category}</h2>
                <p className="mt-1 text-sm text-[#64748b]">{copy.description}</p>
              </div>
              <Badge variant="outline">{resources.length} 份</Badge>
            </div>

            <div className="grid gap-5 lg:grid-cols-2">
              {resources.map((resource) => (
                <ResourceCard key={resource.href} resource={resource} />
              ))}
            </div>
          </section>
        );
      })}

      <section className="border-t border-[#e2e8f0] bg-white">
        <div className="mx-auto flex max-w-7xl flex-col gap-4 px-4 py-8 sm:px-6 md:flex-row md:items-center md:justify-between lg:px-8">
          <div className="flex items-start gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-[#eff6ff] text-[#2563eb]">
              <FolderOpen className="h-5 w-5" />
            </div>
            <div>
              <h2 className="text-base font-semibold text-[#0f172a]">资料会随网站一起发布</h2>
              <p className="mt-1 text-sm text-[#64748b]">本页文件已放入静态资源目录，GitHub Pages 部署后可以外网下载。</p>
            </div>
          </div>
          <Link href="/cspj">
            <Button variant="outline" className="border-[#cbd5e1]">
              返回 CSP-J 专区
            </Button>
          </Link>
        </div>
      </section>
    </div>
  );
}
