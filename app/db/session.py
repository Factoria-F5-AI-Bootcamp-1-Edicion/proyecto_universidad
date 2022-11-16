from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


""" Creación del motor Engine para la conexión a la base de datos, si no se quiere
utilizar el Alembic para las migraciones, el Engine ya queda configurado"""

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

"""Configuración de la sesión"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
