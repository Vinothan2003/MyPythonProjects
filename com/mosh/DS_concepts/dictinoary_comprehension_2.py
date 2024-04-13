values = []
for i in range(1, 6):  # appending using for loop
    values.append(i * 2)
print(f"for loop : {values}")

# [expression for item in items]

values_2 = [i * 2 for i in range(1, 6)]  # list comprehension
print(f"list comprehension : {values_2}")

set_values = {i * 2 for i in range(1, 6)}
print(type(set_values))

dic_values = {i : i * 2 for i in range(1, 6)}
print(type(dic_values))
print(dic_values)
