def create_matrix(n):
    m = []
    for _ in range(n):
        m.append([int(i) for i in input().split(', ')])
    return m


def sum_matrix(m):
    total_sum = 0
    for r in m:
        total_sum += sum(r)
    return total_sum


rows, columns = input().split(', ')
matrix = create_matrix(int(rows))
print(sum_matrix(matrix))
print(matrix)
