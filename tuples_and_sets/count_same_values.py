def input_to_list(string):
    return string.split()


def from_list_to_dict(list_collection):
    res = {}
    for element in list_collection:
        if element not in res:
            res[element] = 0
        res[element] += 1
    return res


def print_result(dictionary):
    for key, value in dictionary.items():
        print(f"{float(key)} - {value} times")


nums = input_to_list(input())
print_result(from_list_to_dict(nums))


