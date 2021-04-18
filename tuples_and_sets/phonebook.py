def get_phonebook():
    data = input()
    result = {}
    while data:
        if not data.isdigit():
            name, number = data.split("-")
            result[name] = number
        else:
            break
        data = input()
    return [result, data]


def print_result(n, collection):
    for _ in range(int(n)):
        contact = input()
        if contact in collection:
            print(f"{contact} -> {collection[contact]}")
        else:
            print(f"Contact {contact} does not exist.")


phonebook, num = get_phonebook()
print_result(num, phonebook)
