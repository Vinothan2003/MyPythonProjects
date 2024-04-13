word = input("Enter a word :").lower()
guess_chance = 3
guess_count = 0

while guess_count < guess_chance:
    guess_count = guess_count + 1
    print(f"Your word is {word}")
    word = input(f"Enter a magic word to 'quit' from the loop : ").lower()
    if word == "quit":
        print("You the guessed the magic word and escaped from the loop")
        break
else:
    print(f"you WASTED your chance")

"""while word != "quit":
    print(f"your word is {word} ")
    word = input("Enter a magic word to 'quit' from this loop : ").lower()
print(f"you escaped from the loop")"""
