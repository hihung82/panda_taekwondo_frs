# ảnh từ server là bytes, ta phải chuyển về .img
import cv2
import numpy as np

def bytes_to_image(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img