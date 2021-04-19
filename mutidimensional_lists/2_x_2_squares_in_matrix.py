def create_matrix(count_rows):
    matrix_result = []
    for _ in range(count_rows):
        matrix_result.append(input().split())
    return matrix_result


def find_squares(iterable):
    count = 0
    for row in range(len(iterable) - 1):
        for column in range(len(iterable[row]) - 1):
            c1, c2, c3, c4 = iterable[row][column], iterable[row + 1][column], \
                             iterable[row + 1][column + 1], iterable[row][column + 1]
            if c1 == c2 and c2 == c3 and c3 == c4:
                count += 1
    return count


def print_result(count):
    print(count)


rows, columns = input().split()
matrix = create_matrix(int(rows))
equal_squares_count = find_squares(matrix)
print_result(equal_squares_count)
