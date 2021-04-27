data = [int(x) for x in input().split(", ")]
numbers = {'Positive': [str(x) for x in data if x >= 0],
           'Negative': [str(x) for x in data if x < 0],
           'Even': [str(x) for x in data if x % 2 == 0],
           'Odd': [str(x) for x in data if not x % 2 == 0]}
result = {print(f"{key}: {', '.join(value)}") for key, value in numbers.items()}
