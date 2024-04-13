# if statement --> it will execute if the statement is ture

age = int(input("enter your age :"))

if age == 100:
    print("what the fuck!!!!!!!!!")
elif age >= 50:
    print("old people are not allowed!x")
elif age >= 18:
    print("your welcome to the club!!!" + str(age))
else:
    print("your are under age!!!")
