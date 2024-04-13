"""from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def rent(self, days):
        pass


class Car(Vehicle):
    def rent(self, days):
        return 1000 * days


class Motorcycle(Vehicle):
    def rent(self, days):
        return 300 * days


class Van(Vehicle):
    def rent(self, days):
        return 2000 * days


def total_cost(vehicle, total_days):
    print(vehicle.rent(total_days))


car = Car()
van = Van()
total_cost(car, 3)
total_cost(van, 3)
"""