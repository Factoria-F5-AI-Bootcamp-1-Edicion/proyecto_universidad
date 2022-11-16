from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.alumno import Alumno
from app.schemas.alumno import AlumnoCreate, AlumnoUpdate

"""Clase CRUDAlumno--->Hereda de CRUDBase----> Se definen los métodos básicos del CRUD --->get, create, update, delete
 Esta clase será importada y llamada por cada entidad donde se configuraran las rutas o endpoints"""

class CRUDAlumno(CRUDBase[Alumno, AlumnoCreate, AlumnoUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Alumno]:
        return db.query(Alumno).filter(Alumno.email == email).first()

    def create(self, db: Session, *, obj_in: AlumnoCreate) -> Alumno:
        db_obj = Alumno(
            email=obj_in.email,
            # hashed_password=get_password_hash(obj_in.password),
            nombre=obj_in.nombre,
            apedillo_1=obj_in.apedillo_1,
            apedillo_2=obj_in.apedillo_2,
            edad=obj_in.edad,
            # is_superalumno=obj_in.is_superalumno,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Alumno, obj_in: Union[AlumnoUpdate, Dict[str, Any]]
    ) -> Alumno:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        # if update_data["password"]:
        #     hashed_password = get_password_hash(update_data["password"])
        #     del update_data["password"]
        #     update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    # def authenticate(self, db: Session, *, email: str, password: str) -> Optional[Alumno]:
    #     alumno = self.get_by_email(db, email=email)
    #     if not alumno:
    #         return None
    #     if not verify_password(password, alumno.hashed_password):
    #         return None
    #     return alumno

    # def is_active(self, alumno: Alumno) -> bool:
    #     return alumno.is_active
    #
    # def is_superalumno(self, alumno: Alumno) -> bool:
    #     return alumno.is_superalumno


alumno = CRUDAlumno(Alumno) #Éste será llamado en los endpoints para crear cada ruta o endpoint para cada entidad



"""NOTA: Las líneas de código comentadas serán implemenatdas en un futuro para 
definirir super usuarios, administradores principales y hashed password para reforzar 
la autenticación y seguridad del API"""