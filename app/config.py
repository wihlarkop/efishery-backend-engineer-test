import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    PORT: int
    SECRET_KEY: str
    ENABLE_API_DOCS: bool

    # uvicorn config
    RELOAD: bool

    # database
    DB: str
    DB_POOL_RECYCLE: int = 3600

    class Config:
        env_file = os.environ.get('ENV_FILE', '.env')
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
