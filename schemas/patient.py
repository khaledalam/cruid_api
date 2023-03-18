from datetime import datetime
from typing import List
from pydantic import BaseModel


class CreatePatient(BaseModel):
    name: str
    email: str
    dob: datetime
    medical_record_number: str


class UpdatePatient(BaseModel):
    name: str
    email: str
    dob: datetime
    medical_record_number: str
    updated: datetime


class GetPatient(BaseModel):
    id: int
    name: str
    email: str
    dob: datetime
    medical_record_number: str
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True


class ListPatientSchema(BaseModel):
    users: List[GetPatient]
