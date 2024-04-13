class Laptop:
    def __init__(self, name, processor, gen):  # self = # lenovo # asus # red_magic
        self.name = name
        self.processor = processor
        self.gen = gen
        print("constructor is called by default")

    def about(self):
        print(f"{self.name} laptop")  # self.name = lenovo.name
        print(f"Processor : {self.processor}")  # self.processor = lenovo.processor
        print(f"Gen : {self.gen}")  # self.gen = lenovo.gen
        print("_________________")

    """def display(self):
        print(f"Welcome to {self.name} Laptop screen")"""


lenovo = Laptop("Lenovo", processor="Intel i5", gen="8th GEN")  # keyword argument is used
lenovo.about()
# lenovo.display()

asus = Laptop("Asus", "Intel i10", "10th gen")  # positional argument is used
asus.about()

red_magic = Laptop("Red Magic", "ADM", "11th gen")
red_magic.about()
