from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

"""Este método es para declarar el nombre de  cada tabla que se creará en la base
 de datos a partir del nombre de las Clases de las entidades definidas o declaradas en .models/"""
@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() #lower es para q  el nombre quede en minuscula
