from fastapi import APIRouter
from fastapi import Depends, FastAPI, File, UploadFile, Body
from starlette.requests import Request
from db.models import User,Calendar
from schemas.schemas import UserBase, CreateCal, UpdateCal
from sqlalchemy.orm.session import Session
from pydantic import BaseModel

from db.database import engine, get_db
from utils.dbutils import get_connection

import uuid
import shutil
from OcrClient import OcrClient
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name = "dv2q2aczs",
    api_key = "323881737694222",
    api_secret = "SJ1COcW-Z7DcRP4vQBwvYZjDdqs",
)

router = APIRouter(
    prefix='/post',
    tags=['post']
)

def mkid():
    id = uuid.uuid4()
    return str(id)

def analyze(imagepath:str):
    ocr_text = OcrClient.search(img = imagepath)
    return ocr_text

def download(upload_file: UploadFile):
    path = f'images/{upload_file.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return (path)

@router.post('/user')
async def get_user(user: UserBase, db: Session = Depends(get_db)):
    new_account = User(
        user_id = user.userid,
        name = user.username,
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

@router.post('/newplan')
async def create_newplan(plan: CreateCal = Body(...), image:UploadFile = File(...) ,db: Session = Depends(get_db)):
    path = download(image)
    anltext = analyze(f"./{path}")
    newcal_id = mkid()
    resurl = cloudinary.uploader.upload(file= f"./{path}")
    new_plan = Calendar(
        user_id = plan.userid,
        cal_id = str(newcal_id),
        date = plan.date,
        text = anltext,
        url = resurl["url"],
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return (new_plan)

