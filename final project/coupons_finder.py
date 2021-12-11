import datetime
from coupons_model import *

STORE_NAME_INDEX = 0


def main():
    try:
        # Print welcome
        print("\nWelcome to Coupons Finder!")

        # Get user's input
        store_name = input("Please enter the name of the store: ")

        ask = True

        while ask:
            # Check if the store name exists in database
            store_name = check_existing_store(store_name)

            if store_name:
                # Stop loop
                ask = False

                # When using datetime.now(), we need to use datetime.datetime
                date = datetime.datetime.date(datetime.datetime.now())

                # Print available coupons taking today's day as the reference
                # print_available_coupons(store_name, date)
                print(create_available_coupons_info(store_name, date))

            else:
                print("We are sorry. We don't work with that store at the present time, but here is the list of stores we have available:")
                print(create_stores_list())
                store_name = input(
                    "\nPlease enter the name of an available store: ")

    except (ValueError, TypeError) as error:
        print(type(error).__name__, error, sep=": ")


def check_existing_store(store_name):
    """ 
    Checks if the store name exists in database
    """
    stores = get_stores()
    stores_list = []
    for store in stores:
        store_dbname = store[STORE_NAME_INDEX]
        stores_list.append(store_dbname.upper())

    if store_name.upper() in stores_list:
        return store_name
    else:
        return False


def create_available_coupons_info(store_name, date):
    """
    Creates a string with the info of available coupons 
    for a specific store according to the date
    """
    COUPON_CODE = 1
    START_DATE = 2
    EXPIRATION_DATE = 3
    DISCOUNT = 5

    available_coupons_info = ""

    coupons_list = get_coupons_by_store(
        store_name, date)
    if len(coupons_list) == 0:
        available_coupons_info = "We are sorry. There are no coupons available for that store at this moment."
    else:
        available_coupons_info = "Good news! We found these coupons for you:"
        for coupon_info in coupons_list:
            text = "\n\t{} gets you {}% OFF. Valid from {:%B %e, %Y} to {:%B %e, %Y}"
            available_coupons_info += text.format(
                coupon_info[COUPON_CODE], coupon_info[DISCOUNT], coupon_info[START_DATE], coupon_info[EXPIRATION_DATE]).expandtabs(2)

    return available_coupons_info


def create_stores_list():
    """ 
    Create a string with the list of stores
    """
    stores = get_stores()
    length = len(stores)
    store_list = ""
    for store in stores:
        if store != stores[length-1]:
            store_list += f"\t{store[STORE_NAME_INDEX]}\n".expandtabs(2)
        else:
            store_list += f"\t{store[STORE_NAME_INDEX]}".expandtabs(2)

    return store_list


# These lines make sure main doesn't run automatically in the test file.
if __name__ == "__main__":
    main()
