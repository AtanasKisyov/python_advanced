from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(';')
starting_time = datetime.strptime(input(), "%H:%M:%S") + timedelta(seconds=1)


available_robots = deque()
unavailable_robots = []

for robo in robots_data:
    name, time = robo.split("-")
    robot = {'name': name, 'time_needed': int(time), 'available_time': starting_time}
    available_robots.append(robot)

products = deque()

data = input()
END = 'End'

while not data == END:
    products.append(data)
    data = input()

current_time = starting_time

while products:
    for r in unavailable_robots:
        if current_time >= r['available_time']:
            unavailable_robots.remove(r)
            available_robots.append(r)
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_time'] = current_time + timedelta(seconds=current_robot['time_needed'])
        unavailable_robots.append(current_robot)
        print(f"{current_robot['name']} - {current_product} [{current_time.strftime('%H:%M:%S')}]")
    else:
        products.append(current_product)
    current_time += timedelta(seconds=1)
