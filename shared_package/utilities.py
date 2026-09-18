# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: utilities.py

def is_valid_password(password):
    """Returns True if the password is at least 8 characters long, otherwise False."""
    return len(password) >= 8

def slugify(text):
    """Converts a string into a lowercase, hyphen-separated slug."""
    return text.lower().replace(" ", "-")