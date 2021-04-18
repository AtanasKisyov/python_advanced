def create_matrix(n):
    m = []
    for _ in range(n):
        m.append([int(i) for i in input().split(', ')])
    return m


def find_biggest_sum(m, row, col):
    biggest_sum = 0
    biggest_square = []
    for c in range(col - 1):
        for r in range(row - 1):
            c1 = m[r][c]
            c2 = m[r + 1][c]
            c3 = m[r][c + 1]
            c4 = m[r + 1][c + 1]
            current_sum = c1 + c2 + c3 + c4
            if current_sum > biggest_sum:
                biggest_sum = current_sum
                biggest_square = [c1, c3, c2, c4]
    return biggest_sum, biggest_square


rows, columns = input().split(', ')
matrix = create_matrix(int(rows))
result_sum, result_list = find_biggest_sum(matrix, int(rows), int(columns))
print(result_list[0], result_list[1])
print(result_list[2], result_list[3])
print(result_sum)
