from __future__ import annotations
from pydantic import BaseModel, ConfigDict


class ProblemBase(BaseModel):
    title: str
    description: str
    difficulty: int
    problem_type: str = "exercise"
    is_public: bool = True


class ProblemCreate(ProblemBase):
    time_limit: int = 1000
    memory_limit: int = 256
    template_code: str | None = None
    solution_code: str | None = None


class ProblemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    difficulty: int | None = None
    time_limit: int | None = None
    memory_limit: int | None = None
    template_code: str | None = None
    solution_code: str | None = None
    problem_type: str | None = None
    is_public: bool | None = None


class ProblemListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    difficulty: int
    problem_type: str
    is_public: bool
    time_limit: int
    memory_limit: int


class ProblemDetail(ProblemListItem):
    description: str
    template_code: str | None
    solution_code: str | None
