# string.isnumeric() --> it will return if string is numeric
#                    --> it will not take -1 and . decimal values as numeric value
number_string = input("> ")
if number_string.isnumeric():
    print(f"The number is numeric : {number_string}")
else:
    print(f" it is {number_string} not a numeric")
