import random
import string

print(random.random())  # print value between [0, 1]
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8], k=2))

print("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=7)))

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print("Password : ", ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10)))

number = [1, 2, 3, 4, 5]
another = number
random.shuffle(number)

print(number)
print(another)
