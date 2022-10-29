from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class AsignaturaBase(BaseModel):
    nombre: Optional[str] = None



# Properties to receive on item creation
class AsignaturaCreate(AsignaturaBase):
    nombre: str


# Properties to receive on item update
class AsignaturaUpdate(AsignaturaBase):
    pass


# Properties shared by models stored in DB
class AsignaturaInDBBase(AsignaturaBase):
    id: int
    nombre: str

    class Config:
        orm_mode = True


# Properties to return to client
class Asignatura(AsignaturaInDBBase):
    pass


# Properties properties stored in DB
class AsignaturaInDB(AsignaturaInDBBase):
    pass
