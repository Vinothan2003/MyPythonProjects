items = [
    ("Product No 1 ", 10),
    ("Product No 2 ", 12),
    ("Product No 3 ", 4),
    ("Product No 4 ", 9)
]
# filter(function, iterable) --> it will return filtered iterable elements if the CONDITION is satisfied
filtered_item = list(filter(lambda item: item[1] >= 10, items))
print(filtered_item)
print(items)

"""for filtered in items:
    if filtered[1] >= 10:
        filter_item.append(filtered)
print(filter_item)"""
