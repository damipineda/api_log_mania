from datetime import datetime
from pydantic import BaseModel

class RegistroBase(BaseModel):
    timestamp: datetime
    nombre_servicio: str
    nivel: str
    mensaje: str

class RegistroCrear(RegistroBase):
    pass

class Registro(RegistroBase):
    id: int

    class Config:
        orm_mode = True  # Permite que los datos de SQLAlchemy se conviertan automáticamente a Pydantic
