from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from app.core.database import get_db
from app.core.deps import require_role, get_current_user
from app.models.user import User, UserRole
from app.models.category import Category
from app.models.chapter import Chapter
from app.models.progress import UserProgress
from app.schemas.chapter import (
    ChapterCreate, ChapterUpdate,
    ChapterListItem, ChapterDetail, ChapterWithCategory
)

router = APIRouter(prefix="/api/chapters", tags=["教程"])


@router.get("/", response_model=list[ChapterListItem])
def list_chapters(
    difficulty: int | None = Query(None, ge=1, le=5),
    category_id: int | None = None,
    db: Session = Depends(get_db),
) -> list[ChapterListItem]:
    query = db.query(Chapter).options(joinedload(Chapter.category))
    if difficulty:
        query = query.filter(Chapter.difficulty == difficulty)
    if category_id:
        query = query.filter(Chapter.category_id == category_id)
    query = query.order_by(Chapter.category_id, Chapter.order)
    chapters = query.all()
    return [
        ChapterListItem(
            id=c.id,
            title=c.title,
            slug=c.slug,
            difficulty=c.difficulty,
            order=c.order,
            category_id=c.category_id,
            category_name=c.category.name,
            category_slug=c.category.slug,
        )
        for c in chapters
    ]


@router.get("/slug/{slug}", response_model=ChapterWithCategory)
def get_chapter_by_slug(slug: str, db: Session = Depends(get_db)) -> ChapterWithCategory:
    chapter = db.query(Chapter).options(joinedload(Chapter.category)).filter(Chapter.slug == slug).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return ChapterWithCategory(
        id=chapter.id,
        title=chapter.title,
        slug=chapter.slug,
        content=chapter.content,
        difficulty=chapter.difficulty,
        order=chapter.order,
        category_id=chapter.category_id,
        category_name=chapter.category.name,
        category_slug=chapter.category.slug,
    )


@router.get("/{chapter_id}", response_model=ChapterWithCategory)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)) -> ChapterWithCategory:
    chapter = db.query(Chapter).options(joinedload(Chapter.category)).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return ChapterWithCategory(
        id=chapter.id,
        title=chapter.title,
        slug=chapter.slug,
        content=chapter.content,
        difficulty=chapter.difficulty,
        order=chapter.order,
        category_id=chapter.category_id,
        category_name=chapter.category.name,
        category_slug=chapter.category.slug,
    )


@router.post("/", response_model=ChapterDetail)
def create_chapter(data: ChapterCreate, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> ChapterDetail:
    cat = db.query(Category).filter(Category.id == data.category_id).first()
    if not cat:
        raise HTTPException(status_code=400, detail="Category not found")
    chapter = Chapter(**data.model_dump())
    db.add(chapter)
    db.commit()
    db.refresh(chapter)
    return ChapterDetail.model_validate(chapter)


@router.put("/{chapter_id}", response_model=ChapterDetail)
def update_chapter(chapter_id: int, data: ChapterUpdate, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> ChapterDetail:
    chapter = db.query(Chapter).options(joinedload(Chapter.category)).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    for key, value in data.model_dump(exclude_none=True).items():
        setattr(chapter, key, value)
    db.commit()
    db.refresh(chapter)
    return ChapterDetail.model_validate(chapter)


@router.delete("/{chapter_id}")
def delete_chapter(chapter_id: int, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> dict:
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db.delete(chapter)
    db.commit()
    return {"message": "Deleted"}
