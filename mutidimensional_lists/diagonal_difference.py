def matrix_creation(length):
    m_res = []
    for _ in range(length):
        row = [int(i) for i in input().split()]
        m_res.append(row)
    return m_res


def sum_diagonals(iterable):
    primary_d = 0
    sub_d = 0
    for i in range(len(iterable)):
        primary_d += iterable[i][i]
    index = len(iterable)
    for y in range(index):
        index -= 1
        sub_d += iterable[y][index]
    return find_difference(primary_d, sub_d)


def find_difference(num1, num2):
    return abs(num1 - num2)


n = int(input())
matrix = matrix_creation(n)
print(sum_diagonals(matrix))
