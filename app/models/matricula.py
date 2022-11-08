from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Table,ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


# Creacion de tabla intermedia para relacion many to many de productos y orders
matricula = Table('products_orders', Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('Alumno_id', Integer, ForeignKey('Alumno.id')),
    Column('Asignatura_id', Integer, ForeignKey('Asignatura.id'))
)