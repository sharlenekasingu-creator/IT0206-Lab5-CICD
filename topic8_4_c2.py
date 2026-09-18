# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: Topic8_4_c2.py

# Import the custom module
import grading

# Test a few different scores to see them in action
test_scores = [85, 65, 45, 30]

for score in test_scores:
    grade = grading.letter_grade(score)
    print(f"A score of {score} gets a letter grade of: {grade}")