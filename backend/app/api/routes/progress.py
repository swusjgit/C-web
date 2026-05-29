from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.deps import get_current_user, require_approved
from app.models.user import User
from app.models.progress import UserProgress
from app.models.chapter import Chapter
from app.schemas.progress import ProgressCreate, ProgressUpdate, ProgressResponse

router = APIRouter(prefix="/api/progress", tags=["学习进度"])


@router.get("/", response_model=list[ProgressResponse])
def get_my_progress(current_user: User = Depends(require_approved), db: Session = Depends(get_db)) -> list[ProgressResponse]:
    records = db.query(UserProgress).filter(UserProgress.user_id == current_user.id).all()
    return [ProgressResponse.model_validate(p) for p in records]


@router.post("/", response_model=ProgressResponse)
def mark_chapter_completed(data: ProgressCreate, current_user: User = Depends(require_approved), db: Session = Depends(get_db)) -> ProgressResponse:
    chapter = db.query(Chapter).filter(Chapter.id == data.chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    record = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.chapter_id == data.chapter_id,
    ).first()
    if record:
        record.completed = data.completed
    else:
        record = UserProgress(
            user_id=current_user.id,
            chapter_id=data.chapter_id,
            completed=data.completed,
        )
        db.add(record)
    db.commit()
    db.refresh(record)
    return ProgressResponse.model_validate(record)


@router.put("/{progress_id}", response_model=ProgressResponse)
def update_progress(progress_id: int, data: ProgressUpdate, current_user: User = Depends(require_approved), db: Session = Depends(get_db)) -> ProgressResponse:
    record = db.query(UserProgress).filter(
        UserProgress.id == progress_id,
        UserProgress.user_id == current_user.id,
    ).first()
    if not record:
        raise HTTPException(status_code=404, detail="Progress not found")
    record.completed = data.completed
    db.commit()
    db.refresh(record)
    return ProgressResponse.model_validate(record)
