import numpy as np
import cv2


class YuNetDetector:
    def __init__(self, model_path = "models/face_detection_yunet_2023mar.onnx"):
        self.detector = cv2.FaceDetectorYN.create(model_path, "", (320, 320))

    def detect(self, image):
        height, width = image.shape[:2]

        self.detector.setInputSize((width, height))

        _,faces = self.detector.detect(image)
        
        return faces