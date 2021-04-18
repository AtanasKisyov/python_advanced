def get_set(set_range):
    start, end = set_range.split(",")
    return set([int(i) for i in range(int(start), int(end) + 1)])


def get_intersection(set1, set2):
    return set1.intersection(set2)


def intersections_dict():
    result = {}
    for i in range(1, n + 1):
        data = input().split("-")
        set_1 = get_set(data[0])
        set_2 = get_set(data[1])
        result[i] = get_intersection(set_1, set_2)
    return result


def find_longest_intersection(collection):
    collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))
    return list(sorted(collection[0][1]))


n = int(input())

intersections = intersections_dict()

print(f"Longest intersection is {find_longest_intersection(intersections)} "
      f"with length {len(find_longest_intersection(intersections))}")
