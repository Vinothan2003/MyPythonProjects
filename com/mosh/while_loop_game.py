secret_number = 4
guess_count = 0
guess_chance = 3
while guess_count < guess_chance:  # while loop also have else
    guess = int(input("Guess the correct number :"))
    guess_count += 1
    if guess == secret_number:
        print(f"you guessed the 'correct number'")
        break
else:
    print(f"'Better Luck' next time!!")

