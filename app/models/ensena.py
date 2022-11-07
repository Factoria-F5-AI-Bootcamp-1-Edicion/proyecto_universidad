from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Table, ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .asignatura import Asignatura  # noqa: F401


class Ensena(Base):
    id = Column(Integer, primary_key=True, index=True)
    Profesor_id = Column('Profesor_id', Integer, ForeignKey('Profesor.id'), primary_key=True),
    Asignatura_id = Column('Asignatura_id', Integer, ForeignKey('Asignatura.id'), primary_key=True)

    # Creacion de tabla intermedia para relacion many to many de productos y orders
    # Ensena = Table('profesores_asignaturas', Base.metadata,
    # Column('id', Integer, primary_key=True, index=True),
    # Column('Profesor_id', Integer, ForeignKey('Profesor.id')),
    # Column('Asignatura_id', Integer, ForeignKey('Asignatura.id'))
# )
