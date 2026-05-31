import Link from "next/link";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { chapterSummaries } from "@/lib/staticChapters";
import { cspjProblems } from "@/data/cspjProblems";
import { studyPrinciples, syllabusModules, weeklyPracticePlan } from "@/data/cspjSyllabus";

const difficultyLevels = [
  {
    level: 1,
    name: "基础入门",
    desc: "计算机基础、IDE使用、数据类型、变量与常量、运算符、输入输出",
    color: "from-green-50 to-emerald-50",
    border: "border-green-200",
    badge: "success" as const,
    topics: ["Hello World", "变量类型", "分支结构", "循环结构"],
  },
  {
    level: 2,
    name: "语法进阶",
    desc: "数组、字符串处理、函数与递归、结构体、文件操作基础",
    color: "from-emerald-50 to-teal-50",
    border: "border-emerald-200",
    badge: "success" as const,
    topics: ["一维数组", "字符数组", "函数调用", "递归思想"],
  },
  {
    level: 3,
    name: "数据结构",
    desc: "链表、栈与队列、二叉树基础、图的存储与遍历、常用 STL 容器入门",
    color: "from-teal-50 to-cyan-50",
    border: "border-teal-200",
    badge: "info" as const,
    topics: ["vector", "stack/queue", "二叉树", "邻接表"],
  },
  {
    level: 4,
    name: "算法基础",
    desc: "枚举模拟、贪心递推、二分查找、高精度计算、基础排序和初等数论",
    color: "from-blue-50 to-indigo-50",
    border: "border-blue-200",
    badge: "secondary" as const,
    topics: ["排序算法", "前缀和", "gcd/lcm", "素数筛"],
  },
  {
    level: 5,
    name: "CSP-J 冲刺",
    desc: "DFS/BFS 搜索、Flood Fill、一维动态规划、背包和区间 DP 入门",
    color: "from-indigo-50 to-purple-50",
    border: "border-indigo-200",
    badge: "default" as const,
    topics: ["DFS", "BFS", "背包", "区间DP"],
  },
];

export default function HomePage() {
  return (
    <div>
      {/* ── Hero ── */}
      <section className="relative min-h-[560px] overflow-hidden text-white">
        <Image
          src="/img/generated/cspj-hero-classroom.jpg"
          alt=""
          fill
          priority
          sizes="100vw"
          className="object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-[#0f172a]/90 via-[#1e40af]/70 to-[#1e40af]/15" />

        <div className="relative mx-auto flex min-h-[560px] max-w-7xl items-center px-4 py-20 sm:px-6 lg:px-8">
          <div className="max-w-2xl">
            <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-white/15 px-3 py-1 text-sm text-blue-100">
              <span className="h-2 w-2 rounded-full bg-green-400" />
              2026 CSP-J 学习已开启
            </div>
            <h1 className="mb-4 text-4xl font-bold leading-tight md:text-5xl">
              备战 CSP-J
              <br />
              <span className="text-blue-200">按大纲稳步推进</span>
            </h1>
            <p className="mb-8 text-lg leading-relaxed text-blue-100">
              数据谷中学 C++ 学习平台，围绕 NOI 2025 入门级大纲整理学习路线、
              教程章节和基础训练题，帮助学生先把语法、思维和做题习惯打扎实。
            </p>
            <div className="flex flex-wrap gap-3">
              <Link href="/cspj">
                <Button size="lg" className="bg-white font-semibold text-[#2563eb] shadow-lg hover:bg-blue-50">
                  进入 CSP-J 专区
                </Button>
              </Link>
              <Link href="/cspj/problems">
                <Button
                  size="lg"
                  variant="outline"
                  className="border-white/30 bg-transparent text-white hover:bg-white/10"
                >
                  浏览题库
                </Button>
              </Link>
            </div>
            <div className="mt-8 grid max-w-xl grid-cols-3 gap-3 text-sm">
              <div className="rounded-lg border border-white/15 bg-white/10 p-3">
                <div className="font-semibold text-white">{chapterSummaries.length} 章</div>
                <div className="mt-1 text-xs text-blue-100">教程内容</div>
              </div>
              <div className="rounded-lg border border-white/15 bg-white/10 p-3">
                <div className="font-semibold text-white">{cspjProblems.length} 题</div>
                <div className="mt-1 text-xs text-blue-100">基础训练</div>
              </div>
              <div className="rounded-lg border border-white/15 bg-white/10 p-3">
                <div className="font-semibold text-white">{syllabusModules.length} 模块</div>
                <div className="mt-1 text-xs text-blue-100">大纲覆盖</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── CSP-J 专区入口 ── */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6 relative z-10">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            {
              icon: "📖",
              title: "教程中心",
              desc: `${chapterSummaries.length} 章大纲化教程`,
              href: "/cspj/tutorials",
              color: "bg-blue-50 border-blue-100 hover:border-blue-300",
            },
            {
              icon: "💻",
              title: "训练题库",
              desc: `${cspjProblems.length} 道首批精选题`,
              href: "/cspj/problems",
              color: "bg-green-50 border-green-100 hover:border-green-300",
            },
            {
              icon: "📝",
              title: "阶段测评",
              desc: "按模块安排限时练习",
              href: "/cspj",
              color: "bg-amber-50 border-amber-100 hover:border-amber-300",
            },
            {
              icon: "📊",
              title: "大纲路线",
              desc: "入门级 5 大模块覆盖",
              href: "/cspj",
              color: "bg-purple-50 border-purple-100 hover:border-purple-300",
            },
          ].map((item) => (
            <Link key={`${item.title}-${item.href}`} href={item.href} className="block">
              <Card className={`border transition-all hover:shadow-md hover:-translate-y-0.5 ${item.color}`}>
                <CardContent className="p-5 flex items-start gap-3">
                  <span className="text-2xl">{item.icon}</span>
                  <div>
                    <h3 className="font-semibold text-[#0f172a] mb-0.5">{item.title}</h3>
                    <p className="text-xs text-[#64748b]">{item.desc}</p>
                  </div>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </section>

      {/* ── 难度分级 ── */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-[#0f172a] mb-1">学习路径</h2>
          <p className="text-sm text-[#64748b]">从零基础到覆盖 CSP-J 入门级核心考点，5 个阶段循序渐进</p>
        </div>

        {/* 难度进度条 */}
        <div className="hidden md:flex items-center gap-1 mb-8 px-2">
          {[1, 2, 3, 4, 5].map((i) => (
            <div key={i} className="flex-1 flex items-center">
              <div
                className={`h-1.5 flex-1 rounded-full ${
                  i <= 5 ? "bg-gradient-to-r from-green-400 via-blue-500 to-indigo-500" : "bg-slate-200"
                }`}
              />
              <span className="ml-2 text-xs font-medium text-[#64748b] whitespace-nowrap">
                L{i}
              </span>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
          {difficultyLevels.map((item) => (
            <Link key={item.level} href={`/cspj/tutorials?difficulty=${item.level}`} className="block group">
              <Card
                className={`h-full border-2 bg-gradient-to-br ${item.color} ${item.border} transition-all hover:shadow-lg hover:-translate-y-1`}
              >
                <CardHeader className="pb-2">
                  <div className="flex items-center justify-between mb-1">
                    <Badge variant={item.badge} className="text-xs">
                      难度 {item.level}
                    </Badge>
                  </div>
                  <CardTitle className="text-base group-hover:text-[#2563eb] transition-colors">
                    {item.name}
                  </CardTitle>
                </CardHeader>
                <CardContent className="pt-0">
                  <p className="text-xs text-[#64748b] mb-3 leading-relaxed">{item.desc}</p>
                  <div className="flex flex-wrap gap-1">
                    {item.topics.slice(0, 3).map((topic) => (
                      <span
                        key={topic}
                        className="text-xs px-1.5 py-0.5 bg-white/70 rounded text-[#475569]"
                      >
                        {topic}
                      </span>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </section>

      {/* ── 学习节奏 ── */}
      <section className="bg-white border-y border-[#e2e8f0]">
        <div className="mx-auto grid max-w-7xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-[1fr_1.1fr] lg:px-8">
          <div className="relative min-h-[260px] overflow-hidden rounded-xl">
            <Image
              src="/img/generated/cspj-roadmap-milestones.jpg"
              alt="CSP-J 八周学习路线插图"
              fill
              sizes="(min-width: 1024px) 45vw, 100vw"
              className="object-cover"
            />
          </div>
          <div>
            <Badge variant="info" className="mb-3">学习方法</Badge>
            <h2 className="mb-2 text-2xl font-bold text-[#0f172a]">每周都有明确动作</h2>
            <p className="mb-6 text-sm leading-6 text-[#64748b]">
              CSP-J 入门级不靠突击堆题。更稳的方式是：先学一个小知识点，再做同主题练习，
              最后用错题复盘把漏洞补上。
            </p>
            <div className="mb-6 grid gap-3 sm:grid-cols-3">
              {studyPrinciples.map((item) => (
                <Card key={item.title} className="shadow-none">
                  <CardContent className="p-4">
                    <h3 className="mb-2 text-sm font-semibold text-[#0f172a]">{item.title}</h3>
                    <p className="text-xs leading-5 text-[#64748b]">{item.body}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
            <div className="space-y-2">
              {weeklyPracticePlan.map((item) => (
                <div key={item} className="flex gap-2 text-sm leading-6 text-[#475569]">
                  <span className="mt-2 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-[#2563eb]" />
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ── 统计数据 ── */}
      <section>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {[
              { value: String(cspjProblems.length), label: "首批训练题" },
              { value: String(chapterSummaries.length), label: "教学章节" },
              { value: String(syllabusModules.length), label: "大纲模块" },
              { value: "1-5", label: "入门难度系数" },
            ].map((stat) => (
              <div key={stat.label}>
                <div className="text-3xl font-bold text-[#2563eb] mb-1">{stat.value}</div>
                <div className="text-sm text-[#64748b]">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── 学习路线入口 ── */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="bg-gradient-to-r from-[#1e40af] to-[#2563eb] rounded-2xl p-8 md:p-12 text-white flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h2 className="text-2xl font-bold mb-2">先走完一条清晰路线</h2>
            <p className="text-blue-100 text-sm md:text-base">
              目前优先开放教程、路线和训练题；账号、进度和自动评测会在后续接入后开放。
            </p>
          </div>
          <Link href="/cspj">
            <Button size="lg" className="bg-white text-[#2563eb] hover:bg-blue-50 shadow-lg whitespace-nowrap">
              查看备考路线
            </Button>
          </Link>
        </div>
      </section>
    </div>
  );
}
