# Author: Nathan
# This is the order menu for the cafe application.

from time import sleep
import csv
# import json

import input_checker


class Order_menu():
    """Class used as the interface for handling orders.
    """
    def __init__(self) -> None:
        """Initialise order menu object and loads data.
        """
        # List of orders
        self.orders = []
        # Sample order
        self.orders.append({
            'customer_name': 'John',
            'customer_address': 'Planet Earth',
            'customer_phone': '1439280432',
            'status': 'Preparing'
        })
        # Debug stuff to check if it has loaded properly.
        print(self.orders)
        self.load_orders_csv()
        print(self.orders)

    def list_orders(self) -> None:
        """Prints out order list.
        """
        i = 1
        for order in self.orders:
            print(f"""Order No.{i}:
            Customer name: {order['customer_name']}
            Customer address: {order['customer_address']}
            Customer phone number: {order['customer_phone']}
            Order status: {order['status']}
            """)
            sleep(0.5)
            i += 1

    def load_orders(self) -> None:
        """Loads orders from a text file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        fullorderstring = ''
        try:
            with open('data/orderdata.txt', 'r') as file:
                fullorderstring = file.read()
                print('LOADED ORDERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.
        self.orders.clear()
        index = 0
        for orderstring in fullorderstring.split('\n\n'):
            # If blank, do not add this to orders.
            if orderstring == '' or orderstring == '\n':
                continue
            self.orders.append({})
            for order in orderstring.split('\n'):
                if order == '':
                    continue
                suborder = order.split(' ', 1)
                self.orders[index][suborder[0]] = suborder[1]
            index += 1

    def load_orders_csv(self) -> None:
        """Loads orders from a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """        
        try:
            with open('data/orderdata.csv', 'r') as file:
                self.orders.clear()
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    self.orders.append(row)
            print('LOADED ORDERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    # Save orders
    def save_orders(self) -> None:
        """Saves order data to a text file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/orderdata.txt', 'w') as file:
                for order in self.orders:
                    for key in order:
                        file.write(f'{key} {order[key]}\n')
                    file.write('\n')
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

    # Save a csv file for orders
    def save_orders_csv(self) -> None:
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
                    writer.writerow(order)
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

    # Create an order
    def set_order_create(self) -> bool:
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
        index = len(self.orders)  # Index of the new dictionary object
        self.orders.append({})  # Add the new dictionary
        self.orders[index]['customer_name'] = userinput_name
        self.orders[index]['customer_address'] = userinput_address
        self.orders[index]['customer_phone'] = userinput_phone
        self.orders[index]['status'] = 'Preparing'
        return True

    # Update an order
    def set_order_update(self, index: int) -> bool:
        # If input is blank, continue but don't update the order.
        userinput = input('Input customer name: ')
        if userinput.strip() != '':
            self.orders[index]['customer_name'] = userinput
        userinput = input('Input customer address: ')
        if userinput.strip() != '':
            self.orders[index]['customer_address'] = userinput
        userinput = input('Input customer phone number: ')
        if userinput.strip() != '':
            self.orders[index]['customer_phone'] = userinput
        return True

    # Update an order's status
    def set_order_update_status(self, index: int) -> bool:
        print("""
            0. Preparing
            1. Awaiting pickup
            2. Out for delivery
            3. Delivered
    """)
        match input('Input number for order status: '):
            case '0':  # Preparing
                self.orders[index]['status'] = 'Preparing'
            case '1':  # Awaiting pickup
                self.orders[index]['status'] = 'Awaiting pickup'
            case '2':  # Out for delivery
                self.orders[index]['status'] = 'Out for delivery'
            case '3':  # Delivered
                self.orders[index]['status'] = 'Delivered'
            case _:  # Invalid input
                print('Invalid update status entered, status unchanged.')
                return False
        return True

    # This is the orders menu
    def view_orders_menu(self):
        while True:
            print("""-----ORDERS-----
0. Exit
1. Create an order
2. View Order List
3. Update an order's status
4. Update an order
5. Remove an order
---------------------""")
            option = input('Choose command: ')
            match option:
                case '0':  # Exit
                    print('Exiting orders menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    if self.set_order_create():
                        sleep(1)
                        print('Created a new order.')
                    else:
                        sleep(1)
                        print('Did not create a new order.')
                case "2":  # View
                    print('Printing order list...')
                    self.list_orders()
                    sleep(1)
                case '3':  # Update status
                    self.list_orders()
                    index = input_checker.get_input_index('order', 'update')
                    if (index + 1) == 0:
                        print('Selected 0, moving back to order menu.')
                        break
                    self.set_order_update_status(index)
                    print('Updating order...')
                    sleep(1)
                    print('Updated order.')
                case '4':  # Update
                    self.list_orders()
                    index = input_checker.get_input_index('order', 'update')
                    if (index + 1) == 0:
                        print('Selected 0, moving back to order menu.')
                        break
                    self.set_order_update(index)
                    sleep(1)
                    print('Updated order.')
                case '5':  # Remove
                    self.list_orders()
                    index = input_checker.get_input_index('order', 'remove')
                    if (index + 1) == 0:
                        print('Selected 0, moving back to order menu.')
                        break
                    print('Removing order...')
                    sleep(1)
                    print(f'You have removed: {self.orders.pop(index)}.')
                case _:  # Default
                    print('No option selected.')
