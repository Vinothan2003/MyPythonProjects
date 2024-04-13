# format {value : flags}
price1 = 10000.78234
price2 = -9000.2341
price3 = 5000

print(f"decimal:{price1: .2f}")  # it will print the two decimal point numbers
print(f"decimal:{price2: .2f}")
print(f"decimal:{price3: .2f}")

print(f"left assign:{price3:<10}")  # left assign < --> it will assign the value to left
print(f"right assign:{price3:>10}")  # right assign > --> it will assign the value to right
print(f"center assign:{price3:^10}")  # center assign ^ --> it will assign the value to center

print(f"thousand comma separate :{price1:,.2f}")  # a thousand comma , --> it will separate the value

