from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ProfesorBase(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None
    # is_active: Optional[bool] = True
    # is_superprofesor: bool = False



# Properties to receive on item creation
class ProfesorCreate(ProfesorBase):
    email: EmailStr
    # password: str


# Properties to receive on item update
class ProfesorUpdate(ProfesorBase):
    pass
    # password: Optional[str] = None


# Properties shared by models stored in DB
class ProfesorInDBBase(ProfesorBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Profesor(ProfesorInDBBase):
    pass


# Properties properties stored in DB
class ProfesorInDB(ProfesorInDBBase):
    pass
    # hashed_password: str
