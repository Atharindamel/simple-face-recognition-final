from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from recognition_system import FaceRecognitionSystem
import traceback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# system = FaceRecognitionSystem()
# system.load_known_faces("data/known_faces")
system = None

def get_system():
    global system

    if system is None:
        system = FaceRecognitionSystem()
        system.load_known_faces("data/known_faces")

    return system

@app.get("/debug")
def debug():
    return {
        "status": "debug funcionando"
    }

@app.get("/test-vercel")
def test_vercel():
    return {
        "status": "ok",
        "message": "FastAPI funcionando en Vercel"
    }

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
async def recognize(image: UploadFile = File(...)):

    try:
        system = get_system()

        content = await image.read()

        loaded_image = system.loader.load_bytes(content)

        faces =system.detector.detect(loaded_image)

        if faces is None or len(faces) == 0:
            return{
                "person_name": person_name,
                "score": score
            }

        embedding = system.encoder.encode(
            loaded_image,
            faces[0]
        )

        person_name, score = system.recognizer.recognize(
            embedding,
            system.database
        )

        return {
            "person_name": person_name,
            "score": score
        }
    
    except Exception as e:
        return {
            "error": str(e),
            "type": type(e).__name__,
            "trace": traceback.format_exc()
        }

@app.post("/add-person")
async def add_person(
    person_name: str = Form(...),
    image: UploadFile = File(...)
):

    try:
        system = get_system()

        content = await image.read()

        loaded_image = system.loader.load_bytes(content)

        result = system.add_person(
            person_name,
            [loaded_image]
        )

        return {
            "message": "Usuario recibido correctamente",
            "person_name": person_name,
            "images_received": 1,
            **result
        }
    except Exception as e:
        return {
            "error": str(e),
            "type": type(e).__name__,
            "trace": traceback.format_exc()
        }

