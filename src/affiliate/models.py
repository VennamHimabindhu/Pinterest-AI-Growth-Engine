from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    name: str
    category: str
    product_url: str