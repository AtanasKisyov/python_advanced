def create_matrix(n):
    m = []
    for _ in range(n):
        m.append([int(i) for i in input().split()])
    return m


def sum_matrix_columns(m, r, c):

    for i in range(c):
        column_sum = 0
        for y in range(r):
            column_sum += m[y][i]
        print(column_sum)


rows, columns = input().split(', ')
matrix = create_matrix(int(rows))
sum_matrix_columns(matrix, int(rows), int(columns))
