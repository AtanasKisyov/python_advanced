from collections import deque

people = deque()

PAID = 'Paid'
END = 'End'

data = input()

while not data == END:
    if data == PAID:
        while people:
            person = people.popleft()
            print(person)
    else:
        people.append(data)
    data = input()

print(f"{len(people)} people remaining.")
