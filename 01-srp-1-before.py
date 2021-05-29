"""
Before implementation of SRP (Single Responsibility Principle).

Low cohesion between the different methods of the Person class, getting and setting property data
has nothing to do with printing or saving the data.
Tight coupling in the print and save methods, in case we would like to print to a different format or
would like to save the data to a database the complete methods need to be rewritten.
"""


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return self.get_last_name() + ', ' + self.get_first_name()

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def print(self):
        print(f'Full name: {self.get_full_name()}')

    def save(self):
        with open('data.txt', 'w') as writer:
            writer.write(self.get_full_name())
