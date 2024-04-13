vowels = "aeiou"
text = "Hello, how are you?"
count = 0

for char in text:
    if char.lower() in vowels:
        count = count + 1
print(f"Vowel count in the string : {count}")

# for vowels in text: **WRONG**
#    count = count + vowels
# print(count)
