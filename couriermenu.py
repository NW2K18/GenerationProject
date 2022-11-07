# Author: Nathan
# This is the courier menu for the cafe application.

from time import sleep
import csv

import input_checker
import courierclass


class Courier_menu():
    """Class used as the interface for handling couriers."""
    def __init__(self) -> None:
        """Initialise courier menu object and loads data."""
        # Initialise courier list.
        self.couriers = [courierclass.Courier('Larry', '9812734656')]

        # Debug stuff to check if it has loaded properly.
        print(self.couriers)
        self.load_couriers()
        print(self.couriers)

    def list_couriers(self) -> None:
        """Prints out courier list."""
        i = 1
        for courier in self.couriers:
            print(f"""Courier No.{i}:
            Courier name: {courier.name}
            Courier phone: {courier.phone}
            """)
            sleep(0.3)
            i += 1

    def load_couriers(self) -> None:
        """Loads courier data from csv file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/courierdata.csv', 'r') as file:
                self.couriers.clear()
                reader = csv.DictReader(file, delimiter=',')
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

    def set_courier_update(self, index: int) -> bool:
        """Asks for user input to update an courier.

        Args:
            index (int): List index of the courier to be updated.

        Returns:
            bool: True if function successful, False if not.
        """
        # If input is blank, continue but don't update the courier.
        userinput = input('Input courier name: ')
        if userinput.strip() != '':
            self.couriers[index].name = userinput
        userinput = input('Input courier phone number: ')
        if userinput.strip() != '':
            self.couriers[index].phone = userinput
        return True

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
                    print('Exiting couriers menu...')
                    sleep(1)
                    break
                case '1':  # Create
                    if self.set_courier_create():
                        sleep(1)
                        print('Created a new courier.')
                    else:
                        sleep(1)
                        print('Did not create a new courier.')
                case '2':  # View
                    print('Printing courier list...')
                    sleep(1)
                    self.list_couriers()
                    sleep(1)
                case '3':  # Update
                    self.list_couriers()
                    index = input_checker.get_input_index('courier', 'update',
                                                          self.couriers)
                    if index is None:
                        print('Selected 0, moving back to courier menu.')
                        break
                    self.set_courier_update(index)
                    sleep(1)
                    print('Updated courier.')
                case '4':  # Remove
                    self.list_couriers()
                    index = input_checker.get_input_index('courier', 'remove',
                                                          self.couriers)
                    if index is None:
                        print('Selected 0, moving back to courier menu.')
                        break
                    print('Removing courier...')
                    sleep(1)
                    print(f'You have removed: {self.couriers.pop(index)}.')
                case _:  # Default case
                    print('No option selected.')
