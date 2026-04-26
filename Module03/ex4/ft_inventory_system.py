import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return

    inventory = {}
    for param in sys.argv[1:]:
        if ":" not in param:
            print(f"Error - invalid parameter '{param}'")
            continue

        name, qty_str = param.split(":", 1)

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[name] = qty
        except ValueError:
            print(f"Quantity error for '{name}': invalid literal for "
                  f"int() with base 10: '{qty_str}'")

    if not inventory:
        print("Inventory is empty.")
        return

    print("=== Inventory System Analysis ===")
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage = (qty / total_qty) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most_abundant = max(inventory, key=inventory.get)
    least_abundant = min(inventory, key=inventory.get)

    print(f"Item most abundant: {most_abundant} with quantity "
          f"{inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity "
          f"{inventory[least_abundant]}")

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
