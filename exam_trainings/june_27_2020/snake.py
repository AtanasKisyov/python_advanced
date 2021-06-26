def create_field(rows):
    starting_index = []
    result = []
    for i in range(rows):
        result.append(list(input()))
        if "S" in result[i]:
            starting_index = [i, result[i].index("S")]
            result[i][result[i].index("S")] = "."
    return result, starting_index


def move(r_c_tuple, row, col, iterable):
    r, c = r_c_tuple
    row = row + r
    col = col + c
    if row in range(len(iterable)) and col in range(len(iterable[row])):
        return True
    return False


def position(r_c_tuple, row, col, iterable):
    r, c = r_c_tuple
    row = row + r
    col = col + c
    symbol = iterable[row][col]
    return symbol


def find_the_other_hole(iterable):
    for r in range(len(iterable)):
        for c in range(len(iterable[r])):
            if iterable[r][c] == "B":
                return r, c
    return False


n = int(input())
field, current_position = create_field(n)
current_row, current_column = current_position
food = 0
game_over = False
snake_fed = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    if move(directions[command], current_row, current_column, field):
        if position(directions[command], current_row, current_column, field) == "*":
            field[current_row][current_column] = "."
            current_row += directions[command][0]
            current_column += directions[command][1]
            field[current_row][current_column] = "."
            food += 1
        elif position(directions[command], current_row, current_column, field) == "B":
            field[current_row][current_column] = "."
            current_row += directions[command][0]
            current_column += directions[command][1]
            field[current_row][current_column] = "."
            new_position = find_the_other_hole(field)
            current_row = new_position[0]
            current_column = new_position[1]
            field[current_row][current_column] = "."
        elif position(directions[command], current_row, current_column, field) == "-":
            field[current_row][current_column] = "."
            current_row += directions[command][0]
            current_column += directions[command][1]
            field[current_row][current_column] = "."
    else:
        game_over = True
        break
    if food == 10:
        snake_fed = True
        field[current_row][current_column] = "S"
        break

if game_over:
    print("Game over!")
    print(f"Food eaten: {food}")
    for row in field:
        print(*row, sep="")
if snake_fed:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food}")
    for row in field:
        print(*row, sep="")
