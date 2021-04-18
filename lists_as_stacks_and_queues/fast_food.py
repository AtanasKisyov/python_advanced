from collections import deque

food = int(input())

orders_que = deque([int(i) for i in input().split()])

print(max(orders_que))

while orders_que:
    order = orders_que[0]
    if food - order >= 0:
        food -= order
        orders_que.popleft()
    else:
        break

if orders_que:
    print(f"Orders left: {' '.join([str(i) for i in orders_que])}")
else:
    print("Orders complete")
