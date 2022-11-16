from __future__ import with_statement

import os
import sys

import dotenv

from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

"""config ---> Es el objeto para la configuración del Alembic, 
el cual extraerá los valores de las variables de entorno y la 
información del archivo .ini del archivo el uso"""

config = context.config

"""Esta linea es para configurar el loggers"""
fileConfig(config.config_file_name)

"""Aquí se deben añadir los objetos Metadata de nuestros modelos, 
para el soporte de la "autogeneración" de ls revisiones del Alembic. """

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from app.db.base import Base  # noqa

target_metadata = Base.metadata

"""Los valores de las variables de entorno requeridas para la conexión a la base de 
datos se encuentran ene le archivo .env, por fuera de todas las carpetas de este proyecto"""

dotenv.load_dotenv(verbose=True)


def get_url():
    user = os.getenv("POSTGRES_USER", "admin_f5")
    password = os.getenv("POSTGRES_PASSWORD", "")
    server = os.getenv("POSTGRES_SERVER", "13.38.159.23")
    db = os.getenv("POSTGRES_DB", "demo_official")
    return f"postgresql://{user}:{password}@{server}/{db}"


def run_migrations_offline():
    """Método para correr las migraciones en modo 'offline' --->Permite ejecutar las migraciones en modo "offline".

    La configuración se hace solo con una URL y no con un motor, aunque también se puede configurar a través del enginae.
    Al omitir la creación del engine, ni siquiera necesitamos que haya una DBAPI disponible.

    Las llamadas a context.execute() emiten la cadena de texto dada a la salida del script.

    """
    url = get_url()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Correr migraciones en modo 'online'----> Cuando llamamos este método,
    si necesitamos crear un Engine y asociarlo al contexto de la conexión.
    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
