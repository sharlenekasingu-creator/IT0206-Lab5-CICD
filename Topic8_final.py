# Name: Sharlene Kasingu
# Date: September 23, 2026
# Filename: Topic8_final.py

# Import the classes directly from the package
from inventory_package import Product, Inventory

# Create at least three Product objects
laptop = Product("Laptop", 999.99, 10)
mouse = Product("Mouse", 25.50, 3)
keyboard = Product("Keyboard", 75.00, 50)

# Create an Inventory and add the products
store_inventory = Inventory()
store_inventory.add_product(laptop)
store_inventory.add_product(mouse)
store_inventory.add_product(keyboard)

# Print the results
print("Total inventory value: $", store_inventory.total_inventory_value())
print("Low stock products:")
for product in store_inventory.low_stock_products(5):
    print(f"- {product.name} (Qty: {product.quantity})")