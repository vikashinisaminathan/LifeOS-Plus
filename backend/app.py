from fastapi import FastAPI, UploadFile, Form
from nlp import process_text
from ocr import process_image
from speech import process_speech

app = FastAPI()

@app.post("/nlp")
async def nlp_endpoint(text: str = Form(...)):
    result = process_text(text)
    return {"task": result}

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile):
    text = await process_image(file)
    return {"extracted_text": text}

@app.post("/speech")
async def speech_endpoint(file: UploadFile):
    text = await process_speech(file)
    return {"transcribed_text": text}
