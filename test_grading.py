# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: test_grading.py

# Import the module we want to test
import pytest
import grading

def test_boundary_39_40():
    """Test the exact boundary between F and C."""
    assert grading.letter_grade(39) == "F"
    assert grading.letter_grade(40) == "C"

def test_boundary_59_60():
    """Test the exact boundary between C and B."""
    assert grading.letter_grade(59) == "C"
    assert grading.letter_grade(60) == "B"

def test_boundary_79_80():
    """Test the exact boundary between B and A."""
    assert grading.letter_grade(79) == "B"
    assert grading.letter_grade(80) == "A"

def test_invalid_score_150():
    """Test that a score of 150 raises a ValueError."""
    with pytest.raises(ValueError):
        grading.letter_grade(150)

def test_invalid_score_negative():
    """Test that a negative score also raises a ValueError."""
    with pytest.raises(ValueError):
        grading.letter_grade(-10)