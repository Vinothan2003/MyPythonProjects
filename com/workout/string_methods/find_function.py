# find(value, start, stop) --> it will find the character in the string
#                          --> it will return -1 if character does not present in string
#                              it will not rise exception
word = input("Enter a string:")
while True:
    find_word = input("Enter a specific word to find in the string: ")
    if find_word in word:
        print(f"{find_word} : {word.find(find_word)}")
        break
    else:
        print("The character is not presented in the string")
