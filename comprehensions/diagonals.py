def create_matrix(dimensions):
    return [[int(x) for x in input().split(", ")] for _ in range(dimensions)]


def primary_diagonal(iterable):
    return [iterable[x][x] for x in range(len(iterable))]


def sub_diagonal(iterable):
    res = []
    y = len(iterable) - 1
    for i in range(len(iterable)):
        res.append(iterable[i][y])
        y -= 1
    return res


matrix = create_matrix(int(input()))
first_diagonal = primary_diagonal(matrix)
second_diagonal = sub_diagonal(matrix)
print(f"First diagonal: {', '.join(str(x) for x in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")
