"""Configurazione Wallector MCP con Pydantic."""
from pydantic_settings import BaseSettings
from typing import Optional

class Config(BaseSettings):
    # Database
    mysql_host: str = "db4free.net"
    mysql_port: int = 3306
    mysql_user: str = "db_root"
    mysql_password: str = "password"
    mysql_database: str = "db_wallector"
    
    # MCP
    mcp_name: str = "wallector-mcp"
    mcp_version: str = "0.1.0"
    
    # Cache
    cache_ttl_seconds: int = 600
    
    # AUTH Deploy (opzionale)
    mcp_auth_token: Optional[str] = None  # MCP_AUTH_TOKEN
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Config()
