from typing import Optional, List

from pydantic import BaseModel, EmailStr


# Shared properties
# from app.schemas.asignatura import ProfesorAsignaturaSchema

######################################################
class RelateProfesorSchema(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None

    class Config:
        orm_mode = True

class AsignaturaProfesorSchema(BaseModel):
    blurb: str
    author: Optional[RelateProfesorSchema]

    class Config:
        orm_mode = True


class  RelateAsignaturaSchema(BaseModel):
    nombre_asignatura: Optional[str] = None

    class Config:
        orm_mode = True

class ProfesorAsignaturaSchema(BaseModel):
    book: Optional[RelateAsignaturaSchema]

    class Config:
        orm_mode = True

######################################################

class ProfesorBase(BaseModel):
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None
    # is_active: Optional[bool] = True
    # is_superprofesor: bool = False



# Properties to receive on item creation
class ProfesorCreate(ProfesorBase):
    email: EmailStr
    # password: str


# Properties to receive on item update
class ProfesorUpdate(ProfesorBase):
    pass
    # password: Optional[str] = None


# Properties shared by models stored in DB
class ProfesorInDBBase(ProfesorBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    nombre: Optional[str] = None
    apedillo_1: Optional[str] = None
    apedillo_2: Optional[str] = None
    edad: Optional[int] = None
    asignaturas: List[ProfesorAsignaturaSchema]

    def dict(self, **kwargs):
        data = super(ProfesorInDBBase, self).dict(**kwargs)

        for b in data['asignatura']:
            b['id'] = b['asignatura']['id']
            b['nombre_asignatura'] = b['asignatura']['nombre_asignatura']
            del b['asignatura']

        return data

    class Config:
        orm_mode = True

# class ProfesorSchema(ProfesorBase):
#     asignaturas : List[AsignaturaBase]

# Properties to return to client
class Profesor(ProfesorInDBBase):
    pass


# Properties properties stored in DB
class ProfesorInDB(ProfesorInDBBase):
    pass
    # hashed_password: str
