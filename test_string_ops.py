# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: test_string_ops.py

# Import the module we want to test
import string_ops

def test_palindrome():
    """Test that a known palindrome returns True."""
    assert string_ops.is_palindrome("Racecar") == True

def test_non_palindrome():
    """Test that a non-palindrome returns False."""
    assert string_ops.is_palindrome("Hello") == False