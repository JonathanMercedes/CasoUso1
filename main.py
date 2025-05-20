from fastapi import FastAPI, HTTPException
import uvicorn
from routes import user

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Definir las rutas de la API
app.include_router(user.router, prefix="/users", tags=["Users"])

# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)