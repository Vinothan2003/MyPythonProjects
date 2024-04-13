number = [10,20,2,2,10,30,40]
non_repeated = []

for num in number:
    if num not in non_repeated:
        non_repeated.append(num)

non_repeated.sort()
non_repeated.pop()
print(non_repeated)