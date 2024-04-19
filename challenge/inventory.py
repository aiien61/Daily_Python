inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print(f'Total number of items: {item_total}')

def add_to_inventory(inventory: dict, added_items: list) -> dict:
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

if __name__ == '__main__':
    inventory = {'rope': 1, 'gold coin': 42}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)
