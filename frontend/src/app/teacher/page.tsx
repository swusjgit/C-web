"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

interface User {
  id: number;
  username: string;
  email: string;
  role: string;
  status: string;
  created_at: string;
}

type TabType = "pending" | "approved" | "rejected" | "all";

export default function TeacherPage() {
  const router = useRouter();
  const [users, setUsers] = useState<User[]>([]);
  const [tab, setTab] = useState<TabType>("pending");
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState<number | null>(null);
  const [currentUser, setCurrentUser] = useState<User | null>(null);

  useEffect(() => {
    const stored = localStorage.getItem("user");
    if (!stored) { router.push("/login"); return; }
    const u = JSON.parse(stored);
    setCurrentUser(u);
    if (u.role !== "ADMIN" && u.role !== "TEACHER") {
      router.push("/"); return;
    }
    fetchUsers();
  }, []);

  const token = () => localStorage.getItem("token") || "";

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const res = await fetch("/api/admin/users/", {
        headers: { Authorization: `Bearer ${token()}` },
      });
      if (res.ok) {
        const data = await res.json();
        setUsers(data);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleAction = async (userId: number, action: "approve" | "reject") => {
    setActionLoading(userId);
    try {
      const res = await fetch(`/api/admin/users/${userId}/${action}`, {
        method: "PUT",
        headers: { Authorization: `Bearer ${token()}` },
      });
      if (res.ok) {
        await fetchUsers();
      } else {
        const data = await res.json();
        alert(data.detail || "操作失败");
      }
    } finally {
      setActionLoading(null);
    }
  };

  const filteredUsers = users.filter((u) => {
    if (tab === "all") return true;
    return u.status === tab;
  });

  const roleLabel: Record<string, string> = {
    STUDENT: "学生",
    TEACHER: "教师",
    ADMIN: "管理员",
  };

  const statusBadge: Record<string, { label: string; className: string }> = {
    pending: { label: "待审核", className: "bg-amber-100 text-amber-700" },
    approved: { label: "已通过", className: "bg-green-100 text-green-700" },
    rejected: { label: "已拒绝", className: "bg-red-100 text-red-700" },
  };

  const tabs: { key: TabType; label: string }[] = [
    { key: "pending", label: "待审核" },
    { key: "approved", label: "已通过" },
    { key: "rejected", label: "已拒绝" },
    { key: "all", label: "全部" },
  ];

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-[#1e40af]">教师管理后台</h1>
        <p className="text-sm text-[#64748b] mt-1">
          欢迎，{currentUser?.username}（{currentUser?.role === "ADMIN" ? "管理员" : "教师"}）
        </p>
      </div>

      {/* 标签切换 */}
      <div className="flex gap-2 mb-6 border-b border-[#e2e8f0] pb-3">
        {tabs.map((t) => (
          <button
            key={t.key}
            onClick={() => setTab(t.key)}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
              tab === t.key
                ? "bg-[#2563eb] text-white"
                : "bg-white text-[#64748b] border border-[#e2e8f0] hover:bg-[#f1f5f9]"
            }`}
          >
            {t.label}
            {t.key !== "all" && (
              <span className="ml-1.5 text-xs opacity-75">
                ({users.filter((u) => u.status === t.key).length})
              </span>
            )}
          </button>
        ))}
      </div>

      {loading ? (
        <div className="text-center py-20 text-[#64748b]">加载中...</div>
      ) : filteredUsers.length === 0 ? (
        <Card>
          <CardContent className="py-12 text-center text-[#64748b]">
            暂无用户
          </CardContent>
        </Card>
      ) : (
        <div className="space-y-3">
          {filteredUsers.map((user) => (
            <Card key={user.id} className="hover:shadow-sm transition-shadow">
              <CardContent className="py-4 px-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-4">
                    {/* 头像 */}
                    <div className="w-10 h-10 rounded-full bg-[#2563eb] flex items-center justify-center text-white font-bold text-sm flex-shrink-0">
                      {user.username.slice(0, 2).toUpperCase()}
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-medium text-[#1e293b]">{user.username}</span>
                        <Badge className={`text-xs ${statusBadge[user.status]?.className || "bg-gray-100 text-gray-600"}`}>
                          {statusBadge[user.status]?.label || user.status}
                        </Badge>
                        <Badge className="bg-blue-50 text-blue-600 text-xs">
                          {roleLabel[user.role] || user.role}
                        </Badge>
                      </div>
                      <div className="text-xs text-[#94a3b8] mt-0.5">
                        {user.email}
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    {user.status === "pending" ? (
                      <>
                        <Button
                          size="sm"
                          className="bg-green-600 hover:bg-green-700 text-white"
                          disabled={actionLoading === user.id}
                          onClick={() => handleAction(user.id, "approve")}
                        >
                          {actionLoading === user.id ? "处理中..." : "✅ 通过"}
                        </Button>
                        <Button
                          size="sm"
                          variant="outline"
                          className="text-red-500 border-red-200 hover:bg-red-50"
                          disabled={actionLoading === user.id}
                          onClick={() => handleAction(user.id, "reject")}
                        >
                          ❌ 拒绝
                        </Button>
                      </>
                    ) : (
                      <span className="text-xs text-[#94a3b8]">
                        注册时间：{new Date(user.created_at).toLocaleDateString("zh-CN")}
                      </span>
                    )}
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
