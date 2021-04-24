def create_field(dimensions):
    result = []
    for _ in range(dimensions):
        result.append(input().split())
    return result


def starting_position(iterable):
    for r in range(len(iterable)):
        for c in range(len(iterable[r])):
            if iterable[r][c] == "s":
                return [r, c]


def total_coal(iterable):
    res = 0
    for r in range(len(iterable)):
        for c in range(len(iterable[r])):
            if iterable[r][c] == "c":
                res += 1
    return res


def is_valid(r, c, v):
    if r in range(v) and c in range(v):
        return True
    return False


n = int(input())
command = input().split()
field = create_field(n)
position = starting_position(field)
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
all_coal = total_coal(field)
coal = 0
end_of_game = False
row, column = position[0], position[1]

while command:
    current_dir = command.pop(0)
    if is_valid(row + directions[current_dir][0], column + directions[current_dir][1], n):
        row += directions[current_dir][0]
        column += directions[current_dir][1]
    else:
        continue
    if field[row][column] == "c":
        coal += 1
        field[row][column] = "*"
    elif field[row][column] == "e":
        end_of_game = True
        break

if not end_of_game:
    if coal == all_coal:
        print(f"You collected all coals! ({row}, {column})")
    else:
        print(f"{all_coal - coal} coals left. ({row}, {column})")
else:
    print(f"Game over! ({row}, {column})")
