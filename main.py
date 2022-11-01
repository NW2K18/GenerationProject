# Author: Nathan
# This is the main program of the cafe program.

import time
import input_checker
import productmenu
import ordermenu

# Right now couriers are basically the same as products but I don't 
# update the code as much so there will be redundancies.
couriers = ['Larry', 'Curly', 'Moe']

# Prints out courier list.
def list_couriers() -> bool:
    i = 1
    for courier in couriers:
        print(f'Courier No.{i} {courier}')
        time.sleep(0.3)
        i += 1
    return True   


# This is the couriers menu
def view_couriers_menu() -> None:
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
                couriers.append(input("Type in your courier name: "))
            case '2':  # View Courier List
                print('Printing courier list...')
                time.sleep(1)
                list_couriers()
                time.sleep(1)
            case '3':  # Update Courier
                list_couriers()
                index = input_checker.get_input_index('courier', 'update')
                if (index + 1) == 0:
                    print('Selected 0, moving back to couriers menu.')
                    break
                newname = input(f'Type what you wish'
                f' to replace {couriers[index]} with: ')
                print('Updating courier...')
                time.sleep(1)
                couriers[index] = newname
                print('Updated courier.')
            case '4':  # Remove Courier
                list_couriers()
                index = input_checker.get_input_index('courier', 'remove')
                if (index + 1) == 0:
                    print("Selected 0, moving back to couriers menu.")
                    break
                print("Removing courier...")
                time.sleep(1)
                print(f"You have removed: {couriers.pop(index)}.")
            case _:  # Default case
                print('No option selected.')


# Exit program, making sure to save.
def exit_program() -> None:
    #save_products()
    #save_orders()
    print('Exitted!')
    exit()


# Main menu
def main() -> None:
    # Debug stuff to check if it has loaded properly.
    products = productmenu.Product_menu()
    orders = ordermenu.Order_menu()

    
    while True:
        print('''-----MAIN MENU-----
        0. Exit
        1. Products
        2. Couriers
        3. Orders
-------------------''')
        option = input('Choose command: ')
        # option = option_select(input("Choose command: "))
        match option:
            case '0':  # Exit
                print('Exiting program.')
                exit_program()
            case '1':  # Products
                print('Entering products menu...')
                time.sleep(1)
                products.view_products_menu()
            case '2':  # Couriers
                print('Entering couriers menu...')
                time.sleep(1)
                view_couriers_menu()
            case '3':  # Orders
                print('Entering orders menu...')
                time.sleep(1)
                orders.view_orders_menu()
            case _:  # Default
                print('No option selected.')

# Call main function
main()
# exit_program()
