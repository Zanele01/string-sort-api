from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.post("/")
def sort_string(input: InputData):
    sorted_chars = sorted(input.data)
    return {"word": sorted_chars}