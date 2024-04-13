para = input("> ")
words = para.split(" ")
dictionary = {
    ":)": "😀",
    ":(": "🥲",
    ":3": "😺"
}
output = ""
for word in words:
    output += dictionary.get(word, word) + " "
print(output)