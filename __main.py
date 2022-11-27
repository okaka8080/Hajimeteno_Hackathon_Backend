import uuid
import os

from datetime import datetime
import shutil

from fastapi import Depends, FastAPI, File, UploadFile
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from db.models import Base, User, Calendar
from db.database import engine

from OcrClient import OcrClient

# DB接続用のセッションクラス インスタンスが作成されると接続する
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# DB接続のセッションを各エンドポイントの関数に渡す
def get_db(request: Request):
    return request.state.db

class Account(BaseModel):
    id: str
    name: str

class Cal_data(BaseModel):
    id: str
    date: datetime 

def mkid():
    id = uuid.uuid1
    return id

def get_cal(db_session: Session, Cal_id: int):
    return db_session.query(Calendar).filter(Calendar.cal_id == Cal_id).first()
    
def analyze(imagepath:str):
    ocr_text = OcrClient.search(img = imagepath)
    return ocr_text

def download(upload_file: UploadFile):
    path = f'images/{upload_file.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return (path)

app = FastAPI()
@app.get("/")
def hello():
    return("hello world")

@app.get("/calender/{id}")
def read_cals(db: Session = Depends(get_db)):
    plans = db.query(Calendar).all
    return plans

@app.post("/calender/post")
async def create_cals(caldata:Cal_data,image: UploadFile,db: Session = Depends(get_db)):
    path = download(image)
    anltext = analyze(f"./{path}")
    cal_id = mkid()
    plan = Calendar(user_id=caldata.id, Cal_id = cal_id, date = caldata.date, text = anltext, url = Cal_data.url)
    db.add(plan)
    db.commit()
    plan = get_cal(db, plan.cal_id)
    return anltext
    
@app.post("/analyze/")
def startanl(upload_file: UploadFile):
    path = f'images/{upload_file.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    text = analyze(f"./{path}")
    return (text)

@app.post("/signin")
def signin(account:Account):

    return ("success")
