from collections import deque

kids = deque(input().split())

tosses = int(input())

counter = 0

while not len(kids) == 1:
    counter += 1
    current_kid = kids.popleft()
    if counter == tosses:
        print(f"Removed {current_kid}")
        counter = 0
    else:
        kids.append(current_kid)


last_kid = kids.popleft()

print(f"Last is {last_kid}")
