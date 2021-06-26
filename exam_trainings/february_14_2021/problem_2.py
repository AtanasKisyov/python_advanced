from math import floor


def create_field(num):
    res = []
    for _ in range(num):
        res.append(input().split())
    return res


def find_player(iterable):
    for r in range(len(iterable)):
        for c in range(len(iterable[r])):
            if iterable[r][c] == "P":
                return r, c


def in_range(r, c, iterable):
    if r in range(len(iterable)) and c in range(len(iterable[r])):
        return True
    return False


def print_result(status, total_coins, path_list):
    cases = {True: f"You won! You've collected {total_coins} coins.",
             False: f"Game over! You've collected {total_coins} coins."}
    print(cases[status])
    print("Your path:")
    for el in path_list:
        print(f"[{el[0]}, {el[1]}]")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

field = create_field(int(input()))
player_row, player_column = find_player(field)
command = input()
is_win = False
path = []
coins = 0

while command:
    if command in directions:
        player_row += directions[command][0]
        player_column += directions[command][1]
        if not in_range(player_row, player_column, field) or field[player_row][player_column] == "X":
            is_win = False
            coins = floor(coins * 0.5)
            break
        else:
            coins += int(field[player_row][player_column])
            path.append((player_row, player_column))
    if coins >= 100:
        is_win = True
        break
    command = input()

print_result(is_win, coins, path)