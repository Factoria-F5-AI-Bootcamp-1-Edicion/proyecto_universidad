from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Table,ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


# Creacion de tabla intermedia para relacion many to many de productos y orders

matricula = Table(
    "matricula",
    Base.metadata,
    Column("Alumno_id", ForeignKey("alumno.id"), primary_key=True),
    Column("Asignatura_id", ForeignKey("asignatura.id"), primary_key=True),
)
