from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .ensena import ensena  # noqa: F401
#from .asignatura import Asignatura  # noqa: F401

if TYPE_CHECKING:
    from .ensena import ensena  # noqa: F401
    from .asignatura import Asignatura  # noqa: F401



class Profesor(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apedillo_1 = Column(String, index=True)
    apedillo_2 = Column(String, index=True)
    edad = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)

    asignaturas_profes = relationship("Asignatura", secondary="ensena", back_populates='profesores')