items = [
    ("Product No 1 ", 10),  # list of tuples
    ("Product No 2 ", 12),
    ("Product No 3 ", 4),
    ("Product No 4 ", 9)
]
# map(function, *iterative) --> it will return the new iterable elements
quantity = list(map(lambda item: item[1], items))
print(quantity)
print(items)

"""quantity = []

for item in items:
    quantity.append(item[1])
print(quantity)"""
