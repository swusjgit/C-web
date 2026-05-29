from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.deps import require_role
from app.models.user import User, UserRole
from app.models.problem import Problem, ProblemType
from app.schemas.problem import ProblemCreate, ProblemUpdate, ProblemListItem, ProblemDetail

router = APIRouter(prefix="/api/problems", tags=["题库"])


@router.get("/", response_model=list[ProblemListItem])
def list_problems(
    difficulty: int | None = Query(None, ge=1, le=5),
    problem_type: str | None = None,
    is_public: bool | None = None,
    db: Session = Depends(get_db),
) -> list[ProblemListItem]:
    query = db.query(Problem)
    if difficulty:
        query = query.filter(Problem.difficulty == difficulty)
    if problem_type:
        query = query.filter(Problem.problem_type == problem_type)
    if is_public is not None:
        query = query.filter(Problem.is_public == is_public)
    return [ProblemListItem.model_validate(p) for p in query.order_by(Problem.difficulty).all()]


@router.get("/{problem_id}", response_model=ProblemDetail)
def get_problem(problem_id: int, db: Session = Depends(get_db)) -> ProblemDetail:
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return ProblemDetail.model_validate(problem)


@router.post("/", response_model=ProblemDetail)
def create_problem(data: ProblemCreate, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> ProblemDetail:
    problem = Problem(**data.model_dump())
    db.add(problem)
    db.commit()
    db.refresh(problem)
    return ProblemDetail.model_validate(problem)


@router.put("/{problem_id}", response_model=ProblemDetail)
def update_problem(problem_id: int, data: ProblemUpdate, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> ProblemDetail:
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    for key, value in data.model_dump(exclude_none=True).items():
        setattr(problem, key, value)
    db.commit()
    db.refresh(problem)
    return ProblemDetail.model_validate(problem)
