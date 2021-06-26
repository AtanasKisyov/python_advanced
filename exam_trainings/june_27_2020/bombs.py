from collections import deque


def check_bombs(bombs):
    count = 0
    for bomb in bombs.values():
        if bomb >= 3:
            count += 1
    if not count == 3:
        return False
    return True


bomb_types = {
    60: "Cherry Bombs",
    40: "Datura Bombs",
    120: "Smoke Decoy Bombs"
}

created_bombs = {
    40: 0,
    60: 0,
    120: 0
}

effects = deque([int(x) for x in input().split(", ")])
casings = deque([int(x) for x in input().split(", ")])

while True:
    if not effects or not casings or check_bombs(created_bombs):
        break
    current_effect = effects[0]
    current_casing = casings[-1]
    current_sum = current_effect + current_casing
    if current_sum in bomb_types:
        effects.popleft()
        casings.pop()
        created_bombs[current_sum] += 1
    else:
        casings[-1] -= 5

if check_bombs(created_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in effects)}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
else:
    print("Bomb Casings: empty")

sorted_bombs = sorted(created_bombs.items(), key=lambda x: x[0])

for key, value in bomb_types.items():
    print(f"{value}: {created_bombs[key]}")
