"""Modulo di autenticazione centralizzato per Wallector MCP."""
import os
import hashlib
import secrets
from typing import Optional, Tuple
from functools import wraps
from src.config import config


class AuthError(Exception):
    """Eccezione per errori di autenticazione."""
    pass


class AuthManager:
    """Gestore centralizzato dell'autenticazione Bearer token."""
    
    def __init__(self):
        self._token: Optional[str] = None
        self._token_hash: Optional[str] = None
        self._initialize_token()
    
    def _initialize_token(self) -> None:
        """Inizializza il token da environment variable."""
        token = os.environ.get("MCP_AUTH_TOKEN") or config.mcp_auth_token
        
        if token:
            self._validate_token_format(token)
            self._token = token
            # Store only hash for security
            self._token_hash = self._hash_token(token)
            print("Autenticazione Bearer token configurata")
        else:
            print("Nessun token di autenticazione configurato")
    
    def _validate_token_format(self, token: str) -> None:
        """Valida il formato del token."""
        if not token or len(token) < 16:
            raise AuthError("Il token deve essere lungo almeno 16 caratteri")
        
        # Controlla che il token contenga solo caratteri validi
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
        if not all(c in valid_chars for c in token):
            raise AuthError("Il token contiene caratteri non validi")
    
    def _hash_token(self, token: str) -> str:
        """Crea hash del token per confronto sicuro."""
        return hashlib.sha256(token.encode()).hexdigest()
    
    def is_authenticated(self, provided_token: str) -> bool:
        """Verifica se il token fornito è valido."""
        if not self._token_hash:
            return False
        
        provided_hash = self._hash_token(provided_token)
        return secrets.compare_digest(provided_hash, self._token_hash)
    
    def require_auth(self, token: str) -> None:
        """Richiede autenticazione, solleva eccezione se non valido."""
        if not self.is_authenticated(token):
            raise AuthError("Token non valido o mancante")
    
    def is_auth_configured(self) -> bool:
        """Verifica se l'autenticazione è configurata."""
        return self._token_hash is not None
    
    @staticmethod
    def generate_secure_token(length: int = 32) -> str:
        """Genera un token sicuro casuale."""
        return secrets.token_urlsafe(length)


# Decorator per proteggere i tool
def require_authentication(tool_func):
    """Decorator per richiedere autenticazione sui tool MCP."""
    @wraps(tool_func)
    async def wrapper(*args, **kwargs):
        # Estrai il token dal contesto MCP (se disponibile)
        # Nota: FastMCP potrebbe passare il token in kwargs come 'auth_token'
        auth_token = kwargs.get('auth_token') or os.environ.get('MCP_AUTH_TOKEN')
        
        if not auth_token:
            raise AuthError("Token di autenticazione mancante")
        
        # Usa l'istanza globale di auth_manager
        from src.auth import auth_manager
        auth_manager.require_auth(auth_token)
        return await tool_func(*args, **kwargs)
    
    return wrapper


# Istanza globale del gestore autenticazione
auth_manager = AuthManager()