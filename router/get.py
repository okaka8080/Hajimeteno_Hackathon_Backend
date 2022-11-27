from fastapi import APIRouter
from fastapi import Depends, FastAPI, File, UploadFile, Body
from starlette.requests import Request
from db.models import User,Calendar
from schemas.schemas import Userdata, CreateCal, UpdateCal, Calender_View
from sqlalchemy.orm.session import Session
from pydantic import BaseModel

from fastapi import HTTPException
from db.database import engine, get_db
from utils.dbutils import get_connection
from typing import List

router = APIRouter(
    prefix='/get',
    tags=['gets']
)
@router.get('/user', response_model=List[Userdata])
async def get_all_user(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get('/allcal/{id}', response_model= List[Calender_View])
def get_all_plans(id:str, db: Session = Depends(get_db)):
    return db.query(Calendar).filter(Calendar.user_id == id).all

@router.get('/{id}', response_model= Calender_View)
def get_plan(id: str,  db: Session = Depends(get_db)):
    cal_orm = db.query(Calendar).filter(Calendar.cal_id == id).first()
    if cal_orm is None:
        raise HTTPException(status_code=400,detail="cal not exist")
    cal = Calender_View.from_orm(cal_orm)
    return cal