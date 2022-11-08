from typing import Optional

from pydantic import BaseModel


# Shared properties
class EnsenaBase(BaseModel):
    Profesor_id: Optional[int] = None
    Asignatura_id: Optional[int] = None


# Properties to receive on ensena creation
class EnsenaCreate(EnsenaBase):
    pass
    # title: str


# Properties to receive on ensena update
class EnsenaUpdate(EnsenaBase):
    pass


# Properties shared by models stored in DB
class EnsenaInDBBase(EnsenaBase):
    id: int
    Profesor_id: int
    Asignatura_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Ensena(EnsenaInDBBase):
    pass


# Properties properties stored in DB
class EnsenaInDB(EnsenaInDBBase):
    pass
