number = int(input("Enter a range : "))  # Not Solved in list comprehension
list_number = max([int(input("> ")) for i in range(1, number + 1)])
# max() function is used to get the max in number in the list

print(f"the greatest number is : {list_number}")

"""for i in range(1, number + 1):   # solved
    num = int(input("> "))
    list_number.append(num)

greater_number = 0
for j in list_number:
    if j > greater_number:
        greater_number = j
print(f"the greater number in list: {greater_number}")"""
