from fastapi import FastAPI
from pydantic import BaseModel

from nlp import analyze_text

app = FastAPI(title="LifeOS-Plus Backend")

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "LifeOS-Plus backend is running"}

@app.post("/analyze-text")
def analyze_text_endpoint(input: TextInput):
    return analyze_text(input.text)
