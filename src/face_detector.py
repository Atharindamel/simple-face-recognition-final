import numpy as np
import cv2

class FaceDetector:

    def __init__(
        self,
        model_path="models/haarcascade_frontalface_default.xml"
    ):
        
        self.face_cascade = cv2.CascadeClassifier(model_path)

        if self.face_cascade.empty():
            raise FileNotFoundError(
                f"Failed to load face cascade model from {model_path}"
            )

    def detect_faces(self, image: np.ndarray) -> list:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        return faces

    def draw_faces(self, image: np.ndarray, faces: list) -> np.ndarray:
        output = image.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return output