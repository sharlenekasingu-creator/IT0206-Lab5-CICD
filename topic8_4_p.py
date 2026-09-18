# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: Topic8_4_p.py

# Import the custom module
import validators

# Test a typical valid age
try:
    print(f"Is 25 a valid age? {validators.validate_age(25)}")
except ValueError as e:
    print(f"Error: {e}")

# Test the boundary value (120)
try:
    print(f"Is 120 a valid age? {validators.validate_age(120)}")
except ValueError as e:
    print(f"Error: {e}")

# Test an invalid age (150)
try:
    print(f"Is 150 a valid age? {validators.validate_age(150)}")
except ValueError as e:
    print(f"Caught expected error for 150: {e}")