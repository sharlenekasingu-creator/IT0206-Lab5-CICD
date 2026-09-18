# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_3_c1.py

# Import the utilities module
import utilities

# Test with a password that is too short
short_password = "apple"
print(f"Is '{short_password}' valid? {utilities.is_valid_password(short_password)}")

# Test with a password that meets the length requirement
long_password = "securepassword123"
print(f"Is '{long_password}' valid? {utilities.is_valid_password(long_password)}")