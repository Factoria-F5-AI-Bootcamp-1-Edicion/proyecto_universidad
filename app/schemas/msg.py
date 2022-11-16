from pydantic import BaseModel

"""Se crea un archivo de esquema para validar el modelo de cada entidad y 
para cada método CRUD que se va a desarrollar para cada entidad."""

# Atributos compartidos
class Msg(BaseModel):
    msg: str
