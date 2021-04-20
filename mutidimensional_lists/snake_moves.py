from collections import deque


def create_matrix(count_row, count_column):
    result_matrix = []
    for _ in range(count_row):
        current_row = [0 for i in range(count_column)]
        result_matrix.append(current_row)
    return result_matrix


def snake_moves(iterable, string):
    snake_tail = deque(string)
    for row in range(len(iterable)):
        if row % 2 == 0:
            for col in range(len(iterable[row])):
                current_symbol = snake_tail.popleft()
                iterable[row][col] = current_symbol
                snake_tail.append(current_symbol)
        else:
            for col in range(len(iterable[row]) - 1, -1, -1):
                current_symbol = snake_tail.popleft()
                iterable[row][col] = current_symbol
                snake_tail.append(current_symbol)
        print(*iterable[row], sep='')


rows, columns = [int(i) for i in input().split()]
snake = input()

stairs = create_matrix(rows, columns)
snake_moves(stairs, snake)
