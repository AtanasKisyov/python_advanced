import re


categories = {key: {} for key in input().split(", ")}
items_count = int(input())

for i in range(items_count):
    cat, item, qty, quantity, qual, quality = re.split(r"[-;:]", input())
    cat = cat.strip()
    item = item.strip()
    categories[cat].update({item: {'quantity': int(quantity), 'quality': int(quality)}})


count_items = 0
average = 0
categories_count = 0
result_list = []

for k, v in categories.items():
    categories_count += 1
    string_to_append = f"{k} -> {', '.join(v.keys())}"
    for sub_k, sub_v in v.items():
        count_items += sub_v['quantity']
        average += sub_v['quality']
    result_list.append(string_to_append)
average = f"Average quality: {average / categories_count:.2f}"
count_items = f"Count of items: {count_items}"

print(count_items, average, *result_list, sep='\n')


