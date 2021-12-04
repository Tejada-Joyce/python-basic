"""
gets a customer's subtotal as input and gets the current day 
of the week from your computer's clock. Your program must not 
ask the user to enter the day of the week. Instead, it must 
get the day of the week from your computer's clock.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
your program must subtract 10% from the subtotal. Your program must 
then compute the total amount due by adding sales tax of 6% to the 
subtotal. Your program must print the discount amount if applicable, 
the sales tax amount, and the total amount due.
"""

from datetime import datetime
from os import supports_bytes_environ


# Ask for the user's subtotal
# subtotal = float(input("Please enter the subtotal: $"))
asking = True
subtotal = 0

while asking == True:
    item_price = input("Please enter the price of the item: $")
    if item_price.lower()== 'done':
        asking = False
    else:    
        item_price = float(item_price)
        quantity = int(input("Please enter the quantity of items: "))
        subtotal += item_price * quantity

print(f"Subtotal amount: ${subtotal:.2f}")

# Get the current day of the week from your computer's clock.
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
# day_of_week = 0


# If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
# your program must subtract 10% from the subtotal.
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = 0.1*subtotal
    subtotal -= discount
    print(f"Discount amount: {discount:.2f}")
elif subtotal < 50 and (day_of_week == 1 or day_of_week == 2):
    amount_needed = 50 - subtotal
    print(f"You would need to spend ${amount_needed:.2f} more to receive a discount.")


# Compute the total amount due by adding sales tax of 6% to the subtotal.
tax = subtotal * 0.06
total = subtotal + tax

print(f"Sales tax amount: ${tax:.2f}")
print(f"Total: ${total:.2f}")










