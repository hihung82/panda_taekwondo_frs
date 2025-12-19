from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.users import UserCreate, UserResponse
from app.crud.users import create_user, get_all_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)


@router.get("/", response_model=list[UserResponse])
def list_all(db: Session = Depends(get_db)):
    return get_all_users(db)
