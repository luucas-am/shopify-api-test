import requests
from src.constants import STORE_URL, headers


class ProductsService:
    def get_all() -> dict:
        endpoint = f"{STORE_URL}/admin/api/2024-04/products.json"
        response = requests.get(endpoint, headers=headers)
        return response.json()
