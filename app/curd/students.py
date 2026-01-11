# app/crud/students.py
import numpy as np
from sqlalchemy.orm import Session

from app.models.user import User
from app.schema.user import UserCreate
from app.utils.extract_embedding import extract_embedding
from app.utils.comp_embedding import cosine_similarity
from fastapi import HTTPException


def create_student(db: Session, data: UserCreate):
    embedding = extract_embedding(data.image_base64)
    
    if embedding is None:
        raise HTTPException(status_code=400, detail="Không phát hiện khuôn mặt")
    
    existing_students = db.query(User).all()

    for s in existing_students:
        db_embedding = np.frombuffer(s.embedding, dtype=np.float32)
        similarity = cosine_similarity(embedding, db_embedding)

        if similarity >= 0.85:
            raise HTTPException(
                status_code=409,
                detail=f"Khuôn mặt đã tồn tại (trùng với student_id={s.id})"
            )


    student = User(
        name = data.name,
        birthday = data.birthday,
        embedding = embedding.astype(np.float32).tobytes()
    )

    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_all_students(db: Session):
    return db.query(User).all()
