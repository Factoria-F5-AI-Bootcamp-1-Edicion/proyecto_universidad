from typing import Optional, List

from pydantic import BaseModel, EmailStr


# Shared properties
from app.schemas.profesor import AsignaturaProfesorSchema

class AsignaturaBase(BaseModel):
    nombre_asignatura: Optional[str] = None



# Properties to receive on item creation
class AsignaturaCreate(AsignaturaBase):
    nombre_asignatura: str


# Properties to receive on item update
class AsignaturaUpdate(AsignaturaBase):
    pass


# Properties shared by models stored in DB
class AsignaturaInDBBase(AsignaturaBase):
    id: int
    nombre_asignatura: str
    profesores : List[AsignaturaProfesorSchema]

    def dict(self, **kwargs):
        data = super(AsignaturaInDBBase, self).dict(**kwargs)

        for a in data['profesor']:
            a['id'] = a['profesor']['id']
            a['nombre'] = a['profesor']['nombre']
            del a['profesor']

        return data

    # owner_id: int

    class Config:
        orm_mode = True

# class AsignaturaSchema(AsignaturaBase):
#     profesores : List[ProfesorBase]

# Properties to return to client
class Asignatura(AsignaturaInDBBase):
    pass


# Properties properties stored in DB
class AsignaturaInDB(AsignaturaInDBBase):
    pass
