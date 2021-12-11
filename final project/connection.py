# https://realpython.com/python-mysql/#reading-records-from-the-database

import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        # If you are testing this, you would need to change
        # the host, database, user, or password as needed
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

    return connection
