from collections import deque


def input_data():
    return deque([int(i) for i in input().split()])


def fill(cup, bottle):
    if bottle > cup:
        return bottle - cup
    elif cup > bottle:
        cup = cup - bottle
        cups.appendleft(cup)
    return 0


cups = input_data()
bottles = input_data()
wasted_water = 0

while cups:
    if bottles:
        current_cup = cups.popleft()
        current_bottle = bottles.pop()
        wasted_water += fill(current_cup, current_bottle)
    else:
        break

if not cups:
    bottles = reversed(bottles)
    print(f"Bottles: {' '.join(str(b) for b in bottles)}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f"Cups: {' '.join(str(c) for c in cups)}")
    print(f"Wasted litters of water: {wasted_water}")
