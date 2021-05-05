# from itertools import permutations
#
# text = input()
# a = permutations(text, len(text))
# print(*[''.join(x) for x in a], sep="\n")

def permutation(iterable, current_i=0):
    if current_i == len(iterable):
        print(''.join(iterable))
        return

    for i in range(current_i, len(iterable)):
        iterable[current_i], iterable[i] = iterable[i], iterable[current_i]
        permutation(iterable, current_i + 1)
        iterable[current_i], iterable[i] = iterable[i], iterable[current_i]


text = list(input())
permutation(text)
