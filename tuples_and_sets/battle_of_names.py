def sum_letters(string):
    result = 0
    for el in string:
        result += ord(el)
    return result


def divide(num1, num2):
    return num1 // num2


n = int(input())

odd_set = set()
even_set = set()


for i in range(1, n + 1):
    name = input()
    name_result = divide(sum_letters(name), i)
    if name_result % 2 == 0:
        even_set.add(name_result)
    else:
        odd_set.add(name_result)

sum_even = sum(even_set)
sum_odd = sum(odd_set)

if sum_even == sum_odd:
    result = even_set.union(odd_set)
    print(*result, sep=", ")
elif sum_even > sum_odd:
    result = even_set.symmetric_difference(odd_set)
    print(*result, sep=", ")
elif sum_even < sum_odd:
    result = odd_set.difference(even_set)
    print(*result, sep=", ")
