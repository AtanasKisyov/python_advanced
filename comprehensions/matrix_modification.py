def create_matrix():
    return [[int(x) for x in input().split()] for _ in range(int(input()))]


def is_valid(rows, columns, valid_range):
    if rows in range(valid_range) and columns in range(valid_range):
        return True
    return False


def print_result(iterable):
    return [print(*r) for r in iterable]


matrix = create_matrix()

commands = input().split()

while "END" not in commands:
    command = commands[0]
    row, column, value = [int(x) for x in commands[1:]]
    if is_valid(row, column, len(matrix)):
        if command == "Add":
            matrix[row][column] += value
        else:
            matrix[row][column] -= value
    else:
        print("Invalid coordinates")
    commands = input().split()

print_result(matrix)
