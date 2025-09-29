
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE_URL = "sqlite:///./mydatabase.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

DATABASE_URL = os.environ.get("DATABASE_PATH")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
