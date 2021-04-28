data = input().split("|")
res = []

for i in range(len(data) - 1, -1, -1):
    current_el = data[i].split()
    res.extend(current_el)

print(*res)
