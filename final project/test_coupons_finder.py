import datetime
from coupon_finder import *
import pytest

available_stores = [
    'Walmart',
    'Starbucks',
    'Target',
    'Taco Bell',
    'McDonald’s',
    'HBO',
    'Amazon',
    'HP',
    'Dell',
    'JCPenney',
    'Best Buy',
    'WinCo Foods',
    'Sonic',
    'Hulu',
    'AT&T',
    'GameStop'
]


def test_check_existing_store():

    non_available_stores = [
        "Babbleopia",
        "Realcube",
        "Katz",
        "Meevee",
        "Wikibox",
        "Yadel",
        "Tazz",
        "Oozz",
        "Youopia",
        "Tazzy"
    ]
    # store_name = random.choice(stores)
    for store in available_stores:
        assert check_existing_store(store) == store

    for store in non_available_stores:
        assert check_existing_store(store) == False


def test_create_available_coupons_list():

    # Testing AT&T and HP on Dec 6, 2021
    date1 = datetime.date(2021, 12, 6)

    result1 = "Good news! We found these coupons for you:"
    result1 += "\n\tBOHTXP35 gets you 15% OFF. Valid from November 17, 2021 to December 11, 2021"
    result1 += "\n\tRJHXNZ29 gets you 2% OFF. Valid from November 25, 2021 to December 21, 2021"

    assert create_available_coupons_list(
        "at&t", date1) == result1.expandtabs(2)

    result2 = "We are sorry. There are no coupons available for that store at this moment."

    assert create_available_coupons_list("hp", date1) == result2

    # Testing Walmart and HBO on Jan 2, 2022
    date2 = datetime.date(2022, 1, 2)

    result3 = "Good news! We found these coupons for you:"
    result3 += "\n\tEFBIHZ99 gets you 20% OFF. Valid from December 27, 2021 to January  7, 2022"

    assert create_available_coupons_list(
        "Walmart", date2) == result3.expandtabs(2)

    result4 = "Good news! We found these coupons for you:"
    result4 += "\n\tIFYKJT55 gets you 15% OFF. Valid from January  2, 2022 to January 18, 2022"

    assert create_available_coupons_list("HBO", date2) == result4.expandtabs(2)

    # Testing Best Buy and Sonic on Feb 28, 2022
    date3 = datetime.date(2022, 2, 28)

    result5 = "We are sorry. There are no coupons available for that store at this moment."

    assert create_available_coupons_list("best buy", date3) == result5

    result6 = "Good news! We found these coupons for you:"
    result6 += "\n\tRWZKEJ42 gets you 5% OFF. Valid from February 27, 2022 to March 27, 2022"

    assert create_available_coupons_list(
        "soNIC", date3) == result6.expandtabs(2)


def test_create_stores_list():
    store_list = ""
    length = len(available_stores)
    for store in available_stores:
        if store != available_stores[length-1]:
            store_list += f"\t{store}\n".expandtabs(2)
        else:
            store_list += f"\t{store}".expandtabs(2)

    assert create_stores_list() == store_list


    # Call the main function that is part of pytest so that
    # the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
