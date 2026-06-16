"""
core/config.py
--------------
Centralised application settings.
All environment variables are read from the .env file and validated
at startup via Pydantic. If a required variable is missing the app
will refuse to start with a clear error message.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ---- General ----
    APP_NAME: str
    DEBUG: bool = False

    # ---- Database ----
    DATABASE_URL: str       # async URL used by SQLAlchemy at runtime (asyncpg)
    DATABASE_URL_SYNC: str  # sync URL used by Alembic for migrations (psycopg2)

    class Config:
        env_file = ".env"


# Single shared instance imported by the rest of the app
settings = Settings()