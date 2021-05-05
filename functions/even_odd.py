def even_odd(*args):
    commands = {
        'odd': [x for x in args[:-1] if not x % 2 == 0],
        'even': [x for x in args[:-1] if x % 2 == 0]
    }
    return commands[args[-1]]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))