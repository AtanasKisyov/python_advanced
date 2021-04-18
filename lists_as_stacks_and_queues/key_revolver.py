from collections import deque


def shoot(bullet, lock):
    if bullet > lock:
        locks.appendleft(lock)
        return "Ping!"
    else:
        return "Bang!"


bullet_price = int(input())
gun_barrel = int(input())
bullets = deque([int(i) for i in input().split()])
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())
total_fired_bullets = 0
fired_bullets = 0

while bullets:
    if fired_bullets == gun_barrel:
        print("Reloading!")
        fired_bullets = 0
    else:
        if locks:
            total_fired_bullets += 1
            fired_bullets += 1
            print(shoot(bullets.pop(), locks.popleft()))
        else:
            break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - (total_fired_bullets * bullet_price)}")
