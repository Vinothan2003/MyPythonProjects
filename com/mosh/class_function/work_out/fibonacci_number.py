class Fibonacci:  # not understood
    def __init__(self, number):
        self.number = number
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration


user_input = int(input("Enter a number : "))
fib = Fibonacci(user_input)
for num in fib:
    print(num, end=" ")
