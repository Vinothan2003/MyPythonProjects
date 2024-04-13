# def sort_items(item):
#     return item[1]


items = [
    ("Product No 1 ", 10),  # taking the item[1] --> 10,12,4,9 then sorting the list of tuples
    ("Product No 2 ", 12),
    ("Product No 3 ", 4),
    ("Product No 4 ", 9)
]
# lambda function
items.sort(key=lambda item: item[1])  # no positional argument allowed
print(items)  # parameter: expression
