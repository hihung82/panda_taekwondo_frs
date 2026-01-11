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
