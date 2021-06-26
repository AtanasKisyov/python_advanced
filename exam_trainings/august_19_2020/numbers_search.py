def numbers_searching(*args):
    args = sorted(args)
    duplicates = [el for el in args if args.count(el) > 1]
    result = []
    [result.append(el) for el in duplicates if el not in result]
    missing_number = [x for x in range(args[0], args[-1] + 1) if x not in args][0]
    return [missing_number, result]



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))