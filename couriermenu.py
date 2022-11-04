# Author: Nathan
# This is the courier menu for the cafe application.

from time import sleep

import input_checker


class Courier_menu():
    """Class used as the interface for handling couriers."""
    def __init__(self) -> None:
        """Initialise courier menu object and loads data."""
        # Initialise some generic couriers.
        self.couriers = ['Larry', 'Curly', 'Moe']

        # Debug stuff to check if it has loaded properly.
        print(self.couriers)
        self.load_couriers()
        print(self.couriers)

    def list_couriers(self) -> None:
        """Prints out courier list."""
        i = 1
        for courier in self.couriers:
            print(f'Courier No.{i} {courier}')
            sleep(0.3)
            i += 1

    def load_couriers(self) -> None:
        """Loads courier data from text file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        courierstring = ''
        try:
            with open('data/courierdata.txt', 'r') as file:
                courierstring = file.read()
                print('LOADED COURIERS SUCCESSFULLY')
        except Exception as e:
            print(f'THERE WAS AN ISSUE: {e}')
            raise Exception  # Raise exception for debugging.

        self.couriers.clear()
        for courier in courierstring.split('\n'):
            if courier == '':
                continue  # Does not add whitespace.
            self.couriers.append(courier)

    def save_couriers(self) -> None:
        """Saves courier data to a text file.

        Raises:
            Exception: Exception related to not finding a file.
        """
        try:
            with open('data/courierdata.txt', 'w') as file:
                for courier in self.couriers:
                    file.write(f'{courier}\n')
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.

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
                    courier = input('Type in your courier name: ')
                    if courier.strip() != '':
                        self.couriers.append(courier)
                    else:
                        print('No courier name entered.')
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
                    newname = input(f'Type what you wish to replace '
                                    f'{self.couriers[index]} with: ')
                    if newname.strip() != '':
                        print('Updating courier...')
                        sleep(1)
                        self.couriers[index] = newname
                        print('Updated courier.')
                    else:
                        print('No courier name entered.')
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
