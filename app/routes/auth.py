from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.crud.user import create_user
from app.models.user import User
from app.utils.hash import verify_password
from app.utils.jwt import create_access_token
from datetime import timedelta

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
        
    access_token = create_access_token(
        data={"sub": str(db_user.id)},  # "sub" = subject
        expires_delta=timedelta(minutes=60)
    )

    return {"access_token": access_token, "token_type": "bearer", "message": "Login successful", "user": {"id": db_user.id, "name": db_user.name, "email": db_user.email}}

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)
