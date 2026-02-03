from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"},
    echo=True
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM public.id"))
    rows = result.fetchall()

    print("DATA FROM SUPABASE:")
    for row in rows:
        print(dict(row._mapping))
