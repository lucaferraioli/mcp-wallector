"""Tool info server Wallector MCP."""
from fastmcp import FastMCP
from typing import Dict, Any, List


def setup_tools(mcp: FastMCP) -> None:
    """Registra tool server_info."""
    
    @mcp.tool()
    async def get_server_info() -> Dict[str, Any]:
        """
        Restituisce informazioni sul server MCP Wallector.
        
        Utile per diagnostica e discovery tool disponibili.
        """
        tools_list: List[Dict[str, str]] = []

        for name, tool in mcp._tools.items():
            tools_list.append({
                "name": name,
                "description": getattr(tool, 'description', 'No desc')
            })
        
        return {
            "name": "Wallector MCP Server",
            "version": "0.1.0",
            "description": "Server MCP per catalogo opere d'arte Wallector.com",
            "author": "Criticaldrop Entertainment",
            "tools": tools_list,
            "tools_count": len(tools_list),
            "endpoints": ["stdio", "http"]  # Transport support
        }
