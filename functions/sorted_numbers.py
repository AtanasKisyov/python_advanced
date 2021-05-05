def sorted_numbers(numbers):
    return list(sorted(numbers, key=lambda x: x))


nums = [int(x) for x in input().split()]

print(sorted_numbers(nums))
