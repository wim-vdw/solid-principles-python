"""
After implementation of LSP (Liskov Substitution Principle).

For the Car classes the "Break the hierarchy" pattern was applied by introducing a generic Vehicle class.
For the Product classes the "Tell, don't ask" pattern was applied, we no longer ask for permission explicitly
when using instances of Product classes.
"""


class Vehicle:
    def get_interior_width(self):
        pass


class Car(Vehicle):
    def get_interior_width(self):
        return self.get_cabin_width()

    def get_cabin_width(self):
        return 10


class RacingCar(Vehicle):
    def get_interior_width(self):
        return self.get_cockpit_width()

    def get_cockpit_width(self):
        return 5


class Product:
    def __init__(self):
        self.discount = 10

    def get_discount(self):
        return self.discount


class HomeMadeProduct(Product):
    def get_discount(self):
        self.apply_extra_discount()
        return self.discount

    def apply_extra_discount(self):
        self.discount = self.discount * 2


if __name__ == '__main__':
    cars = [Car(), RacingCar()]
    for car in cars:
        print(car.get_interior_width())

    products = [Product(), HomeMadeProduct()]
    for product in products:
        print(product.get_discount())
