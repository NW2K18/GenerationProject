"""Author: Nathan \n
This module provides the means for the program to access the database.
"""
import pymysql
import os
from contextlib import contextmanager
from dotenv import load_dotenv
from typing import List

from productclass import Product
from courierclass import Courier
from orderclass import Order

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

    def load_products(self) -> List:
        """Loads the data from products table.

        Returns:
            List: The data.
        """
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, price '
                               'FROM products')
                rows = cursor.fetchall()
        return rows

    def load_product_id(self, product: Product) -> Product:
        """Searches the database for the product, and appends the database's
        key id to the produce if there is a match.

        Args:
            product (Product): The product.

        Returns:
            Product: Product with the id appended.
        """
        name = product.name
        price = product.price
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = 'SELECT id FROM products WHERE name = %s AND price = %s'
                adr = (name, price)
                cursor.execute(sql, adr)

                row = cursor.fetchone()
        if row is None:
            raise Exception(f'Could not find id for {name}')
        product.id = row['id']
        return product

    def insert_product(self, product: Product) -> Product:
        """Inserts a product into the database while also grabbing the ID from
        the database and applying it to the product object.

        Args:
            product (Product): The product to be inserted.

        Returns:
            Product: The product, now with the database id appended.
        """
        name = product.name
        price = product.price
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = ('INSERT INTO products (name, price) \
                VALUES %s, %s')
                adr = (name, price)
                cursor.execute(sql, adr)
                connection.commit()
        self.load_product_id(product)
        return product

    def update_product(self, product: Product) -> bool:
        """Updates the product in the database with the attributes from the
        product in the program.

        Args:
            product (Product): Product that will update the database

        Returns:
            bool: True if function successful, False if not.
        """
        name = product.name
        price = product.price
        if product.id == 0:
            return False
        id = product.id
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = ('UPDATE products \
                SET name = %s, price = %s \
                WHERE id = %s')
                adr = (name, price, id)
                cursor.execute(sql, adr)
                connection.commit()
        return True

    def remove_product(self, product: Product) -> bool:
        """Removes the input product from the database.

        Args:
            product (Product): Product that will be removed from the database.

        Returns:
            bool: True if function successful, False if not.
        """
        if product.id == 0:
            return False
        id = product.id
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = ('DELETE FROM products \
                WHERE id = %s')
                adr = (id)
                cursor.execute(sql, adr)
                connection.commit()
        return True

    # endregion

    # region <COURIERS>

    def load_couriers(self):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, price '
                               'FROM couriers')
                rows = cursor.fetchall()
        return rows

    # endregion

    # region <ORDERS>

    # endregion
