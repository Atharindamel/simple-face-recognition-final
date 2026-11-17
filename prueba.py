import cv2

from src.image_loader import ImageLoader
from src.yunet_detector import YuNetDetector
from src.face_encoder import FaceEncoder

loader = ImageLoader()
image = loader.load("data/test/Leonel.jpg")

yunet = YuNetDetector("models/face_detection_yunet_2023mar.onnx")
faces = yunet.detect(image)

print(f"Detected {len(faces)} faces.")

encoder = FaceEncoder()

embeddings = encoder.encode(image, faces[0])  # Assuming you want to encode the first detected face

print(type(embeddings))
print(embeddings.shape)
print(embeddings)