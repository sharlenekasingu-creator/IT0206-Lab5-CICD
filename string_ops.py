# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: string_ops.py

def is_palindrome(text):
    """Returns True if a string reads the same forwards and backwards, ignoring case."""
    # Convert to lowercase to ignore case, then compare with its reverse
    text = text.lower()
    return text == text[::-1]