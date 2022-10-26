from typing import Optional
from pydantic import BaseModel


class AsignaturaBase(BaseModel):
    title: str
    description: str | None = None


class AsignaturaCreate(AsignaturaBase):
    pass


class Asignatura(AsignaturaBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class Profesor(BaseModel):
    id: Optional[int]
    nombre: str
    apellido1: str
    apellido2: str
    edad: int
    email: str

    asignaturas: list[AsignaturaBase]

    class Config:
        orm_mode = True

# schemas de la entidad (tabla) Alumnos:
# Shared properties
class AlumnoBase(BaseModel):
    # email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo1: Optional[str] = None
    apedillo2: Optional[str] = None
    edad: Optional[int] = None



# Properties to receive on item creation
class AlumnoCreate(AlumnoBase):
    nombre: str
    apedillo1: str
    apedillo2: str
    edad: int


# Properties to receive on item update
class AlumnoUpdate(AlumnoBase):
    pass


# Properties shared by models stored in DB
class AlumnoInDBBase(AlumnoBase):
    id: int
    nombre: str
    apedillo1: str
    apedillo2: str
    edad: int

    class Config:
        orm_mode = True


# Properties to return to client
class Alumno(AlumnoInDBBase):
    pass


# Properties properties stored in DB
class AlumnoInDB(AlumnoInDBBase):
    pass


