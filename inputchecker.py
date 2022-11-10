# Author: Nathan
# Contains functions to validate input.


from typing import Union


def check_index(list_length: int, input: str) -> bool:
    """Validates the input as an index and returns an appropriate boolean

    Args:
        list_length (int): Length of the list to be checked against.
        input (str): The index to be checked.

    Returns:
        bool: True if the index is valid, False if not.
    """
    try:
        index = int(input)
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
