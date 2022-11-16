

"""Es necesario importar todos los modelos de .models/ en este archivo Bse
Alembic importará todos los modelops desde este archio Base,  para su creación y migración  a la base de datos."""

from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.matricula import matricula # noqa
from app.models.alumno import Alumno  # noqa
from app.models.asignatura import Asignatura # noqa
from app.models.profesor import Profesor  # noqa

# from app.models.item import Alumno  # noqa
# from app.models.item import Asignatura  # noqa