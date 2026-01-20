from pydantic_settings import BaseSettings

class Config(BaseSettings):
    mysql_host: str = "db4free.net"
    mysql_port: int = 3306
    mysql_user: str = "db_root"  # Il tuo user
    mysql_password: str = "password"   # Il tuo pass
    mysql_database: str = "db_wallector"
    cache_ttl_seconds: int = 600

config = Config()
