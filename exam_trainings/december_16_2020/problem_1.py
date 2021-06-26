from collections import deque


males = deque([int(x) for x in input().split() if int(x) > 0])
females = deque([int(x) for x in input().split() if int(x) > 0])
matches_count = 0
special = False

while males and females:
    current_male = males[-1]
    current_female = females[0]
    if current_male % 25 == 0:
        males.pop()
        continue
    if current_female % 25 == 0:
        females.popleft()
        continue
    if current_female == current_male:
        matches_count += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        if current_male - 2 > 0:
            males[-1] -= 2
        else:
            males.pop()


print(f"Matches: {matches_count}")

if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")