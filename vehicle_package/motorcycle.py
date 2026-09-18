# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: motorcycle.py

class Motorcycle:
    """A class representing a Motorcycle with a make and model."""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        """Returns a formatted string describing the motorcycle."""
        return f"Motorcycle: {self.make} {self.model}"