try:
    # file = open("finally_statement.py") --> opening file
    age = int(input("> "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print("invalid value ")
    print(type(error))
finally:
    """ file.close() --> closing the file after the execution of program """
