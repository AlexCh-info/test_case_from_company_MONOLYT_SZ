def get_offer(selected_material, region, materials):
    category_materials = [
        material
        for material in materials
        if material.category == selected_material.category
    ]

    cheapest_material = min(
        category_materials,
        key=lambda material: material.prices[region]
    )

    if cheapest_material.id != selected_material.id:
        return {
            "type": "alternative",
            "material": cheapest_material,
            "price": cheapest_material.prices[region]
        }

    discounted_price = round(
        selected_material.prices[region] * 0.95,
        2
    )

    return {
        "type": "discount",
        "material": selected_material,
        "price": discounted_price
    }