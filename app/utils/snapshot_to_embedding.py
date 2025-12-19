import cv2
import img_to_embedding

img = cv2.imread("snapshot.jpg")
snapshot_embedding = img_to_embedding(img)

if snapshot_embedding is None:
    print("Không phát hiện khuôn mặt")
else:
    print("chuyển đổi thành công")
