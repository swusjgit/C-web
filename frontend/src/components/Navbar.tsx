"use client";

import Link from "next/link";
import Image from "next/image";

const navLinks = [
  { href: "/cspj/tutorials", label: "教程" },
  { href: "/cspj/problems", label: "题库" },
  { href: "/cspj", label: "模拟考试" },
  { href: "/about", label: "关于" },
];

export default function Navbar() {

  return (
    <header className="sticky top-0 z-50 w-full bg-white border-b border-[#e2e8f0] shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* 左：校徽 */}
          <div className="flex items-center gap-3">
            <Link href="/">
              <Image
                src="/school-logo.png"
                alt="数据谷中学校徽"
                width={240}
                height={28}
                className="object-contain"
                priority
              />
            </Link>
          </div>

          {/* 中：导航链接 - 按钮样式 */}
          <nav className="hidden md:flex items-center gap-2">
            {navLinks.map((link) => (
              <Link key={link.href} href={link.href}>
                <button
                  className="px-5 py-2 text-sm font-semibold text-[#475569]
                             bg-white border-2 border-[#e2e8f0] rounded-full
                             hover:border-[#2563eb] hover:text-[#2563eb]
                             hover:shadow-[0_2px_8px_rgba(37,99,235,0.15)]
                             active:scale-95
                             transition-all duration-200 cursor-pointer"
                >
                  {link.label}
                </button>
              </Link>
            ))}
          </nav>

          {/* 右：占位 */}
          <div className="flex items-center gap-3">
          </div>
        </div>

        {/* 移动端导航 */}
        <nav className="md:hidden pb-3 flex flex-wrap gap-2">
          {navLinks.map((link) => (
            <Link key={link.href} href={link.href}>
              <button className="px-4 py-1.5 text-sm font-semibold text-[#64748b] bg-white border-2 border-[#e2e8f0] rounded-full hover:border-[#2563eb] hover:text-[#2563eb] transition-all cursor-pointer">
                {link.label}
              </button>
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
