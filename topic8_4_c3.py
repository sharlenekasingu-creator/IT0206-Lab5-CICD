# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: Topic8_4_c3.py

# Import the custom module
import grading

# Test valid scores
print(f"A score of 85 is a: {grading.letter_grade(85)}")
print(f"A score of 40 is a: {grading.letter_grade(40)}")

# Test an invalid score using a try/except block so the script doesn't crash
try:
    print(f"A score of 150 is a: {grading.letter_grade(150)}")
except ValueError as e:
    print(f"Caught an expected error for 150: {e}")