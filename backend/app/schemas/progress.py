from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProgressBase(BaseModel):
    chapter_id: int
    completed: bool = False


class ProgressCreate(ProgressBase):
    pass


class ProgressUpdate(BaseModel):
    completed: bool


class ProgressResponse(ProgressBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    completed_at: datetime | None
