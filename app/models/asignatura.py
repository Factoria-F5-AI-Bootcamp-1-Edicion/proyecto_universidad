from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .profesor import Profesor
from .matricula import matricula  # noqa: F401
from .ensena import ensena  # noqa: F401

#from .alumno import Alumno  # noqa: F401

if TYPE_CHECKING:
    from .ensena import ensena  # noqa: F401
    from .matricula import matricula  # noqa: F401


class Asignatura(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre_asignatura = Column(String, index=True)

    alumnos = relationship("Alumno", secondary="matricula", back_populates='asignaturas_alumnos')

    profesores = relationship("Profesor", secondary="ensena", back_populates='asignaturas_profes')
