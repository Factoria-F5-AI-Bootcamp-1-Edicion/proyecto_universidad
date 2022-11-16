from typing import Optional

from pydantic import BaseModel, EmailStr

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class ProfesorBase(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None
    # is_active: Optional[bool] = True
    # is_superprofesor: bool = False



# Atributos necesarios para la creación de un item
class ProfesorCreate(ProfesorBase):
    email: EmailStr
    # password: str


# Atributos para actualizar un item en la base de datos a través del API
class ProfesorUpdate(ProfesorBase):
    pass
    # password: Optional[str] = None


# Atributos compartidos por los modelos guardados en la base de datos
class ProfesorInDBBase(ProfesorBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class Profesor(ProfesorInDBBase):
    pass


# Properties properties stored in DB
class ProfesorInDB(ProfesorInDBBase):
    pass
    # hashed_password: str
