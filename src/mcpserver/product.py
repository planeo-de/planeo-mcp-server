from mcp.server.fastmcp import FastMCP
import os
import httpx

API_BASE_URL = os.getenv("PLANEO_API_BASE_URL", "https://www.planeo.de/apiv2")

mcp = FastMCP("Planeo shop MCP")

@mcp.tool()
def get_product_by_sku(sku: str) -> dict:
    """
    Get a product details by SKU.

    Args:
        sku: The SKU of the product.

    Returns:
        A dictionary containing the product data.
    """
    response = httpx.get(f"{API_BASE_URL}/catalog/product/sku/{sku}")
    return response.json()
