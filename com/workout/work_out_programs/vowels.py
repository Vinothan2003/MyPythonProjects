word = input("Enter a word : ").lower()  # solved
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in word:
    if i in vowels:
        count += 1
print(f"Vowels count in the string : {count}")

another_word = input("Enter a string : ").lower()
vowels_2 = "aeiou"

count = [1 for i in another_word if i in vowels_2]
print(f"vowels count in the string : {sum(count)}")
