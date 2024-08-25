from time import sleep
from data_model.base import Base
from sqlalchemy import create_engine, select, text, types
from sqlalchemy.orm import Session
import pg8000
from data_model.patient import Patient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('HOST_PORT')
db_name = os.getenv('DB_NAME')

print(db_password)

def create_db_engine():    
    DATABASE_URL = f"postgresql+pg8000://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(DATABASE_URL)
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
