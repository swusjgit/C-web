"use client";

import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export default function LoginPage() {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [pending, setPending] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setPending(false);
    setLoading(true);

    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username, password }),
      });

      const data = await res.json();

      // 后端明确返回 pending 不发 token，前端收到 403 就显示审核提示
      if (res.status === 403) {
        setPending(true);
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        setLoading(false);
        return;
      }

      if (!res.ok) {
        throw new Error(data.detail || "登录失败");
      }

      // 登录成功
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("user", JSON.stringify(data.user));
      window.dispatchEvent(new Event("authChange"));
      router.push("/");
    } catch (err: any) {
      setError(err.message || "用户名或密码错误");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[calc(100vh-200px)] flex items-center justify-center px-4 py-12 bg-[#f8fafc]">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center pb-2">
          <CardTitle className="text-xl">登录账号</CardTitle>
          <CardDescription>欢迎回到数据谷中学C++学习平台</CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-1.5">
              <Label htmlFor="username">用户名</Label>
              <Input
                id="username"
                type="text"
                placeholder="输入用户名"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="space-y-1.5">
              <div className="flex items-center justify-between">
                <Label htmlFor="password">密码</Label>
              </div>
              <Input
                id="password"
                type="password"
                placeholder="输入密码"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            {error && (
              <div className="text-sm text-red-500 bg-red-50 px-3 py-2 rounded-md">
                {error}
              </div>
            )}

            {pending && (
              <div className="text-sm text-amber-600 bg-amber-50 px-3 py-3 rounded-md text-center">
                ⏳ 您的账号正在审核中，请耐心等待管理员批准后再登录。
              </div>
            )}

            <Button type="submit" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]" disabled={loading}>
              {loading ? "登录中..." : "登录"}
            </Button>
          </form>

          <p className="text-center text-sm text-[#64748b] mt-4">
            还没有账号？{" "}
            <Link href="/register" className="text-[#2563eb] hover:underline font-medium">
              立即注册
            </Link>
          </p>
        </CardContent>
      </Card>
    </div>
  );
}
