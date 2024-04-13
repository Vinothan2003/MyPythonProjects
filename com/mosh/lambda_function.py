items = [
    ("Product No 1 ", 10),
    ("Product No 2 ", 12),
    ("Product No 3 ", 4),
    ("Product No 4 ", 9)
]

items.sort(key=lambda item: item[1])  # lambda argument: expression
print(items)
