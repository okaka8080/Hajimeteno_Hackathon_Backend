from fastapi import FastAPI
from pydantic import BaseModel
from db.models import Base
from db.database import engine

from OcrClient import OcrClient

Base.metadata.create_all(bind=engine)

class Data(BaseModel):
    id: str
    date: str

app = FastAPI()
@app.get("/")
def hello():
    return("hello world")

@app.post("/result/{imagepath}")
def analyze(imagepath:str):
    ocr_text = OcrClient.search(img = imagepath)
    return ocr_text
