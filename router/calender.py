from fastapi import APIRouter
from fastapi import Depends, FastAPI, File, UploadFile, Body
from starlette.requests import Request
from db.models import User,Calendar
from schemas.schemas import UserBase, CreateCal, UpdateCal
from sqlalchemy.orm.session import Session
from pydantic import BaseModel

from db.database import engine, get_db
from utils.dbutils import get_connection


router = APIRouter(
    prefix='/calender',
    tags=['calender']
)

@router.delete('/delete/{id}')
def delete_plan(id: str, db: Session = Depends(get_db)):
    plan = db.query(Calendar).filter(Calendar.cal_id == id)
    plan.delete()
    db.commit()
    return {'message':'success'}

@router.put('/update/{id}')
def update_plan(id: str,request: UpdateCal,db: Session = Depends(get_db)):
    plan =  db.query(Calendar).filter(Calendar.cal_id == id)
    plan.update({
        Calendar.date: request.date,
        Calendar.text: request.text
    })
    db.commit()
    return {'message':'success'}