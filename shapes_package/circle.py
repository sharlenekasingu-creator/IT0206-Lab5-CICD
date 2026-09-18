# circle.py
# Defines the Circle class used to model circular shapes.

import math

class Circle:
    """Represents a circle defined by its radius."""

    def __init__(self, radius):
        self.radius = radius  # Store the radius of the circle

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius