from sqlalchemy import Column, ForeignKey, Integer, String , Table
from sqlalchemy.orm import relationship

from sql_app.config.db_config import Base

# Creacion de tabla intermedia para relacion many to many de profesores y asignaturas
ensena = Table('Profesores_Asignatura', Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('Profesor_id', Integer, ForeignKey('Profesores.id')),
    Column('Asignatura_id', Integer, ForeignKey('Asignaturas.id'))
)


class Profesor(Base):
    __tablename__ = "Profesores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido1 = Column(String,  index=True)
    apellido2 = Column(String, index=True)
    edad = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)

    #asignaturas = relationship("Asignatura", secondary=ensena, back_populates="owner")

    #se crea el constructor __init__ para instanciar los objetos de la clase Profesor
    def __init__(self, nombre, apellido1, apellido2, edad, email):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.edad=edad
        self.email=email


class Asignatura(Base):
    __tablename__ = "Asignaturas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("Profesores.id"))
    #alum_id = Column(Integer, ForeignKey("Alumnos.id"))

    owner = relationship("Profesor", secondary=ensena)
    #alum = relationship("Alumno", back_populates="Asignatura")

    def __init__(self, nombre, description, owner_id):
        self.nombre=nombre
        self.description=description
        self.owner_id=owner_id


class Alumno(Base):
    __tablename__ = "Alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido1 = Column(String, index=True)
    apellido2 = Column(String, index=True)
    edad = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)

    asignaturas = relationship("Asignatura")

    def __init__(self, nombre, apellido1, apellido2, edad, email):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.edad=edad
        self.email=email


# Creacion de tabla intermedia para relacion many to many de productos y orders
matricula = Table('Alumnos_Asignatura', Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('Alumno_id', Integer, ForeignKey('Alumnos.id')),
    Column('Asignatura_id', Integer, ForeignKey('Asignaturas.id'))
)



