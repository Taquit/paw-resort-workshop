from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Paw Resort API")

# Configurar CORS para permitir que el frontend se comunique con la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, restringir a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pet(BaseModel):
    id: int
    name: str
    owner: str
    record: str

# Base de datos en memoria para el workshop
pets_db = [
    Pet(id=1, name="Firulais", owner="Juan Pérez", record="Vacuna antirrábica aplicada."),
    Pet(id=2, name="Misha", owner="Ana López", record="Chequeo general, todo en orden.")
]

@app.get("/api/pets", response_model=List[Pet])
def get_pets():
    return pets_db

@app.post("/api/pets", response_model=Pet)
def add_pet(pet: Pet):
    pets_db.append(pet)
    return pet