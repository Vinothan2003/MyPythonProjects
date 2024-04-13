number = input("> ")
output = ""
num = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
for i in number:
    output += num.get(i, "NOT AVAILABLE") + " "
print(output)
