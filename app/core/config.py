import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
import os
import dotenv


"""Se define la Clase Settings para la configuración de la conexión a la base de datos, 
la llamada de las variables de entorno del archivo .env y los métodos necesarios para validar la conexión."""
class Settings(BaseSettings):
    dotenv.load_dotenv(verbose=True)

    APP_DEBUG: bool = True
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    DESCRIPTION: str = os.getenv("DESCRIPTION")
    VERSION: str = "0.0.1"

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    """BACKEND_CORS_ORIGINS ---> es una lista de os origenes en formato JSON, 
    Por ejemplo: '["http://localhost", "http://localhost:8080"""
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    """Validación de BACKEND_CORS_ORIGINS"""
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    """Definición de parámetros para la conexión de SQLAlchemy"""
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None


    """Validación de la conexión"""
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    """Validación del nombre del proyecto"""
    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v
    """Tiempo para resetear el token por email"""
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    """Validación del email"""
    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    """Cuenta de superadministrador"""

    EMAIL_TEST_USER: EmailStr = "admin@example.com"  # type: ignore
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    USERS_OPEN_REGISTRATION: bool = True

    class Config:
        case_sensitive = True


settings = Settings()
