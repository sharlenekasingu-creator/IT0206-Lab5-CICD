# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: text_utils.py

def truncate(text, max_length):
    """Returns the text unchanged if it is at or under max_length characters, 
    or the first max_length characters followed by '...' if it is longer."""
    
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length] + "..."