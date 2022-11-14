![imagen](https://user-images.githubusercontent.com/110174766/200622165-764b812a-c86f-4ffc-823f-ba7d43db282e.png)

# Universidad Online F5
API rest para la plataforma de una universidad en línea, utilizando el Framework de FastApi [Tiangolo's FastAPI](https://fastapi.tiangolo.com/), el cual conecta una base de datos PostgreSQL a través del ORM SQLAlchemy. 

## Variables de Entorno requeridas

Los siguientes parámetros con necesarios para acceder a la conexión entre el API rest y la base de datos PostgreSQL:

| Variable de entorno | Descripción                    | Ejemplo                |
|---------------------|--------------------------------|------------------------|
| `POSTGRES_USER`     | PostgresSQL DB Usuario         | `postgres`             |
| `POSTGRES_PASSWORD` | PostgresSQL DB Password        | `postgres`             |
| `POSTGRES_SERVER`   | PostgresSQL DB Host URL or DNS | `localhost`            |
| `POSTGRES_PORT`     | PostgresSQL DB Port            | `5432`                 |
| `POSTGRES_DB`       | PostgresSQL DataBase Name      | `Proyecto_Universidad` |
| `PROJECT_NAME`      | Project Name                   | `Proyecto_Universidad` |
| `DESCRIPTION`       | Project description            | `fast-api-demo`        |

## Descargar este repositorio:
[GitHub Repositorio Proyecto_Universidad](https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/proyecto_universidad/edit/main/README.md)

## Instalar todos los paquetes y librerias del file:
`requirements.txt`

## Running with alembic + uvicorn + FastApi
- `alembic upgrade head`
- `uvicorn app.main:app --reload`

## Securización con OAuth2 + JsonWebToken
- Crear usuario de acceso con correo electrónico, contraseña (password).
![img.png](img.png)
- Acceder con correo electrónico y contraseña.
![img_1.png](img_1.png)

## API Doc
La documentación de la API, se puede consultar con `/docs` (http://localhost:5000/docs si lo estás ejecutando localmente, por ejemplo, o con el puerto del servidor seleccionado).

## Pruebas (testing)
En este proyecto utilizamos `Pytest` para ejecutar pruebas unitarias.
- Seleccionar lla carpeta `testing`
- Necesitamos correr el siguiente comando:
`python -m pytest`

## Estructura de este repositorio

| Carpeta   | Fichero            | Descripción                                                       |
|-----------|--------------------|-------------------------------------------------------------------|
| `alembic` | `versions`         | Versiones del API.                                                |
| `app`     | `main.py`          | Archivo principal para el funcionamiento de FastApi.              |
| `app`     | `.env`             | Variables de entorno.                                             |
| `app`     | `requirements.txt` | Librerías y paquetes utilizados par la creación de este proyecto. |
|           | `api`              | Endpoints del API.                                                |           
|           | `core`             | Configuración de la conexión de las variables de entorno.         |
|           | `crud`             | Métodos y funciones para su utilzación en el CRUD.                |
|           | `db`               | Conexión a la base de datos.                                      |
|           | `email-templates`  | Plantillas para la seguridad de los usuarios.                     |
|           | `models`           | Entidades/Clases y tablas de asociación relacionadas.             |
|           | `schemas`          | Esquemas para la validación del CRUD y los endpoints.             |
|           | `tests`            | Ficheros para realizar la prueba del funcionamiento de este API.  |

## Tecnologías aplicadas
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL (Pgadmin4)
- Alembic
- Celery, JWT & OAUth2
- Notion
- Pytest

Para mayor información sobre las versiones de cada librería utilizada en el desarrollo del presente proyecto, se puede consultar el fichero `requirements.txt`