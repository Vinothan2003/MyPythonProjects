secret_number = 5
guess_count = 0
guess_chance = 3
user_input = 0
while True:
    user_input = int(input("Guess the number : "))
    guess_count += 1
    if user_input == secret_number:
        print("You won")
        break
    elif guess_count > guess_chance:
        print("Used all your chance!")
        break
    else:
        print("Wrong guess the number")

