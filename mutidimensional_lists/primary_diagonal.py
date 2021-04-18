def create_matrix(n):
    m = []
    for _ in range(n):
        m.append([int(i) for i in input().split()])
    return m


def sum_matrix_primary_diagonal(m):
    total = 0
    for i in range(len(m)):
        total += m[i][i]
    return total


num = int(input())
print(sum_matrix_primary_diagonal(create_matrix(num)))
