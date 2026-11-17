from pathlib import Path

class KnownFaces:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.known_faces = {}

    def load(self):

        folder = Path(self.folder_path)

        if not folder.exists() or not folder.is_dir():
            raise FileNotFoundError(
                f"Folder {self.folder_path} does not exist or is not a directory."
            )

        for person_folder in folder.iterdir():

            if person_folder.is_dir():
                person_name = person_folder.name
                self.known_faces[person_name] = []

                for image_path in person_folder.glob("*.jpg"):
                    self.known_faces[person_name].append(image_path)

        return self.known_faces

class FaceDatabase:
    def __init__(self):
        self.database = {}

    def add_embedding(self, name, embedding):
        if name not in self.database:
            self.database[name] = []
        self.database[name].append(embedding)

    def get_database(self):
        return self.database