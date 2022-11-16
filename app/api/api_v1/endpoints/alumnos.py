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
    Consultar todos los alumnos existentes en la tabla alumnos
    La consulta es en forma de lista de acuerdo al esquema de este método.
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
    Crear un nuevo alumno---> para crear un alumno sólo es necesario
    introducir el atributo de email, los demás atributos se peuden actualizar despues con el metodo update.
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


@router.put("/Creación_Propia", response_model=schemas.Alumno)
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
    Actualización de los datos propios como alumno.
    Para poder actualziarse como alumno se debe ser un user autenticado.
    """
    current_alumno_data = jsonable_encoder(current_alumno)  #Creación del token para alumno
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


@router.get("/Consulta_Propia", response_model=schemas.Alumno)
def read_alumno_me(
        db: Session = Depends(deps.get_db),
        current_alumno: models.Alumno = Depends(deps.get_current_active_user),
) -> Any:
    """
    Consulta propia como alumno, como usuario autenticado y actualmente activo.
    """
    return current_alumno


@router.post("/Crear_sin_autenticación", response_model=schemas.Alumno)
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
    Creación de un nuevo alumno sin ser usuario autenticado ni hacer log in.
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
    Consultar un alumno específico por id.
    Sirve para consultar otros alumnos que no sea el user actual loggeado
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
    Actualizar un alumno específico por id.
    Sirve para consultar otros alumnos que no sea el user actual loggeado.
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
    Eliminar un alumno específico por id.
    Sirve para consultar otros alumnos que no sea el user actual loggeado.
    Falta implemenatr otorgar este permiso a un super_user o un admin para
    evitar que cualquier ususario elimine alumnos.
    """
    alumno = crud.alumno.get(db=db, id=id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.alumno.is_superuser(current_user) and (alumno.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    alumno = crud.alumno.remove(db=db, id=id)
    return alumno
