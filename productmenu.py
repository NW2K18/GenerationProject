# Author: Nathan
# This is the product menu for the cafe application.

from time import sleep
import csv

import productclass


class Product_menu():
    """Class used as the interface for handling products."""
    def __init__(self) -> None:
        """Initialise product menu object and loads data."""
        # Initialise product list.
        self.products = [productclass.Product('Pepsi', 1.00)]

        self.load_products()

    def list_products(self) -> int:
        """Prints out product list.

        Returns:
            int: Size of product list
        """
        i = 1
        for product in self.products:
            print(f"""Product No.{i}:
            Product name: {product.name}
            Product price: {product.get_product_price()}
            """)
            sleep(0.3)
            i += 1
        return len(self.products)

    def load_products(self) -> None:
        """Loads product data from csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/productdata.csv', 'r') as file:
                self.products.clear()
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    newproduct = productclass.Product(row['name'],
                                                      float(row['price']))
                    self.products.append(newproduct)
            print('LOADED PRODUCTS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    def save_products(self) -> None:
        """Saves product data to a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/productdata.csv', 'w', newline='') as file:
                fieldnames = ['name', 'price']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for product in self.products:
                    writer.writerow(product.get_product())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

    def set_product_create(self) -> bool:
        """Asks for user input to create an product.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, stop function.
        userinput_name = input('Input product name: ')
        if userinput_name.strip() == '':
            return False
        try:
            userinput_price = float(input('Input product price: '))
            if userinput_price == 0:
                return False
        except ValueError:
            print('Input cannot be converted into a floating point number.')
            return False
        # If the inputs are valid, add a new entry.
        new_product = productclass.Product(userinput_name, userinput_price)
        self.products.append(new_product)
        return True

    def set_product_update(self, index: int) -> bool:
        """Asks for user input to update an product.

        Args:
            index (int): List index of the product to be updated.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, continue but don't update the product.
        userinput = input('Input product name: ')
        if userinput.strip() != '':
            self.products[index].name = userinput
        try:
            userinput = float(input('Input product price: '))
            if userinput.strip() != '':
                self.products[index].price = userinput
        except ValueError:
            print('Input cannot be converted into a floating point number.')
        return True
