"""Tool info server Wallector MCP."""
from fastmcp import FastMCP
from typing import Dict, Any


def setup_tools(mcp: FastMCP) -> None:
    """Registra tool server_info."""
    
    @mcp.tool()
    async def get_server_info() -> Dict[str, Any]:
        """
        Restituisce informazioni sul server MCP Wallector.
        
        Utile per diagnostica e discovery tool disponibili.
        """
        return {
            "name": "Wallector MCP Server",
            "version": "0.1.0",
            "description": "Server MCP per catalogo opere d'arte Wallector.com",
            "author": "Criticaldrop Entertainment",
            "tools": [
                {
                    "name": tool.name,
                    "description": tool.description or "No description"
                }
                for tool in mcp.tools.values()
            ],
            "endpoints": ["stdio", "http"]  # Transport support
        }
