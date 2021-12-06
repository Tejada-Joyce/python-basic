# Functions to run queries and retrieve data

def get_coupons_by_store(store_name, date, connection):

    result = None
    query = ("SELECT * FROM coupon c "
             "WHERE c.store_id IN (SELECT store_id FROM store WHERE upper(store_name) = %s)"
             "AND %s BETWEEN c.start_date AND c.expiration_date "
             "ORDER BY c.expiration_date"
             )
    with connection.cursor() as cursor:
        cursor.execute(query, (store_name, date))
        result = cursor.fetchall()
        cursor.close()
    return result


def get_stores(connection):
    """
    Returns stores as a list of tuples
    """
    result = None
    query = ("SELECT store_name FROM store")
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    return result
