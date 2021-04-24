from collections import deque


def create_field(dimensions):
    res = []
    for _ in range(dimensions):
        res.append(list(input()))
    return res


def find_position(iterable):
    for r in range(len(iterable)):
        for c in range(len(iterable[r])):
            if iterable[r][c] == "P":
                iterable[r][c] = "."
                return [r, c]


def bunnie_multiplication(iterable):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for_change = []
    for r in range(len(iterable)):
        for c in range(len(iterable[r])):
            if iterable[r][c] == "B":
                for el in dirs:
                    if r + el[0] in range(len(iterable)) \
                            and c + el[1] in range(len(iterable[r])):
                        for_change.append((r + el[0], c + el[1]))
    while for_change:
        current_change = for_change.pop(0)
        iterable[current_change[0]][current_change[1]] = "B"
    return iterable


rows, columns = [int(i) for i in input().split()]
field = create_field(rows)
commands = deque(input())
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
is_dead = False
is_won = False
row, col = find_position(field)
current_command = ''

while commands:
    current_command = commands.popleft()
    row += directions[current_command][0]
    col += directions[current_command][1]
    if row in range(rows) and col in range(columns):
        field = bunnie_multiplication(field)
        if field[row][col] == "B":
            is_dead = True
            break
    else:
        is_won = True
        field = bunnie_multiplication(field)
        break

for r in field:
    print(*r, sep="")

if is_won:
    row -= directions[current_command][0]
    col -= directions[current_command][1]
    print(f"won: {row} {col}")

if is_dead:
    print(f"dead: {row} {col}")

