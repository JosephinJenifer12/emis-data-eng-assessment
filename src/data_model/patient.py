from typing import Optional
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import Uuid
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
from data_model.base import Base

class Patient(Base):
    __tablename__ = "Patient"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    gender: Mapped[str] = mapped_column(String(30))    
    birth_date: Mapped[str] = mapped_column(Date)    
    family_name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]


    def __init__(self, dict):
        self.id = dict["PatientGuid"]
        self.gender = dict["Gender"]
        self.birth_date = dict["BirthDate"]
        self.family_name = dict["FamilyName"]

