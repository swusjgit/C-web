from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.core.deps import get_current_user
from app.models.user import User, UserRole, UserStatus
from app.schemas.user import (
    UserRegisterStudent, UserRegisterTeacher,
    UserResponse, TokenResponse, UserUpdate, UserPasswordUpdate
)

router = APIRouter(prefix="/api/auth", tags=["认证"])


@router.post("/register/student", response_model=TokenResponse)
def register_student(data: UserRegisterStudent, db: Session = Depends(get_db)) -> TokenResponse:
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
        role=UserRole.STUDENT,
        status=UserStatus.PENDING,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token({"sub": user.id})
    return TokenResponse(
        access_token=token,
        user=UserResponse.model_validate(user),
    )


@router.post("/register/teacher", response_model=TokenResponse)
def register_teacher(data: UserRegisterTeacher, db: Session = Depends(get_db)) -> TokenResponse:
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
        role=UserRole.TEACHER,
        status=UserStatus.APPROVED,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token({"sub": user.id})
    return TokenResponse(
        access_token=token,
        user=UserResponse.model_validate(user),
    )


@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> TokenResponse:
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    if user.status == UserStatus.REJECTED:
        raise HTTPException(status_code=403, detail="Account rejected")
    if user.status == UserStatus.PENDING:
        raise HTTPException(status_code=403, detail="Account pending approval")
    token = create_access_token({"sub": user.id})
    return TokenResponse(
        access_token=token,
        user=UserResponse.model_validate(user),
    )


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)) -> UserResponse:
    return UserResponse.model_validate(current_user)


@router.put("/me", response_model=UserResponse)
def update_me(data: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> UserResponse:
    if data.email and data.email != current_user.email:
        if db.query(User).filter(User.email == data.email).first():
            raise HTTPException(status_code=400, detail="Email already in use")
        current_user.email = data.email
    if data.username and data.username != current_user.username:
        if db.query(User).filter(User.username == data.username).first():
            raise HTTPException(status_code=400, detail="Username already taken")
        current_user.username = data.username
    db.commit()
    db.refresh(current_user)
    return UserResponse.model_validate(current_user)


@router.put("/password", response_model=dict)
def change_password(data: UserPasswordUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> dict:
    if not verify_password(data.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="Old password incorrect")
    current_user.password_hash = hash_password(data.new_password)
    db.commit()
    return {"message": "Password updated"}
