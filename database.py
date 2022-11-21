"""Author: Nathan \n
This module provides the means for the program to access the database.
"""
import pymysql
import os
from contextlib import contextmanager
from dotenv import load_dotenv
from typing import List, Dict

import inputchecker
from productclass import Product
from courierclass import Courier
from orderclass import Order


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
                cursor.execute(
                    'SELECT id, name, price FROM products')
                rows = cursor.fetchall()
        return rows

    def load_product_id(self, product: Product) -> int:
        """Searches the database for the product, and returns the database id
        if there is a match.

        Args:
            product (Product): The product.

        Returns:
            int: Product id.
        """
        name = product.name
        price = product.price
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'SELECT id FROM products WHERE name = %s AND price = %s')
                adr = (name, price)
                cursor.execute(sql, adr)

                row = cursor.fetchone()
        if row is None:
            raise Exception(f'Could not find id for {name}')
        return row['id']

    def save_products(self, products: List[Product]) -> None:
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

    def insert_product(self, product: Product) -> int:
        """Inserts a product into the database while also returning the
        newly generated product ID.\n
        Call this before appending your product to the list.

        Args:
            product (Product): The product to be inserted.

        Returns:
            int: Product id.
        """
        name = product.name
        price = product.price
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'INSERT INTO products (name, price) VALUES (%s, %s)')
                adr = (name, price)
                cursor.execute(sql, adr)
                connection.commit()
        product_id = self.load_product_id(product)
        return product_id

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
                sql = (
                    'UPDATE products SET name = %s, price = %s WHERE id = %s')
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
                sql = (
                    'DELETE FROM products WHERE id = %s')
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
                cursor.execute('SELECT id, name, phone FROM couriers')
                rows = cursor.fetchall()
        return rows

    def load_courier_id(self, courier: Courier) -> Courier:
        """Searches the database for the courier, and returns the database id
        if there is a match.

        Args:
            courier (Courier): The courier.

        Returns:
            int: Courier id.
        """
        name = courier.name
        phone = courier.phone
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'SELECT id FROM couriers WHERE name = %s AND phone = %s')
                adr = (name, phone)
                cursor.execute(sql, adr)

                row = cursor.fetchone()
        if row is None:
            raise Exception(f'Could not find id for {name}')
        return row['id']

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
        """Inserts a courier into the database while also returning the
        newly generated courier ID.\n
        Call this before appending your courier to the list.

        Args:
            courier (Courier): The courier to be inserted.

        Returns:
            int: Courier id.
        """
        name = courier.name
        phone = courier.phone
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'INSERT INTO couriers (name, phone) VALUES (%s, %s)')
                adr = (name, phone)
                cursor.execute(sql, adr)
                connection.commit()
        courier_id = self.load_courier_id(courier)
        return courier_id

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
                sql = (
                    'UPDATE couriers SET name = %s, phone = %s WHERE id = %s')
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
                sql = (
                    'DELETE FROM couriers WHERE id = %s')
                adr = (id)
                cursor.execute(sql, adr)
                connection.commit()
        return True

    # endregion

    # region <ORDERS>

    def load_orders(self) -> List:
        """Loads the data from orders table.

        Returns:
            List: The data.
        """
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, customer_name, customer_address, '
                    'customer_phone, courier, statuscode, items '
                    'FROM orders')
                rows = cursor.fetchall()
        return rows

    def load_order_id(self, order: Order) -> int:
        """Searches the database for the order, and returns the database id
        if there is a match.

        Args:
            order (Order): The order.

        Returns:
            int: Order id.
        """
        customer_name = order.customer_name
        customer_address = order.customer_address
        customer_phone = order.customer_phone
        courier = order.courier
        statuscode = order.statuscode
        items = order.items
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'SELECT id FROM orders WHERE customer_name = %s AND '
                    'customer_address = %s AND customer_phone = %s AND '
                    'courier = %s AND statuscode = %s AND items = %s')
                adr = (
                    customer_name, customer_address, customer_phone, courier,
                    statuscode, items)
                cursor.execute(sql, adr)

                row = cursor.fetchone()
        if row is None:
            raise Exception(
                f'Could not find id for {customer_name}\'s order')
        return row['id']

    def save_orders(self, orders: List[Order]) -> None:
        """Iterates through list of orders, if one doesn't have an ID, add it
        to the database.

        Args:
            orders (List): List of orders.
        """
        for order in orders:
            if order.id == 0:
                self.insert_order(order)
            else:
                self.update_order(order)

    def insert_order(self, order: Order) -> int:
        """Inserts a order into the database while also returning the
        newly generated order ID.\n
        Call this before appending your order to the list.

        Args:
            order (Order): The order to be inserted.

        Returns:
            int: Order id.
        """
        customer_name = order.customer_name
        customer_address = order.customer_address
        customer_phone = order.customer_phone
        courier = order.courier
        statuscode = order.statuscode
        items = order.items
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'INSERT INTO orders (customer_name, customer_address,'
                    'customer_phone, courier, statuscode, items) '
                    'VALUES (%s, %s, %s, %s, %s, %s)')
                adr = (
                    customer_name, customer_address, customer_phone, courier,
                    statuscode, items)
                cursor.execute(sql, adr)
                connection.commit()
        # Load newly generated ID.
        order_id = self.load_order_id(order)
        order.id = order_id
        # Insert items after inserting the order and retrieving ID.
        self.insert_order_items(order)
        return order_id

    def insert_order_items(self, order: Order) -> None:
        """Inserts order items in the order_items table using the order's
        'items' attribute.

        Args:
            order (Order): Order with the items.
        """
        id = order.id
        item_dict = inputchecker.get_item_quantity(order.items)
        for key in item_dict:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    sql = (
                        'INSERT INTO order_items (order_id, product_id, '
                        'product_quantity) VALUES (%s, %s, %s)')
                    adr = (
                        id, key, item_dict[key])
                    cursor.execute(sql, adr)
                    connection.commit()

    def update_order(self, order: Order) -> bool:
        """Updates the order in the database with the attributes from the
        order in the program.

        Args:
            order (Order): Order that will update the database

        Returns:
            bool: True if function successful, False if not.
        """
        customer_name = order.customer_name
        customer_address = order.customer_address
        customer_phone = order.customer_phone
        courier = order.courier
        statuscode = order.statuscode
        items = order.items
        if order.id == 0:
            return False
        id = order.id
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'UPDATE orders SET customer_name = %s, '
                    'customer_address = %s, customer_phone = %s, '
                    'courier = %s, statuscode = %s, items = %s WHERE id = %s')
                adr = (
                    customer_name, customer_address, customer_phone, courier,
                    statuscode, items, id)
                cursor.execute(sql, adr)
                connection.commit()
        self.update_order_items(order)
        return True

    def update_order_items(self, order: Order) -> None:
        """Updates the order's order_items rows by deleting, then re-inserting
        item data into the table.

        Args:
            order (Order): Order with the items.
        """
        # First remove the existing rows related to order.
        self.remove_order_items(order)
        # Now we can re-insert our item rows into table
        self.insert_order_items(order)

    def remove_order(self, order: Order) -> bool:
        """Removes the input order from the database.

        Args:
            order (Order): Order that will be removed from the database.

        Returns:
            bool: True if function successful, False if not.
        """
        if order.id == 0:
            return False
        id = order.id
        # Remove the items first as it contains foreign keys.
        self.remove_order_items(order)
        # Then remove the order proper.
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'DELETE FROM orders WHERE id = %s')
                adr = (id)
                cursor.execute(sql, adr)
                connection.commit()
        return True

    def remove_order_items(self, order: Order) -> None:
        """Removes order's items from the order_items table.

        Args:
            order (Order): Order with the items.
        """
        id = order.id
        with self._connect() as connection:
            with connection.cursor() as cursor:
                sql = (
                    'DELETE FROM order_items WHERE order_id = %s')
                adr = (id)
                cursor.execute(sql, adr)
                connection.commit()

    # endregion
