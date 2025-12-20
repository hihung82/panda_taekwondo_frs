from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name: str
    birthday: date
    embedding: list[float]
