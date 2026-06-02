# Product data (often arrives as strings from files or user input)
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "29.99"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "29.99"
item3_qty = "1"
tax_rate = "0.075"

# Convert to appropriate types for calculation

tax_rate = float(tax_rate)
item1_price = float(4.99)
item2_price = float(29.99)
item3_price = float(29.99)
item1_qty = int(2)
item2_qty = int(1)
item3_qty = int(1)
subtotal1 = item1_price * item1_qty
subtotal2 = item2_price * item2_qty
subtotal3 = item3_price * item3_qty

# Now we can do math
subtotal = subtotal1 + subtotal2 + subtotal3
tax = subtotal * tax_rate
total = subtotal + tax

# Display results
print("=" * 40)
print("Store Receipt")
print("=" * 40)
print()
print(f"Product: {item1_name} Price: ${item1_price} * {item1_qty} ${subtotal1:.2f}")
print(f"         {item2_name} Price: ${item2_price} * {item2_qty} ${subtotal2:.2f}")
print(f"         {item3_name} Price: ${item3_price} * {item3_qty} ${subtotal3:.2f}")
print("-" * 40)
print(f"Subtotal: ${subtotal:.2f}")  # .2f formats to 2 decimal places 
print(f"Tax ({tax_rate * 100}%): ${tax:.2f}")
print("=" * 40)
print(f"Total: ${total:.2f}")
print("=" * 40)
