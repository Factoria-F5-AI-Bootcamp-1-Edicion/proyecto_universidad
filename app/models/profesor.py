from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .ensena import Ensena  # noqa: F401


class Profesor(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apedillo_1 = Column(String, index=True)
    apedillo_2 = Column(String, index=True)
    edad = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    asignaturas = relationship("Ensena", back_populates="profesor")

    # owner = relationship("Asignatura", secondary=Ensena)

    # hashed_password = Column(String, nullable=False)
    # is_active = Column(Boolean(), default=True)
    # is_superprofesor = Column(Boolean(), default=False)
    # asignatura = relationship("Item", back_populates="owner")
