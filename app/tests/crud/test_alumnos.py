from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.alumno import AlumnoCreate, AlumnoUpdate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_alumno(db: Session) -> None:
    email = random_email()
    alumno_in = AlumnoCreate(email=email)
    alumno = crud.alumno.create(db, obj_in=alumno_in)
    assert alumno.email == email


def test_get_alumno(db: Session) -> None:
    email = random_email()
    alumno_in = AlumnoCreate(email=email)
    alumno = crud.alumno.create(db, obj_in=alumno_in)
    user_2 = crud.alumno.get(db, id=alumno.id)
    assert user_2
    assert alumno.email == user_2.email


def test_update_alumno(db: Session) -> None:
    email = random_email()
    alumno_in = AlumnoCreate(email=email)
    alumno = crud.alumno.create(db, obj_in=alumno_in)
    new_email = random_email()
    alumno_in_update = AlumnoUpdate(email=new_email)
    crud.alumno.update(db, db_obj=alumno, obj_in=alumno_in_update)
    user_2 = crud.alumno.get(db, id=alumno.id)
    assert user_2
    assert alumno.email == user_2.email

