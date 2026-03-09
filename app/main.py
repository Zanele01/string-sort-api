from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.get("/")
def sort_string_get(data: str):
    sorted_chars = sorted(data)
    return {"word": sorted_chars}

@app.post("/")
def sort_string_post(input: InputData):
    sorted_chars = sorted(input.data)
    return {"word": sorted_chars}