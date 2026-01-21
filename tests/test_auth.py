"""Test per il modulo di autenticazione."""
import pytest
import os
from unittest.mock import patch
from src.auth import AuthManager, AuthError, require_authentication, auth_manager


class TestAuthManager:
    """Test per AuthManager."""
    
    def setup_method(self):
        """Setup per ogni test."""
        # Pulisci environment variables
        for key in ['MCP_AUTH_TOKEN']:
            if key in os.environ:
                del os.environ[key]
    
    def test_no_token_configured(self):
        """Test quando nessun token è configurato."""
        with patch.dict(os.environ, {}, clear=True):
            manager = AuthManager()
            assert not manager.is_auth_configured()
    
    def test_valid_token_configuration(self):
        """Test configurazione con token valido."""
        valid_token = "valid_token_1234567890123456"
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': valid_token}):
            manager = AuthManager()
            assert manager.is_auth_configured()
    
    def test_invalid_token_too_short(self):
        """Test token troppo corto."""
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': 'short'}):
            with pytest.raises(AuthError, match="deve essere lungo almeno 16 caratteri"):
                AuthManager()
    
    def test_invalid_token_characters(self):
        """Test token con caratteri non validi."""
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': 'invalid_token_with@#$%'}):
            with pytest.raises(AuthError, match="contiene caratteri non validi"):
                AuthManager()
    
    def test_token_authentication_success(self):
        """Test autenticazione con token valido."""
        valid_token = "valid_token_1234567890123456"
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': valid_token}):
            manager = AuthManager()
            assert manager.is_authenticated(valid_token)
    
    def test_token_authentication_failure(self):
        """Test autenticazione con token non valido."""
        valid_token = "valid_token_1234567890123456"
        wrong_token = "wrong_token_1234567890123456"
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': valid_token}):
            manager = AuthManager()
            assert not manager.is_authenticated(wrong_token)
    
    def test_require_auth_success(self):
        """Test require_auth con token valido."""
        valid_token = "valid_token_1234567890123456"
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': valid_token}):
            manager = AuthManager()
            # Non dovrebbe sollevare eccezione
            manager.require_auth(valid_token)
    
    def test_require_auth_failure(self):
        """Test require_auth con token non valido."""
        valid_token = "valid_token_1234567890123456"
        wrong_token = "wrong_token_1234567890123456"
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': valid_token}):
            manager = AuthManager()
            with pytest.raises(AuthError, match="Token non valido o mancante"):
                manager.require_auth(wrong_token)
    
    def test_generate_secure_token(self):
        """Test generazione token sicuro."""
        token = AuthManager.generate_secure_token()
        assert len(token) >= 32
        # Verifica che contenga solo caratteri validi
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
        assert all(c in valid_chars for c in token)


class TestRequireAuthenticationDecorator:
    """Test per il decorator require_authentication."""
    
    @pytest.mark.asyncio
    async def test_decorator_with_valid_token(self):
        """Test decorator con token valido."""
        valid_token = "valid_token_1234567890123456"
        
        # Crea un'istanza di AuthManager per il test
        from src.auth import AuthManager
        test_manager = AuthManager()
        
        # Forza l'inizializzazione del token nel test manager
        test_manager._token = valid_token
        test_manager._token_hash = test_manager._hash_token(valid_token)
        
        with patch('src.auth.auth_manager', test_manager):
            @require_authentication
            async def test_function(*args, **kwargs):
                return "success"
            
            result = await test_function(auth_token=valid_token)
            assert result == "success"
    
    @pytest.mark.asyncio
    async def test_decorator_without_token(self):
        """Test decorator senza token."""
        with patch.dict(os.environ, {}, clear=True):
            @require_authentication
            async def test_function(*args, **kwargs):
                return "success"
            
            with pytest.raises(AuthError, match="Token di autenticazione mancante"):
                await test_function()
    
    @pytest.mark.asyncio
    async def test_decorator_with_invalid_token(self):
        """Test decorator con token non valido."""
        valid_token = "valid_token_1234567890123456"
        wrong_token = "wrong_token_1234567890123456"
        
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': valid_token}):
            @require_authentication
            async def test_function(*args, **kwargs):
                return "success"
            
            with pytest.raises(AuthError, match="Token non valido o mancante"):
                await test_function(auth_token=wrong_token)


if __name__ == "__main__":
    pytest.main([__file__])