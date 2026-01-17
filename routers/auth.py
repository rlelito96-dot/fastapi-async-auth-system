from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserOut, Token
from app.crud import get_user, create_user
from app.auth import issue_jwt, verify_password, get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@router.post("/login", response_model=Token)
def login(user_id: int, password: str, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user or not verify_password(password, db_user.password_hash):
        raise HTTPException(status_code=403, detail="Invalid credentials")

    token = issue_jwt(db_user.id, db_user.role)
    return Token(access_token=token, token_type="bearer")

@router.get("/me",response_model=UserOut)
def get_me(user = Depends(get_current_user)):
    """Example of protected endpoint"""
    return user
