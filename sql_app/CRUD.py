import email
from sqlalchemy.orm import Session

from . import models, schemas

#CRUD -----> PROFESORES
def get_user(db: Session, profesor_id: int):
    return db.query(models.Profesor).filter(models.Profesor.id == profesor_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Profesor).filter(models.Profesor.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profesor).offset(skip).limit(limit).all()


def create_profesor(db: Session, profesor: schemas.Profesor):
    db_profesor = models.Profesor(profesor.nombre, profesor.apellido1, profesor.apellido2,
                                  profesor.edad, profesor.email)
    db.add(db_profesor)
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

#CRUD -----> ASIGNATURAS
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Asignatura).offset(skip).limit(limit).all()

def get_item(db: Session, asignatura_id: int):
    return db.query(models.Asignatura).filter(models.Asignatura.id == asignatura_id).first()


def create_user_item(db: Session, asignatura: schemas.AsignaturaCreate, profesor_id: int):
    db_asignatura = models.Asignatura(**asignatura.dict(), owner_id=profesor_id)
    db.add(db_asignatura)
    db.commit()
    db.refresh(db_asignatura)
    return db_asignatura


#CRUD -----> ESTUDIANTES




#CRUD -----> FACULTAD






#CRUD -----> MATRICULA




#CRUD -----> GRADO