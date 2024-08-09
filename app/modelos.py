from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Registro(Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    nombre_servicio = Column(String, index=True)
    nivel = Column(String)
    mensaje = Column(String)
