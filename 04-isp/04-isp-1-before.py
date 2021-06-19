"""
Before implementation of ISP (Interface Segregation Principle).

ISP violations:
  - The interface MultiFunction is too fat.
  - Low cohesion between methods (printing has nothing to do with scanning).
  - The concrete class StandardPrinter also contains an empty method implementation (scan).
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
