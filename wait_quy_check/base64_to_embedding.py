# services/face_service.py
import base64
import cv2
import numpy as np
from insightface.app import FaceAnalysis

# load model 1 lần
face_app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)
face_app.prepare(ctx_id=0, det_size=(640, 640))


def extract_embedding(image_base64: str) -> np.ndarray:
    # bỏ header "data:image/jpeg;base64,"
    if "," in image_base64:
        image_base64 = image_base64.split(",")[1]

    img_bytes = base64.b64decode(image_base64)
    np_img = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Ảnh không hợp lệ")

    faces = face_app.get(img)

    if len(faces) == 0:
        raise ValueError("Không phát hiện khuôn mặt")

    if len(faces) > 1:
        raise ValueError("Chỉ cho phép 1 khuôn mặt")

    return faces[0].embedding  # shape (512,)
