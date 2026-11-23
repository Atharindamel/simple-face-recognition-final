from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from recognition_system import FaceRecognitionSystem
import shutil
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

system = FaceRecognitionSystem()
system.load_known_faces("data/known_faces")

TEMP_FOLDER = Path("temp")
TEMP_FOLDER.mkdir(exist_ok=True)

@app.get("/")
def home():
    return{
        "Mensaje": "API de reconocimiento facial funcionando"
    }

@app.get("/test")
def test():
    return{
        "estado": "ok",
        "mensaje": "El backend está respondiendo correctamente"
    }

@app.post("/recognize")
def recognize(image: UploadFile = File(...)):
    
    image_path = TEMP_FOLDER / image.filename

    with open(image_path,"wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    person_name, score = system.recognize_image(str(image_path))

    return{
        "person_name": person_name,
        "score": score
    }

@app.post("/add-person")
def add_person(
    person_name: str = Form(...),
    images: list[UploadFile] = File(...)
):

    return {
        "message": "Usuario recibido correctamente",
        "person_name": person_name,
        "images_received": len(images)
    }

