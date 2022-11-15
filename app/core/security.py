from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

"""Algoritmo utilizado por jwt para la encriptación del token"""
ALGORITHM = "HS256"

"""Método create_access_token---> para ser llamado cuando se crea un nuevo usuario 
y se genere la variable donde se encripta el token para cada usuario."""
def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

"""Verificación del password generado por cada usuario"""
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

"""Método para la obtención de un password hash para cada email y usuario"""
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
