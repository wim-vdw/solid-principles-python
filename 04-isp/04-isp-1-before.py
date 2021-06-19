"""
Before implementation of ISP (Interface Segregation Principle).

The interface MultiFunction is too fat and has low cohesion (printing has nothing to do with scanning).
The concrete StandardPrinter implementation also has and empty 'scan' method.
"""


class MultiFunction:
    def print(self):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError


class StandardPrinter(MultiFunction):
    def print(self):
        print('Printing...')

    def scan(self):
        """Empty method implementation."""
        pass


class MultiPurposePrinter(MultiFunction):
    def print(self):
        print('Printing...')

    def scan(self):
        print('Scanning...')
