words = ['a', 'a', 'b', 'c', 'd']
# unordered, unchangeable, and not allow duplicate items
first_words = set(words)  # casting
print(first_words)

second_words = {'e', 'f', 'g', 'h', 'b', 'c'}

print(first_words | second_words)  # union --> add the two sets
print(first_words & second_words)  # intersection --> print the items that exists in both sets
print(first_words - second_words)  # difference --> difference between the both sets
print(first_words ^ second_words)  # symmetric difference --> the items that does not exists in both sets
