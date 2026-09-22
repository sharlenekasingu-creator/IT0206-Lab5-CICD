# Name: Sharlene Kasingu
# Date: September 23, 2026
# Filename: test_inventory.py

import pytest
from inventory_package import Product, Inventory

def test_total_value_single_product():
    """Test that a single product calculates its total value correctly."""
    p = Product("Phone", 500, 2)
    assert p.total_value() == 1000

def test_inventory_total_value():
    """Test that the inventory calculates the combined total value correctly."""
    inv = Inventory()
    inv.add_product(Product("A", 10, 5))  # Value: 50
    inv.add_product(Product("B", 20, 3))  # Value: 60
    assert inv.total_inventory_value() == 110

def test_low_stock_detection():
    """Test that low stock products are correctly identified based on a threshold."""
    inv = Inventory()
    inv.add_product(Product("Low", 10, 2))   # Below threshold
    inv.add_product(Product("High", 10, 10)) # Above threshold
    
    low_stock = inv.low_stock_products(5)
    
    assert len(low_stock) == 1
    assert low_stock[0].name == "Low"