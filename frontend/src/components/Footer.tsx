import Link from "next/link";

export default function Footer() {
  return (
    <footer className="w-full border-t border-[#e2e8f0] bg-white mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* 平台信息 */}
          <div>
            <h3 className="font-semibold text-[#0f172a] mb-3">数据谷中学C++学习网站</h3>
            <p className="text-sm text-[#64748b] leading-relaxed">
              面向中学生的 CSP-J 竞赛训练平台，基于 NOI大纲，
              系统梳理核心知识点，配套在线评测。
            </p>
          </div>

          {/* 快速链接 */}
          <div>
            <h4 className="font-medium text-[#0f172a] mb-3 text-sm">快速链接</h4>
            <ul className="space-y-2">
              {[
                { href: "/cspj/tutorials", label: "教程中心" },
                { href: "/cspj/problems", label: "在线题库" },
                { href: "/resources", label: "资料下载" },
                { href: "/cspj", label: "模拟考试" },
              ].map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-[#64748b] hover:text-[#2563eb] transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* 联系信息 */}
          <div>
            <h4 className="font-medium text-[#0f172a] mb-3 text-sm">联系我们</h4>
            <ul className="space-y-2 text-sm text-[#64748b]">
              <li>地址：重庆市两江新区学青路366号</li>
              <li>邮编：401120</li>
              <li>邮箱：740474907@qq.com</li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-6 border-t border-[#e2e8f0] text-center text-xs text-[#94a3b8]">
          <p>© {new Date().getFullYear()} 数据谷中学 · CSP竞赛训练平台 · 曾玺晔</p>
        </div>
      </div>
    </footer>
  );
}
