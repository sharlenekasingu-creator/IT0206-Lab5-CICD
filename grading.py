# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: grading.py

def letter_grade(score):
    """Returns the letter grade based on the numeric score.
    Raises a ValueError if the score is outside the 0-100 range."""
    
    # Check for invalid scores first
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    
    # Return the correct letter grade
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "F"