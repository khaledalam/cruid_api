from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(225), nullable=False)
    email = Column(String(225), nullable=False)
    dob = Column(DateTime, nullable=False)
    medical_record_number = Column(String(225), nullable=False)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)
