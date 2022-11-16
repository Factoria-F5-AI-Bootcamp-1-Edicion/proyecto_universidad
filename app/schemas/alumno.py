from typing import Optional

from pydantic import BaseModel, EmailStr

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class AlumnoBase(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[str] = None



# Atributos necesarios para la creación de un item
class AlumnoCreate(AlumnoBase):
    email: EmailStr
    # nombre: str
    # apedillo1: str
    # apedillo2: str
    # edad: int


# Atributos para actualizar un item en la base de datos a través del API
class AlumnoUpdate(AlumnoBase):
    pass



# Atributos compartidos por los modelos guardados en la base de datos
class AlumnoInDBBase(AlumnoBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[str] = None

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class Alumno(AlumnoInDBBase):
    pass


# Atributos guardados en la base de datos
class AlumnoInDB(AlumnoInDBBase):
    pass
