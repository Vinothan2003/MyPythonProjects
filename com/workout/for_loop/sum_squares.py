number = int(input("Enter a number : "))    # FAILED
sum_numbers = 0
for sqr in range(1, number + 1):
    square = sqr ** 2
    sum_numbers = sum_numbers + square
print(f"The sum of square of numbers : {sum_numbers}")
