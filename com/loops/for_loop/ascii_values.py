print("ASCII value for lower case letters")
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), "-", char)

print("ASCII value for upper case letters")
for char in range(ord('A'), ord('Z') + 1):
    print(chr(char), "-", char)
