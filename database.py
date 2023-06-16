from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = "sqlite:///./sql_app.db" #конфигурация бд

engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)    #сессия с бд
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally: 
        db.close() 

