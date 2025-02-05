from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    SERVER_ADDRESS: str = "0.0.0.0"
    SERVER_PORT: int = "8080"
    # POSTGRES_CONN: str
    # POSTGRES_JDBC_URL: str
    # POSTGRES_USERNAME: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_HOST: str
    # POSTGRES_PORT: int
    # POSTGRES_DATABASE: str
    # REDIS_HOST: str
    # REDIS_PORT: int
    # ANTIFRAUD_ADDRESS: str
    # RANDOM_SECRET: str
    ENVIRONMENT: Literal["local", "staging", "production"] = "production"
    # FIRST_SUPERUSER: str = "admin@admin.com"
    # FIRST_SUPERUSER_PASSWORD: str = "admin"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = (
    #     60 * 24 * 8
    # )  # 60 minutes * 24 hours * 8 days = 8 days
    GEMINI_API: str
    SECRET_KEY: str = "secret_key_here"


settings = Settings()


if settings.ENVIRONMENT == "local":
    print(settings.dict())
