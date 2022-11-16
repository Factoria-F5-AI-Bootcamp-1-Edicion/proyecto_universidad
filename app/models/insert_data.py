# Insert data
from sqlalchemy.orm import Session
from .alumno import Alumno  # noqa: F401
from .asignatura import Asignatura  # noqa: F401
from .profesor import Profesor  # noqa: F401


with Session(bind=engine) as session:

    asignatura1 = Asignatura(title="Dead People Who'd Be Influencers Today")
    asignatura2 = Asignatura(title="How To Make Friends In Your 30s")

    profesor1 = Profesor(name="Blu Renolds")
    profesor2 = Profesor(name="Chip Egan")
    profesor3 = Profesor(name="Alyssa Wyatt")

    alumno1 = Alumno(name="Blu Renolds")
    alumno2 = Profesor(name="Chip Egan")
    alumno3 = Profesor(name="Alyssa Wyatt")


    asignatura1.authors = [profesor1, profesor2]
    asignatura2.authors = [profesor1, profesor3]

    session.add_all([asignatura1, asignatura2, profesor1, profesor2, profesor3])
    session.commit()

    """Este archivo sirve para insertar datos desde Python y comprobar las relaciones entre las tablas.
    
    Para futuras implementaciones"""