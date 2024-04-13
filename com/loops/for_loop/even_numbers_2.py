starting = int(input("Enter a starting number:"))
ending = int(input("Enter a ending number:"))
for_count = 0
if_count = 0

for numbers in range(starting, ending):
    for_count = for_count + 1
    if (numbers % 2) == 0:
        if_count = if_count + 1
        print(f"Even numbers are: {numbers}")
print(for_count)
print(if_count)