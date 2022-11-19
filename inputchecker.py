"""Author: Nathan \n
Contains functions to validate input.
"""


from typing import List, Union

from productclass import Product
from courierclass import Courier


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
                    list_length: int) -> Union[int, None]:
    """Contains a while loop with an input function that asks for user input,
    and returns an index once you input a valid index.

    Args:
        option (str): The object type that the user wants to modify.
        action (str): What the user wants to do to the object.
        list_length (int): Length of the list to be checked against.

    Returns:
        int: The index of the list object, e.g Item No.1 = Index 0
        None: If the input is zero.
    """
    while True:  # Doesn't break from loop until valid input.
        index = (input(f'Type the index of the \
{option} you wish to {action}: '))
        if index == '0':
            return None
        elif check_index(list_length, index):
            return int(index) - 1
        else:
            continue


def validate_phone(userinput_phone: str) -> str:
    """Validates the passed in string as a phone number, returns it back if it
    is valid, or a blank string if it is invalid.

    Args:
        userinput_phone (str): String to be validated as a phone number.

    Returns:
        str: Returns the string back if valid, or blank string if invalid.
    """
    pass  # TODO


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
