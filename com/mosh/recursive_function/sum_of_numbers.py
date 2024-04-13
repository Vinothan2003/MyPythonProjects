def sum_number(number_sum):
    if number_sum == 0:  # or number_sum == 1:  # base case -- > this will terminate the recursion
        return 0
    else:
        return number_sum + sum_number(number_sum - 1)  # recursion case -- > here the function call by itself


number = int(input("Enter a  number : "))

sum_of_numbers = sum_number(number)
print(f"the sum of the number {number} : {sum_of_numbers}")
