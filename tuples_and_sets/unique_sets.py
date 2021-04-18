def get_set(lenght):
    result = set()
    for _ in range(lenght):
        result.add(int(input()))
    return result


def print_unique_nums(batch_1, batch_2):
    nums = batch_1.intersection(batch_2)
    for num in nums:
        print(num)


lenght_set_1, lenght_set_2 = input().split()
set_1 = get_set(int(lenght_set_1))
set_2 = get_set(int(lenght_set_2))
print_unique_nums(set_1, set_2)
