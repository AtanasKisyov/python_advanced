def min_num(numbers):
    return f"The minimum number is {min(numbers)}"


def max_num(numbers):
    return f"The maximum number is {max(numbers)}"


def sum_num(numbers):
    return f"The sum number is: {sum(numbers)}"


nums = [int(x) for x in input().split()]

result = [min_num(nums), max_num(nums), sum_num(nums)]

[print(el) for el in result]
