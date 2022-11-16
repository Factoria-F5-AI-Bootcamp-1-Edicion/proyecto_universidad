from typing import Optional

from pydantic import BaseModel, EmailStr

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Atributos para recibir a través del API para la creación
class UserCreate(UserBase):
    email: EmailStr
    password: str


#Atributos para actualizar un item en la base de datos a través del API
class UserUpdate(UserBase):
    password: Optional[str] = None

#Atributos compartidos por los modelos guardados en la base de datos
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class User(UserInDBBase):
    pass


# Propiedades adicionales para guardar en la base de datos
class UserInDB(UserInDBBase):
    hashed_password: str
