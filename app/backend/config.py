from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
      DB_HOST: str
      DB_USER: str
      DB_PASSWORD: str
      DB_PORT: int
      DB_NAME: str

      SECRET_KEY:str
      

      model_config = SettingsConfigDict(env_file='app/backend/.env', env_file_encoding='utf-8')
      

cfg = DatabaseConfig()

