import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Any, Optional
from functools import lru_cache
from src.config import config

class MySQLClient:
    def __init__(self):
        self.config = {
            "host": config.mysql_host,
            "port": config.mysql_port,
            "user": config.mysql_user,
            "password": config.mysql_password,
            "database": config.mysql_database,
        }
    
    def get_connection(self):
        return mysql.connector.connect(**self.config)
    
    @lru_cache(maxsize=128)
    def get_table_schema(self, table: str) -> List[Dict[str, str]]:
        """Schema tabella (colonne, tipi)."""
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"DESCRIBE `{table}`")
        schema = [{"Field": row["Field"], "Type": row["Type"]} for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return schema
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Esegui query sicura con params."""
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    def get_all_products(self) -> Optional[Dict[str, Any]]:
        """
        Get tutti i prodotti da Artworks.
        JOIN con Artists/Categories per dati completi.
        """
        query = """
        SELECT 
            a.Sku, a.Name, a.PriceToWallector, a.ImageUrl, 
            a.Height, a.Width, a.Depth,
            art.Name as ArtistName,
            c.Name as CategoryName
        FROM Artworks a
        LEFT JOIN Artists art ON a.ArtistId = art.Id
        LEFT JOIN Categories c ON a.CategoryId = c.Id
        """
        results = self.execute_query(query, ())
        return results if results else None
    
    def get_product(self, sku: str) -> Optional[Dict[str, Any]]:
        """
        Get prodotto da Artworks per SKU.
        JOIN con Artists/Categories per dati completi.
        """
        query = """
        SELECT 
            a.Sku, a.Name, a.PriceToWallector, a.ImageUrl, 
            a.Height, a.Width, a.Depth,
            art.Name as ArtistName,
            c.Name as CategoryName
        FROM Artworks a
        LEFT JOIN Artists art ON a.ArtistId = art.Id
        LEFT JOIN Categories c ON a.CategoryId = c.Id
        WHERE a.Sku = %s
        LIMIT 1
        """
        results = self.execute_query(query, (sku,))
        return results[0] if results else None
    
    # Bonus: artworks by artist
    def get_artworks_by_artist(self, artist: str, limit: int = 10) -> List[Dict[str, Any]]:
        query = """
        SELECT a.Sku, a.Name, a.PriceToWallector, art.Name as ArtistName
        FROM Artworks a
        JOIN Artists art ON a.ArtistId = art.Id
        WHERE art.Name LIKE %s
        ORDER BY a.PriceToWallector DESC
        LIMIT %s
        """
        return self.execute_query(query, (f"%{artist}%", limit))

db = MySQLClient()
