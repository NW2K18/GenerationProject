"""Author: Nathan \n
This is the courier menu for the cafe application.
"""

from time import sleep
import csv

import courierclass


class Courier_menu():
    """Class used as the interface for handling couriers."""

    def __init__(self) -> None:
        """Initialise courier menu object and loads data."""
        # Initialise courier list.
        self.couriers = [courierclass.Courier('Larry', '9812734656')]

        self.load_couriers()

    def list_couriers(self) -> int:
        """Prints out courier list.

        Returns:
            int: Size of courier list
        """
        i = 1
        for courier in self.couriers:
            print(f"""Courier No.{i}:
            Courier name: {courier.name}
            Courier phone: {courier.phone}
            """)
            sleep(0.3)
            i += 1
        return len(self.couriers)

    # region <SAVE AND LOAD>

    def load_couriers(self) -> None:
        """Loads courier data from csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/courierdata.csv', 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                self.couriers.clear()
                for row in reader:
                    newcourier = courierclass.Courier(row['name'],
                                                      row['phone'])
                    self.couriers.append(newcourier)
            print('LOADED COURIERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

    def save_couriers(self) -> None:
        """Saves courier data to a csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/courierdata.csv', 'w', newline='') as file:
                fieldnames = ['name', 'phone']
                writer = csv.DictWriter(file, fieldnames)
                writer.writeheader()
                for courier in self.couriers:
                    writer.writerow(courier.get_courier())
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

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
        if userinput_phone.strip() == '':
            return False
        # If the inputs are valid, add a new entry.
        new_courier = courierclass.Courier(userinput_name, userinput_phone)
        self.couriers.append(new_courier)
        return True

    def set_courier_update(self, index: int) -> None:
        """Asks for user input to update an courier.

        Args:
            index (int): List index of the courier to be updated.
        """
        # If input is blank, continue but don't update the courier.
        userinput = input('Input courier name: ')
        if userinput.strip() != '':
            self.couriers[index].name = userinput
        userinput = input('Input courier phone number: ')
        if userinput.strip() != '':
            self.couriers[index].phone = userinput

    def set_courier_remove(self, index: int) -> str:
        """Removes the courier at the specified index of the list.

        Args:
            index (int): List index of the courier to be removed.

        Returns:
            str: Name of the removed courier.
        """
        removed_courier = self.couriers[index].name
        self.couriers.pop(index)
        return removed_courier

    # endregion
