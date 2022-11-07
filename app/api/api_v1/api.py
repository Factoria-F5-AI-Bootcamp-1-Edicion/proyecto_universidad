from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils,profesores,alumnos,asignaturas

api_router = APIRouter()
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(profesores.router, prefix="/profesores", tags=["Profesores"])
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["Alumnos"])
api_router.include_router(asignaturas.router, prefix="/asignaturas", tags=["Asignaturas"])

# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])

