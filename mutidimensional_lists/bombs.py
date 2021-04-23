def create_matrix(dimensions):
    result_matrix = []
    for _ in range(dimensions):
        r = [int(z) for z in input().split()]
        result_matrix.append(r)
    return result_matrix


def bomb_coordinates():
    initial_array = input().split()
    coordinate = []
    for el in initial_array:
        el = [int(y) for y in el.split(",")]
        coordinate.extend(el)
    return coordinate


n = int(input())
matrix = create_matrix(n)
coordinates = bomb_coordinates()
destination = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for dest in range(0, len(coordinates), 2):
    row = coordinates[dest]
    column = coordinates[dest + 1]
    value = matrix[row][column]
    if matrix[row][column] > 0:
        for d in destination:
            current_row = row + d[0]
            current_col = column + d[1]
            if current_col in range(n) and current_row in range(n):
                try:
                    if matrix[current_row][current_col] > 0:
                        matrix[current_row][current_col] -= value
                except IndexError:
                    continue
    else:
        continue
    matrix[row][column] = 0

active_cells_sum = 0
active_cells_count = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
            active_cells_count += 1
            active_cells_sum += matrix[row][col]

print(f"Alive cells: {active_cells_count}")
print(f"Sum: {active_cells_sum}")

for row in matrix:
    print(*row)
