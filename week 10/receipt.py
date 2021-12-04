import csv
from datetime import datetime

"""
Print the store name at the top of the receipt.
Print the list of ordered items.
Sum and print the number of ordered items.
Sum and print the subtotal due.
Compute and print the sales tax amount. Use 6% as the sales tax rate.
Compute and print the total amount due.
Print a thank you message.
Get the current date and time from your computer's operating system and print the current date and time.
Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""

PRODUCT_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
QUANTITY_INDEX = 1

def main():

  # Include a try block and except blocks to handle 
  # FileNotFoundError, PermissionError, and KeyError.
  try:   
    # Calls the read_products function and stores the 
    # products dictionary in a variable named products.
    products = read_products("products.csv")

    store_name = "Inkom Emporium"
    # items_total = 0
    # subtotal = 0
    tax_rate = 0.06
    # Get the current date and time from your computer's operating system
    current_date_and_time = datetime.now()

    # Print the store name at the top of the receipt.
    print(f"{store_name}\n")
    
    # Call function to process the request, print the list of ordered items,
    # and get items total and subtotal.
    sales_data = process_request("request.csv", products)
    items_total = sales_data[0]
    subtotal = sales_data[1]

    # Compute the sales tax amount. 
    sales_tax = subtotal * tax_rate
    # Compute the total amount due.
    total = subtotal + sales_tax

    print( 
      # Print the number of ordered items.
      f"\nNumber of Items: {items_total}\n"
      # Print the subtotal due
      f"Subtotal: {subtotal:.2f}\n"
      # Print the sales tax amount. 
      f"Sales Tax: {sales_tax:.2f}\n"
      # Print the total amount due.
      f"Total: {total:.2f}\n\n"
      # Print a thank you message.
      f"Thank you for shopping at the {store_name}.\n"
      # Print the current date and time.
      f"{current_date_and_time:%c}")

  except FileNotFoundError as not_found_err:
    print(not_found_err)
    print("Please choose a different file.")
  except PermissionError as perm_err:
    print(perm_err)
    print("Please choose a different file.")   
  except KeyError as key_err:
    print(f"The {key_err} key doesn't exist.\n"
           "Please use a valid key.")   

def read_products(filename):
    """
    will open the products.csv file for reading and use a 
    csv.reader to read each row and populate a dictionary 
    named products with the contents of the products.csv file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            key =  row[PRODUCT_INDEX]
            dictionary[key] = [row[NAME_INDEX], float(row[PRICE_INDEX])]

    return dictionary

def process_request(request_filename, products_data):

  items_total = 0
  subtotal = 0

  # Opens the request.csv file for reading.
  with open(request_filename, "rt") as csv_file:
      reader = csv.reader(csv_file)
      next(reader)

      # Contains a loop that reads and processes each row 
      # from the request.csv file
      for row in reader:
          product =  row[PRODUCT_INDEX]

          # Use the requested product number to find 
          # the corresponding item in the products dictionary.
          if product in products_data:
            name = products_data[product][0]
            quantity = int(row[QUANTITY_INDEX])
            price = float(products_data[product][1])

            # Sum the number of ordered items.
            items_total += quantity
            # Sum the subtotal due.
            subtotal += price * quantity
          
          # Print the product name, requested quantity, and product price.
          # Print the list of ordered items.
          print(f"{name}: {quantity} @ {price}")

  return [items_total, subtotal]

# Call main to start this program.
if __name__ == "__main__":
    main()
