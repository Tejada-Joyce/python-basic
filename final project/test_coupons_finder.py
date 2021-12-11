import datetime
from coupons_finder import *
from coupons_model import *
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

unavailable_stores = [
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


def test_check_existing_store():
    """
    Test check_existing_store from coupons_finder file
    """

    # store_name = random.choice(stores)
    for store in available_stores:
        assert check_existing_store(store) == store

    for store in unavailable_stores:
        assert check_existing_store(store) == False


def test_create_available_coupons_info():
    """
    Test create_available_coupons_info from coupons_finder file
    """

    # Testing AT&T and HP "on" Dec 6, 2021
    date1 = "2021-12-6"

    result1 = "Good news! We found these coupons for you:"
    result1 += "\n\tBOHTXP35 gets you 15% OFF. Valid from November 17, 2021 to December 11, 2021"
    result1 += "\n\tRJHXNZ29 gets you 2% OFF. Valid from November 25, 2021 to December 21, 2021"

    assert create_available_coupons_info(
        "at&t", date1) == result1.expandtabs(2)

    result2 = "We are sorry. There are no coupons available for that store at this moment."

    assert create_available_coupons_info("hp", date1) == result2

    # Testing Walmart and HBO "on" Jan 2, 2022
    date2 = "2022-1-2"

    result3 = "Good news! We found these coupons for you:"
    result3 += "\n\tEFBIHZ99 gets you 20% OFF. Valid from December 27, 2021 to January  7, 2022"

    assert create_available_coupons_info(
        "Walmart", date2) == result3.expandtabs(2)

    result4 = "Good news! We found these coupons for you:"
    result4 += "\n\tIFYKJT55 gets you 15% OFF. Valid from January  2, 2022 to January 18, 2022"

    assert create_available_coupons_info("HBO", date2) == result4.expandtabs(2)

    # Testing Best Buy and Sonic "on" Feb 28, 2022
    date3 = "2022-2-28"

    result5 = "We are sorry. There are no coupons available for that store at this moment."

    assert create_available_coupons_info("best buy", date3) == result5

    result6 = "Good news! We found these coupons for you:"
    result6 += "\n\tRWZKEJ42 gets you 5% OFF. Valid from February 27, 2022 to March 27, 2022"

    assert create_available_coupons_info(
        "soNIC", date3) == result6.expandtabs(2)


def test_create_stores_list():
    """
    Test create_stores_list from coupons_finder file
    """

    store_list = ""
    length = len(available_stores)
    for store in available_stores:
        if store != available_stores[length-1]:
            store_list += f"\t{store}\n".expandtabs(2)
        else:
            store_list += f"\t{store}".expandtabs(2)

    assert create_stores_list() == store_list


def test_get_coupons_by_store():
    """
    Test get_coupons_by_store from coupons_model file
    """

    # Tuples include coupon_id, coupon_code, start_date, expiration_date, store_id, and discount

    """
    Tests with expected no empty results 
    """
    # Testing Hulu "on" Dec 15, 2021
    coupons1 = [(3, 'YBAOSJ24', datetime.date(2021, 12, 9), datetime.date(2022, 1, 6), 14, 2),
                (4, 'OREWNZ13', datetime.date(2021, 12, 15), datetime.date(2022, 1, 8), 14, 20)]

    assert get_coupons_by_store(
        "Hulu", "2021-12-15") == coupons1

    # Testing WinCo Foods "on" Jan 10, 2022
    coupons2 = [(44, 'IQCFGR52', datetime.date(2022, 1, 2),
                 datetime.date(2022, 1, 14), 12, 10)]

    assert get_coupons_by_store(
        "winco foods", datetime.date(2022, 1, 10)) == coupons2

    # Testing Amazon "on" Feb 1, 2022
    coupons3 = [(15, 'USJYIX73', datetime.date(2022, 1, 22), datetime.date(2022, 2, 1), 7, 5),
                (81, 'USEORA87', datetime.date(2022, 1, 28),
                 datetime.date(2022, 2, 7), 7, 5),
                (50, 'XDZPSJ89', datetime.date(2022, 2, 1), datetime.date(2022, 2, 15), 7, 15)]

    assert get_coupons_by_store(
        "AmaZoN", datetime.date(2022, 2, 1)) == coupons3

    """
    Tests with expected empty results
    """
    coupons4 = []

    # Testing Taco Bell "on" Mar 26, 2022
    assert get_coupons_by_store(
        "TACO BELL", datetime.date(2022, 3, 26)) == coupons4

    # Testing Starbucks "on" Dec 31, 2021
    assert get_coupons_by_store(
        "Starbucks", datetime.date(2021, 12, 31)) == coupons4

    # Testing unavailable stores "on" Jan 10, 2022
    for store in unavailable_stores:
        assert get_coupons_by_store(
            store, datetime.date(2022, 1, 10)) == coupons4


def test_get_stores():
    """
    Test get_stores from coupons_model file
    """

    stores = [('Walmart',), ('Starbucks',),
              ('Target',), ('Taco Bell',),
              ('McDonald’s',), ('HBO',),
              ('Amazon',), ('HP',),
              ('Dell',), ('JCPenney',),
              ('Best Buy',), ('WinCo Foods',),
              ('Sonic',), ('Hulu',),
              ('AT&T',), ('GameStop',)]

    assert get_stores() == stores

    # Call the main function that is part of pytest so that
    # the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
