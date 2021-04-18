stack = [int(i) for i in input().split()]
capacity = int(input())
racks_used = 0
used_capacity = 0

while stack:
    item = stack[-1]
    used_capacity += item
    if used_capacity > capacity:
        racks_used += 1
        used_capacity = 0
    elif used_capacity == capacity:
        racks_used += 1
        used_capacity = 0
        stack.pop()
    else:
        stack.pop()

if used_capacity > 0:
    racks_used += 1

print(racks_used)
