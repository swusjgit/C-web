from __future__ import annotations
from pydantic import BaseModel, ConfigDict


class ChapterBase(BaseModel):
    title: str
    slug: str
    difficulty: int
    order: int = 0
    category_id: int


class ChapterCreate(ChapterBase):
    content: str


class ChapterUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    difficulty: int | None = None
    order: int | None = None
    category_id: int | None = None


class ChapterListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    slug: str
    difficulty: int
    order: int
    category_id: int
    category_name: str
    category_slug: str


class ChapterDetail(ChapterListItem):
    category_name: str | None = None
    category_slug: str | None = None
    content: str | None = None


class ChapterWithCategory(ChapterDetail):
    category_name: str
    category_slug: str
