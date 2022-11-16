"""Author: Nathan \n
This module provides the means for the program to access the database.
"""
import pymysql
import os
from contextlib import contextmanager
from dotenv import load_dotenv
# TODO functions to insert data for products and couriers.


class Database():

    def __init__(self) -> None:
        load_dotenv()
        self.host = os.environ.get("mysql_host")
        self.user = os.environ.get("mysql_user")
        self.password = os.environ.get("mysql_pass")
        self.database = os.environ.get("mysql_db")

    @contextmanager
    def _connect(self):
        database_connection = pymysql.connect(
            self.host,
            self.user,
            self.password,
            self.database,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            yield database_connection
        finally:
            database_connection.close()

    # region <PRODUCTS>

    def load_products(self):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, price '
                               'FROM products')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Product ID: {row["id"]}, '
                          f'Product Name: {row["name"]}, '
                          f'Product Price: {row["price"]}')

    # endregion

    # region <COURIERS>

    def load_couriers(self):
        pass

    # endregion

    # region <ORDERS>

    # endregion
