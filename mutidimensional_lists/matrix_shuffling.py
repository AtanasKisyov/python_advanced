def create_matrix(count_row):
    matrix_result = []
    for _ in range(count_row):
        matrix_result.append(input().split())
    return matrix_result


def is_valid_length(iterable):
    if len(iterable) == 5 and iterable[0] == "swap":
        return True
    else:
        return False


def swap(iterable_1, iterable_2):
    try:
        r1, c1, r2, c2 = [int(iterable_2[i]) for i in range(1, 5)]
        value_one = iterable_1[r1][c1]
        value_two = iterable_1[r2][c2]
        iterable_1[r1][c1] = value_two
        iterable_1[r2][c2] = value_one
    except:
        return False
    return True


rows, columns = input().split()
matrix = create_matrix(int(rows))

data = input()
END = "END"

while not data == END:
    command_data = data.split()
    if is_valid_length(command_data) and swap(matrix, command_data):
        for row in matrix:
            print(*row)
    else:
        print("Invalid input!")
    data = input()
