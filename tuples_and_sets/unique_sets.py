def get_collection(n):
    return {int(input()) for _ in range(n)}


first, second = input().split()
first, second = int(first), int(second)

first_set = get_collection(first)
second_set = get_collection(second)
print(*first_set.intersection(second_set), sep="\n")
