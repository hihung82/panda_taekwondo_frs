from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models.user import User
from .schema.user import UserCreate
from .router.activities import router as activities_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from .router.students import router as students_router #...

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PandaTaekwondo", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://panda-taekwondo.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello World!"}

# serve ảnh tĩnh
if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# đăng ký router
app.include_router(activities_router)

app.include_router(students_router) # đăng kí router giống trên chat