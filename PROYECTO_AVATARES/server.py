from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Avatar(BaseModel):
    skin_color: str
    hair_color: str

avatars = []

@app.post("/guardar_avatar/")
def guardar_avatar(avatar: Avatar):
    avatars.append(avatar.dict())
    return {"mensaje": "Avatar guardado con éxito"}

@app.get("/avatares/")
def obtener_avatares():
    return avatars
