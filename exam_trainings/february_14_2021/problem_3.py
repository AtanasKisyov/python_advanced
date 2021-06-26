def stock_availability(inventory, command, *args):
    if command == "delivery":
        inventory.extend(args)
        return inventory
    if len(args) == 0:
        inventory.pop(0)
        return inventory
    if isinstance(args[0], int):
        for i in range(int(args[0])):
            inventory.pop(0)
        return inventory
    for item in args:
        if item in inventory:
            while item in inventory:
                inventory.remove(item)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
