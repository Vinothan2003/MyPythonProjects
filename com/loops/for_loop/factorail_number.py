number = int(input("Enter a number :"))
fact = 1

if number < 0:
    print(f"factorial cannot be done for negatives numbers : {number}")

elif number == 0:
    print(f"factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        fact = fact * i
    print(f"the factorial of {number} is : {fact}")