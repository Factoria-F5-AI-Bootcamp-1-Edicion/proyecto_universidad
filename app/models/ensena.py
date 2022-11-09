from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Table, ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .asignatura import Asignatura  # noqa: F401


ensena = Table(
    "ensena",
    Base.metadata,
    Column("Profesor_id", ForeignKey("profesor.id"), primary_key=True),
    Column("Asignatura_id", ForeignKey("asignatura.id"), primary_key=True),
)



