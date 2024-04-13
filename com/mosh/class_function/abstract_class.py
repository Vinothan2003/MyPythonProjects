# Abstraction --> showing only essential parts and hiding the implementation details

# Abstract Class --> which have abstract methods
# Abstract Method --> Methods are declared but not the definition
# Concrete Class --> class without abstract methods


# Abstract class -------> Concrete class(inherit abstract class)
#             * all methods should be overrides in concrete class otherwise that concrete class also become abstract class


from abc import ABC, abstractmethod  # abc, ABC --> Abstract Base Class


class InvalidOperationError(Exception):  # Custom error handling
    pass


class Stream(ABC):  # Abstract class --> cannot create instance or object for abstract class
    def __init__(self):
        self.flag = False

    def open(self):
        if self.flag:
            raise InvalidOperationError("Stream is already opened.")
        self.flag = True

    def close(self):
        if not self.flag:
            raise InvalidOperationError("Stream is already closed.")
        self.flag = False

    @abstractmethod  # Abstract method --> this method should be in which the class (Derived) inherit the stream abstract class
    def read(self):  # method is declared but not the definition
        pass

    @abstractmethod
    def show(self):  # method is declared but not the definition
        pass


class FileStream(Stream):  # Concrete class --> without abstract method
    def show(self):  # all the method in abstract class is overrides in the concrete class (derived class)
        print('File stream is showed..')

    def read(self):
        print("File stream is reading..")


class NetworkStream(Stream):  # Concrete class --> without abstract method

    def show(self):
        print("Network Stream is showed..")

    def read(self):
        print("Network stream is reading..")


file = FileStream()
file.open()
file.read()
file.show()
file.close()

network = NetworkStream()
network.open()
network.read()
network.show()
network.close()
