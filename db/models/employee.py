from .base import Base
from sqlalchemy import Column, String, Integer, Date

class Employee(Base):
    __tablename__ = 'employees'

    id           = Column(Integer, primary_key=True, autoincrement=True)
    name         = Column(String)
    email        = Column(String)
    registration = Column(String)
    cpf          = Column(String)
    cep          = Column(String)
    gender       = Column(String)
    street       = Column(String)
    linguee      = Column(String)
    number       = Column(Integer)
    birthday     = Column(Date)
    created_at   = Column(Date)
    updated_at   = Column(Date)