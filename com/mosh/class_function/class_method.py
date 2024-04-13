class Car:

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    @classmethod
    def low_end_model(cls):
        print("Low End Model")
        return cls(name="BMW", model=2018, price=2000000)

    @classmethod
    def high_end_model(cls):
        print("High End Model")
        return cls(name="BMW", model=2024, price=70000000)

    def details(self):
        print(f"Car details\nName : {self.name}, Model : {self.model}, Price : {self.price:,}")


bmw = Car.low_end_model()
bmw.details()

bmw_2 = Car.high_end_model()
bmw_2.details()
