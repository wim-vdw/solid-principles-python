"""
After implementation of OCP (Open Closed Principle).

The animal class can now be extended just by subclassing it and without modifying it directly.
The animal class is now closed for modification but open for extension.
"""


class Animal:
    def __init__(self, animal):
        self._animal = animal

    @property
    def animal(self):
        return self._animal

    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__('cat')

    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def __init__(self):
        super().__init__('dog')

    def make_sound(self):
        return 'woof'


class Lion(Animal):
    def __init__(self):
        super().__init__('lion')

    def make_sound(self):
        return 'roar'


if __name__ == '__main__':
    animals = [Cat(), Dog(), Lion()]
    for animal in animals:
        print(animal.animal, '->', animal.make_sound())
