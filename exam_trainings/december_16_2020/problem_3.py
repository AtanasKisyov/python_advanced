def index_exist(row, col, iterable):
    if row in range(len(iterable)) and col in range(len(iterable[row])):
        return True
    return False


def create_triangle(n):
    triangle = [[1], [1, 1]]
    for r in range(2, n):
        triangle.append([])
        for c in range(r + 1):
            triangle[r].append(0)
    return triangle


def get_magic_triangle(n):
    triangle = create_triangle(n)
    for row in range(2, len(triangle)):
        for col in range(len(triangle[row])):
            cell = 0
            if index_exist(row - 1, col - 1, triangle):
                cell += triangle[row - 1][col - 1]
            if index_exist(row - 1, col, triangle):
                cell += triangle[row - 1][col]
            triangle[row][col] = cell
    return triangle


up_left = (-1, -1)
up_right = (-1, 0)

print(*get_magic_triangle(6), sep="\n")