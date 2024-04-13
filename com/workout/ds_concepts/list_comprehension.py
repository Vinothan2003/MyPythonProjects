number = int(input("> "))
target_num = 3
star = [ [x, y] for x in range(1, number + 1) for y in range(1, x + 1) if x + y != 3]
print(star)