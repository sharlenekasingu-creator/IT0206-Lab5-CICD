# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_2_c1.py

# Import Contact directly from the package
from contact_package import Contact

# Create two Contact objects
person1 = Contact("Sharlene Kasingu", "081-234-5678")
person2 = Contact("John Doe", "072-987-6543")

# Print them (this automatically calls the __str__ method)
print(person1)
print(person2)