from data.materials import materials
from services.renetation import get_offer
from services.order import save_order


REGIONS = ["СПБ", "МСК", "КРД"]


def choose_region():

    print("Выберите регион:\n")

    for i, region in enumerate(REGIONS, start=1):
        print(f"{i}. {region}")

    while True:

        try:
            choice = int(input("\nВведите номер региона: "))

            if 1 <= choice <= len(REGIONS):
                return REGIONS[choice - 1]

        except ValueError:
            pass

        print("Некорректный ввод.")


def choose_material(region):

    print("\nКаталог товаров:\n")

    for material in materials:
        print(
            f"{material.id}. "
            f"{material.name} "
            f"({material.category}) - "
            f"{material.prices[region]} руб."
        )

    while True:

        try:
            material_id = int(input("\nВведите номер товара: "))

            material = next(
                (
                    material
                    for material in materials
                    if material.id == material_id
                ),
                None
            )

            if material:
                return material

        except ValueError:
            pass

        print("Некорректный ввод.")


def main():

    region = choose_region()

    material = choose_material(region)

    current_price = material.prices[region]

    print("\nВаш заказ:")
    print(material.name)
    print(f"Цена: {current_price} руб.")

    answer = input(
        "\nОформляем заявку? (y/n): "
    ).lower()

    if answer == "y":

        save_order(
            material,
            region,
            current_price
        )

    else:

        offer = get_offer(
            material,
            region,
            materials
        )

        if offer["type"] == "alternative":

            print("\nМы можем предложить более дешевый аналог:")

            print(
                f"{offer['material'].name}"
            )

            print(
                f"Цена: {offer['price']} руб."
            )

        else:

            print("\nДля вас доступна скидка 5%")

            print(
                f"Новая цена: {offer['price']} руб."
            )


if __name__ == "__main__":
    main()