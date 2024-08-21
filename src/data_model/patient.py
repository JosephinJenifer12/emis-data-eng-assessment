from typing import Optional
from sqlalchemy import Integer,String, Uuid,Boolean, DateTime, Double, Date,func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
import datetime
from data_model.base import Base

class Patient(Base):
    __tablename__ = "Patient"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    gender: Mapped[str] = mapped_column(String(30))    
    birth_date: Mapped[str] = mapped_column(Date)    
    family_name: Mapped[str] = mapped_column(String(30))
    given_name: Mapped[str] = mapped_column(String(30))
    prefix: Mapped[Optional[str]]
    multiple_birth: Mapped[Optional[bool]]
    deceased_datetime: Mapped[Optional[datetime.datetime]]
    race: Mapped[Optional[str]]
    ethnicity: Mapped[Optional[str]]
    mothers_maiden_name: Mapped[Optional[str]]
    birth_sex: Mapped[str] = mapped_column(String(1))
    birth_place_city: Mapped[str] = mapped_column(String(30))
    birth_place_state: Mapped[str] = mapped_column(String(100))
    birth_place_country: Mapped[str] = mapped_column(String(30))
    disability_adjusted_life_years: Mapped[Optional[float]]
    quality_adjusted_life_years: Mapped[Optional[float]]
    current_address: Mapped[str] = mapped_column(String(100))
    current_address_city: Mapped[str] = mapped_column(String(30))
    Curren_address_state: Mapped[str] = mapped_column(String(30))
    currentAddressCountry: Mapped[str] = mapped_column(String(10))
    marital_status: Mapped[str] = mapped_column(String(15))
    communication_language: Mapped[str] = mapped_column(String(10))
    home_phone: Mapped[Optional[str]]
    ssn: Mapped[str] = mapped_column(String(11))
    driving_licence: Mapped[Optional[str]]
    passport_number: Mapped[Optional[str]]



    def __init__(self, dict):
        self.id = dict["PatientGuid"]
        self.gender = dict["Gender"]
        self.birth_date = dict["BirthDate"]
        self.family_name = dict["FamilyName"]
        self.multiple_birth = dict["MultipleBirthBoolean"]
        self.deceased_datetime = dict["DeceasedDateTime"]
        self.given_name = dict["GivenName"]
        self.prefix = dict["Prefix"]
        self.race = dict["Race"]
        self.ethnicity = dict["Ethnicity"]
        self.mothers_maiden_name = dict["MothersMaidenName"]
        self.birth_sex = dict["BirthSex"]
        self.birth_place_city = dict["BirthPlaceCity"]
        self.birth_place_state = dict["BirthPlaceState"]
        self.birth_place_country = dict["BirthPlaceCountry"]
        self.disability_adjusted_life_years = dict["DisabilityAdjustedLifeYears"]
        self.quality_adjusted_life_years = dict["QualityAdjustedLifeYears"]
        self.current_address = dict["CurrentAddress"]
        self.current_address_city = dict["CurrentAddressCity"]
        self.Curren_address_state = dict["CurrentAddressState"]
        self.currentAddressCountry = dict["CurrentAddressCountry"]
        self.marital_status = dict["MaritalStatus"]
        self.communication_language = dict["CommunicationLanguage"]
        self.home_phone = dict["HomePhone"]
        self.ssn = dict["SSN"]
        self.driving_licence = dict["DrivingLicence"]
        self.passport_number = dict["PassportNumber"]