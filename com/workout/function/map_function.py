# string to numbers using map
number_as_string = ['1', '4', '5', '10', '7']
number = list((map(int, number_as_string)))
print(number)
print(type(number))
print(type(number[0]))
print('-' * 15)

# length of string using map
strings = ("apple", "banana", "mango")
words = list(map(lambda length_words: len(length_words), strings))
print(words)
print('-' * 15)

# lower to upper
strings = {'Vinothan', 'Jesus', 'kadavul'}
upper_words = list(map(lambda x: x.upper(), strings))
print(upper_words)
print('-' * 15)

items = [
    ("Product No 1 ", 10),
    ("Product No 2 ", 12),
    ("Product No 3 ", 4),
    ("Product No 4 ", 9)
]

formatted_item = list(map(lambda item: item[1] >= 10, items))
print(formatted_item)
