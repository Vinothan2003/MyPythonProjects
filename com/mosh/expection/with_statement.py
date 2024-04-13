# with statement --> using this it will close file automatically no need to close manually using "finally"
#                --> we can open multiple file

try:
    with (open("with_statement.py") as file,  # file and file_finally --> are return 
          open("finally_statement.py") as file_finally):  # it will automatically close the file
        print("filed is opened!")
    age = int(input("> "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("invalid value ")
