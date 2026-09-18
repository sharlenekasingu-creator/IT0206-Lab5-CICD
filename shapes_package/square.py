# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: square.py

class Square:
    """A class representing a square with a single side attribute."""

    def __init__(self, side):
        self.side = side

    def area(self):
        """Calculates and returns the area of the square."""
        return self.side ** 2

# Discussion: Why not inherit from Rectangle?
# Even though a square is mathematically a special case of a rectangle, 
# inheriting from a Rectangle class causes design issues (specifically violating 
# the Liskov Substitution Principle). A Rectangle has two independent dimensions 
# (width and height). If Square inherited from it, we would either have to force 
# the user to pass the same number twice (which is redundant), or we would have 
# to override the width/height methods so that changing one automatically changes 
# the other. This breaks the expected behavior of a Rectangle and makes the code 
# prone to bugs. Keeping Square separate with a single 'side' attribute is cleaner, 
# safer, and strictly enforces the rule that all sides must be equal.