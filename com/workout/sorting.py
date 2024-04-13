items = [10, 2, 4, 6, 1, 3, 5]
items.sort()  # --> this will sort the original list
# print(items)

# print(sorted(items, reverse=True))  # this will make the copy of list and sort them ,original remains the same
print(items)

sentence = "This a string".lower()
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0
for letter in sentence:
    if letter in vowels:
        vowels_count = vowels_count + 1
print(f"vowels count : {vowels_count}")

