"""Author: Nathan \n
This is the courier menu for the cafe application.
"""

from time import sleep
import csv
from typing import Union

import inputchecker
from courierclass import Courier
from database import Database


class Courier_menu():
    """Class used as the interface for handling couriers."""

    def __init__(self) -> None:
        """Initialise courier menu object and loads data."""
        # Initialise courier list.
        self.couriers = [Courier('Larry', '9812734656')]
        self.database = Database()

        # self.load_couriers_csv()
        self.load_couriers_database()

    def list_couriers(self) -> int:
        """Prints out courier list.

        Returns:
            int: Size of courier list
        """
        for courier in self.couriers:
            print(
                f'Courier No.{courier.id}:'
                f'\n\tCourier name: {courier.name}'
                f'\n\tCourier phone: {courier.phone}')
            sleep(0.3)
        return len(self.couriers)

    # region <SAVE AND LOAD>

    def load_couriers_csv(self) -> None:
        """Loads courier data from csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/courierdata.csv', 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                self.couriers.clear()
                for row in reader:
                    newcourier = Courier(
                        row['name'], row['phone'])
                    newcourier.id = self.database.load_courier_id(newcourier)
                    self.couriers.append(newcourier)
            print('LOADED COURIERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    def save_couriers_csv(self) -> None:
        """Saves courier data to a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/courierdata.csv', 'w', newline='') as file:
                fieldnames = ['id', 'name', 'phone']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for courier in self.couriers:
                    writer.writerow(courier.get_courier())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

    def load_couriers_database(self) -> None:
        """Loads courier data from database."""
        rows = self.database.load_couriers()
        self.couriers.clear()
        for row in rows:
            newcourier = Courier(
                row['name'], (row['phone']))
            newcourier.id = row['id']
            self.couriers.append(newcourier)
        print('LOADED COURIERS FROM DATABASE')

    def save_couriers_database(self) -> None:
        """Saves courier data to database."""
        self.database.save_couriers(self.couriers)

    # endregion
    # region <MODIFY COURIERS>

    def set_courier_create(self) -> bool:
        """Asks for user input to create an courier.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, stop function.
        userinput_name = input('Input courier name: ')
        if userinput_name.strip() == '':
            return False
        userinput_phone = input('Input courier phone number: ')
        userinput_phone = inputchecker.validate_phone(userinput_phone)
        if userinput_phone.strip() == '':
            return False
        # If the inputs are valid, add a new entry.
        new_courier = Courier(userinput_name, userinput_phone)
        new_courier.id = self.database.insert_courier(new_courier)
        self.couriers.append(new_courier)
        return True

    def set_courier_update(self, index: int) -> None:
        """Asks for user input to update an courier.

        Args:
            index (int): List index of the courier to be updated.
        """
        print(f'Updating {self.couriers[index].name}')
        # If input is blank, continue but don't update the courier.
        userinput = input('Input courier name: ')
        if userinput.strip() != '':
            self.couriers[index].name = userinput
        userinput = input('Input courier phone number: ')
        userinput = inputchecker.validate_phone(userinput)
        if userinput.strip() != '':
            self.couriers[index].phone = userinput
        self.database.update_courier(self.couriers[index])

    def set_courier_remove(self, index: int) -> str:
        """Removes the courier at the specified index of the list.

        Args:
            index (int): List index of the courier to be removed.

        Returns:
            str: Name of the removed product.
        """
        removed_courier_name = self.couriers[index].name
        self.database.remove_courier(self.couriers[index])
        self.couriers.pop(index)
        return removed_courier_name

    # endregion
