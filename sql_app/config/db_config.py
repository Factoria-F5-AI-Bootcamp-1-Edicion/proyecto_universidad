from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Leo URL de conexion a BBDD de archivo de configuracion (a traves de objeto de clase Setting definida en archivo config.py)
CONECTION_URL = settings.DATABASE_URL

#Se crea el objeto SQL engine para efectuar la conexión
#El motor se usa principalmente para manejar dos elementos:
# los pools de conexiones(para manejar las conexiones a la base de datos)
# y el dialecto a utilizar(configura el dialecto y se encarga de hacer las traducciones necesarias a código SQL propias de cada motor de BBDD)
engine = create_engine(CONECTION_URL)

#Se crea la Clase SessionLocal ---> Each instance of the SessionLocal class will be a database session
#Una sesión es  una transacción -->registra una lista de objetos creados,
#modificados o eliminados dentro de una misma transacción

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Se crea la Clase Base
#Later we will inherit from this class to create each of
# the database models or classes (the ORM models)
# Base : clase de la que hereden todos los modelos
# y tiene la capacidad de realizar el mapeo correspondiente a partir de la metainformación
Base = declarative_base()

#Base ---> Esta clase será de la que hereden todos los
# modelos y tiene la capacidad de realizar el mapeo correspondiente
# a partir de la metainformación (atributos de clase, nombre de la
# clase, etc.) que encuentre, precisamente, en cada uno de los modelos.


#OTRA OPCION DE CREAR LOS OBJETOS DE CONEXION
#meta = MetaData()
#connector = engine.connect()