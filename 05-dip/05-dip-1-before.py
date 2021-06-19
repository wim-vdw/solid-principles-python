"""
Before implementation of DIP (Dependency Inversion Principle).

The Products class strongly depends on the low-level classes Database and CSV which is not good.
"""


class Products:
    def __init__(self):
        self._products = []

    def get_products_db(self):
        client = Database()
        self._products = client.select_products_from_db()

    def get_products_csv(self):
        client = CSV()
        self._products = client.select_products_from_csv()

    @property
    def products(self):
        return self._products


class Database:
    @staticmethod
    def select_products_from_db():
        """Mock data retrieval from a database."""
        return ['Laptop', 'Car']


class CSV:
    @staticmethod
    def select_products_from_csv():
        """Mock data retrieval from a CSV file."""
        return ['TV', 'Radio']


if __name__ == '__main__':
    products = Products()
    print(products.products)
    products.get_products_db()
    print(products.products)
    products.get_products_csv()
    print(products.products)
