number = [10, 20, 40, 50, 30]
max_number = number[0]
for great_num in number:
    if great_num > max_number:
        max_number = great_num
        print(max_number)
print(f"Greatest number in list :{max_number}")

number.remove(10)
print(number)

print(number.index(0))