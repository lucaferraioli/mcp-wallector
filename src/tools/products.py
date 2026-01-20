from fastmcp import FastMCP
from pydantic import BaseModel
from typing import Optional, Dict, Any
from ..config import config  # Da creare dopo
from src.utils.mysql_client import db

class ListProductsInput(BaseModel):
    artist: Optional[str] = None
    sku: Optional[str] = None
    limit: int = 10
    offset: int = 0

def register_products(mcp: FastMCP) -> None:
    print("🔧 Registrando tool PRODOTTI...")
    @mcp.tool()
    async def listproducts(input: ListProductsInput) -> Dict[str, Any]:
        products: list[Dict[str, Any]] = [
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
        """Dettaglio opera + widget."""
        product = db.get_product(sku)  # ← Helper centralizzato!
        
        if not product:
            return {"error": f"SKU {sku} non trovato"}
        
        return {
            "sku": product["Sku"],
            "name": product["Name"],
            "artist": product["ArtistName"],
            "price": product["PriceToWallector"],
            "image_url": product["ImageUrl"],
            "structuredContent": {  # Widget OpenAI
                "type": "ui.widget",
                "contents": [
                    {"type": "image", "source": product["ImageUrl"]},
                    {"type": "text", "text": f"🖼️ {product['ArtistName']} - €{product['PriceToWallector']}"}
                ]
            }
        }
    
    @mcp.tool()
    async def artworks_by_artist(artist: str, limit: int = 10) -> list[Dict[str, Any]]:
        """Opere per artista."""
        return db.get_artworks_by_artist(artist, limit)
    
    @mcp.tool()
    async def most_expensive_artwork() -> Dict:
        """Opera più costosa nel DB."""
        query = "SELECT * FROM Artworks ORDER BY PriceToWallector DESC LIMIT 1"
        return db.execute_query(query)[0]