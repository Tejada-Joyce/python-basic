import connection

# Create connection to database
connection_db = connection.create_connection()

# Functions to run queries and retrieve data


def get_coupons_by_store(store_name, date):
    """
    Parameters
        - store_name: The name of the store with no specific format
        - date: The date formated with datetime.date correctly or the regular format "YYYY-MM-DD"
                Ex. datetime.date(2022, 1, 10) or 2022-1-10 or 2022-01-10
    Return a list of tuples with the coupons' information according 
    to the store and date passed
    """
    result = None
    query = ("SELECT * FROM coupon c "
             "WHERE c.store_id IN (SELECT store_id FROM store WHERE store_name = %s)"
             "AND %s BETWEEN c.start_date AND c.expiration_date "
             "ORDER BY c.expiration_date"
             )
    with connection_db.cursor() as cursor:
        cursor.execute(query, (store_name, date))
        result = cursor.fetchall()
        cursor.close()
    return result


def get_stores():
    """
    Return a list of tuples with the names of the stores
    """
    result = None
    query = ("SELECT store_name FROM store")
    with connection_db.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    return result
