"""
Before implementation of OCP (Open Closed Principle).

The Animal class can not be extended without modifying the make_sound method.
For every animal we would like to add to the class we need to modify the class.
So the class could not be extended without modifying it, which is not good.
"""


class Animal:
    def __init__(self, animal):
        self._animal = animal

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        self._animal = animal

    def make_sound(self):
        if self._animal == 'cat':
            return 'meow'
        elif self._animal == 'dog':
            return 'woof'


if __name__ == '__main__':
    animals = [Animal('cat'), Animal('dog')]
    for animal in animals:
        print(animal.animal, '->', animal.make_sound())
