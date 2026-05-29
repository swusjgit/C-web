"use client";

import Link from "next/link";
import Image from "next/image";
import { useEffect, useState } from "react";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";

const navLinks = [
  { href: "/cspj/tutorials", label: "教程" },
  { href: "/cspj/problems", label: "题库" },
  { href: "/cspj", label: "模拟考试" },
  { href: "/about", label: "关于" },
];

interface User {
  id: number;
  username: string;
  email: string;
  role: string;
  status: string;
}

export default function Navbar() {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const stored = localStorage.getItem("user");
    if (stored) {
      setUser(JSON.parse(stored));
    }

    const onAuthChange = () => {
      const u = localStorage.getItem("user");
      setUser(u ? JSON.parse(u) : null);
    };
    window.addEventListener("authChange", onAuthChange);
    window.addEventListener("storage", (e) => {
      if (e.key === "user" || e.key === "token") {
        const u = localStorage.getItem("user");
        setUser(u ? JSON.parse(u) : null);
      }
    });

    return () => {
      window.removeEventListener("authChange", onAuthChange);
    };
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    window.dispatchEvent(new Event("authChange"));
    window.location.href = "/";
  };

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

          {/* 右：用户信息或登录/注册 */}
          <div className="flex items-center gap-3">
            {user ? (
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" className="flex items-center gap-2 px-3">
                    <Avatar className="h-8 w-8">
                      <AvatarFallback className="bg-[#2563eb] text-white text-xs">
                        {user.username.slice(0, 2).toUpperCase()}
                      </AvatarFallback>
                    </Avatar>
                    <span className="text-sm font-medium text-[#334155] hidden sm:block">
                      {user.username}
                    </span>
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end" className="w-48">
                  <div className="px-2 py-1.5 text-sm text-[#64748b]">
                    {user.role === "STUDENT" ? "学生" : user.role === "TEACHER" ? "教师" : "管理员"}
                  </div>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem asChild>
                    <Link href="/student">学习中心</Link>
                  </DropdownMenuItem>
                  {(user.role === "ADMIN" || user.role === "TEACHER") && (
                    <DropdownMenuItem asChild>
                      <Link href="/teacher">教师后台</Link>
                    </DropdownMenuItem>
                  )}
                  <DropdownMenuSeparator />
                  <DropdownMenuItem onClick={handleLogout} className="text-red-500 cursor-pointer">
                    退出登录
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            ) : (
              <>
                <Link href="/login">
                  <Button variant="ghost" size="sm" className="text-[#334155]">
                    登录
                  </Button>
                </Link>
                <Link href="/register">
                  <Button size="sm" className="bg-[#2563eb] hover:bg-[#1d4ed8]">
                    注册
                  </Button>
                </Link>
              </>
            )}
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
