from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal


"""Generación de usuario, password y tokenURL"""
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token",
    #Para determinar si un usuario es administrador, se podria utilizar la siguiente linea
    # scopes={"es_admin": "admin","es_profesor": "profesor","es_alumno": "alumno"}
)

"""Definición de métodos para el acceso autorizado al API, a través de la figura de User"""
""" reusable_oauth2 --> se utiliza como una dependencia con Depends en 
la operación de ruta para /token y en los métodos que lo heredan: """

"""get_db-->Método para definir una sesión de base de datos"""
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

"""get_current_user-->Método para definir el usuario actual"""
def get_current_user(
        db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

"""get_current_active_user-->Método para definir el usuario actual que está activo"""
def get_current_active_user(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

"""get_current_active_superuser-->Método para definir el super_usuario actual"""
#Esto aún no está impelmentado
def get_current_active_superuser(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user