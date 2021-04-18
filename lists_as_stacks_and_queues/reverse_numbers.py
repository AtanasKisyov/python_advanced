stack = [int(i) for i in input().split()]

reverse_stack = []

while stack:
    reverse_stack.append(stack.pop())

print(*reverse_stack)
