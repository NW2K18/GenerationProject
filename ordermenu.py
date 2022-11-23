"""Author: Nathan \n
This is the order menu for the cafe application.
"""

from time import sleep
import csv
from typing import List, Union

import inputchecker
import datalogger
from orderclass import Order
from productmenu import Product_menu
from couriermenu import Courier_menu
from productclass import Product
from courierclass import Courier
from database import Database


class Order_menu():
    """Class used as the interface for handling orders."""

    def __init__(self) -> None:
        """Initialise order menu object and loads data."""
        # List of orders with a sample order.
        self.orders = [Order(
            'John', 'Planet Earth', '1439280432')]
        self.database = Database()

        self.load_orders_database()

    def list_orders(
            self, orderlist: List[Order], productlist: List[Product],
            courierlist: List[Courier]) -> int:
        """Prints out order list.

        Args:
            orderlist (List[Order]): List of orders to be listed.
            productlist (List[Product]): Used to print out item info.
            courierlist (List[Courier]): Used to print out courier info.

        Returns:
            int: Size of order list
        """
        for order in orderlist:
            # Create a string to print.
            print_list = (
                f'Order No.{order.id}:'
                f'\n\tCustomer name: {order.customer_name}'
                f'\n\tCustomer address: {order.customer_address}'
                f'\n\tCustomer phone number: {order.customer_phone}')
            # Adding the courier.
            if order.get_courier() is not None:
                courier_index = inputchecker.get_courier_index(
                    courierlist, order.get_courier())
                print_list += (
                    f'\n\tCourier: {order.get_courier()} - '
                    f'{courierlist[courier_index].name}')
            print_list += (
                f'\n\tOrder status: {order.status}')
            # Adding the products.
            if order.get_items() is not None:
                print_list += ('\n\tItems:')
                for item in order.get_items().split(','):
                    product_index = inputchecker.get_product_index(
                        productlist, item)
                    print_list += (
                        f'\n\t\t{productlist[product_index].name} - '
                        f'{productlist[product_index].get_product_price()}')
            print(print_list)
            sleep(0.5)
        return len(self.orders)

    def list_sorted_orders(
            self, option: str, productlist: List[Product],
            courierlist: List[Courier]) -> int:
        """Prints a list sorted through the specified option

        Args:
            option (str): courier, status
            productlist (List[Product]): Used to print out item info.
            courierlist (List[Courier]): Used to print out courier info.

        Raises:
            Exception: When an invalid option has been passed in.

        Returns:
            int: Size of order list
        """
        sorted_list = []
        match option:
            case 'courier':
                sorted_list = sorted(
                    self.orders, key=lambda order: order.courier)
            case 'status':
                sorted_list = sorted(
                    self.orders, key=lambda order: order.statuscode)
            case _:
                raise Exception('Invalid option passed to list_orders_custom')
        self.list_orders(sorted_list, productlist, courierlist)
        return len(self.orders)

    # region <SAVE AND LOAD>

    def load_orders_csv(self) -> None:
        """Loads orders from a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/orderdata.csv', 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                self.orders.clear()
                for row in reader:
                    neworder = Order(
                        row['customer_name'], row['customer_address'],
                        row['customer_phone'])
                    # Load ID from database.
                    neworder.set_order_status(row['statuscode'])
                    neworder.set_courier(row['courier'])
                    neworder.set_items(row['items'])
                    neworder.id = self.database.load_order_id(neworder)
                    self.orders.append(neworder)
            print('LOADED ORDERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    def save_orders_csv(self) -> None:
        """Saves order data to a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/orderdata.csv', 'w', newline='') as file:
                fieldnames = [
                    'id', 'customer_name', 'customer_address',
                    'customer_phone', 'courier',
                    'statuscode', 'items']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for order in self.orders:
                    writer.writerow(order.get_order())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.
        print('EXPORTED ORDERS SUCCESSFULLY')

    def load_orders_database(self) -> None:
        """Loads order data from database."""
        rows = self.database.load_orders()
        self.orders.clear()
        for row in rows:
            neworder = Order(
                row['customer_name'], row['customer_address'],
                row['customer_phone'])
            # Load ID from database.
            neworder.id = int((row['id']))
            neworder.set_order_status(row['statuscode'])
            neworder.set_courier(row['courier'])
            neworder.set_items(row['items'])
            self.orders.append(neworder)
        print('LOADED PRODUCTS FROM DATABASE')

    def save_orders_database(self) -> None:
        """Saves order data to database."""
        self.database.save_orders(self.orders)

    # endregion

    def set_order_create(
            self, productmenu: Product_menu,
            couriermenu: Courier_menu) -> bool:
        """Asks for user input to create an order.

        Args:
            productmenu (Product_menu): Object.
            couriermenu (Courier_menu): Object.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, stop function.
        userinput_name = input('Input customer name: ')
        userinput_name = inputchecker.sanitise_input(userinput_name)
        if userinput_name.strip() == '':
            return False
        userinput_address = input('Input customer address: ')
        userinput_address = inputchecker.sanitise_input(userinput_address)
        if userinput_address.strip() == '':
            return False
        userinput_phone = input('Input customer phone number: ')
        userinput_phone = inputchecker.validate_phone(userinput_phone)
        if userinput_phone.strip() == '':
            return False
        # If the inputs are valid, add a new entry.
        new_order = Order(
            userinput_name, userinput_address, userinput_phone)
        # Adding courier
        userinput_courier = self.set_order_get_courier(couriermenu)
        if userinput_courier != 0:
            new_order.set_courier(userinput_courier)
        else:
            return False
        # Adding items
        itemstring = self.set_order_get_items(productmenu)
        if itemstring.strip() != '':
            new_order.set_items(itemstring)
        else:
            return False
        # If all inputs are valid, append the new entry.
        new_order.id = self.database.insert_order(new_order)
        self.orders.append(new_order)
        # Append to log.
        datalogger.log_create(f'Order: {new_order.customer_name}\'s order')
        return True

    def set_order_get_courier(self, couriermenu: Courier_menu) -> int:
        """Takes in user input and returns courier ID.

        Args:
            couriermenu (Courier_menu): Object.

        Returns:
            int: Integer of courier ID.
        """
        couriermenu.list_couriers()
        userinput_courier = input(
            'Input index of courier to assign to order: ')
        userinput_courier = inputchecker.get_courier_id(
            couriermenu.couriers, userinput_courier)
        return userinput_courier

    def set_order_get_items(self, productmenu: Product_menu) -> str:
        """Takes in user input and returns string of items to append to order.

        Args:
            productmenu (Product_menu): Object.

        Returns:
            str: String of item IDs.
        """
        productmenu.list_products()
        itemstring = ''
        while True:
            userinput_items = input(
                'Input index of product to assign to order'
                '(Valid input needs at least one product,'
                'blank input to exit): ')
            if userinput_items.strip() != '':
                itemstring += inputchecker.get_item_id(
                    productmenu.products, userinput_items)
                itemstring += ', '
                productmenu.list_products()
            else:
                itemstring = itemstring[:-2]
                break
        return itemstring

    # region <ORDER UPDATE FUNCTIONS>

    def set_order_update(self, index: int, productmenu: Product_menu,
                         couriermenu: Courier_menu,) -> None:
        """Asks for user input to update an order.

        Args:
            index (int): List index of the order to be updated.
            couriermenu (Courier_menu): Object.
            productmenu (Product_menu): Object.
        """
        print(f'Updating {self.orders[index].customer_name}\'s order')
        # If input is blank, continue but don't update the order.
        userinput = input('Input customer name: ')
        userinput = inputchecker.sanitise_input(userinput)
        if userinput.strip() != '':
            self.orders[index].customer_name = userinput
        userinput = input('Input customer address: ')
        userinput = inputchecker.sanitise_input(userinput)
        if userinput.strip() != '':
            self.orders[index].customer_address = userinput
        userinput = input('Input customer phone number: ')
        userinput = inputchecker.validate_phone(userinput)
        if userinput.strip() != '':
            self.orders[index].customer_phone = userinput

        userinput_courier = self.set_order_get_courier(couriermenu)
        if userinput_courier != 0:
            self.orders[index].set_courier(userinput_courier)

        itemstring = self.set_order_get_items(productmenu)
        if itemstring.strip() != '':
            self.orders[index].set_items(itemstring)

        self.database.update_order(self.orders[index])
        # Append to log.
        datalogger.log_update(
            f'Order: {self.orders[index].customer_name}\'s order')

    def set_order_update_status(self, index: int) -> None:
        """Asks for user input to update an order's status.

        Args:
            index (int): List index of the order to be updated.
        """
        print(f'Updating {self.orders[index].customer_name}\'s order')
        print("""
            0. Preparing
            1. Awaiting pickup
            2. Out for delivery
            3. Delivered
            """)
        new_status = input('Input number for order status: ')
        self.orders[index].set_order_status(new_status)
        self.database.update_order(self.orders[index])
        # Append to log.
        datalogger.log_update(
            f'Order: {self.orders[index].customer_name}\'s order')

    # endregion

    def set_order_remove(self, index: int) -> str:
        """Removes the order at the specified index of the list.

        Args:
            index (int): List index of the order to be removed.

        Returns:
            str: Customer name of the removed order. None if not
            removed.
        """
        removed_order = self.orders[index].customer_name
        self.database.remove_order(self.orders[index])
        self.orders.pop(index)
        # Append to log.
        datalogger.log_remove(
            f'Order: {removed_order}\'s order')
        return f'{removed_order}\'s order'
