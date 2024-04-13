word = "hello world"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in word:
    if i in vowels:
        count = count + 1
        print(f"vowels are {i}")
print(f"vowels count : {count}")

