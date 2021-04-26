def to_list():
    return input().split(", ")


def char_to_ascii(iterable):
    return {char: ord(char) for char in iterable}


def print_result(iterable):
    print(iterable)


chars = to_list()
result = char_to_ascii(chars)
print_result(result)
