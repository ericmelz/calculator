from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    openai_api_key: SecretStr
    db_host: str
