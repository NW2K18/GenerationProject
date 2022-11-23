"""Author: Nathan \n
This is the product menu for the cafe application.
"""

from time import sleep
import csv

import datalogger
import inputchecker
from productclass import Product
from database import Database


class Product_menu():
    """Class used as the interface for handling products."""

    def __init__(self) -> None:
        """Initialise product menu object and loads data."""
        # Initialise product list.
        self.products = [Product('Pepsi', 1.00)]
        self.database = Database()

        # self.load_products_csv()
        self.load_products_database()

    def list_products(self) -> int:
        """Prints out product list.

        Returns:
            int: Size of product list
        """
        for product in self.products:
            print(
                f'Product No.{product.id}:'
                f'\n\tProduct name: {product.name}'
                f'\n\tProduct price: {product.get_product_price()}')
            sleep(0.3)
        return len(self.products)

    # region <SAVE AND LOAD>

    def load_products_csv(self) -> None:
        """Loads product data from csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/productdata.csv', 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                self.products.clear()
                for row in reader:
                    newproduct = Product(row['name'],
                                         float(row['price']))
                    newproduct.id = self.database.load_product_id(newproduct)
                    self.products.append(newproduct)
            print('LOADED PRODUCTS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    def save_products_csv(self) -> None:
        """Saves product data to a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/productdata.csv', 'w', newline='') as file:
                fieldnames = ['id', 'name', 'price']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for product in self.products:
                    writer.writerow(product.get_product())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.
        print('EXPORTED PRODUCTS SUCCESSFULLY')

    def load_products_database(self) -> None:
        """Loads product data from database."""
        rows = self.database.load_products()
        self.products.clear()
        for row in rows:
            newproduct = Product(
                row['name'], float(row['price']))
            newproduct.id = row['id']
            self.products.append(newproduct)
        print('LOADED PRODUCTS FROM DATABASE')

    def save_products_database(self) -> None:
        """Saves product data to database."""
        self.database.save_products(self.products)

    # endregion
    # region <MODIFY PRODUCTS>

    def set_product_create(self) -> bool:
        """Asks for user input to create an product.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, stop function.
        userinput_name = input('Input product name: ')
        userinput_name = inputchecker.sanitise_input(userinput_name)
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
        new_product = Product(userinput_name, userinput_price)
        new_product.id = self.database.insert_product(new_product)
        self.products.append(new_product)
        # Append to log.
        datalogger.log_create(f'Product: {new_product.name}')
        return True

    def set_product_update(self, index: int) -> None:
        """Asks for user input to update an product.

        Args:
            index (int): List index of the product to be updated.
        """
        print(f'Updating {self.products[index].name}')
        # If input is blank, continue but don't update the product.
        userinput = input('Input product name: ')
        userinput = inputchecker.sanitise_input(userinput)
        if userinput.strip() != '':
            self.products[index].name = userinput
        try:
            userinput = input('Input product price: ')
            if userinput.strip() != '':
                self.products[index].price = float(userinput)
        except ValueError:
            print('Input cannot be converted into a floating point number.')
        self.database.update_product(self.products[index])
        # Append to log.
        datalogger.log_update(f'Product: {self.products[index].name}')

    def set_product_remove(self, index: int) -> str:
        """Removes the product at the specified index of the list.

        Args:
            index (int): List index of the product to be removed.

        Returns:
            str: Name of the removed product.
        """
        removed_product_name = self.products[index].name
        self.database.remove_product(self.products[index])
        self.products.pop(index)
        # Append to log.
        datalogger.log_remove(f'Product: {removed_product_name}')
        return removed_product_name

    # endregion
