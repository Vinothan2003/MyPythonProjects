hello = "H\te\tl\tl\to"  # \t --> by default 8 spaces is set
tab = int(input("Enter a tab value: "))

print(hello)
print(hello.expandtabs(tabsize=tab))
