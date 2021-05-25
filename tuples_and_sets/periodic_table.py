def get_collection(n):
    res = set()
    for _ in range(n):
        current_line = input().split()
        res.update({el for el in current_line})
    return res


chemicals = get_collection(int(input()))
print(*chemicals, sep="\n")
