import csv


PRODUCT_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
QUANTITY_INDEX = 1

def main():
    """
    - Calls the read_products function and stores the products dictionary in a variable 
      named products.
    - Prints the products dictionary.
    - Opens the request.csv file for reading.
    - Contains a loop that reads and processes each row from the request.csv file. 
      Within the body of the loop, your program must do the following for each row:
        - Use the requested product number to find the corresponding item in the 
          products dictionary.
        - Print the product name, requested quantity, and product price.

    """
    # Calls the read_products function and stores the 
    # products dictionary in a variable named products.
    products = read_products("products.csv")

    # Prints the products dictionary.
    print("Products")
    for product_key,product_value in products.items():
      print(f"{product_key} {product_value}")

    print("")

    print("Requested Items")

    # Opens the request.csv file for reading.
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        # Contains a loop that reads and processes each row 
        # from the request.csv file
        for row in reader:
            product =  row[PRODUCT_INDEX]

            # Use the requested product number to find 
            # the corresponding item in the products dictionary.
            if product in products:
              name = products[product][0]
              quantity = int(row[QUANTITY_INDEX])
              price = float(products[product][1])
            
            # Print the product name, requested quantity, and product price.
            print(f"{name}: {quantity} @ {price}")
    


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


# Call main to start this program.
if __name__ == "__main__":
    main()
