from typing import Optional

from pydantic import BaseModel


# Shared properties
class MatriculaBase(BaseModel):
    Alumno_id: Optional[int] = None
    Asignatura_id: Optional[int] = None


# Properties to receive on ensena creation
class MatriculaCreate(EnsenaBase):
    pass
    # title: str


# Properties to receive on ensena update
class MatriculaUpdate(EnsenaBase):
    pass


# Properties shared by models stored in DB
class MatriculaInDBBase(EnsenaBase):
    id: int
    Alumno_id: int
    Asignatura_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Matricula(MatriculaInDBBase):
    pass


# Properties properties stored in DB
class MatriculaInDB(MatriculaInDBBase):
    pass
