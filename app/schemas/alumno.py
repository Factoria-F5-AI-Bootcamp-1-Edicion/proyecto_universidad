from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class AlumnoBase(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[str] = None



# Properties to receive on item creation
class AlumnoCreate(AlumnoBase):
    email: EmailStr
    # nombre: str
    # apedillo1: str
    # apedillo2: str
    # edad: int


# Properties to receive on item update
class AlumnoUpdate(AlumnoBase):
    pass


# Properties shared by models stored in DB
class AlumnoInDBBase(AlumnoBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Alumno(AlumnoInDBBase):
    pass


# Properties properties stored in DB
class AlumnoInDB(AlumnoInDBBase):
    pass
