from typing import Optional
from sqlalchemy import ForeignKey, Integer,String, Uuid,Boolean, DateTime, Double, Date,func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
import datetime
from data_model.base import Base
from data_model.patient import Patient

class Observation(Base):
    __tablename__ = "Observation"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    patient_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Patient.id))
    # encounter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("encounter.id"))
    status: Mapped[str] = mapped_column(String(10))
    effective_datetime: Mapped[datetime.datetime] = mapped_column( DateTime(timezone=True), server_default=func.now())    
    issued_datetime: Mapped[datetime.datetime] = mapped_column( DateTime(timezone=True), server_default=func.now())   
    category: Mapped[Optional[str]]
    code: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(100))
    value: Mapped[Optional[float]]
    unit: Mapped[Optional[str]]
    

    def __init__(self, dict):
        self.id = dict["ObservationGuid"]
        self.patient_id = dict["PatientGuid"].split(":")[2]
        # self.encounter_id = dict["EncounterGuid"].split(":")[2]
        self.status = dict["Status"]
        self.effective_datetime = dict["EffectiveDateTime"]
        self.issued_datetime = dict["IssuedDateTime"]
        self.category = dict["Category"]
        self.code = dict["Code"]
        self.description = dict["Description"]
        self.value = dict["Value"]
        self.unit = dict["Unit"]
