# Topic8_1_d.py
# Demonstrates importing and using a custom module named math_utils

import math_utils  # Import the entire module

# Call functions defined inside the math_utils module
result_sum = math_utils.add(10, 5)
result_diff = math_utils.subtract(10, 5)
result_even = math_utils.is_even(10)

print("Sum:", result_sum)
print("Difference:", result_diff)
print("Is 10 even?", result_even)