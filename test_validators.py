# Name: Sharlene Kasingu
# Date: September 18, 2026
# Filename: test_validators.py

import pytest
import validators

def test_typical_valid_age():
    """Confirm a typical valid age passes and returns True."""
    assert validators.validate_age(25) == True

def test_boundary_value():
    """Confirm the boundary value (120) passes and returns True."""
    assert validators.validate_age(120) == True
    # Testing the lower boundary (0) as well just to be thorough!
    assert validators.validate_age(0) == True

def test_invalid_age():
    """Confirm an invalid age raises a ValueError."""
    with pytest.raises(ValueError):
        validators.validate_age(150)