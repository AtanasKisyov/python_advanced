from collections import deque

water = int(input())

START = "Start"
END = "End"
REFILL = "refill"
que = deque()

data = input()

while not data == START:
    que.append(data)
    data = input()

data = input()

while not data == END:
    if data.startswith(REFILL):
        water += int(data.split()[1])
    else:
        liters = int(data)
        if water - liters >= 0:
            person = que.popleft()
            print(f"{person} got water")
            water -= liters
        else:
            person = que.popleft()
            print(f"{person} must wait")
    data = input()

print(f"{water} liters left")
