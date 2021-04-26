def create_matrix(dimensions):
    return [[int(x) for x in input().split(", ")] for _ in range(dimensions)]


def flatten(iterable):
    # A short for cycle reads better than the nested comprehension:
    # [x for row in matrix for x in row]
    res = []
    for row in iterable:
        res.extend(row)
    return res


matrix = create_matrix(int(input()))
flat_matrix = flatten(matrix)
print(flat_matrix)
