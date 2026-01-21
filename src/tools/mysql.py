from fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Dict, Any
from src.utils.mysql_client import db
from src.auth import require_authentication, AuthError

class QueryInput(BaseModel):
    query: str
    params: List[str] = []

def register_mysql_tools(mcp: FastMCP):
    @mcp.tool()
    async def list_tables() -> List[str]:
        """Elenca tabelle ArtEcommerce DB."""
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return tables
    
    @mcp.tool()
    async def describe_table(table: str) -> Dict[str, Any]:
        """Schema tabella (colonne, tipi)."""
        schema = db.get_table_schema(table)
        return {"table": table, "schema": schema}
    
    @mcp.tool()
    @require_authentication
    async def execute_query(query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Esegui query SQL sicura su ArtEcommerce.
        LIMIT automatico per sicurezza.
        Richiede autenticazione.
        """
        # Validazione input per sicurezza
        if not query.strip().upper().startswith('SELECT'):
            raise AuthError("Sono consentite solo query SELECT")
        
        if limit > 100:
            raise AuthError("Il limite massimo è 100 righe")
        
        safe_query = f"{query} LIMIT {limit}"
        results = db.execute_query(safe_query)
        return results[:limit]