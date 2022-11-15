from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.asignatura import AsignaturaCreate, AsignaturaUpdate
from app.tests.utils.utils import random_lower_string


def test_create_asignatura(db: Session) -> None:
    nombre_asignatura = random_lower_string()
    asignatura_in = AsignaturaCreate(nombre_asignatura=nombre_asignatura)
    asignatura = crud.asignatura.create(db, obj_in=asignatura_in)
    assert asignatura.nombre_asignatura == nombre_asignatura


def test_get_asignatura(db: Session) -> None:
    nombre_asignatura = random_lower_string()
    asignatura_in = AsignaturaCreate(nombre_asignatura=nombre_asignatura)
    asignatura = crud.asignatura.create(db, obj_in=asignatura_in)
    user_2 = crud.asignatura.get(db, id=asignatura.id)
    assert user_2
    assert asignatura.nombre_asignatura == user_2.nombre_asignatura


def test_update_asignatura(db: Session) -> None:
    nombre_asignatura = random_lower_string()
    asignatura_in = AsignaturaCreate(nombre_asignatura=nombre_asignatura)
    asignatura = crud.asignatura.create(db, obj_in=asignatura_in)
    new_nombre_asignatura = random_lower_string()
    asignatura_in_update = AsignaturaUpdate(nombre_asignatura=nombre_asignatura)
    crud.asignatura.update(db, db_obj=asignatura, obj_in=asignatura_in_update)
    user_2 = crud.asignatura.get(db, id=asignatura.id)
    assert user_2
    assert asignatura.nombre_asignatura == user_2.nombre_asignatura

