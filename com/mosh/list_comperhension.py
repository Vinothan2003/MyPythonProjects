items = [
    ("Product No 1 ", 10),  # list of tuples
    ("Product No 2 ", 12),
    ("Product No 3 ", 4),
    ("Product No 4 ", 9)
]

mapping = [item[1] for item in items]
print(f"mapping : {mapping}")
print()

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [num for num in number if (num % 2 == 0)]
print(f"filtered : {filtered}")
