even_count = 0
odd_count = 0
for i in range(1, 11):
    if (i % 2) == 0:
        even_count = even_count + 1
        print(f"Even number : {i}")
    else:
        odd_count = odd_count + 1
        print(f"Odd number : {i}")
print(f"Even number count : {even_count}")
print(f"Odd number count : {odd_count}")
