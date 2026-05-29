# 数据谷中学 C++ 学习网站

面向中学生 CSP-J 学习的 Next.js + FastAPI 项目。

## GitHub Pages 部署

本仓库已包含 `.github/workflows/pages.yml`。推送到 GitHub 的 `main` 分支后，GitHub Actions 会构建 `frontend` 并发布静态站点到 GitHub Pages。

前端教程内容已静态化，适合 GitHub Pages。登录、注册、教师后台等需要后端 API 的功能，需要将 `backend` 另行部署到支持 Python/FastAPI 和数据库的平台后再接入。

## 本地运行

```bash
cd frontend
npm install
npm run dev
```
