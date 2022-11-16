from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Asignatura])
def read_asignaturas(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Leer todas las asignaturas generadas a través del API y migraadas a la base de datos.
    """
    asignaturas = crud.asignatura.get_multi(db, skip=skip, limit=limit)

    # if crud.user.is_superuser(current_user):
    #     asignaturas = crud.asignatura.get_multi(db, skip=skip, limit=limit)
    # else:
    #     asignaturas = crud.asignatura.get_multi_by_owner(
    #         db=db, owner_id=current_user.id, skip=skip, limit=limit
    #     )
    return asignaturas


@router.post("/", response_model=schemas.Asignatura)
def create_asignatura(
    *,
    db: Session = Depends(deps.get_db),
    asignatura_in: schemas.AsignaturaCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Crear una nueva asignatura.
    """
    asignatura = crud.asignatura.create_with_owner(db=db, obj_in=asignatura_in) #, owner_id=current_user.id
    return asignatura


@router.put("/{id}", response_model=schemas.Asignatura)
def update_asignatura(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    asignatura_in: schemas.AsignaturaUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Actualizar una asignatura por ID.
    """
    asignatura = crud.asignatura.get(db=db, id=id)
    if not asignatura:
        raise HTTPException(status_code=404, detail="Asignatura not found")
    # if not crud.user.is_superuser(current_user) : # and (asignatura.owner_id != current_user.id)
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    asignatura = crud.asignatura.update(db=db, db_obj=asignatura, obj_in=asignatura_in)
    return asignatura


@router.get("/{id}", response_model=schemas.Asignatura)
def read_asignatura(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Consultar una asignatura por ID.
    """
    asignatura = crud.asignatura.get(db=db, id=id)
    if not asignatura:
        raise HTTPException(status_code=404, detail="Asignatura not found")
    # if not crud.user.is_superuser(current_user) : # and (asignatura.owner_id != current_user.id)
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return asignatura


@router.delete("/{id}", response_model=schemas.Asignatura)
def delete_asignatura(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Eliminar una asignatura por ID.
    """
    asignatura = crud.asignatura.get(db=db, id=id)
    if not asignatura:
        raise HTTPException(status_code=404, detail="Asignatura not found")
    # if not crud.user.is_superuser(current_user) : # and (asignatura.owner_id != current_user.id)
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    asignatura = crud.asignatura.remove(db=db, id=id)
    return asignatura
