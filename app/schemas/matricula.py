from typing import Optional

from pydantic import BaseModel

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class MatriculaBase(BaseModel):
    Alumno_id: Optional[int] = None
    Asignatura_id: Optional[int] = None


# Atributos necesarios para la creación de un item
class MatriculaCreate(EnsenaBase):
    pass
    # title: str


# Atributos para actualizar un item en la base de datos a través del API
class MatriculaUpdate(EnsenaBase):
    pass


# Atributos compartidos por los modelos guardados en la base de datos
class MatriculaInDBBase(EnsenaBase):
    id: int
    Alumno_id: int
    Asignatura_id: int

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class Matricula(MatriculaInDBBase):
    pass


# Properties properties stored in DB
class MatriculaInDB(MatriculaInDBBase):
    pass
