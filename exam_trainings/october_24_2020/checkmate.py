def find_the_king(iterable):
    for r in range(len(iterable)):
        for c in range(len(iterable)):
            if iterable[r][c] == "K":
                return r, c


def in_range(r, c, iterable):
    if r in range(len(iterable)) and c in range(len(iterable[r])):
        return True
    return False


def check_cell(iterable, r, c):
    if iterable[r][c] == "Q":
        return True
    return False


directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
)

field = [input().split() for _ in range(8)]
king = find_the_king(field)
king_row, king_column = king

result = []

for row, col in directions:
    current_row, current_col = king_row, king_column
    while in_range(current_row, current_col, field):
        if check_cell(field, current_row, current_col):
            result.append([current_row, current_col])
            break
        current_row += row
        current_col += col

if result:
    print(*result, sep="\n")
else:
    print("The king is safe!")