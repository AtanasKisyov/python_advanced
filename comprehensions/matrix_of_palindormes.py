rows, columns = [int(i) for i in input().split()]
matrix = []
for row in range(rows):
    current_row = []
    for column in range(columns):
        cell = f"{chr(row + 97)}{chr(row + column + 97)}{chr(row + 97)}"
        current_row.append(cell)
    matrix.append(current_row)

[print(' '.join(row)) for row in matrix]
