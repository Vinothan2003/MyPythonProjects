word = input("Enter a word: ").lower()
guess_chance = 3
guess_count = 0

while guess_count < guess_chance:
    guess_count += 1
    print(f"Your word is {word}")
    word = input("Enter a magic word to 'quit' from this loop: ").lower()
    if word == "quit":
        print("You guessed the magic word and escaped from the loop.")
        break
else:
    print("You wasted all your chances.")