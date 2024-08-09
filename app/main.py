from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from typing import List
from . import crud, modelos, esquemas, base_datos
from .base_datos import SessionLocal, motor
from fastapi.security.api_key import APIKeyHeader

# Crear las tablas en la base de datos
modelos.Base.metadata.create_all(bind=motor)

# Instanciar la aplicación FastAPI
app = FastAPI()

# Definir nombre del encabezado de la API Key
NOMBRE_CLAVE_API = "Authorization"
api_key_header = APIKeyHeader(name=NOMBRE_CLAVE_API)

# Middleware para gestionar la sesión de la base de datos
@app.middleware("http")
async def middleware_sesion_bd(request: Request, call_next):
    response = Response("Error interno del servidor", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependencia para obtener la base de datos de la solicitud
def obtener_bd(request: Request):
    return request.state.db

# Lista de claves API válidas para autenticación
CLAVES_API_VALIDAS = ["mi_clave_secreta"]

# Endpoint para crear un nuevo registro
@app.post("/registros/", response_model=esquemas.Registro)
def crear_registro(registro: esquemas.RegistroCrear, db: Session = Depends(obtener_bd), clave_api: str = Depends(api_key_header)):
    if clave_api not in CLAVES_API_VALIDAS:
        raise HTTPException(status_code=403, detail="Clave API no válida")
    return crud.crear_registro(db=db, registro=registro)

# Endpoint para obtener registros con paginación
@app.get("/registros/", response_model=List[esquemas.Registro])
def leer_registros(skip: int = 0, limit: int = 10, db: Session = Depends(obtener_bd)):
    registros = crud.obtener_registros(db, skip=skip, limit=limit)
    return registros
