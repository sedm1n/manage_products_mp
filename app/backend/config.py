from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
      MODE:Literal["DEV","PROD","TEST"]
      
      DB_HOST: str
      DB_USER: str
      DB_PASSWORD: str
      DB_PORT: int
      DB_NAME: str

      TEST_DB_HOST: str
      TEST_DB_USER: str
      TEST_DB_PASSWORD: str
      TEST_DB_PORT: int
      TEST_DB_NAME: str

      

      SECRET_KEY:str
      

      model_config = SettingsConfigDict(env_file='app/backend/.env', env_file_encoding='utf-8')
      

cfg = Config()

