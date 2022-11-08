# Author: Nathan
# This is the order menu for the cafe application.

from time import sleep
import csv
# import json

import orderclass


class Order_menu():
    """Class used as the interface for handling orders."""
    def __init__(self) -> None:
        """Initialise order menu object and loads data."""
        # List of orders with a sample order.
        self.orders = [orderclass.Order('John', 'Planet Earth',
                                        '1439280432')]
        # Debug stuff to check if it has loaded properly.
        self.list_orders()
        self.load_orders()
        self.list_orders()

    def list_orders(self) -> None:
        """Prints out order list."""
        i = 1
        for order in self.orders:
            print(f"""Order No.{i}:
            Customer name: {order.customer_name}
            Customer address: {order.customer_address}
            Customer phone number: {order.customer_phone}
            Order status: {order.status}
            """)
            sleep(0.5)
            i += 1

    def load_orders(self) -> None:
        """Loads orders from a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/orderdata.csv', 'r') as file:
                self.orders.clear()
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    neworder = orderclass.Order(row['customer_name'],
                                                row['customer_address'],
                                                row['customer_phone'])
                    neworder.status = row['status']
                    self.orders.append(neworder)
            print('LOADED ORDERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    def save_orders(self) -> None:
        """Saves order data to a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/orderdata.csv', 'w', newline='') as file:
                fieldnames = ['customer_name', 'customer_address',
                              'customer_phone', 'status']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for order in self.orders:
                    writer.writerow(order.get_order())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

    def set_order_create(self) -> bool:
        """Asks for user input to create an order.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, stop function.
        userinput_name = input('Input customer name: ')
        if userinput_name.strip() == '':
            return False
        userinput_address = input('Input customer address: ')
        if userinput_address.strip() == '':
            return False
        userinput_phone = input('Input customer phone number: ')
        if userinput_phone.strip() == '':
            return False
        # If the inputs are valid, add a new entry.
        new_order = orderclass.Order(userinput_name, userinput_address,
                                     userinput_phone)
        self.orders.append(new_order)
        return True

    def set_order_update(self, index: int) -> bool:
        """Asks for user input to update an order.

        Args:
            index (int): List index of the order to be updated.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, continue but don't update the order.
        userinput = input('Input customer name: ')
        if userinput.strip() != '':
            self.orders[index].customer_name = userinput
        userinput = input('Input customer address: ')
        if userinput.strip() != '':
            self.orders[index].customer_address = userinput
        userinput = input('Input customer phone number: ')
        if userinput.strip() != '':
            self.orders[index].customer_phone = userinput
        return True

    def set_order_update_status(self, index: int) -> bool:
        """Asks for user input to update an order's status.

        Args:
            index (int): List index of the order to be updated.

        Returns:
            bool: True if function successful, False if not.
        """
        print("""
            0. Preparing
            1. Awaiting pickup
            2. Out for delivery
            3. Delivered
    """)
        new_status = input('Input number for order status: ')
        self.orders[index].set_order_status(new_status)
