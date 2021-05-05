def expressions(numbers, current_sum=0, expression=''):
    if not numbers:
        return [(expression, current_sum)]

    plus = expressions(numbers[1:], current_sum + numbers[0], f"{expression}+{numbers[0]}")
    minus = expressions(numbers[1:], current_sum - numbers[0], f"{expression}-{numbers[0]}")
    return plus + minus


nums = [int(x) for x in input().split(", ")]
print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep='\n')
