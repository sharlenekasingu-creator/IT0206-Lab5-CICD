# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: Topic8_3_p.py

# Import the custom module
import text_utils

# Define a long text and a short max_length
long_text = "This is a very long sentence that definitely needs to be truncated."
limit_1 = 25

# Call the function and print the result
result_1 = text_utils.truncate(long_text, limit_1)
print(f"Script 1 (Limit: {limit_1}) -> {result_1}")