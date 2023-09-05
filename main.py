from fastapi import FastAPI, Depends, HTTPException, Security

from translator import translateText

from pydantic import BaseModel

from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Example route
@app.get("/")
def read_root():
    return {"message": "Translator API"}


class Translate(BaseModel):
    text:str
    lang:str = 'en'

@app.post("/translate")
async def translate_to_language(request: Translate):
    text = request.text
    if(request.lang!='en'):
        text = translateText(text,request.lang,'en')
    return {"success":True, "result":text}