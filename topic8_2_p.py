# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_2_p.py

# Import both classes directly from the package
from vehicle_package import Car, Motorcycle

# Create one Car and one Motorcycle
my_car = Car("Toyota", "Camry")
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster")

# Print their descriptions
print(my_car.describe())
print(my_motorcycle.describe())