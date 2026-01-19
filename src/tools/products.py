from fastmcp import FastMCP
from pydantic import BaseModel
from typing import Optional, Dict, Any
from ..config import config  # Da creare dopo

class ListProductsInput(BaseModel):
    artist: Optional[str] = None
    sku: Optional[str] = None
    limit: int = 10
    offset: int = 0

def register_products(mcp: FastMCP) -> None:
    @mcp.tool()
    async def listproducts(input: ListProductsInput) -> Dict[str, Any]:
        products: List[Dict[str, Any]] = [
            {"sku": "ART001", "artist": "Banksy"},
            {"sku": "ART002", "artist": "Da Vinci"},
        ]
        filtered = [
            p for p in products
            if not input.artist or input.artist.lower() in p["artist"].lower()
        ]
        return {
            "items": filtered[input.offset: input.offset + input.limit],
            "total": len(filtered),
        }

    @mcp.tool()
    async def getproduct(sku: str) -> Dict[str, Any]:
        return {
            "sku": sku,
            "name": f"Opera {sku}",
            "price": 1500,
        }