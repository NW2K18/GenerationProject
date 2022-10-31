# Author

import time
#import filesystem

#String.isdigit(

# Initialise the product list, has values already in.
products = ['Pepsi', 'Coca Cola', 'Dr Pepper']
couriers = ['Larry', 'Curly', 'Moe']
# List of orders
orders = []

# Sample order
orders.append({
    'customer_name': 'John',
    'customer_address': 'Planet Earth',
    'customer_phone': '1439280432',
    'status': 'Preparing'
})


# Gets user input, returns user input as int if it is valid
def get_input_index(option, action):
    while True:
        index = (input(f'Type the index of the'
                f' {option} you wish to {action}: '))
        if check_index(option, index):
            return int(index) - 1
        else:
            continue


# Validates index, returns an appropriate boolean.
def check_index(option, input):
    try:
        index = int(input)
        index -= 1
        match option:
            case 'product':
                products[index]
            case 'courier':
                couriers[index]
            case 'order':
                orders[index]
            case _:
                raise Exception('Error in the check_index function:'
                ' no option selected.')
    except IndexError:
        print('This order does not exist.')
        return False
    except ValueError:
        print('Input cannot be converted into an integer.')
        return False
    return True


# Prints out product list.
def list_products():
    i = 1
    for product in products:
        print(f'Product No.{i} {product}')
        time.sleep(0.3)
        i += 1


# Prints out courier list.
def list_couriers():
    i = 1
    for courier in couriers:
        print(f'Courier No.{i} {courier}')
        time.sleep(0.3)
        i += 1


# Prints out orders.
def list_orders():
    i = 1
    for order in orders:
        print(f'''Order No.{i}:
        Customer name: {order['customer_name']}
        Customer address: {order['customer_address']}
        Customer phone number: {order['customer_phone']}
        Order status: {order['status']}
        ''')
        time.sleep(0.5)
        i += 1


# Load products
def load_products():
    productstring = ''
    try:
        with open('GenerationProject\productdata.txt', 'r') as file:
            productstring = file.read()
            print('LOADED PRODUCTS SUCCESSFULLY')
    except Exception as e:
        print(f'THERE WAS AN ISSUE: {e}')
        raise Exception

    products.clear()
    for product in productstring.split('\n'):
        if product == '': continue
        products.append(product)


# Load orders
def load_orders():
    fullorderstring = ''
    try:
        with open('GenerationProject\orderdata.txt', 'r') as file:
            fullorderstring = file.read()
            print('LOADED ORDERS SUCCESSFULLY')
    except Exception as e:
        print(f'THERE WAS AN ISSUE: {e}')
        raise Exception
    orders.clear()
    index = 0
    for orderstring in fullorderstring.split('\n\n'):
        if orderstring == '' or orderstring == '\n': continue  # If blank, do not add this to orders.
        orders.append({})
        for order in orderstring.split('\n'):
            if order == '': continue
            suborder = order.split(' ', 1)
            orders[index][suborder[0]] = suborder[1]
        index += 1


# Save products
def save_products():
    try:
        with open('GenerationProject\productdata.txt', 'w') as file:
            for product in products:
                file.write(f'{product}\n')
    except Exception as e:
        print(f'there was a problem at writing to file. {e}')
        raise Exception


# Save orders
def save_orders():
    try:
        with open('GenerationProject\orderdata.txt', 'w') as file:
            for order in orders:               
                for key in order:
                    file.write(f'{key} {order[key]}\n')
                file.write('\n')
    except Exception as e:
        print(f'there was a problem at writing to file. {e}')
        raise Exception


# Create an order
def set_order_create():
    userinput_name = input('Input customer name: ')
    if userinput_name.strip() == '': return False
    userinput_address = input('Input customer address: ')
    if userinput_address.strip() == '': return False
    userinput_phone = input('Input customer phone number: ')
    if userinput_phone.strip() == '': return False
    # If the inputs are valid, add a new entry.
    index = len(orders)  # Index of the new dictionary object
    orders.append({})  # Add the new dictionary
    orders[index]['customer_name'] = userinput_name
    orders[index]['customer_address'] = userinput_address
    orders[index]['customer_phone'] = userinput_phone
    orders[index]['status'] = 'Preparing'
    return True


# Update an order
def set_order_update(index):
    userinput = input('Input customer name: ')
    if userinput.strip() != '':
        orders[index]['customer_name'] = userinput
    userinput = input('Input customer address: ')
    if userinput.strip() != '':
        orders[index]['customer_address'] = userinput
    userinput = input('Input customer phone number: ')
    if userinput.strip() != '':
        orders[index]['customer_phone'] = userinput
    return True


# Update an order's status
def set_order_update_status(index):
    print('''
        0. Preparing
        1. Awaiting pickup
        2. Out for delivery
        3. Delivered
''')
    match input('Input number for order status: '):
        case '0':  # Preparing
            orders[index]['status'] = 'Preparing'
        case '1':  # Awaiting pickup
            orders[index]['status'] = 'Awaiting pickup'
        case '2':  # Out for delivery
            orders[index]['status'] = 'Out for delivery'
        case '3':  # Delivered
            orders[index]['status'] = 'Delivered'
        case _:  # Invalid input
            print('Invalid update status entered, status unchanged.')
            return False
    return True


# This is the products menu
def view_products_menu():
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
                    products.append(product)
                else:
                    print('No product name entered.')
            case '2':  # View
                print('Printing product list...')
                time.sleep(1)
                list_products()
                time.sleep(1)
            case '3':  # Update
                list_products()
                index = get_input_index('product', 'update')
                if (index + 1) == 0:
                    print('Selected 0, moving back to products menu.')
                    break
                newname = input(f'Type what you wish'
                f' to replace {products[index]} with: ')
                if newname.strip() != '':
                    print('Updating product...')
                    time.sleep(1)
                    products[index] = newname
                    print('Updated product.')
                else:
                    print('No product name entered.')
            case '4':  # Remove
                list_products()
                index = get_input_index('product', 'remove')
                if (index + 1) == 0:
                    print('Selected 0, moving back to products menu.')
                    break
                print('Removing product...')
                time.sleep(1)
                print(f'You have removed: {products.pop(index)}.')
            case _:  # Default
                print('No option selected.')


# This is the couriers menu
def view_couriers_menu():
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
                index = get_input_index('courier', 'update')
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
                index = get_input_index('courier', 'remove')
                if (index + 1) == 0:
                    print("Selected 0, moving back to couriers menu.")
                    break
                print("Removing courier...")
                time.sleep(1)
                print(f"You have removed: {couriers.pop(index)}.")
            case _:  # Default case
                print('No option selected.')


# This is the orders menu
def view_orders_menu():
    while True:
        print('''-----ORDERS-----
        0. Exit
        1. Create an order
        2. View Order List
        3. Update an order's status
        4. Update an order
        5. Remove an order
---------------------''')
        option = input('Choose command: ')
        match option:
            case '0':  # Exit
                print("Exiting orders menu...")
                time.sleep(1)
                break
            case '1':  # Create
                if set_order_create():
                    time.sleep(1)
                    print('Created a new order.')
                else:
                    time.sleep(1)
                    print('Did not create a new order.')
            case "2":  # View
                print('Printing order list...')
                list_orders()
                time.sleep(1)
            case '3':  # Update status
                list_orders()
                index = get_input_index('order', 'update')
                if (index + 1) == 0:
                    print('Selected 0, moving back to order menu.')
                    break
                set_order_update_status(index)
                print('Updating order...')
                time.sleep(1)
                print('Updated order.')
            case '4':  # Update
                list_orders()
                index = get_input_index('order', 'update')
                if (index + 1) == 0:
                    print("Selected 0, moving back to order menu.")
                    break
                set_order_update(index)
                time.sleep(1)
                print('Updated order.')
            case '5':  # Remove
                list_orders()
                index = get_input_index('order', 'remove')
                if (index + 1) == 0:
                    print("Selected 0, moving back to order menu.")
                    break
                print("Removing order...")
                time.sleep(1)
                print(f"You have removed: {orders.pop(index)}.")
            case _:  # Default
                    print("No option selected.")


# Exit program, making sure to save.
def exit_program():
    save_products()
    save_orders()
    print('Exitted!')
    exit()


# Main menu
def main():
    # Debug stuff.
    print(products)
    load_products()
    print(products)
    print(orders)
    load_orders()
    print(orders)
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
                view_products_menu()
            case '2':  # Couriers
                print('Entering couriers menu...')
                time.sleep(1)
                view_couriers_menu()
            case '3':  # Orders
                print('Entering orders menu...')
                time.sleep(1)
                view_orders_menu()
            case _:  # Default
                print('No option selected.')

# Call main function
main()
# exit_program()
