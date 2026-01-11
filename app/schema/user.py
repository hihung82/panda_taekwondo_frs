# app/schema/user.py
from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name: str
    birthday: date
    image_base64: str

class StudentResponse(BaseModel):
    id: int
    name: str
    birthday: date

    class Config:
        from_attributes = True
