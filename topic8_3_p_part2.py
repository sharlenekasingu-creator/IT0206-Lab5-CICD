# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: Topic8_3_p_part2.py

# Import the same custom module
import text_utils

# Define a short text and a larger max_length
short_text = "Hello World!"
limit_2 = 50

# Call the function and print the result
result_2 = text_utils.truncate(short_text, limit_2)
print(f"Script 2 (Limit: {limit_2}) -> {result_2}")