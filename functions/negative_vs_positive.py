def separate_negative_from_positive(numbers):
    return {
        'negatives': [x for x in numbers if x < 0],
        'positives': [x for x in numbers if x > 0]
    }


def sum_negative_and_positive(numbers):
    return {
        'negatives': sum(numbers['negatives']),
        'positives': sum(numbers['positives'])
    }


def print_result(iterable):
    print(iterable['negatives'])
    print(iterable['positives'])
    iterable = sorted(iterable.items(), key=lambda x: -abs(x[1]))
    print(f"The {iterable[0][0]} are stronger than the {iterable[1][0]}")


nums = [int(x) for x in input().split()]
separated_numbers = separate_negative_from_positive(nums)
sum_numbers = sum_negative_and_positive(separated_numbers)
print_result(sum_numbers)
