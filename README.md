<img src="https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/proyecto_universidad/blob/feature/login_and_profesor/logo-color.png" width="100px"><img src="https://user-images.githubusercontent.com/110174766/200622165-764b812a-c86f-4ffc-823f-ba7d43db282e.png" width="700px">

# Universidad Online F5
API rest para la plataforma de una universidad en línea, utilizando el Framework de FastApi [Tiangolo's FastAPI](https://fastapi.tiangolo.com/), el cual conecta una base de datos PostgreSQL a través del ORM SQLAlchemy. 

## ACCESO AL API
El primer paso para la utilización de esta API es acceder al repositorio GitHub y crear una copia local del mismo.

## Descargar este repositorio:
[GitHub Repositorio Proyecto_Universidad](https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/proyecto_universidad/edit/main/README.md)

## Instalar todos los paquetes y librerias del fichero:
`requirements.txt`

## Variables de Entorno requeridas
El segundo paso es crear un archivo `.env`, donde se configuren las variables de entorno necesarias y requeridas para la conexión segura a la base de datos y asegurar la externalización de datos sensibles. 

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

## Conectar con la base de datos PostgreSQL:
Se realiza la conexión a la base de datos `PostgreSQL` a través de la ORM `SQLAlchemy`, el driver `psycopg2` y las migraciones a través de `alembic`, todo sincronizado bajo el framework y funcionamiento de `FastApi`.
Correr los sigueintes dos comandos en la terminal para iniciar esta conexión, tanto en el puerto como su visualización en la base de datos postgresSQL.
- `alembic upgrade head`
- `uvicorn app.main:app --reload`
- Iniciar sesión con usuario y contraseña en la base de datos de postgresSQL en el pgAdmin4.

## Creación de usuario para acceso seguro:
Esta API está securizada con OAuth2 + JsonWebToken, para acceder a estas funcionalidades de seguridad se deben seguir los siguienets pasos:
- Crear usuario de acceso con correo electrónico, contraseña (password).
![imagen](https://user-images.githubusercontent.com/110174766/201629221-6044219b-b542-437e-b7d9-3d116c6639f4.png)

- Acceder con correo electrónico y contraseña.
![imagen](https://user-images.githubusercontent.com/110174766/201629359-1395d189-a768-40e7-b60c-ce09673fd03d.png)

## Acceso a los endpoints:
Se puede acceder a los métodos CRUD para cada entidad (Profesores, Alumnos, Asignaturas), mediante los cuales se puede crear, seleccionar, actualizar y eliminar información de la base de datos.
Los principales endpoints son:

**Login**
   `PUT /acces_token` `PUT /test_token`  `PUT /recover_password` `PUT /reset_password` 

**Users**
 `GET /users` `GET /users{id}`  `POST /users` `POST /users_open` `PUT /users{id}` 

**Profesores**
   `GET /profesores` `GET /profesores{id}`  `POST /profesores{id}` `PUT /profesores{id}` `DELETE /profesores{id}`
    
**Alumnos**
    `GET /alumnos`   `GET /alumnos/{id}` `POST /alumnos{id}` `PUT /alumnos{id}` `DELETE /alumnos{id}`
    
**Asignaturas**
    `GET /asignaturas`  `GET /asignaturas{id}`  `POST /asignaturas{id}`   `DELETE /asignaturas{id}`
    
## API Doc
Para información más detallada de este API, se puede consultar la documentación r con `/docs` que facilita FastApi (http://localhost:5000/docs (si lo estás ejecutando localmente, por ejemplo, o con el puerto del servidor seleccionado) o redirigiendote directamente a la [documentación API Proyecto_Universidad](https://www.notion.so/API-UNIVERSIDAD-F5-0b53649aa0e4431298483a4c63bc2064).

## Pruebas (testing)
En este proyecto utilizamos `Pytest` para ejecutar pruebas unitarias y testing total del funcionamiento del API.
- Seleccionar la carpeta `test`
- Correr el siguiente comando:
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

## Futuras mnodidifcaciones o implementaciones
Para futuras modificaciones o implementaciones de esta API rest, se debe tener en cuenta las siguientes recomendaciones:

-Modifica o añade los **modelos** de SQLAlchemy en .app/models/.

-Modificación o adición de los **esquemas** de Pydantic en .app/schemas/.

-Modificación o adición de los **endpoints** de la API en .app/api/.

-Modificación o adición de las utilidades o **métodos CRUD** (Create, Read, Update, Delete) en .app/crud/. 


Se recomienda modificar modelos, endpoints y utilidades CRUD de acuerdo a tus necesidades.

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
