from collections import deque


def create_bomb(e, p):
    num = e + p
    possible_bombs = {"crossete": num % 3 == 0 and num % 5 == 0, "willow": num % 5 == 0, "palm": num % 3 == 0}
    for bomb_type, formula in possible_bombs.items():
        if formula:
            return bomb_type
    return False


def print_status(status, effect_status, power_status, all_bombs):
    status_cases = {True: "Congrats! You made the perfect firework show!",
                    False: "Sorry. You can't make the perfect firework show."}
    print(status_cases[status])
    if len(effect_status) > 0:
        print(f"Firework Effects left: {', '.join(str(x) for x in effect_status)}")
    if len(power_status) > 0:
        print(f"Explosive Power left: {', '.join(str(x) for x in power_status)}")
    print(f"Palm Fireworks: {all_bombs['palm']}")
    print(f"Willow Fireworks: {all_bombs['willow']}")
    print(f"Crossette Fireworks: {all_bombs['crossete']}")


effects = deque([int(x) for x in input().split(", ") if int(x) > 0])
power = deque([int(x) for x in input().split(", ") if int(x) > 0])
is_ready = False

bombs = {
    "palm": 0,
    "willow": 0,
    "crossete": 0
}

while effects and power:
    current_effect = effects[0]
    current_power = power[-1]
    current_bomb = create_bomb(current_effect, current_power)
    if current_bomb:
        bombs[current_bomb] += 1
        effects.popleft()
        power.pop()
    else:
        if current_effect - 1 > 0:
            effects.append(effects.popleft() - 1)
        else:
            effects.popleft()
    if bombs["palm"] >= 3 and bombs["willow"] >= 3 and bombs["crossete"] >= 3:
        is_ready = True
        break

print_status(is_ready, effects, power, bombs)
