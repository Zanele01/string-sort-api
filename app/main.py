from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sort_string(data: str):
    sorted_chars = sorted(data)
    return {"word": sorted_chars}