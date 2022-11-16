"""Author: Nathan \n
This is the main module of the cafe program and contains the menus.
"""

from time import sleep

import productmenu
import couriermenu
import ordermenu
import inputchecker

from productclass import Product


class Menu():

    def __init__(self) -> None:
        """Initialise main menu."""
        self.products = productmenu.Product_menu()
        self.orders = ordermenu.Order_menu()
        self.couriers = couriermenu.Courier_menu()

    # region <MAIN MENU>

    def main(self) -> None:
        """This contains the main menu loop."""

        while True:
            print("""-----MAIN MENU-----
            0. Exit
            1. Products
            2. Couriers
            3. Orders
-------------------""")

            # self.products.load_products_database()
            # testproduct = Product('Water', 1.00)
            # testproduct = self.products.database.load_product_id(testproduct)
            # print(testproduct.id)

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
                case _:  # Default
                    print('No option selected.')
        # End of loop, save data.
        self.products.save_products()
        self.orders.save_orders()
        self.couriers.save_couriers()
        print('Exitted!')

    # endregion
    # region <PRODUCTS MENU>

    def view_products_menu(self) -> None:
        """This contains the product menu loop."""
        while True:
            print("""-----PRODUCTS-----
        0. Exit
        1. Create Product
        2. View Product List
        3. Update Product
        4. Remove Product
---------------------""")

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
                        'product', 'update', len(self.products.products))
                    if index is None:
                        print('Selected 0, moving back to product menu.')
                        break
                    self.products.set_product_update(index)
                    sleep(1)
                    print('Updated product.')
                case '4':  # Remove
                    self.products.list_products()
                    index = inputchecker.get_input_index(
                        'product', 'remove', len(self.products.products))
                    if index is None:
                        print('Selected 0, moving back to product menu.')
                        break
                    sleep(1)
                    print(f'You have removed: \
                        {self.products.set_product_remove(index)}')
                case _:  # Default
                    print('No option selected.')

    # endregion
    # region <COURIER MENU>

    def view_couriers_menu(self) -> None:
        """This contains the courier menu loop."""
        while True:
            print("""-----COURIERS-----
        0. Exit
        1. Add Courier
        2. View Courier List
        3. Update Courier
        4. Remove Courier
---------------------""")
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
                        'courier', 'update', len(self.couriers.couriers))
                    if index is None:
                        print('Selected 0, moving back to courier menu.')
                        break
                    self.couriers.set_courier_update(index)
                    sleep(1)
                    print('Updated courier.')
                case '4':  # Remove
                    self.couriers.list_couriers()
                    index = inputchecker.get_input_index(
                        'courier', 'remove', len(self.couriers.couriers))
                    if index is None:
                        print('Selected 0, moving back to courier menu.')
                        break
                    sleep(1)
                    print(f'You have removed: \
                        {self.couriers.set_courier_remove(index)}')
                case _:  # Default case
                    print('No option selected.')

    # endregion
    # region <ORDER MENU>

    def view_orders_menu(self):
        """This contains the order menu loop."""
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
                    print('Exitting orders menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    if self.orders.set_order_create(
                        self.couriers.list_couriers,
                        self.products.list_products
                    ):
                        sleep(1)
                        print('Created a new order.')
                    else:
                        sleep(1)
                        print('Did not create a new order.')
                case "2":  # View
                    print("""
            0. Normal
            1. Sort by courier
            2. Sort by status
""")
                    option = input('Input number for order status: ')
                    match option:
                        case '0':  # Normal
                            self.orders.list_orders()
                        case '1':  # Courier sort
                            self.orders.list_sorted_orders('courier')
                        case '2':  # Status sort
                            self.orders.list_sorted_orders('status')
                        case _:
                            print('Invalid input.')
                    sleep(1)
                case '3':  # Update status
                    self.orders.list_orders()
                    index = inputchecker.get_input_index(
                        'order', 'update', len(self.orders.orders))
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    self.orders.set_order_update_status(index)
                    sleep(1)
                    print('Updated order.')
                case '4':  # Update
                    self.orders.list_orders()
                    index = inputchecker.get_input_index(
                        'order', 'update', len(self.orders.orders))
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    self.orders.set_order_update(
                        index, self.couriers.list_couriers,
                        self.products.list_products)
                    sleep(1)
                    print('Updated order.')
                case '5':  # Remove
                    self.orders.list_orders()
                    index = inputchecker.get_input_index(
                        'order', 'remove', len(self.orders.orders))
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    sleep(1)
                    print(f'You have removed: \
                        {self.orders.set_order_remove(index)}')
                case _:  # Default
                    print('No option selected.')

# endregion


# Call main function
if __name__ == '__main__':
    Menu().main()
