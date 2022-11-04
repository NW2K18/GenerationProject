# Author: Nathan
# This is the product menu for the cafe application.

from time import sleep

import input_checker


class Product_menu():
    """Class used as the interface for handling products."""
    def __init__(self) -> None:
        """Initialise product menu object and loads data."""
        # Initialise some generic products.
        self.products = ['Pepsi', 'Coca Cola', 'Dr Pepper']

        # Debug stuff to check if it has loaded properly.
        print(self.products)
        self.load_products()
        print(self.products)

    def list_products(self) -> None:
        """Prints out product list."""
        i = 1
        for product in self.products:
            print(f'Product No.{i} {product}')
            sleep(0.3)
            i += 1

    def load_products(self) -> None:
        """Loads product data from text file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        productstring = ''
        try:
            with open('data/productdata.txt', 'r') as file:
                productstring = file.read()
                print('LOADED PRODUCTS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

        self.products.clear()
        for product in productstring.split('\n'):
            if product == '':
                continue  # Does not add whitespace.
            self.products.append(product)

    def save_products(self) -> None:
        """Saves product data to a text file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/productdata.txt', 'w') as file:
                for product in self.products:
                    file.write(f'{product}\n')
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

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
                    print('Exiting products menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    product = input('Type in your product name: ')
                    if product.strip() != '':
                        self.products.append(product)
                    else:
                        print('No product name entered.')
                case '2':  # View
                    print('Printing product list...')
                    sleep(1)
                    self.list_products()
                    sleep(1)
                case '3':  # Update
                    self.list_products()
                    index = input_checker.get_input_index('product', 'remove',
                                                          self.products)
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    newname = input(f'Type what you wish to replace '
                                    f'{self.products[index]} with: ')
                    if newname.strip() != '':
                        print('Updating product...')
                        sleep(1)
                        self.products[index] = newname
                        print('Updated product.')
                    else:
                        print('No product name entered.')
                case '4':  # Remove
                    self.list_products()
                    index = input_checker.get_input_index('product', 'remove',
                                                          self.products)
                    if index is None:
                        print('Selected 0, moving back to order menu.')
                        break
                    print('Removing product...')
                    sleep(1)
                    print(f'You have removed: {self.products.pop(index)}.')
                case _:  # Default
                    print('No option selected.')
