# slicing --> creating a substring by extracting elements from another string
#               index []            or  slice()
#               [start:stop:step]       (start,stop,step)

word = "my name is vinothan"
sl = "http://flipkart.com"

first = word[4:]
second = word[:10]
third = word[::2]
reversed_string = word[::-1]

print(first)
print(second)
print(third)
print(reversed_string)

website1 = "http://youtube.com"
website2 = "http://amazone.com"

slicing = slice(7, -4, 2)

print(website1[slicing])
print(website2[slicing])
