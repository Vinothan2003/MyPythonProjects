def addition(numbers):
    int_number = [float(i) for i in numbers]
    return sum(int_number)


def subtraction(numbers):
    int_number = [float(i) for i in numbers]
    subtraction_number = int_number[0]
    for j in int_number[1:]:
        subtraction_number -= j
    return subtraction_number


def multiple(numbers):
    int_number = [float(i) for i in numbers]
    multiplication_numbers = 1
    for i in int_number:
        multiplication_numbers *= i
    return multiplication_numbers


def division(numbers):
    int_numbers = [float(i) for i in numbers]
    division_number = int_numbers[0]
    for i in int_numbers[1:]:
        try:
            division_number = division_number / i
        except ZeroDivisionError:
            print("Cannot divided by zero!!")
            return "Enter a proper value!!"

        return division_number


print("""
1.Addition
2.subtraction
3.Multiplication
4.Division
""")

while True:

    user_input = input("Enter any one 1 | 2 | 3 | 4 | quit : ")

    if user_input == "1":
        add_number = input("enter the numbers to add :").split()
        add_result = addition(add_number)
        print(f"Addition of numbers : {add_result}")
        print(f"If Want to Exit type --> 'quit' ")
        print()

    elif user_input == "2":
        sub_number = input("Enter the numbers to subtract :").split()
        sub_result = subtraction(sub_number)
        print(f"Subtraction of numbers : {sub_result}")
        print(f"If Want to Exit type --> 'quit' ")
        print()

    elif user_input == "3":
        mult_number = input("Enter the numbers to multiple :").split()
        mult_result = multiple(mult_number)
        print(f"Multiplication of numbers : {mult_result} ")
        print(f"If Want to Exit type --> 'quit' ")
        print()

    elif user_input == "4":
        div_number = input("Enter the numbers to divide :").split()
        div_result = division(div_number)
        print(f"Division of numbers : {div_result}")
        print(f"If Want to Exit type --> 'quit' ")
        print()

    elif user_input.lower().strip() == "quit":
        print("Bye :)")
        break
    else:
        print("Invalid")
