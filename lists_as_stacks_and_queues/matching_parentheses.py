expression = input()

OPEN_SYMBOL = "("
CLOSING_SYMBOL = ")"

stack = []

for i in range(len(expression)):
    symbol = expression[i]
    if symbol == OPEN_SYMBOL:
        stack.append(i)
    elif symbol == CLOSING_SYMBOL:
        i_1 = stack.pop()
        print(expression[i_1:i + 1])
