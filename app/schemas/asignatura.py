from typing import Optional

from pydantic import BaseModel, EmailStr

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class AsignaturaBase(BaseModel):
    nombre_asignatura: Optional[str] = None



# Atributos necesarios para la creación de un item
class AsignaturaCreate(AsignaturaBase):
    nombre_asignatura: str


# Atributos para actualizar un item en la base de datos a través del API
class AsignaturaUpdate(AsignaturaBase):
    pass


# Atributos compartidos por los modelos guardados en la base de datos
class AsignaturaInDBBase(AsignaturaBase):
    id: int
    nombre_asignatura: str
    # owner_id: int

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class Asignatura(AsignaturaInDBBase):
    pass


# Properties properties stored in DB
class AsignaturaInDB(AsignaturaInDBBase):
    pass
