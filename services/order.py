import json
from pathlib import Path
from datetime import datetime
from dataclasses import asdict

from models.order import Order


def save_order(material, region, price):

    order = Order(
        material=material.name,
        category=material.category,
        region=region,
        price=price,
        created_at=datetime.now().isoformat()
    )

    Path("orders").mkdir(exist_ok=True)

    filename = (
        f"orders/order_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            asdict(order),
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"\nЗаявка сохранена в {filename}")