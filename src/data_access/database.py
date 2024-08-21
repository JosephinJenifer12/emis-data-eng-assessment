from data_model.base import Base
from sqlalchemy import create_engine, select, text, types
from sqlalchemy.orm import Session
import pg8000
from data_model.patient import Patient

def create_db_engine():    
    DATABASE_URL = "postgresql+pg8000://postgres:postgres@db:5432/DB"
    engine = create_engine(DATABASE_URL, echo=True)    
    Base.metadata.create_all(engine)
    return engine

def insert_data(engine, data):
    with Session(engine) as session:
        session.add(data)
        session.commit()        
        print(f"Inserted {data.id}")
