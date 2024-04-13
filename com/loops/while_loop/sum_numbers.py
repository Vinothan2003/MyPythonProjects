number = int(input("Enter a number : "))
sum_numbers = 0
increment = 1

while increment <= number:
    sum_numbers += increment
    increment += 1
print(f"the sum numbers {number} is {sum_numbers}")