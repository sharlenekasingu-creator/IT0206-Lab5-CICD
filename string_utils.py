# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: string_utils.py

def shout(text):
    """Returns the given text converted to uppercase, followed by an exclamation mark."""
    return text.upper() + "!"

def word_count(text):
    """Returns the number of whitespace-separated words in a string."""
    # split() with no arguments splits on any whitespace and returns a list of words
    return len(text.split())