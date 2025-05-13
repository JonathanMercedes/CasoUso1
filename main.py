from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)