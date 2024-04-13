def fizzbuzz(number):
    if (number % 3) == 0 and (number % 5) == 0:
        return "FizzBuzz"
    elif (number % 3) == 0:
        return "Buzz"
    elif (number % 5) == 0:
        return "Fizz"
    else:
        return f"{number}"


print(fizzbuzz(17))
