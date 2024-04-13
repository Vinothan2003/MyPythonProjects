x = 10  # swapping the numbers using temp variable
y = 15

temp = x
x = y
y = temp

print("x", x)
print("y", y)
print("-" * 15)

a = 20  # Here swapping the number with tuple,list etc.
b = 30
a, b = b, a  # unpacking is done here

print("a", a)
print("b", b)
