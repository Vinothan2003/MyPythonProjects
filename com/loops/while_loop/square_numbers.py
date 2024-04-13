import math

number = 1
count = 1

while count <= 5:
    square_number = math.pow(number, 2)
    print(round(square_number))
    count += 1
    number += 1 