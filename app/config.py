# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_name: str = "fastapi"
    database_username: str = "postgres"
    database_password: str = "awab"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"  # Optional: allows loading from a .env file

settings = Settings()
