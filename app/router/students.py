# app/router/students.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schema.user import UserCreate, StudentResponse
from app.curd.students import create_student, get_all_students


router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=StudentResponse)
def create(data: UserCreate, db: Session = Depends(get_db)):
    return create_student(db, data)

@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return get_all_students(db)