"""Author: Nathan \n
This is the main module of the cafe program and contains the menus.
"""

from time import sleep

from productmenu import Product_menu
from couriermenu import Courier_menu
from ordermenu import Order_menu
import inputchecker


class Menu():

    def __init__(self) -> None:
        """Initialise main menu."""
        self.products = Product_menu()
        self.couriers = Courier_menu()
        self.orders = Order_menu()

    # region <MAIN MENU>

    def main(self) -> None:
        """This contains the main menu loop."""

        while True:
            print(
                '-----MAIN MENU-----\n\t'
                '0. Exit\n\t'
                '1. Products\n\t'
                '2. Couriers\n\t'
                '3. Orders\n\t'
                '4. Export csv file\n\t'
                '5. Import csv file\n'
                '-------------------')

            option = input('Choose command: ')
            match option:
                case '0':  # Exit
                    print('Exiting program.')
                    break
                case '1':  # Products
                    print('Entering products menu...')
                    sleep(1)
                    self.view_products_menu()
                case '2':  # Couriers
                    print('Entering couriers menu...')
                    sleep(1)
                    self.view_couriers_menu()
                case '3':  # Orders
                    print('Entering orders menu...')
                    sleep(1)
                    self.view_orders_menu()
                case '4':  # Export
                    sleep(1)
                    option = input('Are you sure you wish to export? (y/n): ')
                    if option == 'y':
                        self.products.save_products_csv()
                        self.couriers.save_couriers_csv()
                        self.orders.save_orders()
                case '5':  # Import
                    sleep(1)
                    option = input('Are you sure you wish to import? (y/n): ')
                    if option == 'y':
                        self.products.load_products_csv()
                        self.couriers.load_couriers_csv()
                        self.orders.load_orders()
                case _:  # Default
                    print('No option selected.')
        # End of loop, save data.
        self.products.save_products_database()
        self.couriers.save_couriers_database()
        self.orders.save_orders_database()
        print('Exited!')

    # endregion
    # region <PRODUCTS MENU>

    def view_products_menu(self) -> None:
        """This contains the product menu loop."""
        while True:
            print(
                '-----PRODUCTS-----\n\t'
                '0. Exit\n\t'
                '1. Create Product\n\t'
                '2. View Product List\n\t'
                '3. Update Product\n\t'
                '4. Remove Product\n'
                '---------------------')

            option = input('Choose command: ')

            match option:
                case '0':  # Exit
                    print('Exitting products menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    if self.products.set_product_create():
                        sleep(1)
                        print('Created a new product.')
                    else:
                        sleep(1)
                        print('Did not create a new product.')
                case '2':  # View
                    print('Printing product list...')
                    sleep(1)
                    self.products.list_products()
                    sleep(1)
                case '3':  # Update
                    self.products.list_products()
                    index = inputchecker.get_input_index(
                        'product', 'update', self.products.products)
                    if index is None:
                        print('Selected 0, moving back to product menu.')
                        break
                    self.products.set_product_update(index)
                    sleep(1)
                    print('Updated product.')
                case '4':  # Remove
                    self.products.list_products()
                    index = inputchecker.get_input_index(
                        'product', 'remove', self.products.products)
                    if index is None:
                        print('Selected 0, moving back to product menu.')
                        break
                    sleep(1)
                    option = input(
                        'Do you really wish to remove '
                        f'{self.products.products[index].name}? (y/n): ')
                    if option == 'y':
                        print(f'You have removed: \
                            {self.products.set_product_remove(index)}')
                case _:  # Default
                    print('No option selected.')

    # endregion
    # region <COURIER MENU>

    def view_couriers_menu(self) -> None:
        """This contains the courier menu loop."""
        while True:
            print(
                '-----COURIERS-----\n\t'
                '0. Exit\n\t'
                '1. Add Courier\n\t'
                '2. View Courier List\n\t'
                '3. Update Courier\n\t'
                '4. Remove Courier\n'
                '---------------------')
            option = input('Choose command: ')

            match option:
                case '0':  # Exit
                    print('Exitting couriers menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    if self.couriers.set_courier_create():
                        sleep(1)
                        print('Created a new courier.')
                    else:
                        sleep(1)
                        print('Did not create a new courier.')
                case '2':  # View
                    print('Printing courier list...')
                    sleep(1)
                    self.couriers.list_couriers()
                    sleep(1)
                case '3':  # Update
                    self.couriers.list_couriers()
                    index = inputchecker.get_input_index(
                        'courier', 'update', self.couriers.couriers)
                    if index is None:
                        print('Selected 0, moving back to courier menu.')
                        break
                    self.couriers.set_courier_update(index)
                    sleep(1)
                    print('Updated courier.')
                case '4':  # Remove
                    self.couriers.list_couriers()
                    index = inputchecker.get_input_index(
                        'courier', 'remove', self.couriers.couriers)
                    if index is None:
                        print('Selected 0, moving back to courier menu.')
                        break
                    sleep(1)
                    option = input(
                        'Do you really wish to remove '
                        f'{self.couriers.couriers[index].name}? (y/n): ')
                    if option == 'y':
                        print(f'You have removed: \
                            {self.couriers.set_courier_remove(index)}')
                case _:  # Default case
                    print('No option selected.')

    # endregion
    # region <ORDER MENU>

    def view_orders_menu(self):
        """This contains the order menu loop."""
        while True:
            print(
                '-----ORDERS-----\n\t'
                '0. Exit\n\t'
                '1. Create an order\n\t'
                '2. View Order List\n\t'
                '3. Update an order\'s status\n\t'
                '4. Update an order\n\t'
                '5. Remove an order\n'
                '---------------------')
            option = input('Choose command: ')
            match option:
                case '0':  # Exit
                    print('Exitting orders menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    if self.orders.set_order_create(
                            self.products, self.couriers):
                        sleep(1)
                        print('Created a new order.')
                    else:
                        sleep(1)
                        print('Did not create a new order.')
                case "2":  # View
                    print(
                        '\t0. Normal'
                        '\n\t1. Sort by courier'
                        '\n\t2. Sort by status')
                    option = input('Input choice for sorting through orders. ')
                    match option:
                        case '0':  # Normal
                            self.orders.list_orders(
                                self.orders.orders, self.products.products,
                                self.couriers.couriers)
                        case '1':  # Courier sort
                            self.orders.list_sorted_orders(
                                'courier', self.products.products,
                                self.couriers.couriers)
                        case '2':  # Status sort
                            self.orders.list_sorted_orders(
                                'status', self.products.products,
                                self.couriers.couriers)
                        case _:
                            print('Invalid input.')
                    sleep(1)
                case '3':  # Update status
                    self.orders.list_orders(
                        self.orders.orders, self.products.products,
                        self.couriers.couriers)
                    index = inputchecker.get_input_index(
                        'order', 'update', self.orders.orders)
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    self.orders.set_order_update_status(index)
                    sleep(1)
                    print('Updated order.')
                case '4':  # Update
                    self.orders.list_orders(
                        self.orders.orders, self.products.products,
                        self.couriers.couriers)
                    index = inputchecker.get_input_index(
                        'order', 'update', self.orders.orders)
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    self.orders.set_order_update(
                        index, self.products, self.couriers)
                    sleep(1)
                    print('Updated order.')
                case '5':  # Remove
                    self.orders.list_orders(
                        self.orders.orders, self.products.products,
                        self.couriers.couriers)
                    index = inputchecker.get_input_index(
                        'order', 'remove', self.orders.orders)
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    sleep(1)
                    option = input(
                        'Do you really wish to remove '
                        f'{self.orders.orders[index].customer_name}\'s order? '
                        '(y/n): ')
                    if option == 'y':
                        print(f'You have removed: \
                            {self.orders.set_order_remove(index)}')
                case _:  # Default
                    print('No option selected.')

    # endregion


# Call main function
if __name__ == '__main__':
    Menu().main()
