# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: topic8_1_c3.py

# Import the custom module
import string_utils

# Read a sentence from the user
user_sentence = input("Enter a sentence: ")

# Get the shouted version and the word count
shouted_text = string_utils.shout(user_sentence)
count = string_utils.word_count(user_sentence)

# Print the results
print("Shouted:", shouted_text)
print("Word Count:", count)