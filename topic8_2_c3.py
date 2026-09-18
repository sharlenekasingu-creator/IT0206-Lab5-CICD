# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_2_c3.py

# Import both classes directly from the package
from school_package import Student, Teacher

# Create one Student with at least three grades
my_student = Student("Alice", [85, 92, 88])

# Print their average
print(f"{my_student.name}'s average grade is: {my_student.average_grade()}")