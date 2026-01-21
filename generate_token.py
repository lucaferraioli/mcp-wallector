#!/usr/bin/env python3
"""Script per generare un token sicuro per MCP Wallector."""

import os
import sys
from pathlib import Path

# Aggiungi la directory src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from auth import AuthManager

def main():
    """Genera un token sicuro e mostra come configurarlo."""
    
    # Genera token
    token = AuthManager.generate_secure_token(32)
    
    print("Token MCP Wallector Generato")
    print("=" * 50)
    print(f"Token: {token}")
    print()
    
    print("Come configurarlo:")
    print()
    
    print("1. Environment Variable (temporaneo):")
    print(f"   export MCP_AUTH_TOKEN='{token}'")
    print(f"   set MCP_AUTH_TOKEN={token}")
    print()
    
    print("2. File .env (consigliato):")
    print("   Crea/Modifica .env nella root del progetto:")
    print(f"   MCP_AUTH_TOKEN={token}")
    print()
    
    print("3. FastMCP Cloud:")
    print("   Imposta MCP_AUTH_TOKEN nelle environment variables del deployment")
    print()
    
    print("Verifica configurazione:")
    print("   python main.py")
    print("   Dovresti vedere: Autenticazione Bearer token attiva")
    print()
    
    print("Conserva questo token in un posto sicuro!")

if __name__ == "__main__":
    main()