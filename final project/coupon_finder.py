# from datetime import datetime
import datetime
import connection

STORE_NAME_INDEX = 0


def main():
    try:
        # Print title
        print("Coupons Finder")

        # Get user's input
        store_name = input("Please enter the name of the store: ")

        # Check if the store name exists in database
        store_name = check_existing_store(store_name)

        if store_name:
            # When using datetime.now(), we need to use datetime.datetime
            date = datetime.datetime.date(datetime.datetime.now())

            # When we pass a specific date, we only use datetime once
            # date = datetime.date(2022, 2, 11)

            # Print available coupons taking today's day as the reference
            print__available_coupons(store_name, date)
        else:
            print("We are sorry. We don't work with that store at the present time, but here is the list of stores we have available:")
            print_stores()

    except ValueError as error:
        print(type(error).__name__, error, sep=": ")


def print__available_coupons(store_name, date):
    """
    Prints available coupons for a specific store
    according to the date
    """
    COUPON_CODE = 1
    START_DATE = 2
    EXPIRATION_DATE = 3
    DISCOUNT = 5

    coupons_list = connection.get_coupons_by_store(store_name.upper(), date)
    if len(coupons_list) == 0:
        print("We are sorry. There are no coupons available for that store at this moment.")
    else:
        print("Good news! We found these coupons for you:")
        for coupon_info in coupons_list:
            text = "\t{} gets you {}% OFF. Valid from {:%B %e, %Y} to {:%B %e, %Y}"
            print(text.format(
                coupon_info[COUPON_CODE], coupon_info[DISCOUNT], coupon_info[START_DATE], coupon_info[EXPIRATION_DATE]).expandtabs(2))


def check_existing_store(store_name):
    """ 
    Checks if the store name exists in database
    """
    stores = connection.get_stores()
    stores_list = []
    for store in stores:
        store_dbname = store[STORE_NAME_INDEX]
        stores_list.append(store_dbname.upper())

    if store_name.upper() in stores_list:
        return store_name
    else:
        return False


def print_stores():
    """ 
    Prints list of stores
    """
    stores = connection.get_stores()

    for store in stores:
        print(f"\t{store[STORE_NAME_INDEX]}".expandtabs(2))


# These lines make sure main doesn't run automatically in the test file.
if __name__ == "__main__":
    main()
