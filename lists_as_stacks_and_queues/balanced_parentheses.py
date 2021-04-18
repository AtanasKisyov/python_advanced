opening_parentheses = ['{', '[', '(']
closing_parentheses = {'}': '{', ']': '[', ')': '('}

sequence = list(input())

stack = []

validate = True

for i in range(len(sequence)):
    element = sequence[i]
    if element in opening_parentheses:
        stack.append(element)
    else:
        try:
            if stack[-1] == closing_parentheses[element]:
                stack.pop()
            else:
                validate = False
        except IndexError:
            validate = False

if validate:
    print("YES")
else:
    print('NO')
