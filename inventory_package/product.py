# Name: Sharlene Kasingu
# Date: September 23, 2026
# Filename: product.py

class Product:
    """A class representing a product with a name, price, and quantity."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """Calculates and returns the total value of this product's stock."""
        return self.price * self.quantity