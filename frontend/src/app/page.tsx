import Link from "next/link";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

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
    desc: "链表、栈与队列、二叉树基础、基础图论、STL容器入门",
    color: "from-teal-50 to-cyan-50",
    border: "border-teal-200",
    badge: "info" as const,
    topics: ["vector", "stack/queue", "map/set", "邻接表"],
  },
  {
    level: 4,
    name: "算法基础",
    desc: "贪心算法、二分查找、高精度计算、基础排序、初次数论",
    color: "from-blue-50 to-indigo-50",
    border: "border-blue-200",
    badge: "secondary" as const,
    topics: ["排序算法", "二分答案", "gcd/lcm", "快速幂"],
  },
  {
    level: 5,
    name: "CSP-J 冲刺",
    desc: "DFS/BFS 搜索、动态规划入门、图论综合、最短路算法",
    color: "from-indigo-50 to-purple-50",
    border: "border-indigo-200",
    badge: "default" as const,
    topics: ["DFS", "BFS", "DP入门", "Dijkstra"],
  },
];

export default function HomePage() {
  return (
    <div>
      {/* ── Hero ── */}
      <section className="relative bg-gradient-to-br from-[#1e40af] via-[#2563eb] to-[#3b82f6] text-white overflow-hidden">
        {/* 装饰圆形 */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/3" />
        <div className="absolute bottom-0 left-0 w-64 h-64 bg-white/5 rounded-full translate-y-1/2 -translate-x-1/4" />

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-28">
          <div className="flex flex-col md:flex-row items-center gap-10">
            <div className="flex-1 max-w-2xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 bg-white/15 rounded-full text-sm text-blue-100 mb-6">
                <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
                2026 CSP-J 学习已开启
              </div>
              <h1 className="text-4xl md:text-5xl font-bold leading-tight mb-4">
                备战 CSP-J
                <br />
                <span className="text-blue-200">从这里开始</span>
              </h1>
              <p className="text-lg text-blue-100 mb-8 leading-relaxed">
                数据谷中学专属 C++ 学习平台，基于 NOI大纲，
                系统梳理核心知识点，配套在线评测与历年真题。
              </p>
              <div className="flex flex-wrap gap-3">
                <Link href="/cspj">
                  <Button size="lg" className="bg-white text-[#2563eb] hover:bg-blue-50 shadow-lg font-semibold">
                    进入 CSP-J 专区
                  </Button>
                </Link>
                <Link href="/cspj/problems">
                  <Button
                    size="lg"
                    variant="outline"
                    className="border-white/30 text-white hover:bg-white/10 bg-transparent"
                  >
                    浏览题库
                  </Button>
                </Link>
              </div>
            </div>

            {/* 右侧代码预览 */}
            <div className="hidden md:block flex-shrink-0 w-[380px]">
              <div className="bg-[#0f172a]/80 backdrop-blur rounded-2xl border border-white/10 shadow-2xl overflow-hidden">
                <div className="flex items-center gap-1.5 px-4 py-3 bg-[#1e293b] border-b border-white/10">
                  <span className="w-3 h-3 rounded-full bg-red-400" />
                  <span className="w-3 h-3 rounded-full bg-yellow-400" />
                  <span className="w-3 h-3 rounded-full bg-green-400" />
                  <span className="ml-3 text-xs text-slate-400 font-mono">main.cpp</span>
                </div>
                <pre className="p-5 text-sm font-mono leading-relaxed overflow-x-auto">
                  <code className="text-slate-300">
                    <span className="text-purple-400">#include</span> <span className="text-green-400">&lt;iostream&gt;</span>
                    {"\n"}<span className="text-purple-400">using namespace</span> std;
                    {"\n"}<span className="text-purple-400">int</span> main() {"{"}
                    {"\n"}  {"  "}<span className="text-purple-400">int</span> n;
                    {"\n"}  {"  "}cin {">>"} n;
                    {"\n"}  {"  "}<span className="text-purple-400">while</span>(n--) {"{"}
                    {"\n"}    {"    "}solve();
                    {"\n"}  {"  "}{"}"}
                    {"\n"}  {"  "}<span className="text-purple-400">return</span> 0;
                    {"\n"}{"}"}
                  </code>
                </pre>
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
              desc: "5个难度梯度，系统学习",
              href: "/cspj/tutorials",
              color: "bg-blue-50 border-blue-100 hover:border-blue-300",
            },
            {
              icon: "💻",
              title: "在线题库",
              desc: "历年真题 + 专项练习",
              href: "/cspj/problems",
              color: "bg-green-50 border-green-100 hover:border-green-300",
            },
            {
              icon: "📝",
              title: "模拟考试",
              desc: "在线作答，自动评分",
              href: "/cspj",
              color: "bg-amber-50 border-amber-100 hover:border-amber-300",
            },
            {
              icon: "📊",
              title: "学习进度",
              desc: "跟踪章节完成情况",
              href: "/login",
              color: "bg-purple-50 border-purple-100 hover:border-purple-300",
            },
          ].map((item) => (
            <Link key={item.href} href={item.href} className="block">
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
          <p className="text-sm text-[#64748b]">从零基础到 CSP-J 获奖，5个阶段循序渐进</p>
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

      {/* ── 统计数据 ── */}
      <section className="bg-white border-y border-[#e2e8f0]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {[
              { value: "200+", label: "在线题目" },
              { value: "50+", label: "教学章节" },
              { value: "10+", label: "历年真题" },
              { value: "5", label: "难度梯度" },
            ].map((stat) => (
              <div key={stat.label}>
                <div className="text-3xl font-bold text-[#2563eb] mb-1">{stat.value}</div>
                <div className="text-sm text-[#64748b]">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── 学习进度入口 ── */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="bg-gradient-to-r from-[#1e40af] to-[#2563eb] rounded-2xl p-8 md:p-12 text-white flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h2 className="text-2xl font-bold mb-2">记录你的学习轨迹</h2>
            <p className="text-blue-100 text-sm md:text-base">
              登录后自动保存学习进度，查看各章节完成情况
            </p>
          </div>
          <Link href="/register">
            <Button size="lg" className="bg-white text-[#2563eb] hover:bg-blue-50 shadow-lg whitespace-nowrap">
              立即开始学习
            </Button>
          </Link>
        </div>
      </section>
    </div>
  );
}
