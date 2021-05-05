def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


nums = [int(x) for x in input().split()]

print(even_numbers(nums))
