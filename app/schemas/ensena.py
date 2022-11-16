from typing import Optional

from pydantic import BaseModel

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class EnsenaBase(BaseModel):
    Profesor_id: Optional[int] = None
    Asignatura_id: Optional[int] = None


# Atributos necesarios para la creación de un item
class EnsenaCreate(EnsenaBase):
    pass
    # title: str


# Atributos para actualizar un item en la base de datos a través del API
class EnsenaUpdate(EnsenaBase):
    pass


# Atributos compartidos por los modelos guardados en la base de datos
class EnsenaInDBBase(EnsenaBase):
    id: int
    Profesor_id: int
    Asignatura_id: int

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class Ensena(EnsenaInDBBase):
    pass


# Properties properties stored in DB
class EnsenaInDB(EnsenaInDBBase):
    pass
