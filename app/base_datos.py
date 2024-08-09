from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de la base de datos
URL_BASE_DATOS = "sqlite:///./registros.db"

# Creación del motor de la base de datos
motor = create_engine(URL_BASE_DATOS)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)
Base = declarative_base()

# Inicialización de la base de datos
def inicializar_bd():
    Base.metadata.create_all(bind=motor)
