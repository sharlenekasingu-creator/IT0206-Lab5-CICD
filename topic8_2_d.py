# Topic8_2_d.py
# Demonstrates importing classes from a custom package named shapes_package

from shapes_package import Circle, Rectangle

circle = Circle(4)
print("Circle area:", round(circle.area(), 2))
print("Circle circumference:", round(circle.circumference(), 2))

rectangle = Rectangle(5, 3)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())