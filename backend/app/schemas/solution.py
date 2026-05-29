from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SolutionBase(BaseModel):
    problem_id: int
    code: str


class SolutionCreate(SolutionBase):
    pass


class SolutionResponse(SolutionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    status: str
    score: int | None
    time_used: int | None
    memory_used: int | None
    submitted_at: datetime
