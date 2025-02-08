from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    pass


class AppSettings(Settings):
    DB_ECHO: bool
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    CORS_ALLOWED_ORIGINS: str


class DBSettings(Settings):
    pass


class UvicornSettings(Settings):
    APP_HOST: str
    APP_PORT: str
    RELOAD: bool
    WORKERS: int


app_settings = AppSettings()
db_settings = DBSettings()
uvicorn_settings = UvicornSettings()