# Author: Nathan
# This is the main program of the cafe program.

import time
import input_checker
import productmenu
import couriermenu
import ordermenu

# Main menu
def main() -> None:
    # Debug stuff to check if it has loaded properly.
    products = productmenu.Product_menu()
    orders = ordermenu.Order_menu()
    couriers = couriermenu.Courier_menu()

    
    while True:
        print('''-----MAIN MENU-----
        0. Exit
        1. Products
        2. Couriers
        3. Orders
-------------------''')
        option = input('Choose command: ')
        match option:
            case '0':  # Exit
                print('Exiting program.')
                break
            case '1':  # Products
                print('Entering products menu...')
                time.sleep(1)
                products.view_products_menu()
            case '2':  # Couriers
                print('Entering couriers menu...')
                time.sleep(1)
                couriers.view_couriers_menu()
            case '3':  # Orders
                print('Entering orders menu...')
                time.sleep(1)
                orders.view_orders_menu()
            case _:  # Default
                print('No option selected.')
    # End of loop.
    products.save_products()
    orders.save_orders()
    couriers.save_couriers()
    print('Exitted!')
    exit()

# Call main function
main()
