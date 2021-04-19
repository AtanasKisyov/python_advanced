import sys


def create_matrix(count_rows):
    result_matrix = []
    for _ in range(count_rows):
        current_row = [int(i) for i in input().split()]
        result_matrix.append(current_row)
    return result_matrix


def find_biggest_matrix(iterable):
    biggest_matrix = []
    biggest_sum = -sys.maxsize
    for row in range(len(iterable) - 1):
        for column in range(len(iterable) - 1):
            try:
                current_matrix = [
                    [iterable[row][column], iterable[row][column + 1], iterable[row][column + 2]],
                    [iterable[row + 1][column], iterable[row + 1][column + 1], iterable[row + 1][column + 2]],
                    [iterable[row + 2][column], iterable[row + 2][column + 1], iterable[row + 2][column + 2]],
                ]
                current_sum = sum(current_matrix[0]) + sum(current_matrix[1]) + sum(current_matrix[2])
                if current_sum > biggest_sum:
                    biggest_sum = current_sum
                    biggest_matrix = current_matrix.copy()
            except IndexError:
                continue
    return biggest_matrix, biggest_sum


def print_result(iterable, num):
    print(f"Sum = {num}")
    for row in iterable:
        print(*row)


rows, columns = input().split()
matrix = create_matrix(int(rows))
result = find_biggest_matrix(matrix)
print_result(result[0], result[1])
