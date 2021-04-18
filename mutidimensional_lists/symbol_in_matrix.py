def create_matrix(n):
    m = []
    for _ in range(n):
        m.append(list(input()))
    return m


def find_symbol(m, s):
    for row in range(len(m)):
        if s in m[row]:
            return f"({row}, {m[row].index(s)})"
    return f"{s} does not occur in the matrix"


rows = int(input())
matrix = create_matrix(rows)
symbol = input()
print(find_symbol(matrix, symbol))
