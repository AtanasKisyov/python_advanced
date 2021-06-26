def check_range(row, column, iterable):
    if row in range(len(iterable)) and column in range(len(iterable[row])):
        return True
    return False


def cell_value(row, col, mapper, iterable):
    result = 0
    for key, value in mapper.items():
        current_r = row + value[0]
        current_c = col + value[1]
        if check_range(current_r, current_c, iterable) and iterable[current_r][current_c] == "*":
            result += 1
    return result


directions_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}


field_range = int(input())
field = []
bomb_positions = []

for i in range(field_range):
    field.append([])
    for _ in range(field_range):
        field[i].append(0)

bombs_count = int(input())

for _ in range(bombs_count):
    current_bomb = input().strip("()")
    current_row, current_col = [int(x) for x in current_bomb.split(", ")]
    if check_range(current_row, current_col, field):
        field[current_row][current_col] = "*"

for r in range(len(field)):
    for c in range(len(field[r])):
        if not field[r][c] == "*":
            field[r][c] = cell_value(r, c, directions_mapper, field)

for r in field:
    print(*r, sep=" ")
