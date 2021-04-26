def valid_num(n):
    return [x for x in range(2, 11) if n % x == 0]


def numbers(start, end):
    return [x for x in range(start, end + 1) if valid_num(x)]


start_num = int(input())
end_num = int(input())
print(numbers(start_num, end_num))
