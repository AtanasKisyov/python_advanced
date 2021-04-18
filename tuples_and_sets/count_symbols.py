def count_symbols(string):
    result = {}
    for el in string:
        result[el] = string.count(el)
    return result


def print_result(collection):
    for element, count in collection:
        print(f"{element}: {count} time/s")


def sort_symbols(collection):
    return sorted(collection.items(), key=lambda x: x[0])


symbols_in_string = sort_symbols(count_symbols(input()))
print_result(symbols_in_string)
