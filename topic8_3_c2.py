# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_3_c2.py

# Import the utilities module
import utilities

# Define the text we want to slugify
original_text = "Advanced Python Topics"

# Call the function and print the result
slug = utilities.slugify(original_text)

print(f"Original text: {original_text}")
print(f"Slugified text: {slug}")