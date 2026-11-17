import cv2

class FaceEncoder:

    def __init__(self, model_path = "models/face_recognition_sface_2021dec.onnx"):
        self.model_path = model_path
        self.recognizer = cv2.FaceRecognizerSF.create(
            model_path,
            ""
        )


    def encode(self, image, face):

        aligned_face = self.recognizer.alignCrop(image, face)

        embedding = self.recognizer.feature(aligned_face)

        return embedding

    def compare(self, embedding1, embedding2):
        similarity = self.recognizer.match(embedding1, embedding2)
        return similarity