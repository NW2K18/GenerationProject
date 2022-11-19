"""Author: Nathan \n
This is the order menu for the cafe application.
"""

from time import sleep
import csv
from typing import List, Union

from orderclass import Order
from productmenu import Product_menu
from couriermenu import Courier_menu
import inputchecker


class Order_menu():
    """Class used as the interface for handling orders."""

    def __init__(self) -> None:
        """Initialise order menu object and loads data."""
        # List of orders with a sample order.
        self.orders = [Order(
            'John', 'Planet Earth', '1439280432')]
        self.load_orders()

    def list_orders(self, orderlist: List[Order]) -> int:
        """Prints out order list.

        Args:
            orderlist (List[Order]): List of orders to be listed.

        Returns:
            int: Size of order list
        """
        i = 1
        for order in orderlist:
            print(
                f'Order No.{i} ({order.id}):'
                f'\n\tCustomer name: {order.customer_name}'
                f'\n\tCustomer address: {order.customer_address}'
                f'\n\tCustomer phone number: {order.customer_phone}'
                f'\n\tCourier: {order.get_courier()} - COURIER HERE'
                f'\n\tOrder status: {order.status}'
                f'\n\tItems: {order.get_items()}')
            sleep(0.5)
            i += 1
        return len(self.orders)

    def list_sorted_orders(self, option: str) -> int:
        """Prints a list sorted through the specified option

        Args:
            option (str): courier, status

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
        self.list_orders(sorted_list)
        return len(self.orders)

    # region <SAVE AND LOAD>

    def load_orders(self) -> None:
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
                    neworder.status = row['status']
                    neworder.set_courier(row['courier'])
                    neworder.set_items(row['items'])
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
                fieldnames = [
                    'id', 'customer_name', 'customer_address',
                    'customer_phone', 'courier',
                    'status', 'items']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for order in self.orders:
                    writer.writerow(order.get_order())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

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
        if userinput_name.strip() == '':
            return False
        userinput_address = input('Input customer address: ')
        if userinput_address.strip() == '':
            return False
        userinput_phone = input('Input customer phone number: ')
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
        self.orders.append(new_order)
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
                itemstring += ','
                productmenu.list_products()
            else:
                itemstring = itemstring[:-1]
                break
        return itemstring

    # region <ORDER UPDATE FUNCTIONS>

    def set_order_update(self, index: int, productmenu: Product_menu,
                         couriermenu: Courier_menu,) -> bool:
        """Asks for user input to update an order.

        Args:
            index (int): List index of the order to be updated.
            couriermenu (Courier_menu): Object.
            productmenu (Product_menu): Object.

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

        userinput_courier = self.set_order_get_courier(couriermenu)
        if userinput_courier != 0:
            self.orders[index].set_courier(userinput_courier)

        itemstring = self.set_order_get_items(productmenu)
        if itemstring.strip() != '':
            self.orders[index].set_items(itemstring)
        return True

    def set_order_update_status(self, index: int) -> None:
        """Asks for user input to update an order's status.

        Args:
            index (int): List index of the order to be updated.
        """
        print("""
            0. Preparing
            1. Awaiting pickup
            2. Out for delivery
            3. Delivered
            """)
        new_status = input('Input number for order status: ')
        self.orders[index].set_order_status(new_status)

    # endregion

    def set_order_remove(self, index: int) -> Union[str, None]:
        """Asks the user to confirm their choice, then removes the order at
        the specified index of the list.

        Args:
            index (int): List index of the order to be removed.

        Returns:
            Union[str, None]: Customer name of the removed order. None if not
            removed.
        """
        removed_order = self.orders[index].customer_name
        option = input(
            f'Do you really wish to remove {removed_order}\'s order? (y/n): ')
        if option == 'y':
            self.orders.pop(index)
            return f'{removed_order}\'s order'
        return None
