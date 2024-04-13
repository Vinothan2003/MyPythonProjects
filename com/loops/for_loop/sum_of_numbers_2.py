""" sum_number = 0
for i in range(1,8):
    print(i)
    sum_number = sum_number + i
print(f"sum of numbers : {sum_number}") """

"""number = []

for i in range(1, 8):
    num = int(input(f"Enter any number {i} : "))
    number.append(num)
sum_numbers = sum(number)
avg_numbers = sum_numbers/len(number)
print(number)
print(f"sum of numbers : {sum_numbers}")
print(f"Average of numbers : {avg_numbers}")"""

number = int(input("Enter a number :"))
natural_numbers = ' '
sum_numbers = 0
for i in range(1, number + 1):
    sum_numbers = sum_numbers + i
    natural_numbers = natural_numbers + str(i) + ' '
print(f"The first {number} Natural numbers are : {natural_numbers}")
print(f"The sum of {number} is : {sum_numbers}")
