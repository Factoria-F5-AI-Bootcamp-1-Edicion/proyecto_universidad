from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.Profesor])
def read_alumnos(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user),#get_current_active_superuser
) -> Any:
    """
    Retrieve alumnos.
    """
    alumnos = crud.alumno.get_multi(db, skip=skip, limit=limit)
    return alumnos


@router.post("/", response_model=schemas.Profesor)
def create_alumnos(
        *,
        db: Session = Depends(deps.get_db),
        alumno_in: schemas.AlumnoCreate,
        current_alumno: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new alumno.
    """
    alumno = crud.alumno.get_by_email(db, email=alumno_in.email)
    if alumno:
        raise HTTPException(
            status_code=400,
            detail="The alumno with this alumnoname already exists in the system.",
        )
    alumno = crud.alumno.create(db, obj_in=alumno_in)
    if settings.EMAILS_ENABLED and alumno_in.email:
        send_new_account_email(
            email_to=alumno_in.email, alumnoname=alumno_in.email, password=alumno_in.password
        )
    return alumno


@router.put("/me", response_model=schemas.Alumno)
def update_alumno_me(
        *,
        db: Session = Depends(deps.get_db),
        # password: str = Body(None),
        nombre: str = Body(None),
        apedillo_1: str = Body(None),
        apedillo_2: str = Body(None),
        edad: str = Body(None),
        email: EmailStr = Body(None),
        current_alumno: models.Alumno = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own alumno.
    """
    current_alumno_data = jsonable_encoder(current_alumno)
    alumno_in = schemas.AlumnoUpdate(**current_alumno_data)
    # if password is not None:
    #     alumno_in.password = password
    if nombre is not None:
        alumno_in.nombre = nombre
    if apedillo_1 is not None:
        alumno_in.apedillo_1 = apedillo_1
    if apedillo_2 is not None:
        alumno_in.apedillo_2 = apedillo_2
    if edad is not None:
        alumno_in.edad = edad
    if email is not None:
        alumno_in.email = email
    alumno = crud.alumno.update(db, db_obj=current_alumno, obj_in=alumno_in)
    return alumno


@router.get("/me", response_model=schemas.Alumno)
def read_alumno_me(
        db: Session = Depends(deps.get_db),
        current_alumno: models.Alumno = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current alumno.
    """
    return current_alumno


@router.post("/open", response_model=schemas.Alumno)
def create_alumno_open(
        *,
        db: Session = Depends(deps.get_db),
        # password: str = Body(...),
        email: EmailStr = Body(...),
        nombre: str = Body(None),
        apedillo_1: str = Body(None),
        apedillo_2: str = Body(None),
        edad: str = Body(None),
) -> Any:
    """
    Create new alumno without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open alumno registration is forbidden on this server",
        )
    alumno = crud.alumno.get_by_email(db, email=email)
    if alumno:
        raise HTTPException(
            status_code=400,
            detail="The alumno with this alumno email already exists in the system",
        )
    alumno_in = schemas.AlumnoCreate(email=email, nombre=nombre, apedillo_1=apedillo_1,
                                         apedillo_2=apedillo_2, edad=edad)  # password=password,
    alumno = crud.alumno.create(db, obj_in=alumno_in)
    return alumno


@router.get("/{alumno_id}", response_model=schemas.Alumno)
def read_alumno_by_id(
        alumno_id: int,
        current_alumno: models.Alumno = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific alumno by id.
    """
    alumno = crud.alumno.get(db, id=alumno_id)
    # if alumno == current_alumno:
    #     return alumno
    # if not crud.user.is_superuser(current_alumno):
    #     raise HTTPException(
    #         status_code=400, detail="The alumno doesn't have enough privileges"
    #     )
    return alumno


@router.put("/{alumno_id}", response_model=schemas.Alumno)
def update_alumno(
        *,
        db: Session = Depends(deps.get_db),
        alumno_id: int,
        alumno_in: schemas.AlumnoUpdate,
        current_alumno: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a alumno.
    """
    alumno = crud.alumno.get(db, id=alumno_id)
    if not alumno:
        raise HTTPException(
            status_code=404,
            detail="The alumno with this alumno name does not exist in the system",
        )
    alumno = crud.alumno.update(db, db_obj=alumno, obj_in=alumno_in)
    return alumno


@router.delete("/{alumno_id}", response_model=schemas.Alumno)
def delete_alumno(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    alumno = crud.alumno.get(db=db, id=id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.alumno.is_superuser(current_user) and (alumno.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    alumno = crud.alumno.remove(db=db, id=id)
    return alumno
