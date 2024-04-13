sentence = "This a common interview question"
print(sentence.find("common"))

char_repetition = dict()

for char in sentence:
    if char in char_repetition:
        char_repetition[char] = char_repetition[char] + 1
    else:
        char_repetition[char] = 1


def sort(value):
    return value[1]


char_sort = sorted(char_repetition.items(), key=sort, reverse=True)
print(char_sort)
