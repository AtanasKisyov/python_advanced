from functools import reduce


def operate(operator, *args):
    possible_operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    return reduce(possible_operators[operator], args)
