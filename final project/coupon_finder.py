from datetime import datetime
import connection

def main():
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        print("Coupons Finder")

        store = input("Please enter the name of the store: ")

        date = datetime.date(datetime.now())
  
        # Print the list of phone numbers which will show that
        # some of the phone number don't have an area code.
        find_coupons(store, date)

        # print(coupons_list)

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def find_coupons(store_name, date):
    """Phone numbers in the U.S. are often stored as ten digits and
    two dashes in this format: "ddd-ddd-dddd" where each d is a digit.
    If the length of phone_number is less than 12 characters, add the
    area code "208-" at the beginning of the phone_number and return
    phone_number.

    Parameter phone_number: a string of digits formatted as
        "ddd-dddd" or "ddd-ddd-dddd"
    Return: a string of digits formated as "ddd-ddd-dddd"
    """
    
    coupons_list = connection.get_coupons(store_name.upper(), date)
    if len(coupons_list) == 0:
        print("We are sorry. There are no coupons available for that store at this moment.")
    else:
        for row in coupons_list:
            print(row)
    # return coupons_list


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

