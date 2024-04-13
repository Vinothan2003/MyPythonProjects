def prime(number):
    if number < 1 or number == 1:
        return f"{number} is not prime number"
    elif number == 2:
        return f"{number} is prime number"
    else:
        for i in range(2, number):
            if number % i == 0:
                return f"{number} is not a prime number"
            else:
                return f"{number} is a prime number"


number = int(input("> "))
result = prime(number)
print(result)
"""if number < 1:
    print(f"{number} is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(i, end=" ")
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is prime number")"""
