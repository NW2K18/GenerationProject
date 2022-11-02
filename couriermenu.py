# Author: Nathan
# This is the courier menu for the cafe application.

import time
import input_checker

class Courier_menu():

    def __init__(self):
        # Initialise couriers
        self.couriers = ['Larry', 'Curly', 'Moe']

        # Debug stuff to check if it has loaded properly.
        print(self.couriers)
        self.load_couriers()
        print(self.couriers)


    # Prints out courier list.
    def list_couriers(self) -> bool:
        i = 1
        for courier in self.couriers:
            print(f'Courier No.{i} {courier}')
            time.sleep(0.3)
            i += 1
        return True


    # Load courier
    def load_couriers(self) -> bool:
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
            if courier == '': continue  # Does not add whitespace.
            self.couriers.append(courier)
        return True


    # Save couriers
    def save_couriers(self) -> bool:
        try:
            with open('data/courierdata.txt', 'w') as file:
                for courier in self.couriers:
                    file.write(f'{courier}\n')
        except Exception as e:
            print(f'there was a problem at writing to file. {e}')
            raise Exception  # Raise exception for debugging.
        return True


    # This is the couriers menu
    def view_couriers_menu(self) -> None:
        while True:
            print('''-----COURIERS-----
0. Exit
1. Add Courier
2. View Courier List
3. Update Courier
4. Remove Courier
---------------------''')
            option = input('Choose command: ')

            match option:
                case '0':  # Exit
                    print('Exiting couriers menu...')
                    time.sleep(1)
                    break
                case '1':  # Create Courier
                    self.couriers.append(input("Type in your courier name: "))
                case '2':  # View Courier List
                    print('Printing courier list...')
                    time.sleep(1)
                    self.list_couriers()
                    time.sleep(1)
                case '3':  # Update Courier
                    self.list_couriers()
                    index = input_checker.get_input_index('courier', 'update')
                    if (index + 1) == 0:
                        print('Selected 0, moving back to couriers menu.')
                        break
                    newname = input(f'Type what you wish'
                    f' to replace {self.couriers[index]} with: ')
                    print('Updating courier...')
                    time.sleep(1)
                    self.couriers[index] = newname
                    print('Updated courier.')
                case '4':  # Remove Courier
                    self.list_couriers()
                    index = input_checker.get_input_index('courier', 'remove')
                    if (index + 1) == 0:
                        print("Selected 0, moving back to couriers menu.")
                        break
                    print("Removing courier...")
                    time.sleep(1)
                    print(f"You have removed: {self.couriers.pop(index)}.")
                case _:  # Default case
                    print('No option selected.')
