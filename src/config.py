from pydantic_settings import BaseSettings

class Config(BaseSettings):
    wallector_api_url: str = "http://localhost:8080/api"
    cache_ttl_seconds: int = 600  # 10min
    api_timeout: float = 10.0

config = Config()
