from .base import Base
from sqlalchemy import Column, Integer, String, Date

class Admin(Base):
    __tablename__ = 'admins'

    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String)
    email      = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)