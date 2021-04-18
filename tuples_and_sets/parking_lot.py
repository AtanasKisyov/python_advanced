def parking_lot(num):
    result = set()
    for _ in range(num):
        command, car = input().split(", ")
        if command == "OUT" and car in result:
            result.remove(car)
        elif command == "IN":
            result.add(car)
    return result


def result_print(collection):
    if collection:
        for car in collection:
            print(car)
    else:
        print("Parking Lot is Empty")


lot = parking_lot(int(input()))
result_print(lot)
