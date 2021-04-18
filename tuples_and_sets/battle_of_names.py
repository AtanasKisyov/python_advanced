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

even_list = list(sorted(even_set, key=lambda x: -x))
odd_list = list(sorted(odd_set, key=lambda x: -x))

if sum(even_set) == sum(odd_list):
    print(*even_list, *odd_list, sep=", ")
elif sum(even_list) > sum(odd_list):
    print(*even_list, *odd_list, sep=", ")
elif sum(even_list) < sum(odd_list):
    print(*odd_list, sep=", ")
