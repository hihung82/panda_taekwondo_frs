from app.database import SessionLocal
import numpy as np
from app.models import User
import snapshot_embedding


db = SessionLocal()

# lấy embe từ SQL
users = db.query(User).all()

# XEM ĐỘ GIỐNG CỦA 2 VECTOR
# function so sánh
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

best_user = None
best_score = 0

for u in users:
    score = cosine_similarity(snapshot_embedding, u.embedding)

    if score > best_score:
        best_score = score
        best_user = u

#độ giống min = 0.6
THRESHOLD = 0.6

if best_score >= THRESHOLD:
    print("Điểm danh:", best_user.name) # hoặc làm gì tiếp theo.........
else:
    print("Không nhận diện được")
