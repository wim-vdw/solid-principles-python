"""
After implementation of DIP (Dependency Inversion Principle).

The dependency (Database or CSV) is now injected in the Products class via a repository of type Database or CSV.
A factory is used to create a Database or CSV repository.
"""


class ProductRepository:
    @staticmethod
    def select_products():
        raise NotImplementedError


class DatabaseProductRepository(ProductRepository):
    @staticmethod
    def select_products():
        """Mock data retrieval from a database."""
        return ['Laptop', 'Car']


class CSVProductRepository(ProductRepository):
    @staticmethod
    def select_products():
        """Mock data retrieval from a CSV file."""
        return ['TV', 'Radio']


class ProductFactory:
    @staticmethod
    def create(repo_type):
        if repo_type == 'DB':
            return DatabaseProductRepository()
        else:
            return CSVProductRepository()


class Products:
    def __init__(self, repo: ProductRepository):
        self._products = []
        self.repo = repo

    def get_products(self):
        self._products = self.repo.select_products()

    @property
    def products(self):
        return self._products


if __name__ == '__main__':
    product_repo = ProductFactory.create('DB')
    products = Products(product_repo)
    products.get_products()
    print(products.products)
    product_repo = ProductFactory.create('CSV')
    products = Products(product_repo)
    products.get_products()
    print(products.products)
