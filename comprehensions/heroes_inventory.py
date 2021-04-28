heroes = input().split(", ")

inventory = {key: {"items": [], "cost": []} for key in heroes}

items = input()

res = []

while not items == "End":
    name, item, cost = items.split("-")
    if item not in inventory[name]['items']:
        inventory[name]['items'].append(item)
        inventory[name]['cost'].append(int(cost))
    items = input()

{print(f"{name} -> Items: {len(inventory[name]['items'])}, Cost: {sum(inventory[name]['cost'])}") for name in inventory}
