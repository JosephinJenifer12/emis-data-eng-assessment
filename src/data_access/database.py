from time import sleep
from data_model.base import Base
from sqlalchemy import create_engine, select, text, types
from sqlalchemy.orm import Session
import pg8000
from data_model.patient import Patient

def create_db_engine():    
    DATABASE_URL = "postgresql+pg8000://postgres:postgres@db:5432/DB" # To connect from docker
    # DATABASE_URL = "postgresql+pg8000://postgres:postgres@127.0.0.1:5432/DB" # To connect from local
    while True:
        try:
            engine = create_engine(DATABASE_URL)
            Base.metadata.create_all(engine)
            return engine
        except Exception as ex:
            sleep(5)
            continue

def insert_data(engine, data):
    with Session(engine) as session:
        session.add(data)
        session.commit()        
        print(f"Inserted {data.id}")

def insert_bulk_data(engine, bulk_data):
    try:
        with Session(engine) as session:
            session.add_all(bulk_data)
            session.commit()        
            print(f"Inserted bulk data successfully")
    except:
        print('Exception')
