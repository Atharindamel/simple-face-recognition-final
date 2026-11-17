from src.recognizer import FaceRecognizer
from src.image_loader import ImageLoader
from src.known_faces import KnownFaces, FaceDatabase
from src.yunet_detector import YuNetDetector
from src.face_encoder import FaceEncoder

def build_database(
    loader,
    yunet_detector,
    encoder,
    known_faces
):
    known_face_list = known_faces.load()
    database = FaceDatabase()

    for person_name, image_paths in known_face_list.items():

        for image_path in image_paths:
        
            known_image = loader.load(str(image_path))

            # print(f"\nProcesando {image_path}")
            # print(f"Tamaño de imagen: {known_image.shape}")

            known_faces_yunet = yunet_detector.detect(known_image)

            if known_faces_yunet is None or len(known_faces_yunet) == 0:
                print(f"No se detectaron rostros en la imagen. {image_path}")
                continue

            # print(f"Resultado de YuNet: {known_faces_yunet}")

            known_embedding = encoder.encode(
                known_image,
                known_faces_yunet[0]
            )
            
            database.add_embedding(
                person_name,
                known_embedding
            )
            
    return database

def main():
    # ===INICIALIZACIÓN DE COMPONENTES===
    loader = ImageLoader()
    yunet_detector = YuNetDetector()
    encoder = FaceEncoder()

    # ===CONSTRUCCIÓN DE LA BASE DE DATOS DE ROSTROS CONOCIDOS===

    known_faces = KnownFaces("data/known_faces")

    database = build_database(
        loader,
        yunet_detector,
        encoder,
        known_faces
    )

    # ===DETECCIÓN DE ROSTROS EN LA IMAGEN DE PRUEBA==

    for name, embeddings in database.get_database().items():
        print(f"Nombre: {name}, Número de embeddings: {len(embeddings)}")

    # Cargar la imagen de prueba

    test_image = loader.load(r"data/test/Leonel.jpg")

    # Detectar rostros en la imagen de prueba

    test_faces = yunet_detector.detect(test_image)

    # Generar el embedding

    test_embedding = encoder.encode(
        test_image,
        test_faces[0]
    )

    # ===Reconocimiento ===
    
    recognizer = FaceRecognizer(encoder)
    person_name, similarity = recognizer.recognize(test_embedding, database)
    print(person_name, similarity)


if __name__ == "__main__":
    main()