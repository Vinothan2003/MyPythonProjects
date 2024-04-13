class Calculator:
    def __init__(self, a, b):
        self.var_a = a
        self.var_b = b

    def addition(self):
        adding = self.var_a + self.var_b
        print(f"Addition of a and b : {adding}")

    def subtraction(self):
        subtracting = self.var_a - self.var_b
        print(f"Subtracting of a and b : {subtracting}")

    def multiple(self):
        multiplication = self.var_a * self.var_b
        print(f"Multiplication of a and b : {multiplication}")


add = Calculator(a=10, b=20)
add.addition()

sub = Calculator(a=10, b=5)
sub.subtraction()

mul = Calculator(a=10, b=10)
mul.multiple()