# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_3_c3.py

import sys
import os
# This tells Python to look in the parent folder to find 'shared_package'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the shared package
import shared_package

# Project C uses the password function
test_password = "short"
print(f"Project C: Is '{test_password}' a valid password? {shared_package.is_valid_password(test_password)}")