"""
Before implementation of LSP (Liskov Substitution Principle).

For the Car classes the get_cabin_width can not be used for RacingCar and therefore breaks the LSP.
For instances of type HomeMadeProduct we explicitly check the type to call another method, this is not good.
"""


class Car:
    def get_cabin_width(self):
        return 10


class RacingCar(Car):
    def get_cabin_width(self):
        raise NotImplementedError

    def get_cockpit_width(self):
        return 5


class Product:
    def __init__(self):
        self.discount = 10

    def get_discount(self):
        return self.discount


class HomeMadeProduct(Product):
    def apply_extra_discount(self):
        self.discount = self.discount * 2


if __name__ == '__main__':
    cars = [Car(), RacingCar()]
    for car in cars:
        try:
            print(car.get_cabin_width())
        except NotImplementedError:
            print('Error has occurred: NotImplementedError')

    products = [Product(), HomeMadeProduct()]
    for product in products:
        # Asking for permission is not good in OOP!
        if isinstance(product, HomeMadeProduct):
            product.apply_extra_discount()
        print(product.get_discount())
