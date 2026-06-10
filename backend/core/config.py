from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool = False
    DATABASE_URL: str
    DATABASE_URL_SYNC: str

    class Config:
        env_file = ".env"

settings = Settings()