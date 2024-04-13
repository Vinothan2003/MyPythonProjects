number = int(input("Enter a number : "))
factorial = 1
for fact in range(1, number + 1):
    factorial = factorial * fact
    print(fact,end=" ")
print()
print(f"The factorial of the number {number} is {factorial}")
