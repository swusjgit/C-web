#!/usr/bin/env python3
"""初始化数据库表和初始数据"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from app.core.database import engine, SessionLocal
from app.core.database import Base
from app.models import *

def init_db():
    # 创建表
    Base.metadata.create_all(bind=engine)
    print("✓ 数据库表创建完成")

    db = SessionLocal()
    try:
        # 插入初始分类
        categories = [
            {"name": "语法", "slug": "syntax", "icon": "📖"},
            {"name": "数据结构", "slug": "data-structure", "icon": "🗂️"},
            {"name": "算法", "slug": "algorithm", "icon": "💡"},
            {"name": "数学", "slug": "math", "icon": "🔢"},
        ]
        from app.models.category import Category
        for cat_data in categories:
            existing = db.query(Category).filter(Category.slug == cat_data["slug"]).first()
            if not existing:
                cat = Category(**cat_data)
                db.add(cat)
        db.commit()
        print("✓ 初始分类插入完成")

        # 创建管理员账号
        from app.models.user import User, UserRole, UserStatus
        from app.core.security import hash_password
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            admin = User(
                username="admin",
                email="admin@cpp-learning.local",
                password_hash=hash_password("admin123"),
                role=UserRole.ADMIN,
                status=UserStatus.APPROVED,
            )
            db.add(admin)
            db.commit()
            print("✓ 管理员账号创建完成 (admin / admin123)")

    finally:
        db.close()


if __name__ == "__main__":
    init_db()
