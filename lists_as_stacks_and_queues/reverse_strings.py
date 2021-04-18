stack = list(input())

reverse = []

while stack:
    reverse.append(stack.pop())

print(''.join(reverse))
