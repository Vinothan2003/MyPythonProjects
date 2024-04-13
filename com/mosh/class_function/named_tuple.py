from collections import namedtuple
# namedtuple --> used when
# its immutable they cannot change or assing value

tuple_color = (225, 225, 225)  # tuple

dic_color = {'red': 225, 'green': 225, 'blue': 225}  # dictionary

Color = namedtuple("Color", ['red', 'green', 'blue'])
color = Color(red=225, green=225, blue=225)
print(color.red)
# color.red = 0 can set value because namedtuple are immutable

print(tuple_color[0])
