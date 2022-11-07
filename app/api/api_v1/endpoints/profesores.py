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
def read_profesores(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve profesores.
    """
    profesores = crud.profesor.get_multi(db, skip=skip, limit=limit)
    return profesores


@router.post("/", response_model=schemas.Profesor)
def create_profesores(
        *,
        db: Session = Depends(deps.get_db),
        profesor_in: schemas.ProfesorCreate,
        current_profesor: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new profesor.
    """
    profesor = crud.profesor.get_by_email(db, email=profesor_in.email)
    if profesor:
        raise HTTPException(
            status_code=400,
            detail="The profesor with this profesorname already exists in the system.",
        )
    profesor = crud.profesor.create(db, obj_in=profesor_in)
    if settings.EMAILS_ENABLED and profesor_in.email:
        send_new_account_email(
            email_to=profesor_in.email, profesorname=profesor_in.email, password=profesor_in.password
        )
    return profesor


@router.put("/me", response_model=schemas.Profesor)
def update_profesor_me(
        *,
        db: Session = Depends(deps.get_db),
        # password: str = Body(None),
        nombre: str = Body(None),
        apedillo_1: str = Body(None),
        apedillo_2: str = Body(None),
        edad: str = Body(None),
        email: EmailStr = Body(None),
        current_profesor: models.Profesor = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own profesor.
    """
    current_profesor_data = jsonable_encoder(current_profesor)
    profesor_in = schemas.ProfesorUpdate(**current_profesor_data)
    # if password is not None:
    #     profesor_in.password = password
    if nombre is not None:
        profesor_in.nombre = nombre
    if apedillo_1 is not None:
        profesor_in.apedillo_1 = apedillo_1
    if apedillo_2 is not None:
        profesor_in.apedillo_2 = apedillo_2
    if edad is not None:
        profesor_in.edad = edad
    if email is not None:
        profesor_in.email = email
    profesor = crud.profesor.update(db, db_obj=current_profesor, obj_in=profesor_in)
    return profesor


@router.get("/me", response_model=schemas.Profesor)
def read_profesor_me(
        db: Session = Depends(deps.get_db),
        current_profesor: models.Profesor = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current profesor.
    """
    return current_profesor


@router.post("/open", response_model=schemas.Profesor)
def create_profesor_open(
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
    Create new profesor without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open profesor registration is forbidden on this server",
        )
    profesor = crud.profesor.get_by_email(db, email=email)
    if profesor:
        raise HTTPException(
            status_code=400,
            detail="The profesor with this profesorname already exists in the system",
        )
    profesor_in = schemas.ProfesorCreate(email=email, nombre=nombre, apedillo_1=apedillo_1,
                                         apedillo_2=apedillo_2, edad=edad)  # password=password,
    profesor = crud.profesor.create(db, obj_in=profesor_in)
    return profesor


@router.get("/{profesor_id}", response_model=schemas.Profesor)
def read_profesor_by_id(
        profesor_id: int,
        current_profesor: models.Profesor = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific profesor by id.
    """
    profesor = crud.profesor.get(db, id=profesor_id)
    # if profesor == current_profesor:
    #     return profesor
    # if not crud.user.is_superuser(current_profesor):
    #     raise HTTPException(
    #         status_code=400, detail="The profesor doesn't have enough privileges"
    #     )
    return profesor


@router.put("/{profesor_id}", response_model=schemas.Profesor)
def update_profesor(
        *,
        db: Session = Depends(deps.get_db),
        profesor_id: int,
        profesor_in: schemas.ProfesorUpdate,
        current_profesor: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a profesor.
    """
    profesor = crud.profesor.get(db, id=profesor_id)
    if not profesor:
        raise HTTPException(
            status_code=404,
            detail="The profesor with this profesorname does not exist in the system",
        )
    profesor = crud.profesor.update(db, db_obj=profesor, obj_in=profesor_in)
    return profesor


@router.delete("/{profesor_id}", response_model=schemas.Profesor)
def delete_profesor(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    profesor = crud.profesor.get(db=db, id=id)
    if not profesor:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.profesor.is_superuser(current_user) and (profesor.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    profesor = crud.profesor.remove(db=db, id=id)
    return profesor
