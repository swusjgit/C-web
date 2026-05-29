from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.deps import require_approved
from app.models.user import User
from app.models.problem import Problem
from app.models.solution import UserSolution
from app.schemas.solution import SolutionCreate, SolutionResponse

router = APIRouter(prefix="/api/solutions", tags=["提交"])


@router.post("/", response_model=SolutionResponse)
def submit_solution(data: SolutionCreate, current_user: User = Depends(require_approved), db: Session = Depends(get_db)) -> SolutionResponse:
    problem = db.query(Problem).filter(Problem.id == data.problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    solution = UserSolution(
        user_id=current_user.id,
        problem_id=data.problem_id,
        code=data.code,
    )
    db.add(solution)
    db.commit()
    db.refresh(solution)
    return SolutionResponse.model_validate(solution)


@router.get("/", response_model=list[SolutionResponse])
def my_solutions(current_user: User = Depends(require_approved), db: Session = Depends(get_db)) -> list[SolutionResponse]:
    records = db.query(UserSolution).filter(UserSolution.user_id == current_user.id).order_by(UserSolution.submitted_at.desc()).all()
    return [SolutionResponse.model_validate(s) for s in records]
