# rectangle.py
# Defines the Rectangle class used to model rectangular shapes.

class Rectangle:
    """Represents a rectangle defined by width and height."""

    def __init__(self, width, height):
        self.width = width    # Store the width of the rectangle
        self.height = height  # Store the height of the rectangle

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)