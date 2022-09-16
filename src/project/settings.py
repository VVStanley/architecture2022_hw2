from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8000

    title: str = "Space ship battle"
    description: str = "Space lovers game"

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    LOG_DIR: Path = Path(__file__).resolve().parent.parent.parent

    database_url: str = ""

    jwt_secret: str = ""
    jwt_algorithm: str = "HS256"
    jwt_expires_s: int = 500600

    DB_USER: str = "postgres"
    DB_PASSWORD: str = "12345"
    DB_HOST: str = "127.0.0.1"
    DB_NAME: str = "shipbattle"
    DB_PORT: str = "5432"


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)
