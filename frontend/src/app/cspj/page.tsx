import Link from "next/link";
import Image from "next/image";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { chapterSummaries } from "@/lib/staticChapters";
import { cspjProblems } from "@/data/cspjProblems";
import { getSyllabusCoverage, roadmapStages, studyPrinciples, weeklyPracticePlan } from "@/data/cspjSyllabus";

const coverage = getSyllabusCoverage(chapterSummaries);

export default function CSPJPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="mb-8">
        <Badge variant="info" className="mb-3">NOI 2025 入门级</Badge>
        <h1 className="text-2xl font-bold text-[#0f172a] mb-1">CSP-J 备考工作台</h1>
        <p className="text-sm text-[#64748b]">
          先把大纲知识点、基础题和阶段训练组织起来，后续再接入账号、进度和自动评测。
        </p>
      </div>

      <section className="mb-10 grid items-center gap-8 lg:grid-cols-[1.05fr_0.95fr]">
        <div>
          <Badge variant="success" className="mb-3">怎么开始</Badge>
          <h2 className="mb-3 text-xl font-bold text-[#0f172a]">从一节课到一道题，再到一次复盘</h2>
          <p className="mb-5 text-sm leading-6 text-[#64748b]">
            学生第一次进入这里时，不需要一下子刷很多题。先选一个模块读完目标，再做同主题短题，
            最后把错因写清楚，下一次训练才会真正变轻松。
          </p>
          <div className="grid gap-3 sm:grid-cols-3">
            {studyPrinciples.map((item) => (
              <Card key={item.title} className="shadow-none">
                <CardContent className="p-4">
                  <h3 className="mb-2 text-sm font-semibold text-[#0f172a]">{item.title}</h3>
                  <p className="text-xs leading-5 text-[#64748b]">{item.body}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
        <div className="relative min-h-[280px] overflow-hidden rounded-xl border border-[#e2e8f0]">
          <Image
            src="/img/generated/cspj-practice-desk.jpg"
            alt="学生练习 CSP-J 编程题的插图"
            fill
            sizes="(min-width: 1024px) 42vw, 100vw"
            className="object-cover"
          />
        </div>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <Card className="hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="text-xs font-semibold text-[#2563eb] mb-2">教程</div>
            <h3 className="font-semibold text-[#0f172a] mb-1">大纲化教程中心</h3>
            <p className="text-sm text-[#64748b] mb-4">
              {chapterSummaries.length} 个章节，按基础、语法、数据结构、算法、数学组织。
            </p>
            <Badge variant="success" className="mb-4">当前可用</Badge>
            <Link href="/cspj/tutorials">
              <Button size="sm" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]">开始学习</Button>
            </Link>
          </CardContent>
        </Card>

        <Card className="hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="text-xs font-semibold text-[#2563eb] mb-2">训练</div>
            <h3 className="font-semibold text-[#0f172a] mb-1">首批基础训练题</h3>
            <p className="text-sm text-[#64748b] mb-4">
              {cspjProblems.length} 道题先覆盖输入输出、分支循环、数组、字符串、二分、搜索和 DP。
            </p>
            <Badge variant="info" className="mb-4">题面与提示</Badge>
            <Link href="/cspj/problems">
              <Button size="sm" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]">进入题库</Button>
            </Link>
          </CardContent>
        </Card>

        <Card className="hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="text-xs font-semibold text-[#2563eb] mb-2">测评</div>
            <h3 className="font-semibold text-[#0f172a] mb-1">阶段测评规划</h3>
            <p className="text-sm text-[#64748b] mb-4">
              先按 8 周路线安排训练任务，自动判题和登录进度后续接入后开放。
            </p>
            <Badge variant="warning" className="mb-4">建设中</Badge>
            <Link href="#roadmap">
              <Button size="sm" variant="outline" className="w-full">查看路线</Button>
            </Link>
          </CardContent>
        </Card>
      </div>

      <section className="mb-10">
        <div className="flex items-end justify-between gap-4 mb-4">
          <div>
            <h2 className="text-lg font-semibold text-[#0f172a]">大纲覆盖矩阵</h2>
            <p className="text-xs text-[#64748b] mt-1">
              先对齐 NOI 2025 入门级五大模块，再逐步补齐缺口。
            </p>
          </div>
          <Badge variant="outline" className="text-xs">可审核版本</Badge>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
          {coverage.map((item) => (
            <Card key={item.slug} className="h-full">
              <CardContent className="p-4">
                <div className="flex items-center justify-between gap-2 mb-2">
                  <Badge variant="secondary" className="text-xs">{item.code}</Badge>
                  <span className="text-xs text-[#64748b]">
                    {item.availableCount}/{item.plannedCount}
                  </span>
                </div>
                <h3 className="font-semibold text-[#0f172a] text-sm mb-2">{item.name}</h3>
                <p className="text-xs text-[#64748b] leading-5 mb-3">{item.focus}</p>
                {item.missingCount > 0 ? (
                  <div className="text-xs text-amber-700 bg-amber-50 border border-amber-100 rounded-md px-2 py-1.5">
                    待补：{item.missing.slice(0, 2).join("、")}
                    {item.missing.length > 2 ? " 等" : ""}
                  </div>
                ) : (
                  <div className="text-xs text-green-700 bg-green-50 border border-green-100 rounded-md px-2 py-1.5">
                    现有章节已覆盖核心条目
                  </div>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <section id="roadmap" className="mb-10 scroll-mt-24">
        <div className="mb-4 flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <h2 className="text-lg font-semibold text-[#0f172a]">8 周备考路线</h2>
            <p className="mt-1 text-xs text-[#64748b]">把一周拆成学习、变式、复盘三段，避免只刷题不沉淀。</p>
          </div>
          <div className="max-w-xl space-y-1">
            {weeklyPracticePlan.map((item) => (
              <div key={item} className="text-xs leading-5 text-[#64748b]">{item}</div>
            ))}
          </div>
        </div>
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
          {roadmapStages.map((stage, index) => (
            <Card key={stage.weeks} className="h-full">
              <CardContent className="p-5">
                <div className="mb-3 flex items-center justify-between gap-3">
                  <Badge variant="outline" className="text-xs">{stage.weeks}</Badge>
                  <span className="font-mono text-xs text-[#94a3b8]">0{index + 1}</span>
                </div>
                <h3 className="font-semibold text-[#0f172a] mb-2">{stage.name}</h3>
                <p className="text-sm text-[#475569] leading-6 mb-3">{stage.goal}</p>
                <div className="space-y-1.5">
                  {stage.tasks.map((task) => (
                    <div key={task} className="text-xs text-[#64748b] leading-5">
                      {task}
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <section>
        <h2 className="text-lg font-semibold text-[#0f172a] mb-4">下一步建设重点</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            "给每章补 3 道选择/判断、2 道代码阅读、2 道编程题",
            "新增排序、cmath、网络、NOI/CSP 规则和高精度除法专题",
            "接入账号、学习进度、错题本和后端判题能力",
          ].map((item) => (
            <Card key={item}>
              <CardContent className="p-4 text-sm text-[#475569] leading-6">{item}</CardContent>
            </Card>
          ))}
        </div>
      </section>
    </div>
  );
}
