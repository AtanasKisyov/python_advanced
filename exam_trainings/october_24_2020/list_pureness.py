from collections import deque


def best_list_pureness(numbers_list, number):
    best_pureness = 0
    best_rotation = 0
    numbers_list = deque(numbers_list)
    for rotation in range(0, number + 1):
        pureness = 0
        for i in range(len(numbers_list)):
            pureness += i * numbers_list[i]
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        else:
            pureness = 0
        numbers_list.appendleft(numbers_list.pop())
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

