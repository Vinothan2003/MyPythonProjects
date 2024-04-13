number = int(input("Enter a number : "))
increment = 1
while increment <= number:
    if (increment % 2) == 0:
        print(f"Even number : {increment}")
    else:
        print(f"Odd number : {increment}")
    increment += 1
