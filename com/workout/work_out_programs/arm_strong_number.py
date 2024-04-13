number = int(input("Enter a number : "))

number_list_string = [i for i in str(number)]

number_list_int = [int(j) for j in number_list_string]  # list(map(int, number_list_string))

"""pow_number = 0

for num in number_list_int:
    pow_number += pow(num, number_list_int[-1])"""

pow_number = sum([pow(num, number_list_int[-1]) for num in number_list_int])

if pow_number == number:
    print(f"it is a Armstrong number {number} : {pow_number} ")
else:
    print(f"it is not a Armstrong number : {number} ")
