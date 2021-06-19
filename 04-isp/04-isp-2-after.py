"""
After implementation of ISP (Interface Segregation Principle).

Use multiple smaller interfaces.
"""


class Print:
    def print(self):
        raise NotImplementedError


class Scan:
    def scan(self):
        raise NotImplementedError


class StandardPrinter(Print):
    def print(self):
        print('Printing...')


class MultiPurposePrinter(Print, Scan):
    def print(self):
        print('Printing...')

    def scan(self):
        print('Scanning...')
