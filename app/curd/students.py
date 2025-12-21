# app/crud/students.py
import numpy as np
from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.extract_embedding import extract_embedding


def create_student(db: Session, data):
    embedding = extract_embedding(data.image_base64)

    student = User(
        name=data.name,
        birthday=data.birthday,
        embedding=embedding.astype(np.float32).tobytes()
    )

    db.add(student)
    db.commit()
    db.refresh(student)
    return {
        "status": "success",
    }
