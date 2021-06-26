from collections import deque


customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])

total_time = 0
success = True

while customers:
    if not taxis:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
        success = False
        break
    current_customer = customers[0]
    current_taxi = taxis[-1]
    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if success:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
