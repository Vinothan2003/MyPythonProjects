"""number = int(input("Guess the number :"))
correct_num = 6

while not number == correct_num:
    print("Guess the correct number")
    number = int(input("Guess the number properly!!! :"))
print(f"You guessed the correct number {number}")"""

secret_number = 7
chance = 0
chance_limit = 3

while chance < chance_limit:
    guessed_num = int(input("Guess the number:"))
    chance = chance + 1
    if secret_number == guessed_num:
        print(f"You Guessed the correct number!!!")
        break
else:
    print("You WASTED your chance")




"""number = int(input("Guess the number :"))
correct_num = 10
chance = 0

while chance < 3:
    if not number == correct_num:
        print("Guess the correct number")
        number = int(input("Guess the number properly! :"))
        chance = chance + 1
    else:
         print("You WASTED your chance")
print(f"You guessed the correct number {number}")"""
