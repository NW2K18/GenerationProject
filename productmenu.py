# Author: Nathan
# This is the product menu for the cafe application.

import time
import input_checker

class Product_menu():
    
    def __init__(self):
        # Initialise the product list, has values already in.
        self.products = ['Pepsi', 'Coca Cola', 'Dr Pepper']

        # Debug stuff to check if it has loaded properly.
        print(self.products)
        self.load_products()
        print(self.products)


    # Prints out product list.
    def list_products(self) -> bool:
        i = 1
        for product in self.products:
            print(f'Product No.{i} {product}')
            time.sleep(0.3)
            i += 1
        return True


    # Load products
    def load_products(self) -> bool:
        productstring = ''
        try:
            with open('productdata.txt', 'r') as file:
                productstring = file.read()
                print('LOADED PRODUCTS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

        self.products.clear()
        for product in productstring.split('\n'):
            if product == '': continue  # Does not add whitespace.
            self.products.append(product)
        return True


    # Save products
    def save_products(self) -> bool:
        try:
            with open('productdata.txt', 'w') as file:
                for product in self.products:
                    file.write(f'{product}\n')
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.
        return True


    # This is the products menu
    def view_products_menu(self) -> None:
        while True:
            print('''-----PRODUCTS-----
        0. Exit
        1. Create Product
        2. View Product List
        3. Update Product
        4. Remove Product
    ---------------------''')
            option = input('Choose command: ')

            match option:
                case '0':  # Exit
                    print('Exiting products menu...')
                    time.sleep(1)
                    break
                case '1':  # Create
                    product = input('Type in your product name: ')
                    if product.strip() != '': 
                        self.products.append(product)
                    else:
                        print('No product name entered.')
                case '2':  # View
                    print('Printing product list...')
                    time.sleep(1)
                    self.list_products()
                    time.sleep(1)
                case '3':  # Update
                    self.list_products()
                    index = input_checker.get_input_index('product', 'update')
                    if (index + 1) == 0:
                        print('Selected 0, moving back to products menu.')
                        break
                    newname = input(f'Type what you wish'
                    f' to replace {self.products[index]} with: ')
                    if newname.strip() != '':
                        print('Updating product...')
                        time.sleep(1)
                        self.products[index] = newname
                        print('Updated product.')
                    else:
                        print('No product name entered.')
                case '4':  # Remove
                    self.list_products()
                    index = input_checker.get_input_index('product', 'remove')
                    if (index + 1) == 0:
                        print('Selected 0, moving back to products menu.')
                        break
                    print('Removing product...')
                    time.sleep(1)
                    print(f'You have removed: {self.products.pop(index)}.')
                case _:  # Default
                    print('No option selected.')
