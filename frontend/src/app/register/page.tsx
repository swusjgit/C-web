"use client";

import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export default function RegisterPage() {
  const router = useRouter();
  const [form, setForm] = useState({ username: "", email: "", password: "", confirm: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    if (form.password !== form.confirm) {
      setError("两次输入的密码不一致");
      return;
    }
    if (form.password.length < 8) {
      setError("密码至少8位");
      return;
    }

    setLoading(true);
    try {
      const res = await fetch("/api/auth/register/student", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: form.username, email: form.email, password: form.password }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "注册失败");

      localStorage.setItem("token", data.access_token);
      localStorage.setItem("user", JSON.stringify(data.user));
      router.push("/");
    } catch (err: any) {
      setError(err.message || "注册失败，请稍后重试");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[calc(100vh-200px)] flex items-center justify-center px-4 py-12 bg-[#f8fafc]">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center pb-2">
          <CardTitle className="text-xl">注册账号</CardTitle>
          <CardDescription>加入数据谷中学C++学习平台</CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-1.5">
              <Label htmlFor="username">用户名</Label>
              <Input id="username" name="username" type="text" placeholder="设置用户名" value={form.username} onChange={handleChange} required />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="email">邮箱</Label>
              <Input id="email" name="email" type="email" placeholder="your@email.com" value={form.email} onChange={handleChange} required />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="password">密码</Label>
              <Input id="password" name="password" type="password" placeholder="至少8位" value={form.password} onChange={handleChange} required />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="confirm">确认密码</Label>
              <Input id="confirm" name="confirm" type="password" placeholder="再次输入密码" value={form.confirm} onChange={handleChange} required />
            </div>
            {error && (
              <div className="text-sm text-red-500 bg-red-50 px-3 py-2 rounded-md">{error}</div>
            )}
            <Button type="submit" className="w-full bg-[#2563eb] hover:bg-[#1d4ed8]" disabled={loading}>
              {loading ? "注册中..." : "注册"}
            </Button>
          </form>
          <p className="text-center text-sm text-[#64748b] mt-4">
            已有账号？{" "}
            <Link href="/login" className="text-[#2563eb] hover:underline font-medium">立即登录</Link>
          </p>
        </CardContent>
      </Card>
    </div>
  );
}