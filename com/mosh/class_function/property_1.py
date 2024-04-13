class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def product_price(self, value):
        print(f"{self.__price} is changed to {value}")
        self.__price = value

    @product_price.deleter
    def product_price(self):
        del self.__price


product = Product(100)
print(product.product_price)

product.product_price = 20000
print(product.product_price)

del product.product_price
print(product.product_price)
