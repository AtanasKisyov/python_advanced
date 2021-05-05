def pull_numbers(key, numbers):
    odd_or_even = {
        'Odd': list(filter(lambda x: not x % 2 == 0, numbers)),
        'Even': list(filter(lambda x: x % 2 == 0, numbers))
    }
    return odd_or_even[key]


def calculate(numbers):
    return sum(numbers) * len(nums)


command = input()
nums = [int(x) for x in input().split()]
filtered_numbers = pull_numbers(command, nums)
print(calculate(filtered_numbers))
