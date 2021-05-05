def func_executor(*args):
    res = [key(*value) for key, value in args]
    return res


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2

