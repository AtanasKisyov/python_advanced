def push(element):
    stack.insert(0, element)
    return stack


def delete():
    stack.pop(0)
    return stack


def maximum():
    return max(stack)


def minimum():
    return min(stack)


n = int(input())

stack = []

for i in range(n):
    data = [int(i) for i in input().split()]
    if data[0] == 1:
        push(data[1])
    elif data[0] == 2:
        if stack:
            delete()
    elif data[0] == 3:
        if stack:
            print(maximum())
    elif data[0] == 4:
        if stack:
            print(minimum())

print(', '.join([str(i) for i in stack]))
