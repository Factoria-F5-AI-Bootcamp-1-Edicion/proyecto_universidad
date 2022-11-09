# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.matricula import matricula # noqa
from app.models.alumno import Alumno  # noqa
from app.models.asignatura import Asignatura # noqa
from app.models.profesor import Profesor  # noqa

# from app.models.item import Alumno  # noqa
# from app.models.item import Asignatura  # noqa