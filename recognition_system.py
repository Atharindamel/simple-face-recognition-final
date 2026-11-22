from src.image_loader import ImageLoader
from src.yunet_detector import YuNetDetector
from src.face_encoder import FaceEncoder
from src.recognizer import FaceRecognizer
from src.known_faces import FaceDatabase, KnownFaces

class FaceRecognitionSystem:

    def __init__(self):
        self.loader = ImageLoader()
        self.detector = YuNetDetector()
        self.encoder = FaceEncoder()
        self.recognizer = FaceRecognizer(self.encoder)
        self.database = FaceDatabase()

    def load_known_faces(self, path):
        known_faces = KnownFaces(path)
        known_faces_list = known_faces.load()

        for person_name, image_paths in known_faces_list.items():

            for image_path in image_paths:
            
                image = self.loader.load(str(image_path))

                faces = self.detector.detect(image)

                if faces is None or len(faces) == 0:
                    print(f"No se detectó rostro en {image_path}")
                    continue

                embedding = self.encoder.encode(
                    image,
                    faces[0]
                )

                self.database.add_embedding(
                    person_name,
                    embedding
                )
    
    print("Base de datos cargada")

if __name__ == "__main__":
    
    system = FaceRecognitionSystem()

    system.load_known_faces("data/known_faces")

    for person_name,embeddings in system.database.get_database().items():
        print(
            f"Persona: {person_name} | Embeddings cargados {len(embeddings)}"
        )