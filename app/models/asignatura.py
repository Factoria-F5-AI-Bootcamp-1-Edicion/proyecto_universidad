from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .profesor import Profesor

if TYPE_CHECKING:
    from .ensena import Ensena  # noqa: F401


class Asignatura(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre_asignatura = Column(String, index=True)
    # profesor_id = Column(Integer, ForeignKey("profesor.id"))
    # owner = relationship("Profesor", secondary=Ensena)

    # edad = Column(String, index=True)
    # email = Column(String, unique=True, index=True, nullable=False)
    # hashed_password = Column(String, nullable=False)
    # is_active = Column(Boolean(), default=True)
    # is_superuser = Column(Boolean(), default=False)

    # is_open = Column(Boolean(), default=True)
