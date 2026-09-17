def calculate_total(price, quantity):
    """Calculate the total cost of an item."""
    total = price * quantity
    return total

def display_total(total):
    """Display the calculated total."""
    print("Total:", total)

price = 500
quantity = 3
total = calculate_total(price, quantity)
display_total(total)
