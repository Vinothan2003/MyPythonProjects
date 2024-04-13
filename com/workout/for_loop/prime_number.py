number = int(input("Enter a number : "))
for i in range(1, number + 1):
    if (i % 1) == 0 and (i % i) == 0:
        print(f"{i} is prime number")
    else:
        print(f"{i} is not prime number")  # FAILED
