"""Author: Nathan \n
Contains functions to validate input.
"""

import html
from typing import List, Union, Dict

from productclass import Product
from courierclass import Courier
from orderclass import Order


def check_index(list_length: int, user_input: str) -> bool:
    """Validates the input as an index and returns an appropriate boolean

    Args:
        list_length (int): Length of the list to be checked against.
        input (str): The index to be checked.

    Returns:
        bool: True if the index is valid, False if not.
    """
    try:
        index = int(user_input)
        if index <= 0 or index > list_length:
            print('This index does not exist.')
            return False
    except ValueError:
        print('Input cannot be converted into an integer.')
        return False
    return True


def get_input_index(option: str, action: str,
                    checked_list: List) -> Union[int, None]:
    """Contains a while loop with an input function that asks for user input,
    and returns an index once you input a valid index.

    Args:
        option (str): The object type that the user wants to modify.
        action (str): What the user wants to do to the object.
        checked_list (List): List to be checked.

    Returns:
        int: The index of the list object, e.g Item No.1 = Index 0
        None: If the input is zero.
    """
    while True:  # Doesn't break from loop until valid input.
        database_id = (input(
            f'Type the ID of the {option} you wish to {action}'
            '(0 to exit): '))
        if database_id == '0':
            return None
        match option:
            case 'product':
                return get_product_index(checked_list, database_id)
            case 'courier':
                return get_courier_index(checked_list, database_id)
            case 'order':
                return get_order_index(checked_list, database_id)
            case _:
                raise Exception('Invalid option passed in as arg')


def sanitise_input(userinput: str) -> str:
    """Takes in user input and sanitises it to prevent potential SQL
    injections.

    Args:
        userinput (str): User input

    Returns:
        str: Sanitised input.
    """
    html.escape(userinput)
    return html.escape(userinput)


def validate_phone(userinput_phone: str) -> str:
    """Validates the passed in string as a phone number, returns it back if it
    is valid, or a blank string if it is invalid.

    Args:
        userinput_phone (str): String to be validated as a phone number.

    Returns:
        str: Returns the string back if valid, or blank string if invalid.
    """
    userinput_phone = sanitise_input(userinput_phone)
    if len(userinput_phone) >= 10 and userinput_phone.isdigit():
        return userinput_phone
    return ''


def get_courier_id(
        couriers: List[Courier], userinput_courier: str) -> int:
    """Checks the list of couriers for id, returns the id if there is a match.

    Args:
        couriers (List[Courier]): To be checked.
        userinput_courier (str): Used to check the list.

    Returns:
        int: The database id as an integer, or 0 if
        there is no match.
    """
    try:  # Checking the list to see if input equals a database id.
        userinput_courier = int(userinput_courier)
        for courier in couriers:
            if userinput_courier == courier.id:
                return userinput_courier
        print('Could not find ID')
    except ValueError:
        print('Could not convert to integer')
    return 0


def get_item_id(
        products: List[Product], userinput_items: str) -> Union[str, None]:
    """Checks the list of product for id, returns the id if there is a match.

    Args:
        products (List[Product]): To be checked.
        userinput_items (str): Used to check the list.

    Returns:
        Union[str, None]: The database id as a string, or none if there is no
        match.
    """
    try:  # Checking the list to see if input equals a database id.
        userinput_items = int(userinput_items)
        for product in products:
            if userinput_items == product.id:
                return str(userinput_items)
        print('Could not find ID')
    except ValueError:
        print('Could not convert to integer')
    return None


def get_item_quantity(items: str) -> Dict[str, int]:
    """Iterates through a string of items, counts number of item occurences,
    and returns a dictionary where key = item, value = item occurences
    throughout string.

    Args:
        items (str): String to be iterated through, seperator is (', ').

    Returns:
        Dict[str, int]: The dictionary.
    """
    item_list = items.split(', ')
    item_occurences = {}
    for item in item_list:
        if item in item_occurences:
            item_occurences[item] += 1
        else:
            item_occurences[item] = 1
    return item_occurences


def get_product_index(
        products: List[Product], database_id: str) -> Union[int, None]:
    """Checks the list of products for id, returns the list index if there
    is a match.

    Args:
        products (List[Product]): To be checked.
        database_id (str): Used to check the list.

    Returns:
        Union[int, None]: The list index, or None if there is no match.
    """
    try:
        database_id = int(database_id)
        index = 0
        for product in products:
            if database_id == product.id:
                return index
            index += 1
        print('Could not find ID')
    except ValueError:
        print('Could not convert to integer')
    return None


def get_courier_index(
        couriers: List[Courier], database_id: str) -> Union[int, None]:
    """Checks the list of couriers for id, returns the list index if there
    is a match.

    Args:
        couriers (List[Courier]): To be checked.
        database_id (str): Used to check the list.

    Returns:
        Union[int, None]: The list index, or None if there is no match.
    """
    try:
        database_id = int(database_id)
        index = 0
        for courier in couriers:
            if database_id == courier.id:
                return index
            index += 1
        print('Could not find ID')
    except ValueError:
        print('Could not convert to integer')
    return None


def get_order_index(
        orders: List[Order], database_id: str) -> Union[int, None]:
    """Checks the list of orders for id, returns the list index if there
    is a match.

    Args:
        orders (List[Order]): To be checked.
        database_id (str): Used to check the list.

    Returns:
        Union[int, None]: The list index, or None if there is no match.
    """
    try:
        database_id = int(database_id)
        index = 0
        for order in orders:
            if database_id == order.id:
                return index
            index += 1
        print('Could not find ID')
    except ValueError:
        print('Could not convert to integer')
    return None
