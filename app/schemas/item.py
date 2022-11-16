from typing import Optional

from pydantic import BaseModel

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Atributos necesarios para la creación de un item
class ItemCreate(ItemBase):
    title: str


# Atributos para actualizar un item en la base de datos a través del API
class ItemUpdate(ItemBase):
    pass


# Atributos compartidos por los modelos guardados en la base de datos
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Atributos adicionales para responder al cliente a través del API
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
