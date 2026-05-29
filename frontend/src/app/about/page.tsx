"use client";

import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export default function AboutPage() {
  const serverIp = "10.3.121.36";

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* 标题区 */}
      <div className="text-center mb-12">
        <h1 className="text-3xl font-bold text-[#0f172a] mb-3">关于数据谷中学 C++ 学习网站</h1>
        <p className="text-[#64748b] text-base max-w-2xl mx-auto">
          专为重庆市渝北区数据谷中学学生打造的 CSP-J 竞赛训练平台，基于 NOI 大纲，系统梳理核心知识点
        </p>
      </div>

      {/* 平台介绍 */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <Card>
          <CardContent className="p-6 text-center">
            <div className="text-4xl mb-3">📚</div>
            <h3 className="font-semibold text-[#0f172a] mb-2">系统教程</h3>
            <p className="text-sm text-[#64748b]">按 NOI 大纲难度梯度编排，适配中学生认知规律</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-6 text-center">
            <div className="text-4xl mb-3">💻</div>
            <h3 className="font-semibold text-[#0f172a] mb-2">在线题库</h3>
            <p className="text-sm text-[#64748b]">200+ 精选题目，历年真题全覆盖，附详细题解</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-6 text-center">
            <div className="text-4xl mb-3">📝</div>
            <h3 className="font-semibold text-[#0f172a] mb-2">模拟考试</h3>
            <p className="text-sm text-[#64748b]">限时作答，自动评分，帮助学生熟悉比赛节奏</p>
          </CardContent>
        </Card>
      </div>

      {/* 访问地址 */}
      <Card className="mb-10">
        <CardContent className="p-6">
          <h2 className="font-semibold text-[#0f172a] mb-3 text-lg">🌐 访问地址</h2>
          <div className="bg-[#f1f5f9] rounded-lg px-4 py-3 text-center">
            <code className="text-base font-semibold text-[#2563eb] break-all">
              http://{serverIp}:3000
            </code>
          </div>
          <p className="text-xs text-[#94a3b8] mt-2 text-center">局域网内可使用以上地址访问本站</p>
        </CardContent>
      </Card>

      {/* 技术栈 */}
      <div className="bg-[#f8fafc] rounded-xl p-6 mb-10">
        <h2 className="font-semibold text-[#0f172a] mb-4 text-lg">技术架构</h2>
        <div className="flex flex-wrap gap-2">
          {["Next.js 15", "React", "TypeScript", "Tailwind CSS", "shadcn/ui", "FastAPI", "MySQL", "Prisma ORM", "Judge0"].map((tech) => (
            <Badge key={tech} variant="outline" className="text-sm px-3 py-1">{tech}</Badge>
          ))}
        </div>
      </div>

      {/* 版权信息 */}
      <div className="text-center text-sm text-[#94a3b8]">
        <p>© 2025 数据谷中学 · 信息科技教研组</p>
        <p className="mt-1">基于 NOI 大纲 2025 难度标准设计</p>
      </div>
    </div>
  );
}
