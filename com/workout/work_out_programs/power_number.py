number_range = int(input("Enter a Number range : "))
"""for i in range(1, number_range + 1): # solved
    print(f" {i} : {pow(i, 2)}")"""

# pow_number = [pow(x, 2) for x in range(1, number_range + 1)] # solved

pow_number = list(map(lambda x: pow(x, 2), range(1, number_range + 1)))  # this part is not solved

print(pow_number)

for i in range(0, len(pow_number)):
    print(f"2 power {i} : {pow_number[i]}")
