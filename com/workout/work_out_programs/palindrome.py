word = input("> ")  # solved
reverse = reversed(word)  # or word[::-1]
# print(reverse)  # it will print the reversed object
reversed_word = ""
for i in reverse:
    reversed_word += i
if reversed_word == word:
    print(f"it is a palindrome {word} : {reversed_word}")
else:
    print(f"it is a not palindrome {word} : {reversed_word}")

""" 
reversed_word = ''.join(reversed(word)) # solved
if reversed_word == word:
    print(f"it is a palindrome {word} : {reversed_word}")
else:
    print(f"it is a not palindrome {word} : {reversed_word}") """
