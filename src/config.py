from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_DB_URL:str

    SECRET_KEY: str
    ALGORITHM:str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()


