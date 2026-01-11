# app/models/user.py
from sqlalchemy import Column, Integer, String, Date, LargeBinary
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)

    embedding = Column(LargeBinary, nullable=False)