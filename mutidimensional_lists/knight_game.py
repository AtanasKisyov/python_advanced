def create_matrix(dimensions):
    result_matrix = [list(input()) for _ in range(dimensions)]
    return result_matrix


def knight_moves(i, c, r):
    moves = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-1, -2), (1, -2), (-2, -1), (2, -1)]
    hits = 0
    for move in moves:
        current_col = c + move[0]
        current_row = r + move[1]
        if current_col in range(n) and current_row in range(n):
            if i[current_row][current_col] == "K":
                hits += 1
    return hits


n = int(input())
matrix = create_matrix(n)
best_knight_coordinates = []
counter = 0
best_knight = 0

while True:
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                current_knight = knight_moves(matrix, col, row)
                if current_knight > best_knight:
                    best_knight = current_knight
                    best_knight_coordinates = [row, col]
    if best_knight_coordinates:
        best_knight = 0
        counter += 1
        matrix[best_knight_coordinates[0]][best_knight_coordinates[1]] = 0
        best_knight_coordinates.clear()
    else:
        break
print(counter)
