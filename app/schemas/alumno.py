from typing import Optional

from pydantic import BaseModel, EmailStr


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
