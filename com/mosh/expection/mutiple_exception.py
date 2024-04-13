try:
    age = int(input("Enter your age :"))
    xfactor = 10 / age
    print(xfactor)
except (ValueError, ZeroDivisionError):  # --> multiple exception is handled  
    print("Invalid value")
# except ZeroDivisionError: --> ignored because exception is handled by before the except block
#     print("Invalid value")
