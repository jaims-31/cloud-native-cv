from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Configuration CORS pour autoriser le futur frontend à interroger l'API
@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to my Cloud-Native CV API"}


@app.get("/api/cv")
def get_cv():
    with open("cv_data.json", "r") as file:
        data = json.load(file)
    return data
