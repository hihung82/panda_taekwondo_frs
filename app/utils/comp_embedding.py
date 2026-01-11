from app.database import SessionLocal
import numpy as np
from app.models.user import User


db = SessionLocal()

# lấy embe từ SQL
users = db.query(User).all()

# XEM ĐỘ GIỐNG CỦA 2 VECTOR
# function so sánh
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

