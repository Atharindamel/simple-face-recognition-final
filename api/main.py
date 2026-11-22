from fastapi import FastAPI, UploadFile, File

app = FastAPI()

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
    return {
        "archivo": image.filename
    }
