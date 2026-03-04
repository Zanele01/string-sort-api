from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.post("/sort")
def sort_string(payload: InputData):
    # Convert string to list of characters
    char_list = list(payload.data)

    # Sort alphabetically
    sorted_chars = sorted(char_list)

    # Return result
    return {"word": sorted_chars}