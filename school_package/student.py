# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: student.py

class Student:
    """A class representing a student with a name and a list of grades."""

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        """Calculates and returns the average of the student's grades."""
        # Using the hint: sum(grades) / len(grades)
        return sum(self.grades) / len(self.grades)