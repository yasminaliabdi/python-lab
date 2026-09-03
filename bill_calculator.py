# Week 2 Assignment: Bill Calculator

# Get item price from user
price = float(input("Enter the price of the item: "))

# Get quantity from user
quantity = int(input("Enter the quantity: "))

# Calculate total cost
total = price * quantity

# Display result
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
