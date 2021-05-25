def get_collection(n):
    return {input() for _ in range(n)}


names = get_collection(int(input()))
print(*names, sep="\n")
