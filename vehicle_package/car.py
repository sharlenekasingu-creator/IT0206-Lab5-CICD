# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: car.py

class Car:
    """A class representing a Car with a make and model."""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        """Returns a formatted string describing the car."""
        return f"Car: {self.make} {self.model}"