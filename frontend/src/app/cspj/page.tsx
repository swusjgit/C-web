import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function CSPJPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-[#0f172a] mb-1">CSP-J 专区</h1>
        <p className="text-sm text-[#64748b]">CSP-J（入门级）竞赛专项训练</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
        {/* 在线题库 */}
        <Card className="hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="text-3xl mb-3">💻</div>
            <h3 className="font-semibold text-[#0f172a] mb-1">在线题库</h3>
            <p className="text-sm text-[#64748b] mb-4">CSP-J 历年真题与专项练习题</p>
            <Badge variant="info" className="mb-4">200+ 题目</Badge>
            <Link href="/cspj/problems">
              <Button size="sm" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]">进入题库</Button>
            </Link>
          </CardContent>
        </Card>

        {/* 教程中心 */}
        <Card className="hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="text-3xl mb-3">📖</div>
            <h3 className="font-semibold text-[#0f172a] mb-1">教程中心</h3>
            <p className="text-sm text-[#64748b] mb-4">5个难度梯度，系统学习 C++</p>
            <Badge variant="success" className="mb-4">50+ 章节</Badge>
            <Link href="/cspj/tutorials">
              <Button size="sm" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]">开始学习</Button>
            </Link>
          </CardContent>
        </Card>

        {/* 模拟考试 */}
        <Card className="hover:shadow-md transition-shadow">
          <CardContent className="p-6">
            <div className="text-3xl mb-3">📝</div>
            <h3 className="font-semibold text-[#0f172a] mb-1">模拟考试</h3>
            <p className="text-sm text-[#64748b] mb-4">在线作答，自动评分，估分</p>
            <Badge variant="warning" className="mb-4">限时作答</Badge>
            <Link href="/login">
              <Button size="sm" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]">立即参加</Button>
            </Link>
          </CardContent>
        </Card>
      </div>

      {/* 历年真题 */}
      <section>
        <h2 className="text-lg font-semibold text-[#0f172a] mb-4">历年真题</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            { year: 2023, items: 4, completed: 0 },
            { year: 2022, items: 4, completed: 0 },
            { year: 2021, items: 4, completed: 0 },
            { year: 2020, items: 4, completed: 0 },
          ].map((exam) => (
            <Card key={exam.year} className="hover:shadow-sm transition-shadow">
              <CardContent className="p-4">
                <div className="flex items-center justify-between mb-2">
                  <h3 className="font-semibold text-[#0f172a]">CSP-J {exam.year}</h3>
                  <Badge variant="outline" className="text-xs">{exam.items} 题</Badge>
                </div>
                <p className="text-xs text-[#64748b] mb-3">
                  已完成 {exam.completed}/{exam.items} 题
                </p>
                <div className="w-full bg-[#e2e8f0] rounded-full h-1.5 mb-3">
                  <div
                    className="bg-[#2563eb] h-1.5 rounded-full"
                    style={{ width: `${(exam.completed / exam.items) * 100}%` }}
                  />
                </div>
                <Link href={`/login`}>
                  <Button size="sm" variant="outline" className="w-full text-xs">立即作答</Button>
                </Link>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>
    </div>
  );
}
