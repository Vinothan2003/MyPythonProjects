word = "hello my name is vinothan"
list_word = list(word.split())
cap_word = ""
for i in list_word:
    cap_word = cap_word + i.capitalize() + " "
print(cap_word)

