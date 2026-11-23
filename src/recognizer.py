
class FaceRecognizer:

    RECOGNITION_THRESHOLD = 0.45
    
    def __init__(self, encoder):
        self.encoder = encoder

    def recognize(self, embedding, database):
        mejor_persona = None
        mejor_score = 0

        for person_name, embeddings in database.get_database().items():
            for known_embedding in embeddings:
                similarity = self.encoder.compare(embedding, known_embedding)
                
                if similarity > mejor_score:
                    mejor_score = similarity
                    mejor_persona = person_name

        if mejor_score >= self.RECOGNITION_THRESHOLD:
            return mejor_persona, mejor_score

        return None, mejor_score