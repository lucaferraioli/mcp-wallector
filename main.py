from fastmcp import FastMCP
from src.tools.server_info import setup_tools
from src.tools.products import register_products
from src.tools.mysql import register_mysql_tools
from src.auth import auth_manager, AuthError
import os

print("🚀 Avvio Wallector MCP...")

# Configurazione autenticazione centralizzata
if auth_manager.is_auth_configured():
    # Configura FastMCP con il token (senza esporlo nei log)
    token = os.environ.get("MCP_AUTH_TOKEN")
    if token:
        os.environ["FAST_MCP_AUTH_TOKEN"] = token  # FastMCP legge questa
    print("🔐 Autenticazione Bearer token attiva")
else:
    print("⚠️ Server in esecuzione senza autenticazione")

mcp = FastMCP("wallector-mcp", version="0.1.0")

print("📋 Registrazione tool...")
setup_tools(mcp)
register_products(mcp)
register_mysql_tools(mcp)  # DB live!

print("✅ TUTTI tool registrati!")
print("🌐 Server HTTP: http://localhost:8080")

if __name__ == "__main__":
    #mcp.run(transport="stdio")
    mcp.run(transport="http", host="0.0.0.0", port=8080)