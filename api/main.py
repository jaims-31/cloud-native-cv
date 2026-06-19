from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to my Cloud-Native CV API"}


@app.get("/api/cv")
def get_cv():
    with open("cv_data.json", "r") as file:
        data = json.load(file)
    return data
