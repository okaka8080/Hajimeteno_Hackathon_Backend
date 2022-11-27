from pydantic import BaseModel
from datetime import datetime
import json

class UserBase(BaseModel):
    userid: str
    username: str

class CreateCal(BaseModel):
    userid: str
    text: str
    date: datetime
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json
    
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value,str):
            return cls(**json.loads(value))
        return value


class UpdateCal(BaseModel):
    cal_id: str
    text: str
    date: datetime

class Userdata(BaseModel):
    user_id: str
    name: str

    class Config :
        orm_mode = True

class Calender_View(BaseModel):
    cal_id: str
    date: datetime
    text: str
    url: str

    class Config :
        orm_mode = True
