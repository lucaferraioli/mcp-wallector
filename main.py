from fastmcp import FastMCP
from src.tools.server_info import setup_tools  # Basic tools
from src.tools.products import register_products  # ← AGGIUNGI

# MCP server base
mcp = FastMCP("wallector-mcp", version="0.1.0")

setup_tools(mcp)
register_products(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
    #mcp.run(transport="http", host="0.0.0.0", port=8080)