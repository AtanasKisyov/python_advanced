def get_unique_chemicals(num):
    result = set()
    for _ in range(num):
        result.update(input().split())
    return result


def print_result(collection):
    for element in collection:
        print(element)


chemicals = get_unique_chemicals(int(input()))
print_result(chemicals)
