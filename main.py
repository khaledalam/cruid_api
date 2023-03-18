from fastapi import FastAPI, status, HTTPException

from starlette import status
from starlette.requests import Request

from models.patient import Patient
from schemas.patient import CreatePatient, UpdatePatient

from email_validator import validate_email, EmailNotValidError

import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Setup DB          =============
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MariaDBSession = sessionmaker(
    bind=create_engine(os.getenv('DB_SQL_URL', '')),
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# Setup FastAPI     =============
fastAPI = FastAPI(
    title="crud_api",
    description="Simple crud api",
    version="0.0.1",
    terms_of_service="https://github.com/khaledalam",
    contact={
        "name": "Khaled Alam",
        "url": "https://linkedin.com/in/khaledalam/",
        "email": "khaledalam.net@gmail.com",
    },
    openapi_url="/api/v1/openapi.json",
    docs_url="/documentation",
    redoc_url="/re-documentation",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


# Routes            =============
@fastAPI.get("/")
def healthz():
    return {
        "status": "OK!"
    }


@fastAPI.get("/patients")
def get_all_patients(request: Request):
    with MariaDBSession() as session:
        patients = session.query(Patient).all()
    return {
        "patients": patients
    }


@fastAPI.post("/patients", status_code=status.HTTP_201_CREATED)
def create_patient(request: Request, payload: CreatePatient):
    with MariaDBSession() as session:
        try:
            validate_email(payload.email.lower(), check_deliverability=True)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Email is not valid")

        patient = Patient(
            name=payload.name,
            email=payload.email.lower(),
            dob=payload.dob,
            medical_record_number=payload.medical_record_number,
            created=datetime.datetime.utcnow(),
            updated=datetime.datetime.utcnow()
        )
        session.add(patient)
        try:
            session.commit()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    return patient.__dict__


@fastAPI.get("/patients/{id}", response_model=None)
def get_patient(request: Request, id: int):
    with MariaDBSession() as session:
        patient = session.query(Patient).filter(Patient.id == str(id)).first()
    if patient is None:
        raise HTTPException(status_code=404, detail=f"Patient with ID {id} not found")
    return patient.__dict__


@fastAPI.put("/patients/{id}")
def update_patient(request: Request, id: int, payload: UpdatePatient):
    with MariaDBSession() as session:
        patient = session.query(Patient).filter(Patient.id == str(id)).first()
        if patient is None:
            raise HTTPException(status_code=404, detail=f"Patient with ID {id} not found")

        try:
            validate_email(payload.email.lower(), check_deliverability=True)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Email is not valid")

        patient.name = payload.name
        patient.email = payload.email.lower()
        patient.dob = payload.dob
        patient.medical_record_number = payload.medical_record_number
        patient.updated = datetime.datetime.utcnow()

        session.add(patient)

        try:
            session.commit()

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    return patient.__dict__


@fastAPI.delete("/patients/{id}",)
def delete_patient(request: Request, id: int):
    with MariaDBSession() as session:
        patient = session.query(Patient).filter(Patient.id == str(id)).first()
        if patient is None:
            raise HTTPException(status_code=404, detail=f"Patient with ID {id} not found")
        session.delete(patient)
        try:
            session.commit()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    return {
        'message': 'Deleted!'
    }
