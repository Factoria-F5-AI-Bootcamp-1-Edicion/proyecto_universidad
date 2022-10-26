from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import CRUD, models, schemas

from sql_app.config.db_config import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app= FastAPI(
    title= "Proyecto Universidad Online Factoria F5 - APIrest",
    description= "API para la gestión de la base de datos del Proyecto Universidad Online para la Asociación Factoria F5",
    openapi_tags=[{
    "name": "Profesores",
    "description":"Profesores pertenecientes a las facultades de la Universidad FactoriaF5"
    }]
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#CRUD PROFESORES

#CREATE----> CREAR: Crear un nuevo usuario tipo Profesor
@app.post("/Profesores", tags=["Profesores"])
def Crear_Profesores_Nuevos(profesor: schemas.Profesor, asignatura: models.Asignatura, db: Session = Depends(get_db)):
    #establecer si la asignatura existe antes de crearla
    #if db.query(asignatura)
    db_profesor = CRUD.get_user_by_email(db, email=profesor.email)

    if db_profesor:
        raise HTTPException(status_code=400, detail="Email already registered")
    return CRUD.create_profesor(db=db, profesor=profesor)
    
#READ ----> Seleccionar todos los profesores

@app.get("/Profesores/", response_model=list[schemas.Profesor], tags=["Profesores"])
def Seleccionar_todos_los_Profesores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = CRUD.get_users(db, skip=skip, limit=limit)
    return users

#READ ----> Seleccionar un profesor determinado
@app.get("/Profesores/{profesor_id}", response_model=schemas.Profesor, tags=["Profesores"])
def Seleccionar_un_Profesor(profesor_id: int, db: Session = Depends(get_db)):
    db_profesor = CRUD.get_user(db, profesor_id=profesor_id)
    if db_profesor is None:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return db_profesor



#CRUD ASIGNATURAS

#CREAR ASIGNATURAS
@app.post("/Profesores/{profesor_id}/Asignaturas", response_model=schemas.Asignatura, tags=["Asignaturas"])
def Crear_Asignatura_para_un_Profesor(
    profesor_id: int, asignatura: schemas.AlumnoCreate, db: Session = Depends(get_db)
):
    return CRUD.create_user_item(db=db, asignatura=asignatura, profesor_id=profesor_id)

#READ ---> Todas las asignaturas
@app.get("/Asignaturas", response_model=list[schemas.Asignatura], tags=["Asignaturas"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    asignaturas = CRUD.get_items(db, skip=skip, limit=limit)
    return asignaturas

#READ ----> Seleccionar una asignatura determinada por profesor
@app.get("/Asignaturas/{asignatura_id}", response_model=schemas.Asignatura, tags=["Asignaturas"])
def read_item(asignatura_id: int, db: Session = Depends(get_db)):
    db_asignatura = CRUD.get_user(db, asignatura_id=asignatura_id)
    if db_asignatura is None:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return db_asignatura


#CRUD ASIGNATURAS

# Se crea la entidad (tabla) de estudiantes:


