from .crud_item import item
from .crud_user import user
from .crud_profesor import profesor
from .crud_alumno import alumno
from .crud_asignatura import asignatura

"""En este archivo init se importan los modelos y esquemas correspondientes a la entidad relacionada con el CRUD.
Para un nuevo set de operaciones CRUD se debería seguir el siguiente esquema de importaciones y declaraciones:

from .base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)

"""

""" Clase CRUDBase----> Se definen los métodos básicos del CRUD --->get, create, update, delete
 Esta clase será importada y llamada por cada entidad donde se configuraran las rutas o endpoints
 
 
 item = CRUDBase[Item, ItemCreate, ItemUpdate](Item) --->Integración de los métodos del CRUD, 
 el modelo de la entidad y el esquema para la validación.
 
 item ---> será llamado en los endpoints para crear cada ruta o endpoint para cada entidad"""

