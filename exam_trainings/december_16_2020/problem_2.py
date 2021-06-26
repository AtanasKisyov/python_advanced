def in_range(r, c, iterable):
    if r in range(len(iterable)) and c in range(len(iterable[r])):
        return True
    return False


directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

initial_string = input()
n = int(input())
field = []
player_position = ''

for i in range(n):
    field.append(list(input()))
    if "P" in field[i]:
        player_position = (i, field[i].index("P"))
        field[player_position[0]][player_position[1]] = "-"

m = int(input())
current_row, current_col = player_position

for _ in range(m):
    command = input()
    current_row += directions[command][0]
    current_col += directions[command][1]
    if in_range(current_row, current_col, field):
        if field[current_row][current_col].isalpha():
            initial_string += field[current_row][current_col]
            field[current_row][current_col] = "-"
    else:
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        if len(initial_string) >= 2:
            initial_string = initial_string[:-1]
        else:
            initial_string = ""

field[current_row][current_col] = "P"
print(initial_string)
[print(*row, sep="") for row in field]
