from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    IP_ADDRESS_API_KEY: str
    IP_ADDRESS_API: str


settings = Settings()
