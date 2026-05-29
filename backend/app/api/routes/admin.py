from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.deps import require_role, require_approved, get_current_user
from app.models.user import User, UserRole
from app.schemas.user import UserResponse

router = APIRouter(prefix="/api/admin/users", tags=["管理员"])


@router.get("/", response_model=list[UserResponse])
def list_users(
    status: str | None = None,
    role: str | None = None,
    db: Session = Depends(get_db),
    _: User = Depends(require_role(UserRole.ADMIN)),
) -> list[UserResponse]:
    query = db.query(User)
    if status:
        query = query.filter(User.status == status)
    if role:
        query = query.filter(User.role == role)
    return [UserResponse.model_validate(u) for u in query.all()]


@router.put("/{user_id}/approve", response_model=UserResponse)
def approve_user(user_id: int, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = "approved"
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


@router.put("/{user_id}/reject", response_model=UserResponse)
def reject_user(user_id: int, db: Session = Depends(get_db), _: User = Depends(require_role(UserRole.ADMIN, UserRole.TEACHER))) -> UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = "rejected"
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)
