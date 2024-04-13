try:
    age = int(input("AGE : "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print(f"Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")