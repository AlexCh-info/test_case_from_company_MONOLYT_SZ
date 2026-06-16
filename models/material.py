from dataclasses import dataclass

@dataclass
class Material:
    id: int
    name: str
    category: str
    prices: dict
