from pydantic_settings import BaseSettings
from typing import Optional

class Config(BaseSettings):
    mysql_host: str
    mysql_port: int = 3306
    mysql_user: str
    mysql_password: str
    mysql_database: str
    
    mcp_auth_token: Optional[str] = None
    mcp_name: str = "wallector-mcp"
    mcp_version: str = "0.1.0"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Config()
