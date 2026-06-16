from dataclasses import dataclass

@dataclass
class Order:
    material: str
    category: str
    region: str
    price: float
    created_at: str