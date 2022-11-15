from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.profesor import ProfesorCreate, ProfesorUpdate
from app.tests.utils.utils import random_email


def test_create_profesor(db: Session) -> None:
    email = random_email()
    profesor_in = ProfesorCreate(email=email)
    profesor = crud.profesor.create(db, obj_in=profesor_in)
    assert profesor.email == email


def test_get_profesor(db: Session) -> None:
    email = random_email()
    profesor_in = ProfesorCreate(email=email)
    profesor = crud.profesor.create(db, obj_in=profesor_in)
    user_2 = crud.profesor.get(db, id=profesor.id)
    assert user_2
    assert profesor.email == user_2.email


def test_update_profesor(db: Session) -> None:
    email = random_email()
    profesor_in = ProfesorCreate(email=email)
    profesor = crud.profesor.create(db, obj_in=profesor_in)
    new_email = random_email()
    profesor_in_update = ProfesorUpdate(email=new_email)
    crud.profesor.update(db, db_obj=profesor, obj_in=profesor_in_update)
    user_2 = crud.profesor.get(db, id=profesor.id)
    assert user_2
    assert profesor.email == user_2.email

