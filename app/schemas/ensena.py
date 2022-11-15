from typing import Optional

from pydantic import BaseModel


# Shared properties
# from app.schemas.asignatura import RelateAsignaturaSchema
#
#
# class EnsenaBase(BaseModel):
#     profesor: Optional[RelateAsignaturaSchema]
#
#
# # Properties to receive on ensena creation
# class EnsenaCreate(EnsenaBase):
#     pass
#     # title: str
#
#
# # Properties to receive on ensena update
# class EnsenaUpdate(EnsenaBase):
#     pass
#
#
# # Properties shared by models stored in DB
# class EnsenaInDBBase(EnsenaBase):
#     profesor: Optional[RelateAsignaturaSchema]
#
#     class Config:
#         orm_mode = True
#
#
# # Properties to return to client
# class Ensena(EnsenaInDBBase):
#     pass
#
#
# # Properties properties stored in DB
# class EnsenaInDB(EnsenaInDBBase):
#     pass
