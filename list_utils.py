# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: list_utils.py

def find_max(numbers):
    """Returns the largest value in a list of numbers without using the built-in max() function."""
    
    # Start by assuming the first number is the largest
    max_value = numbers[0]
    
    # Loop through the list to find the actual largest number
    for num in numbers:
        if num > max_value:
            max_value = num
            
    return max_value