from fastapi import FastAPI

from src.api.endpoints import router

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Añadimos los endpoints definidos
app.include_router(router)

# Inicialización de la aplicación
@app.get("/")
def root():
    return {"Bienvenido a la API del juego de trivia"}
