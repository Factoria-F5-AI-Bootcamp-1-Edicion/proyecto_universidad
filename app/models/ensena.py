from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Table, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .asignatura import Asignatura  # noqa: F401
    from .profesor import Profesor  # noqa: F401

# Creacion de tabla intermedia para relacion many to many de productos y orders
# Ensena = Table('profesores_asignaturas', Base.metadata,
#                Column('Profesor_id', Integer, ForeignKey('Profesor.id'), primary_key=True),
#                Column('Asignatura_id', Integer, ForeignKey('Asignatura.id'), primary_key=True)
#                )


class Ensena(Base):
    profesor_id = Column(ForeignKey('profesor.id'), primary_key=True),
    asignatura_id = Column(ForeignKey('asignatura.id'), primary_key=True)
    profesor = relationship("Profesor", back_populates="profesor")
    asignatura = relationship("Asignatura", back_populates="asignatura")


