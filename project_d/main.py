# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: main.py

import sys
import os
# This tells Python to look in the parent folder to find 'shared_package'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import just the slugify function directly from the shared package
from shared_package import slugify

# Project D uses the slugify function
blog_title = "My First Python Project"
print(f"Project D: The slug for '{blog_title}' is: {slugify(blog_title)}")