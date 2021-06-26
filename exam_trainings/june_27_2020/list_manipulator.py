from collections import deque


def list_manipulator(nums, *args):
    nums = deque(nums)
    if args[0] == "add" and args[1] == "beginning":
        ll = list(args[2:])
        nums = ll + list(nums)
    if args[0] == "add" and args[1] == "end":
        for el in args[2:]:
            nums.append(el)
    if args[0] == "remove" and args[1] == "beginning":
        if len(args) > 2:
            n = args[2]
            for i in range(n):
                nums.popleft()
        else:
            nums.popleft()
    if args[0] == "remove" and args[1] == "end":
        if len(args) > 2:
            n = args[2]
            for i in range(n):
                nums.pop()
        else:
            nums.pop()
    return list(nums)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
