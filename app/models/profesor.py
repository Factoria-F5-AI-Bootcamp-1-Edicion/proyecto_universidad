from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .ensena import ensena  # noqa: F401

if TYPE_CHECKING:
    from .ensena import ensena  # noqa: F401
    from .asignatura import Asignatura  # noqa: F401


"""Declaramos la Clase Profesor"""

class Profesor(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apedillo_1 = Column(String, index=True)
    apedillo_2 = Column(String, index=True)
    edad = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)

    asignaturas_profes = relationship("Asignatura", secondary="ensena", back_populates='profesores')


    """
    El atributo o propiedad asignatura_profes es lo que nos permitira 
    relacionar la entidad profesor con la entidad Asignatura a través de 
    la tabla intermdeia ensena, en una relacion bidireccional entre asignatura y profesor.
    
    relationship-->Entidad con la que se relaciona
    secondary----->tabla intermedia o asociativa
    back_populates---->bidireccionalidad de la relacion: 
                        asignaturas_alumnos -----> atributo de la entidad Alumnos
                        asignaturas_profes -----> atributo de la entidad Profesores
                        alumnos----> atributo de la entidad Asignatura
                        profesores----> atributo de la entidad Asignatura
    
    """