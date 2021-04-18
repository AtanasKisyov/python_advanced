from collections import deque


n = int(input())

index = 0

collection = deque()

for _ in range(n):
    collection.append([int(i) for i in input().split()])

original_collection = collection.copy()
full_circle = len(collection)
validate = False
station = []
liters = 0

while not full_circle == 0:
    station = collection.popleft()
    liters += station[0]
    distance = station[1]
    collection.append(station)
    if liters >= distance:
        full_circle -= 1
        liters -= distance
    else:
        full_circle = len(original_collection)
        liters = 0
    if full_circle == 0:
        validate = True
        starting_item = collection[0]
        print(original_collection.index(starting_item))
        break
