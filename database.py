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
        key id to the product if there is a match.

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

    def save_products(self, products: List) -> None:
        """Iterates through list of products, if one doesn't have an ID, add it
        to the database.

        Args:
            products (List): List of products.
        """
        for product in products:
            if product.id == 0:
                self.insert_product(product)
            else:
                self.update_product(product)

    def insert_product(self, product: Product) -> Product:
        """Inserts a product into the database while also grabbing the ID from
        the database and applying it to the product object. \n
        Call this before appending your product to the list.

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
                VALUES (%s, %s)')
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

    def load_couriers(self) -> List:
        """Loads the data from couriers table.

        Returns:
            List: The data.
        """
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name, phone '
                               'FROM couriers')
                rows = cursor.fetchall()
        return rows

    def load_courier_id(self, courier: Courier) -> Courier:
        """Searches the database for the courier, and appends the database's
        key id to the courier if there is a match.

        Args:
            courier (Courier): The courier.

        Returns:
            courier: Courier with the id appended.
        """
        name = courier.name
        phone = courier.phone
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = 'SELECT id FROM couriers WHERE name = %s AND phone = %s'
                adr = (name, phone)
                cursor.execute(sql, adr)

                row = cursor.fetchone()
        if row is None:
            raise Exception(f'Could not find id for {name}')
        courier.id = row['id']
        return courier

    def save_couriers(self, couriers: List) -> None:
        """Iterates through list of couriers, if one doesn't have an ID, add it
        to the database.

        Args:
            couriers (List): List of couriers.
        """
        for courier in couriers:
            if courier.id == 0:
                self.insert_courier(courier)
            else:
                self.update_courier(courier)

    def insert_courier(self, courier: Courier) -> Courier:
        """Inserts a courier into the database while also grabbing the ID from
        the database and applying it to the courier object. \n
        Call this before appending your courier to the list.

        Args:
            courier (Courier): The courier to be inserted.

        Returns:
            Courier: The courier, now with the database id appended.
        """
        name = courier.name
        phone = courier.phone
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = ('INSERT INTO couriers (name, phone) \
                VALUES (%s, %s)')
                adr = (name, phone)
                cursor.execute(sql, adr)
                connection.commit()
        self.load_courier_id(courier)
        return courier

    def update_courier(self, courier: Courier) -> bool:
        """Updates the courier in the database with the attributes from the
        courier in the program.

        Args:
            courier (Courier): Courier that will update the database

        Returns:
            bool: True if function successful, False if not.
        """
        name = courier.name
        phone = courier.phone
        if courier.id == 0:
            return False
        id = courier.id
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = ('UPDATE couriers \
                SET name = %s, phone = %s \
                WHERE id = %s')
                adr = (name, phone, id)
                cursor.execute(sql, adr)
                connection.commit()
        return True

    def remove_courier(self, courier: Courier) -> bool:
        """Removes the input courier from the database.

        Args:
            courier (Courier): Courier that will be removed from the database.

        Returns:
            bool: True if function successful, False if not.
        """
        if courier.id == 0:
            return False
        id = courier.id
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = ('DELETE FROM couriers \
                WHERE id = %s')
                adr = (id)
                cursor.execute(sql, adr)
                connection.commit()
        return True

    # endregion

    # region <ORDERS>

    # endregion
