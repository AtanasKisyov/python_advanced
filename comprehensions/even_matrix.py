def create_matrix(dimensions):
    return [[int(x) for x in input().split(", ")] for _ in range(dimensions)]


def is_even(n):
    return n % 2 == 0


def filtered_nums(row):
    return [num for num in row if is_even(num)]


def filter_matrix(iterable):
    return [filtered_nums(row) for row in iterable]


matrix = create_matrix(int(input()))
print(filter_matrix(matrix))
