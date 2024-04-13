# logical operator AND OR NOT -->it will execute two or more conditional statement is true

temp = int(input("enter the temperature :"))

if not (temp >= 20 and temp <= 40):
    print("it is a nice warm day")
    print("go outside")

elif not (temp < 0 or temp < 20):
    print("it is cold outside !!!")

elif temp >= 50:
    print("it is hotter oustide")
    print("stay home!!!")
