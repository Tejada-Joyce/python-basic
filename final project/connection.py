# https://realpython.com/python-mysql/#reading-records-from-the-database

import mysql.connector

from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='couponsdb',
                                         user='root',
                                         password='..PSwd2021', auth_plugin='mysql_native_password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)


def get_coupons_by_store(store_name, date):

    result = None
    query = ("SELECT * FROM coupon c "
             "WHERE c.store_id IN (SELECT store_id FROM store WHERE upper(store_name) = %s)"
             "AND %s BETWEEN c.start_date AND c.expiration_date"
             )
    with connection.cursor() as cursor:
        cursor.execute(query, (store_name, date))
        result = cursor.fetchall()
        cursor.close()
    return result


def get_stores():
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
