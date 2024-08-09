from sqlalchemy.orm import Session
from . import modelos, esquemas

# Crear un nuevo registro en la base de datos
def crear_registro(db: Session, registro: esquemas.RegistroCrear):
    db_registro = modelos.Registro(**registro.dict())
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

# Obtener todos los registros con paginación
def obtener_registros(db: Session, skip: int = 0, limit: int = 10):
    return db.query(modelos.Registro).offset(skip).limit(limit).all()

# Obtener un registro por su ID
def obtener_registro(db: Session, registro_id: int):
    return db.query(modelos.Registro).filter(modelos.Registro.id == registro_id).first()
