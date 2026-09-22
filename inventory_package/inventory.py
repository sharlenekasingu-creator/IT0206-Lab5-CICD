# Name: Sharlene Kasingu
# Date: September 23, 2026
# Filename: inventory.py

class Inventory:
    """A class that stores a list of Product objects and manages the inventory."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Adds a Product object to the inventory list."""
        self.products.append(product)

    def total_inventory_value(self):
        """Calculates and returns the combined total value of all products."""
        return sum(p.total_value() for p in self.products)

    def low_stock_products(self, threshold):
        """Returns a list of products where the quantity is below the threshold."""
        return [p for p in self.products if p.quantity < threshold]