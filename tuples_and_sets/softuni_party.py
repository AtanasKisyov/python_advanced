def reservations(num):
    result = set()
    for _ in range(num):
        result.add(input())
    return result


def arrived_guests(collection):
    guest = input()
    while not guest == "END":
        if guest in collection:
            collection.remove(guest)
        guest = input()
    return collection


def print_result(collection):
    collection = sorted(collection)
    print(len(collection))
    for guest in collection:
        print(guest)


reservation_list = reservations(int(input()))
print_result(arrived_guests(reservation_list))
