# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: contact.py

class Contact:
    """A class to store a person's name and phone number."""

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Contact: {self.name} | Phone: {self.phone_number}"