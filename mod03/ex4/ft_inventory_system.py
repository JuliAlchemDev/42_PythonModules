import sys


def get_inventory(data: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for item in data:
        if ":" not in item:
            print(f"Error - invalid parameter '{item}'")
            continue

        data = item.split(":")
        name = data[0]

        if name in inventory.keys():
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            inventory.update({
                name: int(data[1])
            })
        except ValueError as error:
            print(f"Quantity error for '{data[0]}': {error}")

    return inventory


def get_most_least_items(inventory: dict[str, int]) -> list[tuple[str, int]]:
    least = list(inventory.items())[0]
    most = least
    for name, k in inventory.items():
        if k < least[1]:
            least = (name, k)
        if k > most[1]:
            most = (name, k)
    return [most, least]


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = get_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    total_k = sum(list(inventory.values()))
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total_k}")

    for name, k in inventory.items():
        pct = round((k * 100) / total_k, 1)
        print(f"Item {name} represents {pct}%")

    most, least = get_most_least_items(inventory)
    print(f"Item most abundant: {most[0]} with quantity {most[1]}")
    print(f"Item least abundant: {least[0]} with quantity {least[1]}")

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")

    # names = list(inventory)
    # values = list(inventory.values())
    # i = 0
    # for name in names:
    #     if name == "armor":
    #         print(f"{name}: {values[i]}")
    #     i += 1


if __name__ == "__main__":
    main()


# sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
