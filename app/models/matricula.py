from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Table, ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


"""
Declaramos la tabla de asociación/intermedia ensena
"""

matricula = Table(
    "matricula",
    Base.metadata,
    Column("Alumno_id", ForeignKey("alumno.id"), primary_key=True),
    Column("Asignatura_id", ForeignKey("asignatura.id"), primary_key=True),
)


"""NOTA SOBRE RELACION MANY TO MANY
La relacion Many to Many con sqlalchemy añade una tabla de asociación entre dos clases.
La tabla de asociación se indica mediante el argumento relationship.secondary de relationship().
Normalmente, la tabla utiliza el objeto MetaData asociado a la clase base declarativa,
para que las directivas ForeignKey puedan localizar las tablas remotas con las que enlazar.

La tabla de asociación anterior tiene establecidas restricciones de clave foránea 
que se refieren a las dos tablas de entidad a ambos lados de la relación. 
El tipo de datos de cada uno de association.profesor_id y association.asignatura_id se infiere 
normalmente del de la tabla referenciada y puede omitirse. 

También se recomienda, aunque no es requerido por SQLAlchemy, que las columnas que se 
refieren a las dos tablas de entidad se establezcan dentro de una restricción única o 
más comúnmente como la restricción de clave primaria; esto asegura que las filas duplicadas 
no serán persistidas dentro de la tabla sin importar los problemas en el lado de la aplicación:

Para una relación bidireccional, ambos lados de la relación contienen una colección. 
Especifique utilizando relationship.back_populates, y para cada relación() 
especifique la tabla de asociación común.

PAGINAS CONSULTADAS: 
https://www.gormanalysis.com/blog/many-to-many-relationships-in-fastapi/
https://github.com/ben519/fastapi-many-to-many/
https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
https://stackoverflow.com/questions/25002620/argumenterror-relationship-expects-a-class-or-mapper-argument

"""
