# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: validators.py

def validate_age(age):
    """Returns True for any age between 0 and 120 inclusive.
    Raises a ValueError for any value outside that range."""
    
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120 inclusive.")
        
    return True