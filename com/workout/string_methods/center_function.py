string_word = input("Enter a string :")
string_width = int(input("Enter a string width: "))
string_symbol = input("Enter a symbol :")

string_center = string_word.center(string_width, string_symbol)  # string.center(value, character)

print(string_center)
